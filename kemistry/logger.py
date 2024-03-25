import logging
from logging.handlers import RotatingFileHandler


def configure_logging(app):
    # Configure logging to a file
    log_file_path = app.config.get("LOG_FILE_PATH", "kemistry.log")
    handler = RotatingFileHandler(log_file_path, maxBytes=100000, backupCount=5)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # Configure logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    app.logger.addHandler(console_handler)

    # Set the Flask app logger level
    app.logger.setLevel(logging.DEBUG)
