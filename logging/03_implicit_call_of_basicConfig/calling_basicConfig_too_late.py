import logging

logging.warning("a warning using the root logger")
logging.debug("a debug using the root logger")

logging.basicConfig(level=logging.DEBUG)

logging.warning("a warning using the root logger")
logging.debug("a debug using the root logger")
