from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserResponse, PatientResponse, PatientUpdate
from app.schemas.family_member import FamilyMemberResponse, FamilyMemberCreate
from app.db.models import User, Patient, FamilyMember

router = APIRouter()

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(deps.get_current_user)):
    """Retrieves basic profile metadata for the authenticated user."""
    return current_user

@router.get("/patient/profile", response_model=PatientResponse)
def get_patient_profile(
    patient: Patient = Depends(deps.get_current_patient)
):
    """Retrieves patient-specific demographic details."""
    return patient

@router.put("/patient/profile", response_model=PatientResponse)
def update_patient_profile(
    profile_data: PatientUpdate,
    db: Session = Depends(deps.get_db),
    patient: Patient = Depends(deps.get_current_patient)
):
    """Updates contact or address details on the patient profile."""
    for field, value in profile_data.model_dump(exclude_unset=True).items():
        setattr(patient, field, value)
    db.commit()
    db.refresh(patient)
    return patient

@router.get("/family-members", response_model=List[FamilyMemberResponse])
def get_family_members(
    patient: Patient = Depends(deps.get_current_patient)
):
    """Returns a list of registered family members under this patient."""
    return patient.family_members

@router.post("/family-members", response_model=FamilyMemberResponse, status_code=status.HTTP_201_CREATED)
def add_family_member(
    member_data: FamilyMemberCreate,
    db: Session = Depends(deps.get_db),
    patient: Patient = Depends(deps.get_current_patient)
):
    """Registers a relative under the patient's master record."""
    member = FamilyMember(patient_id=patient.id, **member_data.model_dump())
    db.add(member)
    db.commit()
    db.refresh(member)
    return member
