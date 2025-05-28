#!/usr/bin/env python3

import logging

logging.basicConfig(level="DEBUG")


class Typed:
    expected_type = object
    logger = logging.getLogger("Typed")

    def __set_name__(self, cls, name):
        Typed.logger.debug(f"__set_name__({self},{cls},{name})")
        self.key = name

    def __get__(self, instance, cls):
        Typed.logger.debug(f"__get__({self},{instance},{cls})")
        if instance:
            return instance.__dict__[self.key]
        else:
            return self

    def __set__(self, instance, value):
        Typed.logger.debug(f"__set__({self},{instance},{value})")
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type} but got {type(value)}")
        instance.__dict__[self.key] = value

    def __delete__(self, instance):
        raise AttributeError(f"Can't delete attribute '{self.key}' from {instance=}")


class Integer(Typed):
    expected_type = int


class Float(Typed):
    expected_type = float


class String(Typed):
    expected_type = str


class Account:
    owner = String()
    balance = Float()
    logger = logging.getLogger("Account")

    def __init__(self, owner, balance):
        self.logger.debug(f"__init__({owner}, {balance})")
        self.owner = owner
        self.balance = balance


def main():
    logger = logging.getLogger("Descriptors")
    a = Account("Guido", 1000.0)
    b = a.owner
    a.owner = "Eva"
    try:
        del a.owner
    except Exception as e:
        logger.error(f"{e}")
    try:
        del a.balance
    except Exception as e:
        logger.error(f"{e}")
    try:
        a.balance = "a lot"
    except Exception as e:
        logger.error(f"{e}")


if __name__ == "__main__":
    main()
