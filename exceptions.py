class MiceWheelException(Exception):
    """Base exception for this script.

    :note: This exception should not be raised directly."""
    pass

class CursorOutOfBoundsException(MiceWheelException):
    pass