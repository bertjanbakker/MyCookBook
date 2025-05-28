#!/usr/bin/env python3


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


def main():
    a = Account('Guido', 1000)
    print(f"{a = }")
    print(f"{id(a) = }")
    print(f"{a.__dict__ = }")
    a.number = 123456
    print(f"{a.__dict__ = }")
    a.__dict__["number"] = 654321
    print(f"{a.__dict__ = }")

    print(f"{a.__class__ = }")
    print(f"{Account.__dict__.keys() = }")
    print(f"{Account.__dict__['__weakref__'] = }")
    print(f"{type(Account.__dict__['__weakref__']) = }")

    print(f"{Account.__bases__ = }")
    print(f"{Account.__mro__ = }")
    print(f"{dir(Account) = }")
    print(f"{Account.__dir__ = }")

    print(f"{dir(a) = }")
    print(f"{a.__dir__ = }")


if __name__ == "__main__":
    main()
