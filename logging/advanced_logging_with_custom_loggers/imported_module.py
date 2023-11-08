import logging

formatter = logging.Formatter("%(asctime)s - %(levelname)s:%(name)s:%(message)s")
log_handler = logging.FileHandler("employee.log")
log_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)


class Foo:

    def __init__(self):
        logger.info("creating a Foo")


logger.info("logging from %s", __name__)