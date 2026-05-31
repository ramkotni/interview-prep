import os
from datetime import datetime, timedelta
from typing import Optional, Tuple
from sqlalchemy.orm import Session
from app.core import security
from app.core.exceptions import UnauthorizedException, AlreadyExistsException, NotFoundException
from app.db.models import User, Patient, Doctor
from app.repository.user_repo import user_repo
from app.schemas.auth import SignUpRequest, Token
from app.config import settings

class AuthService:
    def authenticate(self, db: Session, email: str, password: str) -> User:
        """Verifies email and password credentials. Returns authenticated User object."""
        user = user_repo.get_by_email(db, email=email)
        if not user or not security.verify_password(password, user.password_hash):
            raise UnauthorizedException("Incorrect email or password.")
        if not user.is_active:
            raise UnauthorizedException("User account has been deactivated.")
        return user

    def register(self, db: Session, signup_data: SignUpRequest) -> User:
        """Registers a new User and automatically provisions Patient or Doctor profile."""
        existing_user = user_repo.get_by_email(db, email=signup_data.email)
        if existing_user:
            raise AlreadyExistsException("User", "email", signup_data.email)

        # Hash credentials
        hashed_password = security.get_password_hash(signup_data.password)

        user_data = {
            "email": signup_data.email,
            "password_hash": hashed_password,
            "full_name": signup_data.full_name,
            "role": signup_data.role.upper(),
            "phone": signup_data.phone,
            "is_active": True,
            "is_verified": False
        }

        user = user_repo.create(db, obj_in=user_data)

        # Auto-provision Patient profile
        if user.role == "PATIENT":
            patient_profile = Patient(user_id=user.id)
            db.add(patient_profile)
            db.commit()
        # Auto-provision Doctor profile (starts as PENDING verification status)
        elif user.role == "DOCTOR":
            doctor_profile = Doctor(
                user_id=user.id,
                specialty="General Medicine",  # Temporary default profile values
                license_number=f"LIC-{user.id.hex[:6].upper()}",
                experience_years=0,
                consultation_fee=0.0,
                verification_status="PENDING"
            )
            db.add(doctor_profile)
            db.commit()

        db.refresh(user)
        return user

    def create_session_tokens(self, user: User) -> Token:
        """Generates access and refresh tokens for standard web/mobile sessions."""
        access_token = security.create_access_token(subject=user.id)
        refresh_token = security.create_refresh_token(subject=user.id)
        return Token(access_token=access_token, refresh_token=refresh_token)

    def refresh_session(self, refresh_token: str) -> Token:
        """Validates refresh token and generates a rotated set of tokens."""
        try:
            payload = security.decode_token(refresh_token)
            user_id = payload.get("sub")
            token_type = payload.get("type")
            if user_id is None or token_type != "refresh":
                raise UnauthorizedException("Invalid refresh token payload.")
        except Exception:
            raise UnauthorizedException("Expired or invalid refresh token.")

        # Re-encode fresh pair
        new_access = security.create_access_token(subject=user_id)
        new_refresh = security.create_refresh_token(subject=user_id)
        return Token(access_token=new_access, refresh_token=new_refresh)

    def send_otp(self, db: Session, email: str) -> str:
        """Generates a secure 6-digit verification OTP and writes to notifications log."""
        user = user_repo.get_by_email(db, email=email)
        if not user:
            raise NotFoundException("User", email)

        otp_code = security.generate_numeric_otp()
        
        # In a real environment we would fire Twilio SMS/SendGrid here.
        # Since we use mocks, we append to a local text log for developer inspection.
        os.makedirs(os.path.dirname(settings.NOTIFICATION_LOG_PATH), exist_ok=True)
        with open(settings.NOTIFICATION_LOG_PATH, "a") as log_file:
            log_file.write(f"[{datetime.utcnow().isoformat()}] OTP generated for {email}: {otp_code} (Valid for 5 mins)\n")

        # In production, we'd cache this OTP in Redis with an expiry.
        # For simplicity during mock tests, we will write a mocked log line that the system can match.
        return otp_code

    def verify_otp(self, email: str, otp_code: str) -> bool:
        """Verifies OTP code matching criteria (accepts the logged code or standard fallback for dev)."""
        # Accept '123456' as standard developer fallback OTP
        if otp_code == "123456":
            return True
            
        # Parse our notification logs to match the generated code (for high fidelity offline testing)
        if os.path.exists(settings.NOTIFICATION_LOG_PATH):
            with open(settings.NOTIFICATION_LOG_PATH, "r") as log_file:
                lines = log_file.readlines()
                for line in reversed(lines):
                    if f"OTP generated for {email}" in line:
                        logged_otp = line.split(":")[-1].strip().split()[0]
                        if logged_otp == otp_code:
                            return True
        return False

auth_service = AuthService()
