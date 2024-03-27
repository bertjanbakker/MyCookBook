import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.warning("This warning message will show")
logger.debug("This debug message will not show")
