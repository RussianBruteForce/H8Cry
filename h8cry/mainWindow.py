from PyQt5.QtWidgets import QWidget
import sys
from mainWindow_ui import Ui_Form
from alarm import Alarm

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.plus_b.clicked.connect(self.onPlusButton)
        self.ui.minus_b.clicked.connect(self.onMinusButton)
        self.ui.exit_b.clicked.connect(self.onExitButton)
        
        self.alarm_list = []
        
    def onPlusButton(self):
        self.alarm_list.append(Alarm())
        self.ui.alarms_layout.addWidget(self.alarm_list[-1])
    
    def onMinusButton(self):
        self.alarm_list.pop(-1).deleteLater()
    
    def onExitButton(self):
        sys.exit()
    
        