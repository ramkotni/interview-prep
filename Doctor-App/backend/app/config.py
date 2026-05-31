import os
from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Doctor Appointment Platform SaaS"
    API_V1_STR: str = "/api/v1"
    
    # JWT Settings (Defaults to secure fallbacks if not provided in environment)
    SECRET_KEY: str = "supersecretsecuritykeyforjwttokenszocdocclone12345!"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS Origins (Allow local environments and subdomains)
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # SQLite / PostgreSQL-ready URL
    # Resolves to doctor_app.db inside backend directory
    DATABASE_URL: str = "sqlite:///./doctor_app.db"

    # Infrastructure Configuration (Mocked by default if not set)
    STRIPE_SECRET_KEY: str = ""
    STRIPE_PUBLISHABLE_KEY: str = ""
    
    AWS_ACCESS_KEY_ID: str = ""
    AWS_SECRET_ACCESS_KEY: str = ""
    AWS_S3_BUCKET: str = ""
    
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = ""
    
    SENDGRID_API_KEY: str = ""
    SENDGRID_FROM_EMAIL: str = "noreply@doctorapp.com"
    
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Upload Directories (Fallback storage when AWS S3 is empty)
    UPLOAD_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "storage", "uploads")
    NOTIFICATION_LOG_PATH: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs", "notifications.log")

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8"
    )

settings = Settings()
