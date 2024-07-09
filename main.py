from PySide6.QtWidgets import QApplication
import sys
from src.logica.Calculos import Mysidebar

app = QApplication(sys.argv)
window = Mysidebar()
window.show()
sys.exit(app.exec())