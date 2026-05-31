from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class AppointmentBase(BaseModel):
    appointment_time: datetime
    appointment_type: str = "IN_PERSON"  # VIRTUAL, IN_PERSON
    reason: Optional[str] = None

class AppointmentCreate(BaseModel):
    doctor_id: UUID
    slot_id: UUID
    appointment_type: str = "IN_PERSON"
    reason: Optional[str] = None

class AppointmentUpdate(BaseModel):
    status: Optional[str] = None  # PENDING, CONFIRMED, CANCELLED, COMPLETED
    payment_status: Optional[str] = None  # PENDING, PAID, REFUNDED

class AppointmentResponse(AppointmentBase):
    id: UUID
    patient_id: UUID
    doctor_id: UUID
    slot_id: UUID
    status: str
    payment_status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Prescription Schemas
class PrescriptionBase(BaseModel):
    notes: str

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionResponse(PrescriptionBase):
    id: UUID
    appointment_id: UUID
    pdf_url: Optional[str] = None
    generated_at: datetime

    model_config = ConfigDict(from_attributes=True)
