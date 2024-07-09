# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1279, 731)
        MainWindow.setStyleSheet(u"background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_18 = QVBoxLayout(self.main_menu)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.Header = QWidget(self.main_menu)
        self.Header.setObjectName(u"Header")
        self.Header.setStyleSheet(u"text-align:left;")
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_menu = QPushButton(self.Header)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/Iconos/iconMove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(40, 40))
        self.btn_menu.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.btn_Inicio = QPushButton(self.Header)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/Iconos/IconHouse.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Inicio.setIcon(icon1)
        self.btn_Inicio.setIconSize(QSize(40, 40))
        self.btn_Inicio.setCheckable(True)
        self.btn_Inicio.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_Inicio)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.label_8 = QLabel(self.Header)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setPixmap(QPixmap(u":/newPrefix/Iconos/TEMPOLARM_BAR_2.png"))
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)

        self.btn_Info = QPushButton(self.Header)
        self.btn_Info.setObjectName(u"btn_Info")
        self.btn_Info.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/Iconos/iconSobre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Info.setIcon(icon2)
        self.btn_Info.setIconSize(QSize(40, 40))
        self.btn_Info.setCheckable(True)
        self.btn_Info.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.btn_Info)


        self.verticalLayout_18.addWidget(self.Header)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(13, 13, 13);\n"
