from typing import Optional, Any
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.repository.base import CRUDBase
from app.db.models import User, Patient, Doctor

class CRUDUser(CRUDBase[User]):
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Fetches a user by their unique email address."""
        statement = select(self.model).where(self.model.email == email)
        return db.scalar(statement)

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_verified(self, user: User) -> bool:
        return user.is_verified

    def get_patient_profile(self, db: Session, user_id: Any) -> Optional[Patient]:
        """Fetches the associated patient record for a user."""
        statement = select(Patient).where(Patient.user_id == user_id)
        return db.scalar(statement)

    def get_doctor_profile(self, db: Session, user_id: Any) -> Optional[Doctor]:
        """Fetches the associated doctor record for a user."""
        statement = select(Doctor).where(Doctor.user_id == user_id)
        return db.scalar(statement)

user_repo = CRUDUser(User)
