from PyQt5.QtWidgets import QApplication
from window.mainWindow import MainPage



app = QApplication([])
window = MainPage()
window.show()
app.exec()
