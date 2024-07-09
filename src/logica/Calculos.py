from src.vista.menuGUI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PySide6.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtWidgets import QVBoxLayout, QDialog

class MatplotlibWidget(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

class GraphWindow(QDialog):
    def __init__(self, x_data, y_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Graph Window")
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        self.canvas = MatplotlibWidget(self)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.plot_graph(x_data, y_data)

    def plot_graph(self, x_data, y_data):
        self.canvas.axes.clear()
        self.canvas.axes.plot(x_data, y_data, 'r-')
        self.canvas.axes.set_title('Método de Euler')
        self.canvas.axes.set_xlabel('x')
        self.canvas.axes.set_ylabel('y')
        self.canvas.draw()


class Mysidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.stackedWidget.setCurrentIndex(0)

        # Ocultar barra iconos
        self.frame_Iconos.setHidden(True)

        # Conexiones de botones para cambiar de página y actualizar label
        self.btn_Inicio.clicked.connect(self.switch_to_Inicio_page)
        self.btn_Info.clicked.connect(self.switch_to_Infor_page)
        self.btn_Calcular.clicked.connect(self.calcular_euler)

        self.btn_Me_Euler_1.clicked.connect(lambda: self.switch_to_Metod_page("METODO DE EULER - 1ER ORDEN"))
        self.btn_Me_Euler_2.clicked.connect(lambda: self.switch_to_Metod_page("METODO DE EULER - 1ER ORDEN"))
        self.btn_Me_Tylor_1.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE TAYLOR - 2DO ORDEN"))
        self.btn_Me_Tylor_2.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE TAYLOR - 2DO ORDEN"))
        self.btn_Me_EM_1.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE EULER -> MOD 2"))
        self.btn_Me_EM_2.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE EULER -> MOD 2"))
        self.btn_Me_Runge_1.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE RUNGE - KUTTA 4TO ORDEN"))
        self.btn_Me_Runge_2.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE RUNGE - KUTTA 4TO ORDEN"))

        # Configuración inicial de la tabla
        self.setup_table()

        # Aplicar estilo a la cabecera de la tabla
        self.tableWidget_Matriz.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: black;
                color: white;
                text-align:center;
            }
        """)

        self.tableWidget_Matriz.verticalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: black;
                color: white;
                text-align:center;
            }
        """)



    # Alternar entre páginas y actualizar label
    def switch_to_Inicio_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_Metod_page(self, metodo=None):
        self.stackedWidget.setCurrentIndex(1)
        if metodo:
            self.label_Op_Elegida.setText(metodo)

    def switch_to_Infor_page(self):
        self.stackedWidget.setCurrentIndex(6)

        # Configurar la tabla

    def setup_table(self):
        self.tableWidget_Matriz.setColumnCount(4)
        self.tableWidget_Matriz.setHorizontalHeaderLabels(["Iteración", "xi", "yi", "y_calculado"])
        self.tableWidget_Matriz.verticalHeader().setVisible(False)  # Quitar la numeración vertical
        self.tableWidget_Matriz.setEditTriggers(QTableWidget.NoEditTriggers)  # Hacer que las celdas no sean editables


    # Obtener datos de la interfaz gráfica
    def datos(self):
        ecuacion = self.lineEdit_Ev_Ec.text()
        x0 = float(self.lineEdit_Int_Ev_x0.text())
        x1 = float(self.lineEdit_Int_Ev_x1.text())
        y0 = float(self.lineEdit_Val_Ev_yx0.text())
        n = int(self.lineEdit_Nro_Inter.text())
        return ecuacion, x0, x1, y0, n


    # METODO EULER
    def calcular_euler(self):
        ecuacion = self.lineEdit_Ev_Ec.text()
        x0 = float(self.lineEdit_Int_Ev_x0.text())
        x1 = float(self.lineEdit_Int_Ev_x1.text())
        y0 = float(self.lineEdit_Val_Ev_yx0.text())
        n = int(self.lineEdit_Nro_Inter.text())

        self.mEuler(ecuacion, x0, x1, y0, n)

        # Mostrar el gráfico
        x_data, y_data = self.get_euler_data(ecuacion, x0, x1, y0, n)
        self.graph_window = GraphWindow(x_data, y_data)
        self.graph_window.show()

    # Definición de la función de Euler

    def funcion(self, expr, x_eval, y_eval):
        x = x_eval
        y = y_eval
        return eval(expr)

    def mEuler(self, ecuacion, x0, x1, y0, n):
        h = (x1 - x0) / n
        x = x0
        y = y0
        x_data = []
        y_data = []

        self.tableWidget_Matriz.setRowCount(0)

        for i in range(n):
            fxy = self.funcion(ecuacion, x, y)
            y_cal = y + h * fxy

            x_data.append(x)
            y_data.append(y)

            self.tableWidget_Matriz.insertRow(i)
            self.tableWidget_Matriz.setItem(i, 0, self.create_centered_item(str(i + 1)))
            self.tableWidget_Matriz.setItem(i, 1, self.create_centered_item(f"{x:.6f}"))
            self.tableWidget_Matriz.setItem(i, 2, self.create_centered_item(f"{y:.6f}"))
            self.tableWidget_Matriz.setItem(i, 3, self.create_centered_item(f"{y_cal:.6f}"))

            x += h
            y = y_cal

        if n > 30:
            self.tableWidget_Matriz.insertRow(n)
            self.tableWidget_Matriz.setItem(n, 0, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 1, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 2, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 3, self.create_centered_item('...'))
            self.tableWidget_Matriz.insertRow(n + 1)
            self.tableWidget_Matriz.setItem(n + 1, 0, self.create_centered_item(str(n)))
            self.tableWidget_Matriz.setItem(n + 1, 1, self.create_centered_item(f"{x:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 2, self.create_centered_item(f"{y:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 3, self.create_centered_item(f"{y_cal:.6f}"))

        self.lineEdit_Resultado.setText(f'y({x1}) = {y_cal:.8f}')

        # Guardar los datos de x y y para el gráfico
        self.euler_x_data = x_data
        self.euler_y_data = y_data

    def get_euler_data(self, ecuacion, x0, x1, y0, n):
        return self.euler_x_data, self.euler_y_data

    def create_centered_item(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        return item