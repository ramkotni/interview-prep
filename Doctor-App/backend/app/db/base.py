# Import all the models, so that Base has them before being
# imported by Alembic or other processes
from app.db.base_class import Base  # noqa
from app.db.models import User, Patient, FamilyMember, Doctor, AvailabilitySlot, Appointment, Prescription, SaaSSubscription, Invoice, AuditLog  # noqa
