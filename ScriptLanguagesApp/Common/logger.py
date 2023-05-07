import logging

class Logger:
    def __init__(self, name='PC-CREATOR-LOGGER'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def log(self, level, message):
        getattr(self.logger, level.lower())(message)