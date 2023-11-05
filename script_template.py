#!/usr/bin/env python3

import argparse
import logging
import os

# Define constants
MY_CONSTANT = 42
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(level=logging.DEBUG)
# Create a logger instance
logger = logging.getLogger(__name__)


def set_log_level(log_level: str) -> None:
    numeric_level = getattr(logging, log_level.upper(), None)
    print("numeric level is ", numeric_level)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")
    logger.setLevel(numeric_level)


def set_log_format(log_format: str) -> None:
    formatter = logging.Formatter(log_format)
    for handler in logger.handlers:
        handler.setFormatter(formatter)


def main(args: argparse.Namespace) -> int:
    # Your script's main logic goes here
    logger.warning("this is a message at warning level")
    logger.info(f"Hello, {args.name}! My constant is {MY_CONSTANT}")
    logger.debug("this is a message at debug level")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple command line script")

    # Define command line arguments
    parser.add_argument("name", help="Name to greet")

    # Parse command line arguments
    args = parser.parse_args()

    # Set the logging level using an environment variable (if provided)
    log_level = os.environ.get("LOG_LEVEL", "INFO")
    print(log_level)

    set_log_level(log_level)

    # Set the log format using the constant
    set_log_format(LOG_FORMAT)

    # Call the main function with parsed arguments
    raise SystemExit(main(args))
