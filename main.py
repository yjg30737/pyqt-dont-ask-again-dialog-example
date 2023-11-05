import os, sys

# Get the absolute path of the current script file
script_path = os.path.abspath(__file__)

# Get the root directory by going up one level from the script directory
project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)
sys.path.insert(0, os.getcwd())  # Add the current directory as well

from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog

from dontAskAgainDialog import DontAskAgainDialog

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support

QApplication.setFont(QFont('Arial', 12))


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Click this to close')
        btn.clicked.connect(self.close)
        self.setCentralWidget(btn)

    def closeEvent(self, e):
        dialog = DontAskAgainDialog()
        if dialog.isAskAgainEnabled():
            e.accept()
        else:
            reply = dialog.exec()
            if reply == QDialog.Accepted:
                e.accept()
            else:
                e.ignore()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())