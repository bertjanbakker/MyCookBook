# SuperFastPython.com
# example of extending the Thread class
from time import sleep
from threading import Thread
import logging


# custom thread class
class CustomThread(Thread):
    # override the run function
    def run(self):
        # block for a moment
        sleep(1)
        # display a message
        logger.info('This is coming from another thread')
        self.value = 99


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(name)s [%(levelname)s] %(message)s"
    )
    logger = logging.getLogger("example03")
    # create the thread
    thread = CustomThread()
    # start the thread
    thread.start()
    # wait for the thread to finish
    logger.info('Waiting for the thread to finish')
    thread.join()
    value = thread.value
    logger.info(f'Got: {value}')


