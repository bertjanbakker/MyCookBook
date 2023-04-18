#!/usr/bin/env python
r"""MultiProcessQueue to let a collection of items be processed by
    multiple processes in simultaneously.
    
    Copyright BertJan Bakker, 2023-04-17."""

import logging
import multiprocessing
import queue
import traceback
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class ItemEntry(object):
    r"""ItemEntry holds info about one item that is put on the queue of the MultiProcessQueue.
    Normally it is created when an item is taken from this queue prior to handling it.
    After the item has been handled the ItemEntry can be completed with the handling
    result. When used in this way the ItemEntry will record start and finish times."""

    def __init__(self, _item, _start=None, _finish=None, _result=None):
        r"""item is mandatory, start will be filled if not provided."""
        self.item = _item
        self.start = _start
        if self.start is None:
            self.start = datetime.now()
        self.finish = _finish
        self.result = _result

    def complete(self, _result, _finish=None):
        r"""result is mandatory, finish will be filled if not provided."""
        self.result = _result
        self.finish = _finish
        if self.finish is None:
            self.finish = datetime.now()

    def __repr__(self):
        r"""the usual"""
        _result = [
            "item: %s" % self.item,
            "start: %s" % self.start,
            "finish: %s" % self.finish,
            "result: %s" % self.result,
        ]
        return "\t".join(_result)


class MultiProcessQueue(object):
    r"""Multi Processing Queue"""

    def __init__(self, _itemhandler, _qsize=multiprocessing.cpu_count()):
        r"""Setup of manager, queue, stop event, processes.
        Will start the main loop of the processes."""
        self.itemhandler = _itemhandler
        self.qsize = _qsize
        self.logger = logging.getLogger("MultiProcessQueue")
        _manager = multiprocessing.Manager()
        self.logger.debug("main proc, create queue of size %d", self.qsize)
        self.queue = _manager.Queue(self.qsize)
        self.logger.debug("main proc, create stop event")
        self.stop_event = _manager.Event()
        self.logger.debug("main proc, create shared dict")
        self.shdict = _manager.dict()
        self.shlist = _manager.list()
        self.logger.debug("main proc, create %d sub-processes", self.qsize)
        self.processes = [
            self._create_process(procnum) for procnum in range(self.qsize)
        ]
        self.logger.debug("main proc, starting sub-processes")
        [p.start() for p in self.processes]
        self.logger.debug("main proc, sub-processes started, setup done")

    def put(self, _item):
        r"""Put the specified item on the queue to be processed."""
        self.queue.put(_item)

    def _create_process(self, procnum):
        r"""Create a new Process that consumes items from the queue."""
        return multiprocessing.Process(target=self._qconsumer, args=[procnum])

    def _qconsumer(self, procnum):
        r"""Generic function, one per process, that takes items
        from the queue and calls the itemhandler on each of them.
        It will keep doing this until the stop event is set.
        The queue will be notified of each completion of the
        itemhandler call.
        When an exception is raised during the itemhandler
        call the queue is still notified. Otherwise the
        queue would keep blocking when calling join on it
        (in finish) even when all items are taken."""
        # create a logger that's private to the process
        _logger = logging.getLogger("proc%02d" % procnum)
        q_timeout = 0.1
        _logger.debug("proc %02d starting", procnum)
        # Keep looping until the stop event is set, even when the queue is empty.
        # Doing so prevents the loop from prematurely exiting (e.g. before the
        # first item is queued).
        while not self.stop_event.is_set():
            try:
                _item = self.queue.get(timeout=q_timeout)
                _logger.debug("proc %02d took from queue: %s", procnum, _item)
            except queue.Empty as q_ex:
                _logger.debug("proc %02d queue timeout %s", procnum, q_ex)
            else:
                try:
                    item_entry = ItemEntry(_item)
                    _logger.debug("proc %02d start %s", procnum, item_entry)
                    #
                    item_result = None
                    # pr = profile.Profile()
                    # pr.enable()
                    # profile.runctx('item_result = self.itemhandler(_item)', globals(), locals(), filename="OpenGLContext.profile")
                    item_result = self.itemhandler(_item)
                    # pr.disable()
                    # pr.dump_stats("OpenGLContext.profile")
                    #
                    item_entry.complete(item_result)
                    _logger.debug("proc %02d finished %s", procnum, item_entry)
                    self.shlist.append(item_entry)
                except Exception as ex:
                    _logger.info("proc %02d caught exception %s", procnum, ex)
                    traceback.print_exc()
                finally:
                    self.queue.task_done()
        _logger.debug("proc %d finish", procnum)

    def _join(self, proc):
        self.logger.debug("joining proc %s", proc)
        proc.join()

    def finish(self):
        r"""To be called when all items are queued.
        Note the order. First wait for the queue to be empty,
        then set the flag, finally wait for each process to finish."""
        self.logger.debug("main proc, finishing, waiting for queue items processing")
        self.queue.join()
        self.logger.debug("main proc, all queue items done, setting stop event")
        self.stop_event.set()
        self.logger.debug("main proc, stop event set, waiting for processes to finish")
        [self._join(process) for process in self.processes]
        self.logger.debug("main proc, all processes finished, bye")
        return self.shlist


if __name__ == "__main__":
    import time

    LOGGER = logging.getLogger(__name__)

    def default_itemhandler(_item):
        r"""item handler for testing."""
        LOGGER.info("handling item %s", _item)
        time.sleep(2)
        if _item[0] == 20:
            raise Exception("This is a test exception")
        return True

    MPQ = MultiProcessQueue(default_itemhandler)

    for i in range(22):
        item = [i, None, "hello"]
        LOGGER.info("main proc, put on queue: item %s", item)
        MPQ.put(item)
        time.sleep(0.1)

    RESULT = MPQ.finish()
    LOGGER.info(RESULT)
