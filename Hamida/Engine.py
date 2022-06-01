from threading import Thread
from Interpreter import Interpreter
from Stream import Stream
from Timer import Timer


class Engine(Thread):

    def __init__(self, capacity, fps):
        Thread.__init__(self)
        self.delay = 1 / fps
        self.capacity = capacity
        self.buffer = capacity * [' ']
        self.stream = Stream()
        self.interpreter = None
        self.render = lambda buffer: None

    def run(self):
        while (True):
            with Timer(self.delay):
                # Send inputs
                for i in range(self.capacity):
                    self.buffer[i] = chr(self.stream.output.receive())
                self.render(self.buffer)

    def execute(self, brainfuck):
        if (not self.interpreter):
            self.interpreter = Interpreter(brainfuck, self.stream)
            self.interpreter.start()
        else:
            raise AlreadyRunning


class AlreadyRunning(Exception):

    def __init__(self):
        super().__init__("The engine is already executing some code")
