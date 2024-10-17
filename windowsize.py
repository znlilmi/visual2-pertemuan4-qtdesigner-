# ============= Window Management ============================
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)

        self.button = QPushButton(self)
        self.button.setText("Button1")
        
        self.setGeometry(0, 0, 400, 400)  # Set window size and position
        self.setWindowTitle("Belajar PyQt5")  # Set window title

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
