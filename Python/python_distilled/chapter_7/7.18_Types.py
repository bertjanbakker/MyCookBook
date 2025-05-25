#!/usr/bin/env python3

class A:
    pass


class B(A):
    pass


class C(B):
    pass


def hierarchy():
    a = A()
    b = B()
    c = C()

    print(f"{type(a) = }")
    print(f"{isinstance(a, A) = }")
    print(f"{isinstance(b, A) = }")
    print(f"{isinstance(b, C) = }")

    print(f"{issubclass(B, A) = }")
    print(f"{issubclass(C, A) = }")


class Stream:
    def receive(self):
        raise NotImplementedError()

    def send(self, msg):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


def main():
    hierarchy()

if __name__ == "__main__":
    main()
