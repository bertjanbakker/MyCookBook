import logging


def try_logging_at_different_levels():
    logger.warning("This will show, because of level warning")
    logger.debug("Will this show? It's level debug")


# create the custom logger
logger = logging.getLogger(__name__)

# only warnings will be shown
try_logging_at_different_levels()

# now add a custom handler
handler = logging.StreamHandler()
logger.addHandler(handler)

# still only warnings will be shown
try_logging_at_different_levels()

logger.setLevel(logging.DEBUG)

# now debug logs will be shown as well
try_logging_at_different_levels()
