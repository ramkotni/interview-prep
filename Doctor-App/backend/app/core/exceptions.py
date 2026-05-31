from fastapi import HTTPException, status

class AppException(Exception):
    """Base application exception for domain logic errors."""
    def __init__(self, message: str, error_code: str, status_code: int = 400):
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        super().__init__(self.message)

class NotFoundException(AppException):
    def __init__(self, resource: str, identifier: str):
        super().__init__(
            message=f"{resource} with identifier {identifier} was not found.",
            error_code="RESOURCE_NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND
        )

class AlreadyExistsException(AppException):
    def __init__(self, resource: str, field: str, value: str):
        super().__init__(
            message=f"{resource} with {field} '{value}' already exists.",
            error_code="RESOURCE_ALREADY_EXISTS",
            status_code=status.HTTP_409_CONFLICT
        )

class UnauthorizedException(AppException):
    def __init__(self, message: str = "Invalid credentials or token."):
        super().__init__(
            message=message,
            error_code="UNAUTHORIZED",
            status_code=status.HTTP_401_UNAUTHORIZED
        )

class ForbiddenException(AppException):
    def __init__(self, message: str = "You do not have permission to perform this action."):
        super().__init__(
            message=message,
            error_code="FORBIDDEN",
            status_code=status.HTTP_403_FORBIDDEN
        )

class ValidationException(AppException):
    def __init__(self, message: str = "Validation failed."):
        super().__init__(
            message=message,
            error_code="VALIDATION_FAILED",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )
