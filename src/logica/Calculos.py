from src.vista.menuGUI import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PySide6.QtCore import Qt

import sympy as sp


class Mysidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.stackedWidget.setCurrentIndex(0)
        self.method = 'Euler'  # Default method

        # Ocultar barra iconos
        self.frame_Iconos.setHidden(True)

        # Conexiones de botones para cambiar de página y actualizar label
        self.btn_Inicio.clicked.connect(self.switch_to_Inicio_page)
        self.btn_Info.clicked.connect(self.switch_to_Infor_page)
        self.btn_Calcular.clicked.connect(self.calcular)
        self.btn_Limpiar.clicked.connect(self.limpiar_todos_los_campos)

        self.btn_Me_Euler_1.clicked.connect(lambda: self.switch_to_Metod_page("METODO DE EULER - 1ER ORDEN", 'Euler'))
        self.btn_Me_Euler_2.clicked.connect(lambda: self.switch_to_Metod_page("METODO DE EULER - 1ER ORDEN", 'Euler'))

        self.btn_Me_Euler_1.clicked.connect(lambda: self.select_method("Euler 1"))
        self.btn_Me_Euler_2.clicked.connect(lambda: self.select_method("Euler 2"))

        self.btn_Me_Tylor_1.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE TAYLOR - 2DO ORDEN", 'Taylor'))
        self.btn_Me_Tylor_2.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE TAYLOR - 2DO ORDEN", 'Taylor'))

        self.btn_Me_Tylor_1.clicked.connect(lambda: self.select_method("Taylor 1"))
        self.btn_Me_Tylor_2.clicked.connect(lambda: self.select_method("Taylor 2"))

        self.btn_Me_EM_1.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE EULER MODIFICADO", 'Euler Mod'))
        self.btn_Me_EM_2.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE EULER MODIFICADO", 'Euler Mod'))

        self.btn_Me_EM_1.clicked.connect(lambda: self.select_method("Euler Modificado"))
        self.btn_Me_EM_2.clicked.connect(lambda: self.select_method("Euler Modificado"))

        self.btn_Me_Runge_1.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE RUNGE-KUTTA", 'Runge-Kutta'))
        self.btn_Me_Runge_2.clicked.connect(lambda: self.switch_to_Metod_page("MÉTODO DE RUNGE-KUTTA", 'Runge-Kutta'))

        self.btn_Me_Runge_1.clicked.connect(lambda: self.select_method("Runge-Kutta"))
        self.btn_Me_Runge_2.clicked.connect(lambda: self.select_method("Runge-Kutta"))


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

        # Atributo para almacenar el método seleccionado
        self.metodo_seleccionado = None


    # Alternar entre páginas y actualizar label
    def switch_to_Inicio_page(self):
        self.limpiar_campos()  # Limpia los campos antes de cambiar de página
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_Metod_page(self, metodo=None, method_type=None):
        self.limpiar_campos()  # Limpia los campos antes de cambiar de página
        self.stackedWidget.setCurrentIndex(1)
        if metodo:
            self.label_Op_Elegida.setText(metodo)
        if method_type:
            self.method = method_type

    def switch_to_Infor_page(self):
        self.limpiar_campos()  # Limpia los campos antes de cambiar de página
        self.stackedWidget.setCurrentIndex(6)

    # Método para limpiar campos
    def limpiar_campos(self):
        self.lineEdit_Resultado.clear()
        self.tableWidget_Matriz.setRowCount(0)


