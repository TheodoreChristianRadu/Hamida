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

    def display(self):
        self.set_text(1000 * "I WANNA See how IT LOOks")


class Window(flx.Widget):

    def init(self):
        with flx.HBox():
            Screen(32, 16).display()


if __name__ == '__main__':
    hamida = Engine(32 * 16, 10)
    hamida.start()
    hamida.execute('+++' + '.' * 10000)
    flx.App(Window).launch('Browser')
    flx.run()
