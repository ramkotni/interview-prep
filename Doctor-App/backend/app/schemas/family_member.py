from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID

class FamilyMemberBase(BaseModel):
    full_name: str
    relation: str  # SPOUSE, CHILD, PARENT, SIBLING, OTHER
    date_of_birth: Optional[date] = None

class FamilyMemberCreate(FamilyMemberBase):
    pass

class FamilyMemberUpdate(FamilyMemberBase):
    pass

class FamilyMemberResponse(FamilyMemberBase):
    id: UUID
    patient_id: UUID
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
