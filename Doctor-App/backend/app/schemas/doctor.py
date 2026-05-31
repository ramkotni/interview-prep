from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal
from uuid import UUID
from app.schemas.user import UserResponse

class DoctorBase(BaseModel):
    specialty: str = Field(..., min_length=2, max_length=100)
    license_number: str = Field(..., min_length=5, max_length=50)
    bio: Optional[str] = Field(None, max_length=1000)
    experience_years: int = Field(default=0, ge=0)
    consultation_fee: Decimal = Field(default=Decimal("0.00"), ge=0.00)
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class DoctorCreate(DoctorBase):
    pass

class DoctorUpdate(BaseModel):
    specialty: Optional[str] = None
    bio: Optional[str] = None
    experience_years: Optional[int] = None
    consultation_fee: Optional[Decimal] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    verification_status: Optional[str] = None  # PENDING, APPROVED, REJECTED (Usually updated by Admin)

class DoctorResponse(DoctorBase):
    id: UUID
    user_id: UUID
    verification_status: str
    created_at: datetime
    user: Optional[UserResponse] = None

    model_config = ConfigDict(from_attributes=True)


# Availability Slot Schemas
class AvailabilitySlotBase(BaseModel):
    start_time: datetime
    end_time: datetime
    is_booked: bool = False

class AvailabilitySlotCreate(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilitySlotBulkCreate(BaseModel):
    slots: List[AvailabilitySlotCreate]

class AvailabilitySlotResponse(AvailabilitySlotBase):
    id: UUID
    doctor_id: UUID

    model_config = ConfigDict(from_attributes=True)
