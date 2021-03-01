import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QWidget()
w.setGeometry(100,50, 500, 500)
w.setWindowTitle("first GUI")
w.setWindowIcon(QIcon("python\\maze-solver\\img\\player.png"))
w.show()

sys.exit(app.exec_())