#!/usr/bin/env python3

import logging

logging.basicConfig(level="DEBUG")


class Lazy:
    logger = logging.getLogger("Lazy")

    def __init__(self, func):
        self.logger.debug(f"__init__({self}, {func})")
        self.func = func

    def __set_name__(self, cls, name):
        self.logger.debug(f"__set_name__({self}, {cls}, {name})")
        self.key = name

    def __get__(self, instance, cls):
        self.logger.debug(f"__get__({self}, {instance}, {cls}, {self.key})")
        if instance:
            value = self.func(instance)
            instance.__dict__[self.key] = value
            return value
        else:
            return self


class Rectangle:
    logger = logging.getLogger(f"{__module__}.{__qualname__}")

    def __init__(self, width, height):
        self.logger.debug(f"__init__({width}, {height})")
        self.width = width
        self.height = height

    area = Lazy(lambda self: self.width * self.height)
    perimeter = Lazy(lambda self: 2 * self.width + 2 * self.height)


def main():
    logger = logging.getLogger("Main")
    logger.info("Start")
    r = Rectangle(3, 4)
    logger.debug(f"{r.__dict__ = }")
    logger.debug(f"{r.area = }")
    logger.debug(f"{r.perimeter = }")
    logger.debug(f"{r.__dict__ = }")
    logger.debug(f"{r.area = }")
    logger.debug(f"{r.perimeter = }")


if __name__ == "__main__":
    main()
