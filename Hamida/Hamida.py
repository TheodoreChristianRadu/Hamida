from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QFont, QAction
from PyQt6.QtCore import pyqtSignal, Qt
from Engine import Engine, AlreadyFucking


class Screen(QWidget):

    update = pyqtSignal(list)

    def __init__(self, *size):
        QWidget.__init__(self)
        self.width, self.height = size
        self.grid = QGridLayout()
        self.grid.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for i in range(self.height):
            for j in range(self.width):
                self.grid.addWidget(self.Element(), i, j)
        self.setLayout(self.grid)
        self.update.connect(lambda data: self.render(data))

    class Element(QLabel):
         def __init__(self):
             QLabel.__init__(self)
             font = QFont('Monospace')
             font.setStyleHint(QFont.StyleHint.Monospace)
             font.setPixelSize(50)
             self.setFont(font)

    def render(self, data):
        for i in range(len(data)):
                element = self.grid.itemAt(i).widget()
                element.setText(data[i])


class Toolbar(QToolBar):

    def __init__(self):
        QToolBar.__init__(self)
        self.play = QAction('Play')
        self.addAction(self.play)


class Application(QApplication, QMainWindow):
    
    def __init__(self, name, size):
        QApplication.__init__(self, [])
        self.setApplicationName(name)
        self.window = QMainWindow()
        self.screen = Screen(*size)
        self.window.setCentralWidget(self.screen)
        self.toolbar = Toolbar()
        self.toolbar.play.triggered.connect(lambda: self.play())
        self.window.addToolBar(self.toolbar)
        self.engine = Engine(size[0] * size[1], 10)
        self.engine.start()
        self.engine.render = lambda buffer: self.update(buffer)

    def play(self):
        try:
            self.engine.execute('>+++++[<++++++++++>-]<[++.-.-.]')
        except AlreadyFucking as exception:
            print(exception)

    def update(self, buffer):
        self.screen.update.emit(buffer)

    def exec(self):
        self.window.showMaximized()
        QApplication.exec()


if __name__ == '__main__':
    hamida = Application('Hamida', (32, 16))
    hamida.exec()
