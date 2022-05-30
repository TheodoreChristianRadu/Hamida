from threading import Thread


class Interpreter(Thread):

    def __init__(self, brainfuck, stream, memory = 1000):
        super().__init__()
        self.brainfuck = brainfuck
        self.input = stream.input
        self.output = stream.output
        self.pointer = 0
        self.memory = memory * [0]

    def __bool__(self):
        return self.is_alive()

    def run(self):
        for opcode in self.brainfuck:
            match(opcode):
                case '>': self.pointer += 1
                case '<': self.pointer -= 1
                case '+': self.memory[self.pointer] += 1
                case '-': self.memory[self.pointer] -= 1
                case '.': self.output(self.memory[self.pointer])
                case ',': self.input.expect(self.memory[self.pointer])
