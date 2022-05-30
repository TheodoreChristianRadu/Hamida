from threading import Thread
from time import sleep


class Timer():

    def __init__(self, duration):
        self.duration = duration

    def __enter__(self):
        self.timer = Thread(target=sleep, args=[self.duration])
        self.timer.start()

    def __exit__(self, *args):
        self.timer.join()
