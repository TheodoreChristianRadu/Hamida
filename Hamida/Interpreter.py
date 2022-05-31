from threading import Thread
from collections import defaultdict


class Interpreter(Thread):

    def __init__(self, brainfuck, stream):
        super().__init__()
        self.input = stream.input
        self.output = stream.output
        self.pointer = 0
        self.memory = defaultdict(int)
        self.code = Interpreter.transpile(brainfuck)

    @classmethod
    def transpile(cls, brainfuck):
        result = ''
        indent = ''
        for opcode in brainfuck:
            result += indent
            match(opcode):
                case '>': result += 'self.pointer += 1'
                case '<': result += 'self.pointer -= 1'
                case '+': result += 'self.memory[self.pointer] += 1'
                case '-': result += 'self.memory[self.pointer] -= 1'
                case ',': result += 'self.input.receive(self.memory[self.pointer])'
                case '.': result += 'self.output.send(self.memory[self.pointer])'
                case '[': result += 'while(self.memory[self.pointer]):'; indent += '\t'
                case ']': indent = indent[:-1]
            result += '\n'
        return compile(result, '<string>', 'exec')

    def run(self):
        exec(self.code)

    def __bool__(self):
        return self.is_alive()
