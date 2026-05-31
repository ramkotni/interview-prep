from typing import List, Optional, Any
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_, func
from app.repository.base import CRUDBase
from app.db.models import Doctor, User, AvailabilitySlot

class CRUDDoctor(CRUDBase[Doctor]):
    def search_doctors(
        self,
        db: Session,
        *,
        specialty: Optional[str] = None,
        min_experience: Optional[int] = None,
        max_fee: Optional[float] = None,
        query_name: Optional[str] = None,
        skip: int = 0,
        limit: int = 20
    ) -> List[Doctor]:
        """Performs structured searching and filtering across doctor profiles."""
        statement = select(Doctor).join(User)
        filters = [Doctor.verification_status == "APPROVED"]

        if specialty:
            filters.append(func.lower(Doctor.specialty) == specialty.lower())
        if min_experience is not None:
            filters.append(Doctor.experience_years >= min_experience)
        if max_fee is not None:
            filters.append(Doctor.consultation_fee <= max_fee)
        if query_name:
            search_pattern = f"%{query_name.lower()}%"
            filters.append(
                or_(
                    func.lower(User.full_name).like(search_pattern),
                    func.lower(Doctor.bio).like(search_pattern)
                )
            )

        statement = statement.where(and_(*filters)).offset(skip).limit(limit)
        return list(db.scalars(statement).all())

    def get_slots(
        self,
        db: Session,
        *,
        doctor_id: Any,
        start_time: datetime,
        end_time: datetime,
        include_booked: bool = False
    ) -> List[AvailabilitySlot]:
        """Fetches calendar availability slots for a doctor within a time window."""
        filters = [
            AvailabilitySlot.doctor_id == doctor_id,
            AvailabilitySlot.start_time >= start_time,
            AvailabilitySlot.end_time <= end_time
        ]
        if not include_booked:
            filters.append(AvailabilitySlot.is_booked == False)

        statement = select(AvailabilitySlot).where(and_(*filters)).order_by(AvailabilitySlot.start_time.asc())
        return list(db.scalars(statement).all())

doctor_repo = CRUDDoctor(Doctor)
