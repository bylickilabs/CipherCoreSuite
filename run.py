from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from ciphercore.ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon("assets/ciphercore.ico"))

    window = MainWindow()
    window.setWindowIcon(QIcon("assets/ciphercore.ico"))
    window.show()

    app.exec()