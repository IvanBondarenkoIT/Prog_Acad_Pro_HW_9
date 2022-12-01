import logging


class MyLoger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.INFO)
        __formatter = logging.Formatter('%(asctime) s %(name)-12s %(levelname)-8s %(message)s')

        __filehandler = logging.FileHandler(f'{__name__}.log')
        __filehandler.setLevel(logging.INFO)
        __filehandler.setFormatter(__formatter)

        __streamhandler = logging.StreamHandler()
        __streamhandler.setLevel(logging.WARNING)
        __streamhandler.setFormatter(__formatter)
        self.logger.addHandler(__filehandler)
        self.logger.addHandler(__streamhandler)

    def add_warning(self, message):
        self.logger.warning(message)

    def add_info(self, message):
        self.logger.info(message)
