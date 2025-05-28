import logging

import imported_module

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

f = imported_module.Foo()
logging.debug("logging from %s", __name__)
logging.info("logging from %s", __name__)
