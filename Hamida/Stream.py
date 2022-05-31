from queue import SimpleQueue as Queue


class Stream():

    def __init__(self):
        self.input = Input()
        self.output = Output()


class Input():

    def __init__(self):
        self.queue = Queue()
        self.request = False

    def send(self, value):
        if (self.request):
            self.queue.put(value)

    def receive(self):
        self.request = True
        result = self.queue.get()
        self.request = False
        return result


class Output():

    def __init__(self):
        self.queue = Queue()

    def send(self, value):
        self.queue.put(value)

    def receive(self):
        return self.queue.get()
