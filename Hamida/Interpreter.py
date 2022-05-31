from threading import Thread
from collections import defaultdict


class Interpreter(Thread):

    def __init__(self, brainfuck, stream):
        super().__init__()
        self.brainfuck = brainfuck
        self.input = stream.input
        self.output = stream.output
        self.pointer = 0
        self.memory = defaultdict(int)

    def __bool__(self):
        return self.is_alive()

    def run(self):
        for opcode in self.brainfuck:
            match(opcode):
                case '>': self.pointer += 1
                case '<': self.pointer -= 1
                case '+': self.memory[self.pointer] += 1
                case '-': self.memory[self.pointer] -= 1
                case '.': self.output.send(self.memory[self.pointer])
                case ',': self.input.receive(self.memory[self.pointer])
