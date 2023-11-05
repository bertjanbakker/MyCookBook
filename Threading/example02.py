#!/usr/bin/env python

from threading import Thread
from time import sleep


def task(sleep_time, message):
    sleep(sleep_time)
    print(message)


thread = Thread(target=task, args=[1.5, "New message from another thread"])

thread.start()
print('Waiting for the thread...')
thread.join()
