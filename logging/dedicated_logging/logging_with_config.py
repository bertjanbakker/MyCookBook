import logging
import logging.config

logging.config.fileConfig('logging_config.ini')

# Create logger instances
root_logger = logging.getLogger()
my_logger = logging.getLogger('my_logger')

# Use the loggers
root_logger.debug("This is a debug message from the root logger.")
my_logger.info("This is an info message from my_logger.")

