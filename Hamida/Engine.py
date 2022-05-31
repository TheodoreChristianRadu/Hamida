from threading import Thread
from Interpreter import Interpreter
from Stream import Stream
from Timer import Timer


class Engine(Thread):

    def __init__(self, capacity, fps):
        super().__init__()
        self.delay = 1 / fps
        self.capacity = capacity
        self.buffer = capacity * [' ']
        self.stream = Stream()
        self.interpreter = None
        self.render = lambda: None

    def run(self):
        while (True):
            with Timer(self.delay):
                # Send inputs
                for i in range(self.capacity):
                    self.buffer[i] = chr(self.stream.output.receive())
                self.render()

    def execute(self, brainfuck):
        if (not self.interpreter):
            self.interpreter = Interpreter(brainfuck, self.stream)
            self.interpreter.start()
        else:
            raise AlreadyRunning


class AlreadyRunning(Exception):

    def __init__(self):
        super().__init__("The engine is already executing some code")
