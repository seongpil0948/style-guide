import logging
import sys
from os.path import join as opjoin
import os

APP_LOGGER_NAME = 'SpApp'


def setup_applevel_logger(logger_name=APP_LOGGER_NAME, file_name=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)
    if file_name:
        fh = logging.FileHandler(file_name)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger


def get_logger(module_name):
    return logging.getLogger(APP_LOGGER_NAME).getChild(module_name)


class Logger:
    def setup_logger(self, log_save_path, name):
        if not os.path.exists(log_save_path):
            os.makedirs(log_save_path, exist_ok=True)
        file_name = f"{name}.log"

        logger = logging.getLogger(APP_LOGGER_NAME)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        sh = logging.StreamHandler(sys.stdout)
        sh.setFormatter(formatter)
        logger.handlers.clear()
        logger.addHandler(sh)
        if file_name:
            fh = logging.FileHandler(file_name)
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        return logger

    def init_logger(self, log_save_path, name):
        self.logger = logging.getLogger(
            APP_LOGGER_NAME).getChild(name)
        self.setup_logger(log_save_path, name)
