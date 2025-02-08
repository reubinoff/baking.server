from abc import abstractmethod

from fastapi import status
from pydantic import PydanticUserError

from server.errors.codes import ErrorCode


class BaseBakingError(Exception):
    """Base exception for all Baking API errors"""

    http_status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    code: str = "internal_error"
    message: str = "An internal error occurred"

    def __init__(self):
        self.message = self._get_message()
        super().__init__(self.message)

    @abstractmethod
    def _get_message(self) -> str:
        pass


class FieldNotFound(BaseBakingError):
    http_status_code = status.HTTP_404_NOT_FOUND
    code = ErrorCode.E1000_FIELD_NOT_FOUND

    def __init__(self, field_name: str):
        self.field_name = field_name

    def _get_message(self) -> str:
        return f"Field '{self.field_name}' not found"


class FieldNotFoundError(PydanticUserError):
    code = ErrorCode.E1000_FIELD_NOT_FOUND

    def __init__(self, field_name: str):
        self.field_name = field_name

    def _get_message(self) -> str:
        return f"Field '{self.field_name}' not found"


class BadFilterFormat(Exception):
    http_status_code = status.HTTP_400_BAD_REQUEST
    code = ErrorCode.E1001_BAD_FILTER_FORMAT

    def __init__(self, filter_name: str):
        self.filter_name = filter_name

    def _get_message(self) -> str:
        return f"Filter '{self.filter_name}' has invalid format"


class InvalidFilterError(PydanticUserError):
    code = ErrorCode.E1002_INVALID_FILTER

    def __init__(self, filter_name: str):
        self.filter_name = filter_name

    def _get_message(self) -> str:
        return f"Filter '{self.filter_name}' has invalid format"
