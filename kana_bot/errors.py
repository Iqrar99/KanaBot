class Error(Exception):
    """Base class for other exceptions."""
    pass

class KanaTypeError(Error):
    """Raised when Kana type is not recognize."""
    pass
