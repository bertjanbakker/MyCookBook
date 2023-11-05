#!/usr/bin/env python

from threading import Thread
from time import sleep


def task():
    sleep(1)
    print('This is from another thread')


thread = Thread(target=task)

thread.start()
print('Waiting for the thread...')
thread.join()
