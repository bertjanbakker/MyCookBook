import logging
import imported_module

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
log_handler = logging.FileHandler("test.log")
log_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(log_handler)
logger.setLevel(logging.DEBUG)

f = imported_module.Foo()

logger.debug("logging from %s", __name__)
