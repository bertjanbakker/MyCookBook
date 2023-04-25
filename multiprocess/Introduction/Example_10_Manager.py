#!/usr/bin/env python3

# example from python documentation
import logging
from multiprocessing import Process, Manager

logging.basicConfig(level=logging.INFO)


def f(d, l):
    logging.info("executing f()")
    d[1] = "1"
    d["2"] = 2
    d[0.25] = None
    l.reverse()


if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        logging.info("before Process: (d, l) = (%s, %s)", d, l)
        p = Process(target=f, args=(d, l))
        logging.info("pid=%s, exitcode=%s", p.pid, p.exitcode)
        p.start()
        logging.info("after start Process: (d, l) = (%s, %s)", d, l)
        logging.info("pid=%s, exitcode=%s", p.pid, p.exitcode)
        p.join()
        logging.info("after join Process: (d, l) = (%s, %s)", d, l)
        logging.info("pid=%s, exitcode=%s", p.pid, p.exitcode)
