from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QTextBrowser
from PyQt6.QtGui import QAction, QFont, QTextOption
from PyQt6.QtCore import pyqtSignal
from Engine import Engine, AlreadyRunning


class Screen(QTextBrowser):

    render = pyqtSignal(str)

    def __init__(self):
        QTextBrowser.__init__(self)
        font = QFont('Monospace')
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setPixelSize(30)
        self.setFont(font)
        self.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)
        self.render.connect(lambda data: self.setText(data))


class Toolbar(QToolBar):

    def __init__(self):
        QToolBar.__init__(self)
        self.play = QAction('Test')
        self.addAction(self.play)


class Window(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.screen = Screen()
        self.setCentralWidget(self.screen)
        self.toolbar = Toolbar()
        self.addToolBar(self.toolbar)


class Application(QApplication):
    
    def __init__(self, name):
        QApplication.__init__(self, [])
        self.setApplicationName(name)
        self.engine = Engine(32 * 16, 10)
        self.engine.start()
        self.engine.render = lambda buffer: self.update(buffer)
        self.window = Window()
        self.window.toolbar.play.triggered.connect(lambda: self.play())

    def play(self):
        try:
            self.engine.execute('>+++++[<++++++++++>-]<[++.-.-.]')
        except AlreadyRunning as exception:
            print(exception)

    def update(self, buffer):
        self.window.screen.render.emit(''.join(buffer))

    def exec(self):
        self.window.showMaximized()
        QApplication.exec()


if __name__ == '__main__':
    hamida = Application('Hamida')
    hamida.exec()
