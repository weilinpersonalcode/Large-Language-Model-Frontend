
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCalendarWidget
from PySide6.QtCore import QTimer, QTime, Qt

class ClockCalendarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock and Calendar")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()

        # Clock
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.time_label)

        # Calendar
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)

        self.setLayout(self.layout)
        self.update_time()

        # Timer to update time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)
        