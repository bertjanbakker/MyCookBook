#!/usr/bin/env python3

# example from python documentation

import multiprocessing as mp


def foo(q):
    q.put("hello")


if __name__ == "__main__":
    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
