import logging

from custom_logging_formatter import CustomFormatter


# Configure logging
def setup_logger(log_file: str = 'agent.log'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Remove any existing handlers to prevent duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Formatter
    formatter = CustomFormatter()
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
