#!/opt/python3/bin/python3
# Author: zhaoyong
import os
import logging
from logging import handlers
from django.conf import settings


class Logger(object):
    """日志类"""
    def __init__(self):
        self.run_log_file = settings.RUN_LOG_FILE
        self.error_log_file = settings.ERROR_LOG_FILE
        self.run_logger = None
        self.error_logger = None
        self.initialize_run_log()
        self.initialize_error_log()

    @staticmethod
    def check_path_exist(log_abs_file):
        log_path = os.path.split(log_abs_file)[0]
        if not os.path.exists(log_path):
            os.mkdir(log_path)

    def initialize_run_log(self):
        """初始化运行日志"""
        self.check_path_exist(self.run_log_file)
        file_1_1 = handlers.TimedRotatingFileHandler(filename=self.run_log_file, when='D', interval=1, backupCount=0, encoding='utf-8')
        fmt = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')
        file_1_1.setFormatter(fmt=fmt)
        logger1 = logging.Logger(name='run.log', level=logging.INFO)
        logger1.addHandler(hdlr=file_1_1)
        self.run_logger = logger1

    def initialize_error_log(self):
        """初始化错误日志"""
        self.check_path_exist(self.error_log_file)
        file_1_1 = handlers.TimedRotatingFileHandler(filename=self.error_log_file, when='D', interval=1, backupCount=0, encoding='utf-8')
        fmt = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s')
        file_1_1.setFormatter(fmt=fmt)
        logger1 = logging.Logger(name='error.log', level=logging.ERROR)
        logger1.addHandler(hdlr=file_1_1)
        self.error_logger = logger1

    def info(self, message):
        """写入info日志"""
        self.run_logger.info(message)

    def error(self, message):
        """写入error日志"""
        self.error_logger.error(message)