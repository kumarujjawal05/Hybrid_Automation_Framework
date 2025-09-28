import logging
import os
from datetime import datetime


class Logger:
    _logger = None
    _log_file_path = None

    @staticmethod
    def setup_logger(log_level=logging.INFO):
        if Logger._logger:
            Logger._logger.setLevel(log_level)
            return Logger._logger

        # Create logs directory if not exists
        logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(logs_dir, exist_ok=True)

        # Create log filename with timestamp (only once per session)
        Logger._log_file_path = os.path.join(
            logs_dir, f"test_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        )

        logger = logging.getLogger("SauceDemo-Automation")
        logger.setLevel(log_level)
        logger.propagate = False

        # Ensure we start with a clean slate of handlers
        logger.handlers.clear()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

        file_handler = logging.FileHandler(Logger._log_file_path, mode="a")
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        Logger._logger = logger
        return Logger._logger
