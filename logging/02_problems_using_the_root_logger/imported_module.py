import logging

logging.basicConfig(level=logging.INFO)


class Foo:
    def __init__(self):
        logging.info("Creating a Foo")


logging.info("logging from %s", __name__)
