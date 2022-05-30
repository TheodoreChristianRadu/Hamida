from queue import SimpleQueue as Queue


class Stream():

    def __init__(self):
        self.input = Input()
        self.output = Output()


class Input():

    def __init__(self):
        self.queue = Queue()
        self.request = False

    def __call__(self, value):
        if (self.request):
            self.queue.put(value)

    def expect(self):
        self.request = True
        result = self.queue.get()
        self.request = False
        return result


class Output():

    def __init__(self):
        self.queue = Queue()

    def __call__(self, value):
        self.queue.put(value)

    def read(self):
        while (not self.queue.empty()):
            yield self.queue.get()
