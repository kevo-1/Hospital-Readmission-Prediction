import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QApplication

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200, 800)
        self.MainLayout = QVBoxLayout()
        
        self.setLayout(self.MainLayout)        
    

def run():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())