"	font: 10pt \"Century Gothic\";\n"
"	color: rgb(255, 249, 250);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(20, 28, 77);\n"
"text-align:center;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(38, 55, 149);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"background-color: rgb(244, 244, 244);\n"
"border: 1px solid rgb(0, 0, 0);\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(0, 0, 0);\n"
"border: 1px border: 1px solid rgb(118, 0, 59);\n"
"}")
        self.Inicio_page = QWidget()
        self.Inicio_page.setObjectName(u"Inicio_page")
        self.verticalLayout_5 = QVBoxLayout(self.Inicio_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_Bienvenida = QLabel(self.Inicio_page)
        self.lbl_Bienvenida.setObjectName(u"lbl_Bienvenida")
        self.lbl_Bienvenida.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 28pt \"Century Gothic\";")
        self.lbl_Bienvenida.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_Bienvenida)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_15 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_15)

        self.lbl_icon = QLabel(self.Inicio_page)
        self.lbl_icon.setObjectName(u"lbl_icon")
        self.lbl_icon.setMinimumSize(QSize(100, 100))
        self.lbl_icon.setMaximumSize(QSize(1080, 700))
        self.lbl_icon.setLayoutDirection(Qt.LeftToRight)
        self.lbl_icon.setPixmap(QPixmap(u":/newPrefix/Iconos/Fondo_1.PNG"))
        self.lbl_icon.setScaledContents(True)
        self.lbl_icon.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.lbl_icon)

        self.horizontalSpacer_16 = QSpacerItem(18, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.stackedWidget.addWidget(self.Inicio_page)
        self.Metod_page = QWidget()
        self.Metod_page.setObjectName(u"Metod_page")
        self.verticalLayout_17 = QVBoxLayout(self.Metod_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_Op_Elegida = QLabel(self.Metod_page)
        self.label_Op_Elegida.setObjectName(u"label_Op_Elegida")
        self.label_Op_Elegida.setMinimumSize(QSize(200, 40))
        self.label_Op_Elegida.setMaximumSize(QSize(16777215, 40))
        self.label_Op_Elegida.setStyleSheet(u"font: 75 14pt \"Century Gothic\";\n"
"background-color: rgb(35, 49, 127);")
        self.label_Op_Elegida.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_Op_Elegida)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox_3 = QGroupBox(self.Metod_page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(16777215, 80))
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(36, 0, 35, -1)
        self.lineEdit_Ecuacion = QLineEdit(self.groupBox_3)
        self.lineEdit_Ecuacion.setObjectName(u"lineEdit_Ecuacion")
        self.lineEdit_Ecuacion.setMaximumSize(QSize(700, 50))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit_Ecuacion.setFont(font)
        self.lineEdit_Ecuacion.setStyleSheet(u"text-align:center;\n"
"font: 75 24pt \"Century Gothic\";")
        self.lineEdit_Ecuacion.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lineEdit_Ecuacion)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addWidget(self.groupBox_3)

        self.label_3 = QLabel(self.Metod_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setStyleSheet(u"font: 75 14pt \"Century Gothic\";")
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.label_3)


        self.verticalLayout_17.addLayout(self.verticalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.Metod_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(300, 0))
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setSpacing(11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.label_11)

        self.lineEdit_Ev_Ec = QLineEdit(self.groupBox)
        self.lineEdit_Ev_Ec.setObjectName(u"lineEdit_Ev_Ec")
        self.lineEdit_Ev_Ec.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.lineEdit_Ev_Ec)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.lineEdit_Int_Ev_x0 = QLineEdit(self.groupBox)
        self.lineEdit_Int_Ev_x0.setObjectName(u"lineEdit_Int_Ev_x0")
        self.lineEdit_Int_Ev_x0.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.lineEdit_Int_Ev_x0)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_6.addWidget(self.label_10)

        self.lineEdit_Int_Ev_x1 = QLineEdit(self.groupBox)
        self.lineEdit_Int_Ev_x1.setObjectName(u"lineEdit_Int_Ev_x1")
        self.lineEdit_Int_Ev_x1.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.lineEdit_Int_Ev_x1)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_6.addWidget(self.label_26)

        self.lineEdit_Val_Ev_yx0 = QLineEdit(self.groupBox)
        self.lineEdit_Val_Ev_yx0.setObjectName(u"lineEdit_Val_Ev_yx0")
        self.lineEdit_Val_Ev_yx0.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.lineEdit_Val_Ev_yx0)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_6.addWidget(self.label_27)

        self.lineEdit_Nro_Inter = QLineEdit(self.groupBox)
        self.lineEdit_Nro_Inter.setObjectName(u"lineEdit_Nro_Inter")
        self.lineEdit_Nro_Inter.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.lineEdit_Nro_Inter)

        self.verticalSpacer_3 = QSpacerItem(0, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.Metod_page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 40))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setSpacing(9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.lineEdit_Resultado = QLineEdit(self.groupBox_2)
        self.lineEdit_Resultado.setObjectName(u"lineEdit_Resultado")
        self.lineEdit_Resultado.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"font: 75 11pt \"Century Gothic\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Resultado.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.lineEdit_Resultado)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.tableWidget_Matriz = QTableWidget(self.Metod_page)
        self.tableWidget_Matriz.setObjectName(u"tableWidget_Matriz")
        self.tableWidget_Matriz.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget_Matriz.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Matriz.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_Matriz.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tableWidget_Matriz)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_Grafico = QPushButton(self.Metod_page)
        self.btn_Grafico.setObjectName(u"btn_Grafico")
        self.btn_Grafico.setMaximumSize(QSize(16777215, 40))
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/Iconos/Graph.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Grafico.setIcon(icon3)
        self.btn_Grafico.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.btn_Grafico)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_Calcular = QPushButton(self.Metod_page)
        self.btn_Calcular.setObjectName(u"btn_Calcular")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/Iconos/iconCheck.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Calcular.setIcon(icon4)
        self.btn_Calcular.setIconSize(QSize(40, 40))
        self.btn_Calcular.setCheckable(True)
        self.btn_Calcular.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_Calcular)

        self.btn_Limpiar = QPushButton(self.Metod_page)
        self.btn_Limpiar.setObjectName(u"btn_Limpiar")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/Iconos/iconRedo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Limpiar.setIcon(icon5)
        self.btn_Limpiar.setIconSize(QSize(40, 40))
        self.btn_Limpiar.setAutoExclusive(True)

        self.horizontalLayout_3.addWidget(self.btn_Limpiar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.verticalLayout_17.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.Metod_page)
        self.Pom_page = QWidget()
        self.Pom_page.setObjectName(u"Pom_page")
        self.verticalLayout_23 = QVBoxLayout(self.Pom_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.groupBox_12 = QGroupBox(self.Pom_page)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(0, 40))
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_21.setSpacing(9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)

        self.verticalLayout_23.addWidget(self.groupBox_12)

        self.stackedWidget.addWidget(self.Pom_page)
        self.Alarm_page = QWidget()
        self.Alarm_page.setObjectName(u"Alarm_page")
        self.verticalLayout_26 = QVBoxLayout(self.Alarm_page)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_38 = QLabel(self.Alarm_page)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_26.addWidget(self.label_38)

        self.stackedWidget.addWidget(self.Alarm_page)
        self.Regis_page = QWidget()
        self.Regis_page.setObjectName(u"Regis_page")
        self.verticalLayout_27 = QVBoxLayout(self.Regis_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.tableRegistro = QTableWidget(self.Regis_page)
        if (self.tableRegistro.columnCount() < 4):
            self.tableRegistro.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableRegistro.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableRegistro.setObjectName(u"tableRegistro")
        self.tableRegistro.horizontalHeader().setVisible(False)
        self.tableRegistro.horizontalHeader().setDefaultSectionSize(125)
        self.tableRegistro.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.tableRegistro)

        self.stackedWidget.addWidget(self.Regis_page)
        self.User_page = QWidget()
        self.User_page.setObjectName(u"User_page")
        self.verticalLayout_13 = QVBoxLayout(self.User_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame = QFrame(self.User_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")

        self.verticalLayout_13.addWidget(self.frame)

        self.stackedWidget.addWidget(self.User_page)
        self.Infor_page = QWidget()
        self.Infor_page.setObjectName(u"Infor_page")
        self.verticalLayout_16 = QVBoxLayout(self.Infor_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.groupBox_5 = QGroupBox(self.Infor_page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_21)

        self.verticalSpacer_12 = QSpacerItem(20, 29, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_12)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_22)

        self.verticalSpacer_11 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_11)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_23)

        self.frame_2 = QFrame(self.groupBox_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 120))
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_6 = QSpacerItem(151, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_6)

        self.label_25 = QLabel(self.frame_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(100, 150))
        self.label_25.setPixmap(QPixmap(u":/newPrefix/Iconos/kewin.jpg"))
        self.label_25.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_25)

        self.horizontalSpacer_7 = QSpacerItem(150, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_7)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_14.addWidget(self.label_24)


        self.verticalLayout_15.addWidget(self.groupBox_5)

        self.btn_GuardarUser_2 = QPushButton(self.Infor_page)
        self.btn_GuardarUser_2.setObjectName(u"btn_GuardarUser_2")
        self.btn_GuardarUser_2.setMinimumSize(QSize(100, 40))
        self.btn_GuardarUser_2.setStyleSheet(u"QPushButton{ \n"
"background-color: rgb(59, 0, 29);\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color: rgb(34, 0, 17);\n"
"}")
        self.btn_GuardarUser_2.setIcon(icon4)
        self.btn_GuardarUser_2.setIconSize(QSize(40, 40))

        self.verticalLayout_15.addWidget(self.btn_GuardarUser_2)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.stackedWidget.addWidget(self.Infor_page)

        self.verticalLayout_18.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        self.frame_Botones = QWidget(self.centralwidget)
        self.frame_Botones.setObjectName(u"frame_Botones")
        self.frame_Botones.setStyleSheet(u"QWidget{\n"
"background-color: rgb(42, 64, 106);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(31, 51, 106);\n"
"text-align:left;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(31, 39, 86);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(31, 39, 86);\n"
"font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.frame_Botones)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 9, -1)
        self.label_2 = QLabel(self.frame_Botones)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(145, 60))
        self.label_2.setMaximumSize(QSize(100, 60))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/Iconos/EDO_LOGO.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_2)

        self.btn_Me_Euler_2 = QPushButton(self.frame_Botones)
        self.btn_Me_Euler_2.setObjectName(u"btn_Me_Euler_2")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/Iconos/E.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Me_Euler_2.setIcon(icon6)
        self.btn_Me_Euler_2.setIconSize(QSize(40, 40))
        self.btn_Me_Euler_2.setCheckable(True)
        self.btn_Me_Euler_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Me_Euler_2)

        self.btn_Me_Tylor_2 = QPushButton(self.frame_Botones)
        self.btn_Me_Tylor_2.setObjectName(u"btn_Me_Tylor_2")
        self.btn_Me_Tylor_2.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/Iconos/T.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Me_Tylor_2.setIcon(icon7)
        self.btn_Me_Tylor_2.setIconSize(QSize(40, 40))
        self.btn_Me_Tylor_2.setCheckable(True)
        self.btn_Me_Tylor_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Me_Tylor_2)

        self.btn_Me_EM_2 = QPushButton(self.frame_Botones)
        self.btn_Me_EM_2.setObjectName(u"btn_Me_EM_2")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/Iconos/EM.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Me_EM_2.setIcon(icon8)
        self.btn_Me_EM_2.setIconSize(QSize(40, 40))
        self.btn_Me_EM_2.setCheckable(True)
        self.btn_Me_EM_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Me_EM_2)

        self.btn_Me_Runge_2 = QPushButton(self.frame_Botones)
        self.btn_Me_Runge_2.setObjectName(u"btn_Me_Runge_2")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/Iconos/RK.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Me_Runge_2.setIcon(icon9)
        self.btn_Me_Runge_2.setIconSize(QSize(40, 40))
        self.btn_Me_Runge_2.setCheckable(True)
        self.btn_Me_Runge_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.btn_Me_Runge_2)

        self.verticalSpacer_2 = QSpacerItem(20, 282, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.pushButton_13 = QPushButton(self.frame_Botones)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/Iconos/iconCerrar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon10)
        self.pushButton_13.setIconSize(QSize(40, 40))
        self.pushButton_13.setCheckable(True)
        self.pushButton_13.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.pushButton_13)


        self.gridLayout.addWidget(self.frame_Botones, 0, 1, 1, 1)

        self.frame_Iconos = QWidget(self.centralwidget)
        self.frame_Iconos.setObjectName(u"frame_Iconos")
        self.frame_Iconos.setStyleSheet(u"QWidget{\n"
"background-color: rgb(42, 64, 106);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(31, 51, 106);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(31, 39, 86);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius:20px;\n"
"border-top-right-radius: 20px;\n"
"border-bottom-right-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Century Gothic\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(31, 39, 86);\n"
"font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.frame_Iconos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_Iconos)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/newPrefix/Iconos/Logo_EDO_1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_Me_Euler_1 = QPushButton(self.frame_Iconos)
        self.btn_Me_Euler_1.setObjectName(u"btn_Me_Euler_1")
        self.btn_Me_Euler_1.setIcon(icon6)
        self.btn_Me_Euler_1.setIconSize(QSize(40, 40))
        self.btn_Me_Euler_1.setCheckable(True)
        self.btn_Me_Euler_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Me_Euler_1)

        self.btn_Me_Tylor_1 = QPushButton(self.frame_Iconos)
        self.btn_Me_Tylor_1.setObjectName(u"btn_Me_Tylor_1")
        self.btn_Me_Tylor_1.setIcon(icon7)
        self.btn_Me_Tylor_1.setIconSize(QSize(40, 40))
        self.btn_Me_Tylor_1.setCheckable(True)
        self.btn_Me_Tylor_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Me_Tylor_1)

        self.btn_Me_EM_1 = QPushButton(self.frame_Iconos)
        self.btn_Me_EM_1.setObjectName(u"btn_Me_EM_1")
        self.btn_Me_EM_1.setIcon(icon8)
        self.btn_Me_EM_1.setIconSize(QSize(40, 40))
        self.btn_Me_EM_1.setCheckable(True)
        self.btn_Me_EM_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Me_EM_1)

        self.btn_Me_Runge_1 = QPushButton(self.frame_Iconos)
        self.btn_Me_Runge_1.setObjectName(u"btn_Me_Runge_1")
        self.btn_Me_Runge_1.setIcon(icon9)
        self.btn_Me_Runge_1.setIconSize(QSize(40, 40))
        self.btn_Me_Runge_1.setCheckable(True)
        self.btn_Me_Runge_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.btn_Me_Runge_1)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.frame_Iconos)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon10)
        self.pushButton_7.setIconSize(QSize(40, 40))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.gridLayout.addWidget(self.frame_Iconos, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_menu.toggled.connect(self.frame_Iconos.setHidden)
        self.btn_menu.toggled.connect(self.frame_Botones.setVisible)
        self.btn_Me_Runge_1.toggled.connect(self.btn_Me_Runge_2.setChecked)
        self.btn_Me_EM_1.toggled.connect(self.btn_Me_EM_2.setChecked)
        self.btn_Me_Tylor_1.toggled.connect(self.btn_Me_Tylor_2.setChecked)
        self.btn_Me_Euler_1.toggled.connect(self.btn_Me_Euler_2.setChecked)
        self.btn_Me_Euler_2.toggled.connect(self.btn_Me_Euler_1.setChecked)
        self.btn_Me_Tylor_2.toggled.connect(self.btn_Me_Tylor_1.setChecked)
        self.btn_Me_EM_2.toggled.connect(self.btn_Me_EM_1.setChecked)
        self.btn_Me_Runge_2.toggled.connect(self.btn_Me_Runge_1.setChecked)
        self.pushButton_7.toggled.connect(MainWindow.close)
        self.pushButton_13.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.btn_Inicio.setText("")
        self.label_8.setText("")
        self.btn_Info.setText("")
        self.lbl_Bienvenida.setText(QCoreApplication.translate("MainWindow", u"BIENVENIDO!", None))
        self.lbl_icon.setText("")
        self.label_Op_Elegida.setText(QCoreApplication.translate("MainWindow", u"METODO DE EULER - 1ER ORDEN", None))
        self.groupBox_3.setTitle("")
        self.lineEdit_Ecuacion.setText(QCoreApplication.translate("MainWindow", u"y' = 2y   con  y(0) = 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"La ecuaci\u00f3n debe estar en funci\u00f3n de f(x,y)", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"DATOS:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ECUACI\u00d3N A EVALUAR:", None))
        self.lineEdit_Ev_Ec.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"INTERVALO DE EVALUACI\u00d3N x0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"INTERVALO DE EVALUACI\u00d3N x1", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"VALOR EVALUADO EN y(x0)", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO DE SUBINTERVALOS", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"RESULTADO", None))
        self.btn_Grafico.setText(QCoreApplication.translate("MainWindow", u"GR\u00c1FICO", None))
        self.btn_Calcular.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
        self.btn_Limpiar.setText(QCoreApplication.translate("MainWindow", u"LIMPIAR", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"GUARDADOS:", None))
        self.label_38.setText("")
        ___qtablewidgetitem = self.tableRegistro.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableRegistro.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tiempo Registrado", None));
        ___qtablewidgetitem2 = self.tableRegistro.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tono", None));
        ___qtablewidgetitem3 = self.tableRegistro.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Repetir", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Acerca de:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\"TEMPOLARM\"", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"________________________________________________", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Es una aplicaci\u00f3n de gesti\u00f3n de tiempo\n"
" multiprop\u00f3sito que combina \n"
"un temporizador, una alarma y un \n"
"temporizador Pomodoro. La aplicaci\u00f3n \n"
"permitir\u00e1 alos usuarios configurar y\n"
" gestionar diferentes tipos de \n"
"temporizadores seg\u00fan sus necesidades, \n"
"con la capacidad de iniciar, pausar, \n"
"reiniciar y salir de cada uno deellos. \n"
"Adem\u00e1s, la aplicaci\u00f3n incluir\u00e1 un ring \n"
"de 3 segundos que se activar\u00e1 al \n"
"finalizar cada temporizador.", None))
        self.label_25.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u00a9alba\u00f1ilesdesoftware", None))
        self.btn_GuardarUser_2.setText(QCoreApplication.translate("MainWindow", u"ACEPTAR", None))
        self.label_2.setText("")
        self.btn_Me_Euler_2.setText(QCoreApplication.translate("MainWindow", u"M\u00c9TODO EULER", None))
        self.btn_Me_Tylor_2.setText(QCoreApplication.translate("MainWindow", u"M\u00c9TODO TAYLOR", None))
        self.btn_Me_EM_2.setText(QCoreApplication.translate("MainWindow", u"M\u00c9TODO EULER M", None))
        self.btn_Me_Runge_2.setText(QCoreApplication.translate("MainWindow", u"M\u00c9TODO RUNGE K.", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"SALIR", None))
        self.label.setText("")
        self.btn_Me_Euler_1.setText("")
        self.btn_Me_Tylor_1.setText("")
        self.btn_Me_EM_1.setText("")
        self.btn_Me_Runge_1.setText("")
        self.pushButton_7.setText("")
    # retranslateUi

