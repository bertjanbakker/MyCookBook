import logging


def try_logging_at_different_levels():
    logger.warning("This warning message will show, because of level warning")
    logger.debug("Will this show? It's level debug")


# create the custom logger
logger = logging.getLogger(__name__)

try_logging_at_different_levels()  # only warnings will be shown

# now add a custom handler
handler = logging.StreamHandler()
logger.addHandler(handler)

try_logging_at_different_levels()  # still only warnings will be shown

logger.setLevel(logging.DEBUG)

try_logging_at_different_levels()  # now debug logs will be shown as well
