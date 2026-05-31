from typing import List, Optional, Any
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from app.repository.base import CRUDBase
from app.db.models import Appointment

class CRUDAppointment(CRUDBase[Appointment]):
    def get_by_patient(self, db: Session, patient_id: Any, *, skip: int = 0, limit: int = 100) -> List[Appointment]:
        """Retrieves appointments booked by a specific patient."""
        statement = (
            select(Appointment)
            .where(Appointment.patient_id == patient_id)
            .order_by(Appointment.appointment_time.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(db.scalars(statement).all())

    def get_by_doctor(self, db: Session, doctor_id: Any, *, skip: int = 0, limit: int = 100) -> List[Appointment]:
        """Retrieves appointments scheduled with a specific doctor."""
        statement = (
            select(Appointment)
            .where(Appointment.doctor_id == doctor_id)
            .order_by(Appointment.appointment_time.desc())
            .offset(skip)
            .limit(limit)
        )
        return list(db.scalars(statement).all())

    def get_by_slot(self, db: Session, slot_id: Any) -> Optional[Appointment]:
        """Fetches the appointment linked to a specific time slot."""
        statement = select(Appointment).where(Appointment.slot_id == slot_id)
        return db.scalar(statement)

appointment_repo = CRUDAppointment(Appointment)
