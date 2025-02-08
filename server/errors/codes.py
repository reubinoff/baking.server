import enum


class ErrorCode(enum.StrEnum):
    E1000_FIELD_NOT_FOUND = "E1000_FieldNotFound"
    E1001_BAD_FILTER_FORMAT = "E1001_BadFilterFormat"
    E1002_INVALID_FILTER = "E1002_InvalidFilter"
