from flexx import flx
from Engine import Engine


class Screen(flx.Label):

    def init(self, *size):
        style = {
            'aspect-ratio': f'{size[0]} / {1.81 * size[1] * 0.7}',
            'background': 'black',
            'color': 'white',
            'font-family': 'monospace',
            'font-size': f'{100 / size[1] / 0.7}vh',
            'line-height': '0.7em',
            'word-break' : 'break-all'
            }
        self.apply_style(style)
        self.set_wrap(1)


class Hamida(flx.PyWidget):

    def init(self):
        with flx.HBox():
            self.button = flx.Button(text='Start')
            self.screen = Screen(32, 16)
        self.engine = Engine(32 * 16, 10)
        self.engine.render = self.render

    @flx.reaction('button.pointer_click')
    def start(self, *events):
        self.engine.start()
        self.engine.execute('>+++++[<++++++++++>-]<[++.-.-.]')

    @flx.reaction
    def render(self, *events):
        self.screen.set_text(''.join(self.engine.buffer))


if __name__ == '__main__':
    flx.App(Hamida).launch('Browser')
    flx.run()
