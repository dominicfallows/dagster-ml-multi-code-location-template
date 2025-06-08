from . import io
from . import tokenizer

__all__ = ["io", "tokenizer"]

def shared_function():
    """Shared function for demonstration purposes."""
    import logging
    logging.info("shared_function called.")
    return "Shared function called."