##****************************##
    # Configurar la tabla
    def setup_table(self):
        self.tableWidget_Matriz.setColumnCount(4)
        self.tableWidget_Matriz.setHorizontalHeaderLabels(["Iteración", "xi", "yi", "y_calculado"])
        self.tableWidget_Matriz.verticalHeader().setVisible(False)  # Quitar la numeración vertical
        self.tableWidget_Matriz.setEditTriggers(QTableWidget.NoEditTriggers)  # Hacer que las celdas no sean editables


    # Obtener datos
    def datos(self):
        try:
            ecuacion = self.lineEdit_Ev_Ec.text()
            x0 = float(self.lineEdit_Int_Ev_x0.text())
            x1 = float(self.lineEdit_Int_Ev_x1.text())
            y0 = float(self.lineEdit_Val_Ev_yx0.text())
            n = int(self.lineEdit_Nro_Inter.text())
            return ecuacion, x0, x1, y0, n
        except ValueError:
            self.alerta("Por favor, ingrese valores numéricos válidos.")
            return None, None, None, None, None


    # Calcular según el método seleccionado
    def calcular(self):
        if self.metodo_seleccionado == "Euler 1" or self.metodo_seleccionado == "Euler 2":
            self.calcular_euler()
        elif self.metodo_seleccionado == "Taylor 1" or self.metodo_seleccionado == "Taylor 2":
            self.calcular_taylor()
        elif self.metodo_seleccionado == "Euler Modificado":
            self.calcular_euler_modificado()
        elif self.metodo_seleccionado == "Runge-Kutta":
            self.calcular_runge_kutta()
        else:
            QMessageBox.warning(self, "Error", "Seleccione un método (Euler, Taylor, Euler Modificado o Runge-Kutta).")

    def select_method(self, method):
        self.metodo_seleccionado = method

        if method == "Euler Modificado":
            self.tableWidget_Matriz.setColumnCount(6)
            enc_y = f'y({self.lineEdit_Int_Ev_x1.text()})'
            self.tableWidget_Matriz.setHorizontalHeaderLabels(
                ["Iteración", "xi", "yi", "y(i+1)", "fxy prom", enc_y])
        elif method == "Runge-Kutta":
            self.tableWidget_Matriz.setColumnCount(8)
            enc_y = f'y({self.lineEdit_Int_Ev_x1.text()})'
            self.tableWidget_Matriz.setHorizontalHeaderLabels(
                ["Iteración", "xi", "yi", "k1", "k2", "k3", "k4", enc_y])
        else:
            self.setup_table()


    # Definición de la función de Euler
    def calcular_euler(self):
        ecuacion, x0, x1, y0, n = self.datos()

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


    # Definición de la función de Taylor
    def calcular_taylor(self):
        ecuacion, x0, x1, y0, n = self.datos()

        h = (x1 - x0) / n
        x = x0
        y = y0
        x_data = []
        y_data = []

        self.tableWidget_Matriz.setRowCount(0)

        for i in range(n):
            fxy = self.funcion(ecuacion, x, y)
            dfdx, dfdy = self.derivar(ecuacion)
            dfxy = self.funcion(dfdx + '+' + dfdy + '*(' + ecuacion + ')', x, y)
            y_cal = y + h * fxy + ((h ** 2) / 2) * dfxy

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
        self.taylor_x_data = x_data
        self.taylor_y_data = y_data



    # Definición de la función de Euler Modificado
    def calcular_euler_modificado(self):
        ecuacion, x0, x1, y0, n = self.datos()

        h = (x1 - x0) / n
        x = x0
        y = y0
        x_data = []
        y_data = []

        self.tableWidget_Matriz.setRowCount(0)
        enc_y = f'y({x1})'

        for i in range(n):
            fxy1 = self.funcion(ecuacion, x, y)
            y_next = y + h * fxy1
            x_next = x + h
            fxy2 = self.funcion(ecuacion, x_next, y_next)
            fxy_prom = (fxy1 + fxy2) / 2
            y_cal = y + h * fxy_prom

            x_data.append(x)
            y_data.append(y)

            self.tableWidget_Matriz.insertRow(i)
            self.tableWidget_Matriz.setItem(i, 0, self.create_centered_item(str(i + 1)))
            self.tableWidget_Matriz.setItem(i, 1, self.create_centered_item(f"{x:.6f}"))
            self.tableWidget_Matriz.setItem(i, 2, self.create_centered_item(f"{y:.6f}"))
            self.tableWidget_Matriz.setItem(i, 3, self.create_centered_item(f"{y_next:.6f}"))
            self.tableWidget_Matriz.setItem(i, 4, self.create_centered_item(f"{fxy_prom:.6f}"))
            self.tableWidget_Matriz.setItem(i, 5, self.create_centered_item(f"{y_cal:.6f}"))

            x += h
            y = y_cal

        if n > 30:
            self.tableWidget_Matriz.insertRow(n)
            self.tableWidget_Matriz.setItem(n, 0, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 1, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 2, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 3, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 4, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 5, self.create_centered_item('...'))
            self.tableWidget_Matriz.insertRow(n + 1)
            self.tableWidget_Matriz.setItem(n + 1, 0, self.create_centered_item(str(n)))
            self.tableWidget_Matriz.setItem(n + 1, 1, self.create_centered_item(f"{x:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 2, self.create_centered_item(f"{y:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 3, self.create_centered_item(f"{y_next:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 4, self.create_centered_item(f"{fxy_prom:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 5, self.create_centered_item(f"{y_cal:.6f}"))

        self.lineEdit_Resultado.setText(f'y({x1}) = {y_cal:.8f}')

        # Guardar los datos de x y y para el gráfico
        self.euler_modificado_x_data = x_data
        self.euler_modificado_y_data = y_data


    # Definición de la función de Runge-Kutta
    def calcular_runge_kutta(self):
        ecuacion, x0, x1, y0, n = self.datos()

        h = (x1 - x0) / n
        x = x0
        y = y0
        x_data = []
        y_data = []

        self.tableWidget_Matriz.setRowCount(0)
        enc_y = f'y({x1})'

        for i in range(n):
            k1 = h * self.funcion(ecuacion, x, y)
            k2 = h * self.funcion(ecuacion, x + h / 2, y + k1 / 2)
            k3 = h * self.funcion(ecuacion, x + h / 2, y + k2 / 2)
            k4 = h * self.funcion(ecuacion, x + h, y + k3)
            y_cal = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

            x_data.append(x)
            y_data.append(y)

            self.tableWidget_Matriz.insertRow(i)
            self.tableWidget_Matriz.setItem(i, 0, self.create_centered_item(str(i + 1)))
            self.tableWidget_Matriz.setItem(i, 1, self.create_centered_item(f"{x:.6f}"))
            self.tableWidget_Matriz.setItem(i, 2, self.create_centered_item(f"{y:.6f}"))
            self.tableWidget_Matriz.setItem(i, 3, self.create_centered_item(f"{k1:.6f}"))
            self.tableWidget_Matriz.setItem(i, 4, self.create_centered_item(f"{k2:.6f}"))
            self.tableWidget_Matriz.setItem(i, 5, self.create_centered_item(f"{k3:.6f}"))
            self.tableWidget_Matriz.setItem(i, 6, self.create_centered_item(f"{k4:.6f}"))
            self.tableWidget_Matriz.setItem(i, 7, self.create_centered_item(f"{y_cal:.6f}"))

            x += h
            y = y_cal

        if n > 30:
            self.tableWidget_Matriz.insertRow(n)
            self.tableWidget_Matriz.setItem(n, 0, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 1, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 2, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 3, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 4, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 5, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 6, self.create_centered_item('...'))
            self.tableWidget_Matriz.setItem(n, 7, self.create_centered_item('...'))
            self.tableWidget_Matriz.insertRow(n + 1)
            self.tableWidget_Matriz.setItem(n + 1, 0, self.create_centered_item(str(n)))
            self.tableWidget_Matriz.setItem(n + 1, 1, self.create_centered_item(f"{x:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 2, self.create_centered_item(f"{y:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 3, self.create_centered_item(f"{k1:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 4, self.create_centered_item(f"{k2:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 5, self.create_centered_item(f"{k3:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 6, self.create_centered_item(f"{k4:.6f}"))
            self.tableWidget_Matriz.setItem(n + 1, 7, self.create_centered_item(f"{y_cal:.6f}"))

        self.lineEdit_Resultado.setText(f'y({x1}) = {y_cal:.8f}')

        # Guardar los datos de x y y para el gráfico
        self.runge_kutta_x_data = x_data
        self.runge_kutta_y_data = y_data

    # Evaluar la función en un punto
    def funcion(self, expr, x_eval, y_eval):
        try:
            x = x_eval
            y = y_eval
            return eval(expr)
        except Exception as e:
            self.alerta(f"Error al evaluar la función: {e}")
            return None

    # Derivar la ecuación
    def derivar(self, ecuacion):
        x = sp.Symbol('x')
        y = sp.Symbol('y')
        derv_x = str(sp.Derivative(ecuacion, x, evaluate=True))
        derv_y = str(sp.Derivative(ecuacion, y, evaluate=True))
        return derv_x, derv_y

    # Obtener datos según el método seleccionado
    def create_centered_item(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return item

    # Mostrar un mensaje de alerta
    def alerta(self, mensaje):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("ATENCION!!")
        dlg.setText(mensaje)
        dlg.setIcon(QMessageBox.Warning)
        dlg.exec()

    def limpiar_todos_los_campos(self):
        self.lineEdit_Ev_Ec.clear()
        self.lineEdit_Int_Ev_x0.clear()
        self.lineEdit_Int_Ev_x1.clear()
        self.lineEdit_Val_Ev_yx0.clear()
        self.lineEdit_Nro_Inter.clear()
        self.lineEdit_Resultado.clear()
        self.tableWidget_Matriz.setRowCount(0)
