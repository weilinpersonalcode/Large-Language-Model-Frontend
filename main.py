
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTabWidget
from clock_calendar import ClockCalendarWidget
from chat_ui import ChatUI
from live2d_widget import Live2DWidget

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live2D Chat Application")
        self.setGeometry(100, 100, 800, 600)

        # Tab widget for switching between features
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add clock/calendar tab
        self.clock_calendar = ClockCalendarWidget()
        self.tabs.addTab(self.clock_calendar, "Clock & Calendar")

        # Add chat UI tab
        self.chat_ui = ChatUI()
        self.tabs.addTab(self.chat_ui, "AI Chat")

        # Add Live2D tab
        self.live2d = Live2DWidget()
        self.tabs.addTab(self.live2d, "Live2D")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
        