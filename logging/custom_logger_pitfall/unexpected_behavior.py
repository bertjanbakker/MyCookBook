import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.warning("This will show")
logger.debug("This will not show")
