from PyQt5.QtWidgets import QApplication#, QSystemTrayIcon
from PyQt5.QtGui import QIcon
import sys
from mainWindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
#    tray = QSystemTrayIcon()
#    tray.setIcon(QIcon("icons/h8code.png"))
#    tray.show()
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
