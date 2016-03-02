from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from PyQt5.QtCore import QTimer, QTime, QUrl, QFileInfo
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from alarm_ui import Ui_Form

class Alarm(QWidget):
    def __init__(self):
        super(Alarm, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.lineEdit.textChanged.connect(self.onTextChanged)
        self.ui.timeEdit.timeChanged.connect(self.onTimeChanged)
        self.ui.groupBox.toggled.connect(self.onGBToggle)
        self.ui.toolButton.clicked.connect(self.onToolButton)
        
        self.go = True
        self.ui.timeEdit.setTime(QTime.currentTime().addSecs(60))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.__alarm)
        self.timer.start(Alarm.__get_diff(self.ui.timeEdit.time()))
        
        self.music = "alarm.mp3"
        self.ui.track_label.setText("DEFAULT")
        
    def __get_diff(time):
        return QTime.currentTime().msecsTo(time)
        
    def onTextChanged(self, text):
        self.ui.groupBox.setTitle(text)
        
    def onTimeChanged(self, time):
        c_time = QTime.currentTime()
        if (c_time > time):
            self.ui.timeEdit.setTime(c_time)
            return
        diff = Alarm.__get_diff(self.ui.timeEdit.time().addSecs(60))
        print("TIME CHANGED", time, diff)
        self.timer.timer.start(diff + (60*1000))
        
    def onGBToggle(self, checked):
        print("ALARM ON IS", checked)
        self.go = checked
        
    def __alarm(self):
        if not self.go:
            return;
        self.timer.stop()
        player = QMediaPlayer(self);
        player.setMedia(QMediaContent(QUrl.fromLocalFile(self.music)));
        player.setVolume(100);
        player.play();
        self.setEnabled(False)
        QMessageBox.critical(self, "ALERTA", "TIME TO DIE<br>" + self.ui.groupBox.title(), QMessageBox.Yes)
        self.setEnabled(True)
        player.stop()
        player.deleteLater()
        
    def onToolButton(self):
        self.music = QFileDialog.getOpenFileName(self, "Open sound", "", "Sound (*.mp3 *.flac *.ogg)")[0]
        self.ui.track_label.setText(QFileInfo(self.music).baseName())
        print(self.music)

        