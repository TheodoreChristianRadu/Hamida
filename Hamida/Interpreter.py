from threading import Thread
from Memory import Memory


class Interpreter(Thread):

    def __init__(self, brainfuck, stream):
        Thread.__init__(self)
        self.code = Interpreter.transpile(brainfuck)
        self.memory = Memory(int)
        self.stream = stream

    @classmethod
    def transpile(cls, brainfuck):
        result = ''
        indent = ''
        for opcode in brainfuck:
            result += indent
            match(opcode):
                case '>': result += 'pointer += 1'
                case '<': result += 'pointer -= 1'
                case '+': result += 'memory[pointer] += 1'
                case '-': result += 'memory[pointer] -= 1'
                case ',': result += 'input.receive(memory[pointer])'
                case '.': result += 'output.send(memory[pointer])'
                case '[': result += 'while(memory[pointer]):'; indent += '\t'
                case ']': indent = indent[:-1]
            result += '\n'
        return compile(result, '<string>', 'exec')

    def run(self):
        variables = {
            'pointer': 0,
            'memory': self.memory,
            'input': self.stream.input,
            'output': self.stream.output
            }
        exec(self.code, variables)

    def __bool__(self):
        return self.is_alive()
