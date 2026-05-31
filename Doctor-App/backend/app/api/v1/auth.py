from fastapi import APIRouter, Depends, Response, Request, status
from sqlalchemy.orm import Session
from app.api import deps
from app.services.auth_service import auth_service
from app.schemas.auth import (
    SignUpRequest, Token, LoginRequest, OTPRequest, OTPVerifyRequest, OTPResponse
)
from app.schemas.user import UserResponse

router = APIRouter()

@router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(signup_data: SignUpRequest, db: Session = Depends(deps.get_db)):
    """Registers a new patient or doctor and provisions the associated profile."""
    return auth_service.register(db, signup_data=signup_data)

@router.post("/login", response_model=Token)
def login(login_data: LoginRequest, response: Response, db: Session = Depends(deps.get_db)):
    """Logs in using credentials and attaches JWTs as HttpOnly cookies for safety."""
    user = auth_service.authenticate(db, email=login_data.email, password=login_data.password)
    tokens = auth_service.create_session_tokens(user)
    
    # Secure Cookie Settings (HttpOnly, SameSite=Lax)
    response.set_cookie(
        key="access_token",
        value=tokens.access_token,
        httponly=True,
        samesite="lax",
        secure=False,  # Set to True in HTTPS production
        max_age=15 * 60  # 15 mins
    )
    response.set_cookie(
        key="refresh_token",
        value=tokens.refresh_token,
        httponly=True,
        samesite="lax",
        secure=False,
        max_age=7 * 24 * 60 * 60  # 7 days
    )
    
    return tokens

@router.post("/refresh", response_model=Token)
def refresh(request: Request, response: Response):
    """Rotates session tokens using the secure refresh cookie."""
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        # Fallback to checking body/header if cookie is absent (needed for API/mobile clients)
        pass
    tokens = auth_service.refresh_session(refresh_token=refresh_token)
    
    response.set_cookie(key="access_token", value=tokens.access_token, httponly=True, samesite="lax", max_age=15 * 60)
    response.set_cookie(key="refresh_token", value=tokens.refresh_token, httponly=True, samesite="lax", max_age=7 * 24 * 60 * 60)
    return tokens

@router.post("/logout")
def logout(response: Response):
    """Clears both access and refresh token cookies, ending the session."""
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Successfully logged out."}

@router.post("/otp/request")
def request_otp(otp_req: OTPRequest, db: Session = Depends(deps.get_db)):
    """Requests a 6-digit verification code sent to the email."""
    auth_service.send_otp(db, email=otp_req.email)
    return {"message": "OTP has been generated and dispatched."}

@router.post("/otp/verify", response_model=OTPResponse)
def verify_otp(verify_req: OTPVerifyRequest, db: Session = Depends(deps.get_db)):
    """Verifies the requested OTP and marks user email as verified."""
    is_valid = auth_service.verify_otp(email=verify_req.email, otp_code=verify_req.otp_code)
    if is_valid:
        user = db.query(deps.User).filter(deps.User.email == verify_req.email).first()
        if user:
            user.is_verified = True
            db.commit()
        return {"message": "Email successfully verified.", "is_verified": True}
    return {"message": "Invalid OTP code provided.", "is_verified": False}
