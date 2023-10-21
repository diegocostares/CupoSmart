import logging
import os

from dotenv import load_dotenv

load_dotenv()

# Códigos de color ANSI
COLORS = {
    "DEBUG": "\033[94m",  # Azul
    "INFO": "\033[92m",  # Verde
    "WARNING": "\033[93m",  # Amarillo
    "ERROR": "\033[91m",  # Rojo
    "CRITICAL": "\033[31m",  # Rojo oscuro
    "ENDC": "\033[0m",  # Resetea el color
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        color = COLORS.get(levelname, COLORS["ENDC"])
        record.levelname = f"{color}{levelname}{COLORS['ENDC']}"
        return super().format(record)


def logger_config(name: str) -> logging.Logger:
    log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    log_file = os.getenv("LOG_FILE", None)

    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)

    formatter = ColoredFormatter(
        "%(levelname)s: \t %(asctime)s - %(name)s - %(message)s"
    )

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
