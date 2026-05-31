from typing import Generator, Optional
import jwt
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.config import settings
from app.core.database import get_db
from app.core.security import decode_token
from app.db.models import User, Patient, Doctor
from app.repository.user_repo import user_repo

# Custom OAuth2 scheme that also accepts JWT from custom header or cookies
class OAuth2PasswordBearerWithCookie(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        # Try finding token in Authorization header
        authorization = request.headers.get("Authorization")
        if authorization:
            try:
                scheme, param = authorization.split()
                if scheme.lower() == "bearer":
                    return param
            except ValueError:
                pass
                
        # Fallback to HttpOnly cookie
        token = request.cookies.get("access_token")
        if token:
            return token
            
        return None

reusable_oauth2 = OAuth2PasswordBearerWithCookie(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)

def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> User:
    """Dependency to validate JWT tokens and inject the authenticated User model."""
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated. Missing token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        token_type = payload.get("type")
        if user_id is None or token_type != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials, invalid token type.",
            )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials, expired or malformed token.",
        )
        
    user = user_repo.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user.")
        
    return user

def get_current_active_admin(current_user: User = Depends(get_current_user)) -> User:
    """RBAC Guard verifying that the user has Administrator privileges."""
    if current_user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The user does not have enough privileges."
        )
    return current_user

def get_current_patient(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> Patient:
    """RBAC Guard that resolves and returns the logged-in Patient profile."""
    if current_user.role != "PATIENT":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only patients can access this resource."
        )
    patient = user_repo.get_patient_profile(db, user_id=current_user.id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient profile not created.")
    return patient

def get_current_doctor(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)) -> Doctor:
    """RBAC Guard that resolves and returns the logged-in Doctor profile."""
    if current_user.role != "DOCTOR":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only doctors can access this resource."
        )
    doctor = user_repo.get_doctor_profile(db, user_id=current_user.id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor profile not created.")
    return doctor
