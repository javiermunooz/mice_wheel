from PyQt5.QtGui import QGuiApplication

from controllers import QCursorController

app = QGuiApplication([])
cursor = QCursorController((0,0),(1000,1000))
cursor.randomize(interval=2)
app.exec_()
app.exit()