import uuid
from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Numeric,
    Float,
    Integer,
    Date,
    Index
)
from sqlalchemy.orm import relationship
from app.db.base_class import Base, GUID, TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default="PATIENT")  # PATIENT, DOCTOR, ADMIN
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    phone = Column(String(50), nullable=True)
    full_name = Column(String(255), nullable=False)

    # Relationships
    patient_profile = relationship("Patient", back_populates="user", uselist=False, cascade="all, delete-orphan")
    doctor_profile = relationship("Doctor", back_populates="user", uselist=False, cascade="all, delete-orphan")
    audit_logs = relationship("AuditLog", back_populates="user")

class Patient(Base, TimestampMixin):
    __tablename__ = "patients"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(GUID, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(50), nullable=True)
    blood_group = Column(String(20), nullable=True)
    address = Column(String(500), nullable=True)

    # Relationships
    user = relationship("User", back_populates="patient_profile")
    family_members = relationship("FamilyMember", back_populates="patient", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="patient")

class FamilyMember(Base, TimestampMixin):
    __tablename__ = "family_members"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    patient_id = Column(GUID, ForeignKey("patients.id", ondelete="CASCADE"), nullable=False)
    full_name = Column(String(255), nullable=False)
    relation = Column(String(100), nullable=False)  # SPOUSE, CHILD, PARENT, SIBLING, OTHER
    date_of_birth = Column(Date, nullable=True)

    # Relationships
    patient = relationship("Patient", back_populates="family_members")

class Doctor(Base, TimestampMixin):
    __tablename__ = "doctors"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(GUID, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    specialty = Column(String(255), index=True, nullable=False)
    license_number = Column(String(100), unique=True, nullable=False)
    bio = Column(String(1000), nullable=True)
    experience_years = Column(Integer, nullable=False, default=0)
    consultation_fee = Column(Numeric(10, 2), nullable=False, default=0.00)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    verification_status = Column(String(50), nullable=False, default="PENDING")  # PENDING, APPROVED, REJECTED

    # Relationships
    user = relationship("User", back_populates="doctor_profile")
    availability_slots = relationship("AvailabilitySlot", back_populates="doctor", cascade="all, delete-orphan")
    appointments = relationship("Appointment", back_populates="doctor")
    subscription = relationship("SaaSSubscription", back_populates="doctor", uselist=False, cascade="all, delete-orphan")

class AvailabilitySlot(Base, TimestampMixin):
    __tablename__ = "availability_slots"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    doctor_id = Column(GUID, ForeignKey("doctors.id", ondelete="CASCADE"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    is_booked = Column(Boolean, default=False, nullable=False)

    # Relationships
    doctor = relationship("Doctor", back_populates="availability_slots")
    appointment = relationship("Appointment", back_populates="slot", uselist=False)

    # Indexes
    __table_args__ = (
        Index("idx_slots_doctor_time", "doctor_id", "start_time", "is_booked"),
    )

class Appointment(Base, TimestampMixin):
    __tablename__ = "appointments"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    patient_id = Column(GUID, ForeignKey("patients.id", ondelete="RESTRICT"), nullable=False)
    doctor_id = Column(GUID, ForeignKey("doctors.id", ondelete="RESTRICT"), nullable=False)
    slot_id = Column(GUID, ForeignKey("availability_slots.id", ondelete="RESTRICT"), unique=True, nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False, default="PENDING")  # PENDING, CONFIRMED, CANCELLED, COMPLETED
    payment_status = Column(String(50), nullable=False, default="PENDING")  # PENDING, PAID, REFUNDED
    appointment_type = Column(String(50), nullable=False, default="IN_PERSON")  # VIRTUAL, IN_PERSON
    reason = Column(String(500), nullable=True)

    # Relationships
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    slot = relationship("AvailabilitySlot", back_populates="appointment")
    prescription = relationship("Prescription", back_populates="appointment", uselist=False, cascade="all, delete-orphan")
    invoice = relationship("Invoice", back_populates="appointment", uselist=False, cascade="all, delete-orphan")

    # Indexes
    __table_args__ = (
        Index("idx_appointments_patient", "patient_id"),
        Index("idx_appointments_doctor", "doctor_id"),
        Index("idx_appointments_status", "status"),
    )

class Prescription(Base, TimestampMixin):
    __tablename__ = "prescriptions"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    appointment_id = Column(GUID, ForeignKey("appointments.id", ondelete="CASCADE"), unique=True, nullable=False)
    notes = Column(String(2000), nullable=False)
    pdf_url = Column(String(1000), nullable=True)
    generated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    appointment = relationship("Appointment", back_populates="prescription")

class SaaSSubscription(Base, TimestampMixin):
    __tablename__ = "saas_subscriptions"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    doctor_id = Column(GUID, ForeignKey("doctors.id", ondelete="CASCADE"), unique=True, nullable=False)
    stripe_sub_id = Column(String(255), unique=True, nullable=True)
    plan_name = Column(String(50), nullable=False, default="BASIC")  # BASIC, PREMIUM
    status = Column(String(50), nullable=False, default="ACTIVE")  # ACTIVE, CANCELLED, PAST_DUE
    end_date = Column(DateTime, nullable=False)

    # Relationships
    doctor = relationship("Doctor", back_populates="subscription")

class Invoice(Base, TimestampMixin):
    __tablename__ = "invoices"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    appointment_id = Column(GUID, ForeignKey("appointments.id", ondelete="CASCADE"), unique=True, nullable=False)
    stripe_charge_id = Column(String(255), unique=True, nullable=True)
    amount = Column(Numeric(10, 2), nullable=False)
    platform_fee = Column(Numeric(10, 2), nullable=False, default=0.00)
    status = Column(String(50), nullable=False, default="PAID")  # PAID, REFUNDED

    # Relationships
    appointment = relationship("Appointment", back_populates="invoice")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(GUID, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    action = Column(String(255), nullable=False)
    details = Column(String(1000), nullable=True)
    ip_address = Column(String(45), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="audit_logs")
