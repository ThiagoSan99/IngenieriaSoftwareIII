# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1348, 748)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"logo1.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-image: url('D:/Udenar/Ingenieria en Sistemas/Semestre 5/Ing. Software lll/Proyecto sw - el que es 2.0/image/fondo.jpg');\n"
"                background-repeat: no-repeat;\n"
"                background-position: center;\n"
"            }\n"
"QPushButton {\n"
"    background-color: #4CAF50; /* Color de fondo verde*/\n"
"    color: black; /* Color del texto blanco */\n"
"    border-radius: 10px; /* Radio del borde redondeado */\n"
"	   font-size: 15px; /* Tama\u00f1o de la letra */\n"
"    padding: 10px 20px; /* Ajuste opcional del relleno */\n"
"font: 700 12pt \"Times New Roman\";\n"
"}\n"
"QPushButton:pressed {\n"
"                background-color: #c0c0c0;\n"
"            }\n"
"QLabel {\n"
"    font:  700 12pt \"Times New Roman\";\n"
"}\n"
"QLineEdit {\n"
"    border-radius: 5px; /* El valor 10px puede ser ajustado seg\u00fan el radio deseado */\n"
"background-color: #556B2F; /* Verde m\u00e1s oscuro */\n"
"color: white;\n"
"}\n"
"QPlainTextEdit:disabled {\n"
"    background-color"
                        ": #FFFFFF; /* Establece el color de fondo a blanco */\n"
"    color: #000000; /* Establece el color del texto a negro */\n"
"}\n"
"QTableWidget {\n"
"    background-color: #E6FFE6; /* Color de fondo */\n"
"    alternate-background-color: #C7FFD8; /* Color de fondo alternativo para filas */\n"
"    gridline-color: #66CC66; /* Color de las l\u00edneas de la cuadr\u00edcula */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px; /* Espaciado interno */\n"
"    border: none; /* Sin borde */\n"
"    color: #003300; /* Color del texto */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #80FF80; /* Color de fondo de las celdas seleccionadas */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_28 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 70))
        self.widget_7.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.lbl_hermedcol = QLabel(self.widget_7)
        self.lbl_hermedcol.setObjectName(u"lbl_hermedcol")
        self.lbl_hermedcol.setMinimumSize(QSize(200, 50))
        self.lbl_hermedcol.setMaximumSize(QSize(200, 50))
        self.lbl_hermedcol.setPixmap(QPixmap(u"image/titul2.png"))
        self.lbl_hermedcol.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.lbl_hermedcol)

        self.lbl_icono = QLabel(self.widget_7)
        self.lbl_icono.setObjectName(u"lbl_icono")
        self.lbl_icono.setMinimumSize(QSize(80, 70))
        self.lbl_icono.setMaximumSize(QSize(80, 70))
        self.lbl_icono.setPixmap(QPixmap(u"image/logo1.png"))
        self.lbl_icono.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.lbl_icono)


        self.verticalLayout_28.addWidget(self.widget_7)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.paginas_usuarios = QStackedWidget(self.widget_2)
        self.paginas_usuarios.setObjectName(u"paginas_usuarios")
        self.page_user = QWidget()
        self.page_user.setObjectName(u"page_user")
        self.verticalLayout_8 = QVBoxLayout(self.page_user)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_user)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 45))
        self.frame.setMaximumSize(QSize(16777215, 45))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_Menu = QPushButton(self.frame)
        self.btn_Menu.setObjectName(u"btn_Menu")
        self.btn_Menu.setMinimumSize(QSize(35, 35))
        self.btn_Menu.setMaximumSize(QSize(35, 35))
        self.btn_Menu.setSizeIncrement(QSize(0, 0))
        icon1 = QIcon()
        icon1.addFile(u"image/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Menu.setIcon(icon1)
        self.btn_Menu.setIconSize(QSize(25, 25))

        self.horizontalLayout_10.addWidget(self.btn_Menu)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)

        self.btn_cerrar_sesion = QPushButton(self.frame)
        self.btn_cerrar_sesion.setObjectName(u"btn_cerrar_sesion")
        self.btn_cerrar_sesion.setMinimumSize(QSize(30, 30))
        self.btn_cerrar_sesion.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"image/cerrar_Sesion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cerrar_sesion.setIcon(icon2)
        self.btn_cerrar_sesion.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.btn_cerrar_sesion)


        self.verticalLayout_8.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_user)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_2)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(0, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_home = QPushButton(self.frame_lateral)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMaximumSize(QSize(16777215, 35))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u"image/inicio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon3)
        self.btn_home.setIconSize(QSize(30, 30))

        self.verticalLayout_10.addWidget(self.btn_home)

        self.btn_recursos = QPushButton(self.frame_lateral)
        self.btn_recursos.setObjectName(u"btn_recursos")
        self.btn_recursos.setMaximumSize(QSize(16777215, 35))
        icon4 = QIcon()
        icon4.addFile(u"image/hoja.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recursos.setIcon(icon4)
        self.btn_recursos.setIconSize(QSize(27, 27))

        self.verticalLayout_10.addWidget(self.btn_recursos)

        self.btn_recetas = QPushButton(self.frame_lateral)
        self.btn_recetas.setObjectName(u"btn_recetas")
        self.btn_recetas.setMaximumSize(QSize(16777215, 35))
        icon5 = QIcon()
        icon5.addFile(u"image/recetas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_recetas.setIcon(icon5)
        self.btn_recetas.setIconSize(QSize(30, 30))

        self.verticalLayout_10.addWidget(self.btn_recetas)

        self.btn_provedores = QPushButton(self.frame_lateral)
        self.btn_provedores.setObjectName(u"btn_provedores")
        self.btn_provedores.setMaximumSize(QSize(16777215, 35))
        icon6 = QIcon()
        icon6.addFile(u"image/prove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_provedores.setIcon(icon6)
        self.btn_provedores.setIconSize(QSize(30, 30))

        self.verticalLayout_10.addWidget(self.btn_provedores)

        self.btn_nosotros = QPushButton(self.frame_lateral)
        self.btn_nosotros.setObjectName(u"btn_nosotros")
        self.btn_nosotros.setMaximumSize(QSize(16777215, 35))
        icon7 = QIcon()
        icon7.addFile(u"image/nosotros.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_nosotros.setIcon(icon7)
        self.btn_nosotros.setIconSize(QSize(30, 30))

        self.verticalLayout_10.addWidget(self.btn_nosotros)

        self.btn_actualizacion = QPushButton(self.frame_lateral)
        self.btn_actualizacion.setObjectName(u"btn_actualizacion")
        icon8 = QIcon()
        icon8.addFile(u"image/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_actualizacion.setIcon(icon8)

        self.verticalLayout_10.addWidget(self.btn_actualizacion)


        self.horizontalLayout_11.addWidget(self.frame_lateral)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.paginas_menu = QStackedWidget(self.frame_4)
        self.paginas_menu.setObjectName(u"paginas_menu")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.verticalLayout_11 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_inicio)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ln_buscar = QLineEdit(self.frame_5)
        self.ln_buscar.setObjectName(u"ln_buscar")

        self.horizontalLayout_12.addWidget(self.ln_buscar)

        self.btn_buscar = QPushButton(self.frame_5)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setMinimumSize(QSize(30, 30))
        self.btn_buscar.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u"image/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon9)
        self.btn_buscar.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.btn_buscar)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.page_inicio)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_6)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.info4 = QFrame(self.frame_36)
        self.info4.setObjectName(u"info4")
        self.info4.setMaximumSize(QSize(120, 16777215))
        self.info4.setFrameShape(QFrame.StyledPanel)
        self.info4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.info4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lbl_img4 = QLabel(self.info4)
        self.lbl_img4.setObjectName(u"lbl_img4")
        self.lbl_img4.setMinimumSize(QSize(170, 150))

        self.verticalLayout_16.addWidget(self.lbl_img4)

        self.lbl_info4 = QLabel(self.info4)
        self.lbl_info4.setObjectName(u"lbl_info4")
        self.lbl_info4.setMinimumSize(QSize(160, 18))
        self.lbl_info4.setMaximumSize(QSize(118, 18))

        self.verticalLayout_16.addWidget(self.lbl_info4)


        self.horizontalLayout_13.addWidget(self.info4)

        self.info5 = QFrame(self.frame_36)
        self.info5.setObjectName(u"info5")
        self.info5.setMaximumSize(QSize(120, 16777215))
        self.info5.setFrameShape(QFrame.StyledPanel)
        self.info5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.info5)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 0, 0, 0)
        self.lbl_img5 = QLabel(self.info5)
        self.lbl_img5.setObjectName(u"lbl_img5")
        self.lbl_img5.setMinimumSize(QSize(170, 150))

        self.verticalLayout_17.addWidget(self.lbl_img5)

        self.lbl_info5 = QLabel(self.info5)
        self.lbl_info5.setObjectName(u"lbl_info5")
        self.lbl_info5.setMinimumSize(QSize(170, 18))
        self.lbl_info5.setMaximumSize(QSize(118, 18))

        self.verticalLayout_17.addWidget(self.lbl_info5)


        self.horizontalLayout_13.addWidget(self.info5)

        self.info6 = QFrame(self.frame_36)
        self.info6.setObjectName(u"info6")
        self.info6.setMaximumSize(QSize(120, 16777215))
        self.info6.setFrameShape(QFrame.StyledPanel)
        self.info6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.info6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lbl_img6 = QLabel(self.info6)
        self.lbl_img6.setObjectName(u"lbl_img6")
        self.lbl_img6.setMinimumSize(QSize(170, 150))

        self.verticalLayout_18.addWidget(self.lbl_img6)

        self.lbl_info6 = QLabel(self.info6)
        self.lbl_info6.setObjectName(u"lbl_info6")
        self.lbl_info6.setMinimumSize(QSize(170, 18))
        self.lbl_info6.setMaximumSize(QSize(118, 18))

        self.verticalLayout_18.addWidget(self.lbl_info6)


        self.horizontalLayout_13.addWidget(self.info6)


        self.verticalLayout_12.addWidget(self.frame_36)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_historial = QPushButton(self.frame_9)
        self.btn_historial.setObjectName(u"btn_historial")
        self.btn_historial.setMaximumSize(QSize(120, 30))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setBold(True)
        font.setItalic(False)
        self.btn_historial.setFont(font)
        self.btn_historial.setStyleSheet(u"QPushButton {\n"
"    background-color: #4CAF50; /* Color de fondo verde */\n"
"    color: #FFFFFF; /* Color del texto blanco */\n"
"    border-radius: 10px; /* Radio del borde redondeado */\n"
"	   font-size: 13px; /* Tama\u00f1o de la letra */\n"
"    padding: 10px 20px; /* Ajuste opcional del relleno */\n"
"font-family: Comic Sans MS;\n"
"}\n"
"QPushButton:pressed {\n"
"                background-color: #c0c0c0;\n"
"            }")

        self.horizontalLayout_15.addWidget(self.btn_historial)


        self.verticalLayout_12.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.info1 = QFrame(self.frame_7)
        self.info1.setObjectName(u"info1")
        self.info1.setMaximumSize(QSize(120, 16777215))
        self.info1.setFrameShape(QFrame.StyledPanel)
        self.info1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.info1)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lbl_img1 = QLabel(self.info1)
        self.lbl_img1.setObjectName(u"lbl_img1")
        self.lbl_img1.setMinimumSize(QSize(170, 150))
        self.lbl_img1.setMaximumSize(QSize(150, 150))
        self.lbl_img1.setPixmap(QPixmap(u"hoja.png"))
        self.lbl_img1.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.lbl_img1)

        self.lbl_info1 = QLabel(self.info1)
        self.lbl_info1.setObjectName(u"lbl_info1")
        self.lbl_info1.setMinimumSize(QSize(170, 18))
        self.lbl_info1.setMaximumSize(QSize(118, 18))

        self.verticalLayout_13.addWidget(self.lbl_info1)


        self.horizontalLayout_78.addWidget(self.info1)

        self.info2 = QFrame(self.frame_7)
        self.info2.setObjectName(u"info2")
        self.info2.setMaximumSize(QSize(120, 16777215))
        self.info2.setFrameShape(QFrame.StyledPanel)
        self.info2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.info2)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lbl_img2 = QLabel(self.info2)
        self.lbl_img2.setObjectName(u"lbl_img2")
        self.lbl_img2.setMinimumSize(QSize(170, 150))

        self.verticalLayout_14.addWidget(self.lbl_img2)

        self.lbl_info2 = QLabel(self.info2)
        self.lbl_info2.setObjectName(u"lbl_info2")
        self.lbl_info2.setMinimumSize(QSize(170, 18))
        self.lbl_info2.setMaximumSize(QSize(118, 18))

        self.verticalLayout_14.addWidget(self.lbl_info2)


        self.horizontalLayout_78.addWidget(self.info2)

        self.info3 = QFrame(self.frame_7)
        self.info3.setObjectName(u"info3")
        self.info3.setMaximumSize(QSize(120, 16777215))
        self.info3.setFrameShape(QFrame.StyledPanel)
        self.info3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.info3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lbl_img3 = QLabel(self.info3)
        self.lbl_img3.setObjectName(u"lbl_img3")
        self.lbl_img3.setMinimumSize(QSize(170, 150))

        self.verticalLayout_15.addWidget(self.lbl_img3)

        self.lbl_info3 = QLabel(self.info3)
        self.lbl_info3.setObjectName(u"lbl_info3")
        self.lbl_info3.setMinimumSize(QSize(170, 18))
        self.lbl_info3.setMaximumSize(QSize(118, 18))

        self.verticalLayout_15.addWidget(self.lbl_info3)


        self.horizontalLayout_78.addWidget(self.info3)


        self.verticalLayout_12.addWidget(self.frame_7)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.paginas_menu.addWidget(self.page_inicio)
        self.page_recursos = QWidget()
        self.page_recursos.setObjectName(u"page_recursos")
        self.verticalLayout_20 = QVBoxLayout(self.page_recursos)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.page_recursos)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1314, 447))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.grid_agregar_recur = QGridLayout()
        self.grid_agregar_recur.setObjectName(u"grid_agregar_recur")

        self.verticalLayout.addLayout(self.grid_agregar_recur)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_20.addWidget(self.scrollArea_2)

        self.paginas_menu.addWidget(self.page_recursos)
        self.page_inforecurso = QWidget()
        self.page_inforecurso.setObjectName(u"page_inforecurso")
        self.verticalLayout_27 = QVBoxLayout(self.page_inforecurso)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.page_inforecurso)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setMaximumSize(QSize(16777215, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_regresar_recurso = QPushButton(self.frame_18)
        self.btn_regresar_recurso.setObjectName(u"btn_regresar_recurso")
        self.btn_regresar_recurso.setMinimumSize(QSize(30, 30))
        self.btn_regresar_recurso.setMaximumSize(QSize(30, 30))
        icon10 = QIcon()
        icon10.addFile(u"image/regresar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_regresar_recurso.setIcon(icon10)
        self.btn_regresar_recurso.setIconSize(QSize(25, 25))

        self.horizontalLayout_18.addWidget(self.btn_regresar_recurso)

        self.horizontalSpacer_14 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_14)


        self.verticalLayout_27.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.page_inforecurso)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_17)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 90))
        self.frame_19.setMaximumSize(QSize(16777215, 90))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lbl_img_recurso = QLabel(self.frame_19)
        self.lbl_img_recurso.setObjectName(u"lbl_img_recurso")
        self.lbl_img_recurso.setMinimumSize(QSize(90, 90))
        self.lbl_img_recurso.setMaximumSize(QSize(90, 90))
        self.lbl_img_recurso.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.lbl_img_recurso)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(10)
        self.label_29 = QLabel(self.frame_19)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_29)

        self.lbl_recurso = QLabel(self.frame_19)
        self.lbl_recurso.setObjectName(u"lbl_recurso")
        self.lbl_recurso.setMinimumSize(QSize(200, 0))
        self.lbl_recurso.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lbl_recurso)

        self.label_31 = QLabel(self.frame_19)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_31)

        self.label_32 = QLabel(self.frame_19)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_32)

        self.label_33 = QLabel(self.frame_19)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_33)

        self.lbl_id_recurso = QLabel(self.frame_19)
        self.lbl_id_recurso.setObjectName(u"lbl_id_recurso")
        self.lbl_id_recurso.setMinimumSize(QSize(200, 0))
        self.lbl_id_recurso.setMaximumSize(QSize(200, 16777215))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lbl_id_recurso)

        self.lbl_nombre_recur = QLabel(self.frame_19)
        self.lbl_nombre_recur.setObjectName(u"lbl_nombre_recur")
        self.lbl_nombre_recur.setMinimumSize(QSize(200, 20))
        self.lbl_nombre_recur.setMaximumSize(QSize(200, 20))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lbl_nombre_recur)

        self.lbl_cienti_recur = QLabel(self.frame_19)
        self.lbl_cienti_recur.setObjectName(u"lbl_cienti_recur")
        self.lbl_cienti_recur.setMinimumSize(QSize(200, 20))
        self.lbl_cienti_recur.setMaximumSize(QSize(200, 20))

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lbl_cienti_recur)


        self.horizontalLayout_19.addLayout(self.formLayout_2)


        self.verticalLayout_29.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_20)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_21)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.frame_21)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 20))
        self.label_34.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_31.addWidget(self.label_34)

        self.scrollArea_5 = QScrollArea(self.frame_21)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setMinimumSize(QSize(0, 82))
        self.scrollArea_5.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1291, 100))
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.lbl_info_produc = QLabel(self.scrollAreaWidgetContents_5)
        self.lbl_info_produc.setObjectName(u"lbl_info_produc")
        self.lbl_info_produc.setMinimumSize(QSize(0, 82))
        self.lbl_info_produc.setMaximumSize(QSize(16777215, 82))
        self.lbl_info_produc.setWordWrap(True)

        self.verticalLayout_58.addWidget(self.lbl_info_produc)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_31.addWidget(self.scrollArea_5)


        self.verticalLayout_30.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_23)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_23)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(0, 20))
        self.label_37.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_32.addWidget(self.label_37)

        self.scrollArea_6 = QScrollArea(self.frame_23)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 82))
        self.scrollArea_6.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 651, 80))
        self.verticalLayout_59 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.lbl_usos_produc = QLabel(self.scrollAreaWidgetContents_6)
        self.lbl_usos_produc.setObjectName(u"lbl_usos_produc")
        self.lbl_usos_produc.setWordWrap(True)

        self.verticalLayout_59.addWidget(self.lbl_usos_produc)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_32.addWidget(self.scrollArea_6)


        self.horizontalLayout_20.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_24)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_24)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 20))
        self.label_39.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_33.addWidget(self.label_39)

        self.scrollArea_7 = QScrollArea(self.frame_24)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMinimumSize(QSize(0, 82))
        self.scrollArea_7.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 651, 80))
        self.verticalLayout_60 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.lbl_contra_produc = QLabel(self.scrollAreaWidgetContents_7)
        self.lbl_contra_produc.setObjectName(u"lbl_contra_produc")
        self.lbl_contra_produc.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.lbl_contra_produc)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_33.addWidget(self.scrollArea_7)


        self.horizontalLayout_20.addWidget(self.frame_24)


        self.verticalLayout_30.addWidget(self.frame_22)


        self.verticalLayout_29.addWidget(self.frame_20)


        self.verticalLayout_27.addWidget(self.frame_17)

        self.paginas_menu.addWidget(self.page_inforecurso)
        self.page_recetas = QWidget()
        self.page_recetas.setObjectName(u"page_recetas")
        self.verticalLayout_23 = QVBoxLayout(self.page_recetas)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_52 = QFrame(self.page_recetas)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 40))
        self.frame_52.setMaximumSize(QSize(16777215, 40))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_21 = QSpacerItem(760, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_21)

        self.cbox_filtro_receta = QComboBox(self.frame_52)
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.addItem("")
        self.cbox_filtro_receta.setObjectName(u"cbox_filtro_receta")

        self.horizontalLayout_33.addWidget(self.cbox_filtro_receta)


        self.verticalLayout_23.addWidget(self.frame_52)

        self.scrollArea_3 = QScrollArea(self.page_recetas)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1296, 383))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.grid_recetas = QGridLayout()
        self.grid_recetas.setObjectName(u"grid_recetas")
        self.grid_recetas.setVerticalSpacing(10)

        self.verticalLayout_24.addLayout(self.grid_recetas)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_23.addWidget(self.scrollArea_3)

        self.paginas_menu.addWidget(self.page_recetas)
        self.page_inforeceta = QWidget()
        self.page_inforeceta.setObjectName(u"page_inforeceta")
        self.verticalLayout_41 = QVBoxLayout(self.page_inforeceta)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_25 = QFrame(self.page_inforeceta)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_25)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_25)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 20))
        self.frame_10.setMaximumSize(QSize(16777215, 30))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_regresar_receta = QPushButton(self.frame_10)
        self.btn_regresar_receta.setObjectName(u"btn_regresar_receta")
        self.btn_regresar_receta.setMinimumSize(QSize(25, 25))
        self.btn_regresar_receta.setMaximumSize(QSize(25, 25))
        self.btn_regresar_receta.setIcon(icon10)
        self.btn_regresar_receta.setIconSize(QSize(25, 25))

        self.horizontalLayout_16.addWidget(self.btn_regresar_receta)

        self.horizontalSpacer_13 = QSpacerItem(866, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)


        self.verticalLayout_36.addWidget(self.frame_10)

        self.lbl_receta = QLabel(self.frame_25)
        self.lbl_receta.setObjectName(u"lbl_receta")
        self.lbl_receta.setMinimumSize(QSize(0, 20))
        self.lbl_receta.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_36.addWidget(self.lbl_receta)

        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 90))
        self.frame_26.setMaximumSize(QSize(16777215, 90))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_26)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(90, 90))
        self.frame_32.setMaximumSize(QSize(90, 90))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.lbl_img_receta = QLabel(self.frame_32)
        self.lbl_img_receta.setObjectName(u"lbl_img_receta")
        self.lbl_img_receta.setMinimumSize(QSize(90, 90))
        self.lbl_img_receta.setMaximumSize(QSize(90, 90))
        self.lbl_img_receta.setPixmap(QPixmap(u"recetas.png"))
        self.lbl_img_receta.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.lbl_img_receta)


        self.horizontalLayout_21.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_26)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_33)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_52 = QLabel(self.frame_33)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(0, 20))
        self.label_52.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_42.addWidget(self.label_52)

        self.scrollArea_8 = QScrollArea(self.frame_33)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1182, 40))
        self.verticalLayout_61 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.lbl_afecci_recetas = QLabel(self.scrollAreaWidgetContents_8)
        self.lbl_afecci_recetas.setObjectName(u"lbl_afecci_recetas")
        self.lbl_afecci_recetas.setWordWrap(True)

        self.verticalLayout_61.addWidget(self.lbl_afecci_recetas)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_42.addWidget(self.scrollArea_8)


        self.horizontalLayout_21.addWidget(self.frame_33)


        self.verticalLayout_36.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_27)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_28)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_28)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 20))
        self.label_46.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_38.addWidget(self.label_46)

        self.scrollArea_9 = QScrollArea(self.frame_28)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1290, 77))
        self.verticalLayout_62 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.lbl_ingredientes_rece = QLabel(self.scrollAreaWidgetContents_9)
        self.lbl_ingredientes_rece.setObjectName(u"lbl_ingredientes_rece")
        self.lbl_ingredientes_rece.setWordWrap(True)

        self.verticalLayout_62.addWidget(self.lbl_ingredientes_rece)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_38.addWidget(self.scrollArea_9)


        self.verticalLayout_37.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_30)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_30)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 20))
        self.label_48.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_39.addWidget(self.label_48)

        self.scrollArea_10 = QScrollArea(self.frame_30)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 642, 80))
        self.verticalLayout_63 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.lbl_prepara_rece = QLabel(self.scrollAreaWidgetContents_10)
        self.lbl_prepara_rece.setObjectName(u"lbl_prepara_rece")
        self.lbl_prepara_rece.setWordWrap(True)

        self.verticalLayout_63.addWidget(self.lbl_prepara_rece)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_39.addWidget(self.scrollArea_10)


        self.horizontalLayout_22.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_31)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_31)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(0, 20))
        self.label_50.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_40.addWidget(self.label_50)

        self.scrollArea_11 = QScrollArea(self.frame_31)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 642, 80))
        self.verticalLayout_64 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.lbl_contra_rece = QLabel(self.scrollAreaWidgetContents_12)
        self.lbl_contra_rece.setObjectName(u"lbl_contra_rece")
        self.lbl_contra_rece.setWordWrap(True)

        self.verticalLayout_64.addWidget(self.lbl_contra_rece)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_12)

        self.verticalLayout_40.addWidget(self.scrollArea_11)


        self.horizontalLayout_22.addWidget(self.frame_31)


        self.verticalLayout_37.addWidget(self.frame_29)

        self.frame_34 = QFrame(self.frame_27)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(0, 35))
        self.frame_34.setMaximumSize(QSize(16777215, 35))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_15 = QSpacerItem(291, 12, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_15)

        self.label_54 = QLabel(self.frame_34)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(0, 20))
        self.label_54.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_24.addWidget(self.label_54)

        self.pushButton_19 = QPushButton(self.frame_34)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(24, 24))
        self.pushButton_19.setMaximumSize(QSize(24, 24))
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"image/estresin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon11)
        self.pushButton_19.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_34)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(24, 24))
        self.pushButton_20.setMaximumSize(QSize(24, 24))
        self.pushButton_20.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}")
        self.pushButton_20.setIcon(icon11)
        self.pushButton_20.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_34)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(24, 24))
        self.pushButton_21.setMaximumSize(QSize(24, 24))
        self.pushButton_21.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}")
        self.pushButton_21.setIcon(icon11)
        self.pushButton_21.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.frame_34)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setMinimumSize(QSize(24, 24))
        self.pushButton_22.setMaximumSize(QSize(24, 24))
        self.pushButton_22.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}")
        self.pushButton_22.setIcon(icon11)
        self.pushButton_22.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.frame_34)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(24, 24))
        self.pushButton_23.setMaximumSize(QSize(24, 24))
        self.pushButton_23.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: none;\n"
"    background-repeat: none;\n"
"}")
        self.pushButton_23.setIcon(icon11)
        self.pushButton_23.setIconSize(QSize(20, 20))

        self.horizontalLayout_24.addWidget(self.pushButton_23)


        self.verticalLayout_37.addWidget(self.frame_34)


        self.verticalLayout_36.addWidget(self.frame_27)

        self.frame_13 = QFrame(self.frame_25)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(1, 1, 1, 1)
        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_45)

        self.lbl_prom_rec = QLabel(self.frame_13)
        self.lbl_prom_rec.setObjectName(u"lbl_prom_rec")

        self.horizontalLayout_63.addWidget(self.lbl_prom_rec)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_54)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_47)

        self.horizontalLayout_63.setStretch(0, 8)
        self.horizontalLayout_63.setStretch(1, 1)

        self.horizontalLayout_73.addLayout(self.horizontalLayout_63)


        self.verticalLayout_36.addWidget(self.frame_13)


        self.verticalLayout_41.addWidget(self.frame_25)

        self.paginas_menu.addWidget(self.page_inforeceta)
        self.page_provedores = QWidget()
        self.page_provedores.setObjectName(u"page_provedores")
        self.verticalLayout_43 = QVBoxLayout(self.page_provedores)
        self.verticalLayout_43.setSpacing(5)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.page_provedores)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(0, 40))
        self.frame_35.setMaximumSize(QSize(16777215, 40))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_42 = QLabel(self.frame_35)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_25.addWidget(self.label_42)

        self.horizontalSpacer_16 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_16)

        self.cbox_filtro_prove = QComboBox(self.frame_35)
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.addItem("")
        self.cbox_filtro_prove.setObjectName(u"cbox_filtro_prove")

        self.horizontalLayout_25.addWidget(self.cbox_filtro_prove)


        self.verticalLayout_43.addWidget(self.frame_35)

        self.scrollArea_4 = QScrollArea(self.page_provedores)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1314, 402))
        self.verticalLayout_44 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.grid_prove = QGridLayout()
        self.grid_prove.setSpacing(10)
        self.grid_prove.setObjectName(u"grid_prove")
        self.grid_prove.setContentsMargins(-1, -1, -1, 0)

        self.verticalLayout_44.addLayout(self.grid_prove)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_43.addWidget(self.scrollArea_4)

        self.paginas_menu.addWidget(self.page_provedores)
        self.page_nosotros = QWidget()
        self.page_nosotros.setObjectName(u"page_nosotros")
        self.verticalLayout_51 = QVBoxLayout(self.page_nosotros)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.page_nosotros)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(0, 90))
        self.frame_41.setMaximumSize(QSize(16777215, 90))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.frame_41)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setPixmap(QPixmap(u"image/Hermedcol.png"))
        self.label_76.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_76)


        self.verticalLayout_51.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.page_nosotros)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMinimumSize(QSize(0, 90))
        self.frame_42.setMaximumSize(QSize(16777215, 90))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(135, 70))
        self.frame_44.setMaximumSize(QSize(135, 70))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_44)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_77 = QLabel(self.frame_44)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(40, 40))
        self.label_77.setMaximumSize(QSize(40, 40))
        self.label_77.setPixmap(QPixmap(u"image/userhembra.png"))
        self.label_77.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.label_77)

        self.label_79 = QLabel(self.frame_44)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(0, 28))
        self.label_79.setMaximumSize(QSize(16777215, 28))
        self.label_79.setPixmap(QPixmap(u"image/mari.png"))
        self.label_79.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.label_79)


        self.horizontalLayout_29.addWidget(self.frame_44)

        self.frame_48 = QFrame(self.frame_42)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMinimumSize(QSize(135, 70))
        self.frame_48.setMaximumSize(QSize(135, 70))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_48)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_86 = QLabel(self.frame_48)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(40, 40))
        self.label_86.setMaximumSize(QSize(40, 40))
        self.label_86.setPixmap(QPixmap(u"image/usermacho.png"))
        self.label_86.setScaledContents(True)

        self.verticalLayout_56.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_48)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(0, 23))
        self.label_87.setMaximumSize(QSize(16777215, 25))
        self.label_87.setPixmap(QPixmap(u"image/juan.png"))
        self.label_87.setScaledContents(True)

        self.verticalLayout_56.addWidget(self.label_87)


        self.horizontalLayout_29.addWidget(self.frame_48)

        self.frame_45 = QFrame(self.frame_42)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(135, 70))
        self.frame_45.setMaximumSize(QSize(135, 70))
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_45)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_80 = QLabel(self.frame_45)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(40, 40))
        self.label_80.setMaximumSize(QSize(40, 40))
        self.label_80.setPixmap(QPixmap(u"image/userhembra.png"))
        self.label_80.setScaledContents(True)

        self.verticalLayout_53.addWidget(self.label_80)

        self.label_81 = QLabel(self.frame_45)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(0, 28))
        self.label_81.setMaximumSize(QSize(16777215, 20))
        self.label_81.setPixmap(QPixmap(u"image/nidia.png"))
        self.label_81.setScaledContents(True)

        self.verticalLayout_53.addWidget(self.label_81)


        self.horizontalLayout_29.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_42)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QSize(135, 70))
        self.frame_46.setMaximumSize(QSize(135, 70))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_46)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_82 = QLabel(self.frame_46)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(40, 40))
        self.label_82.setMaximumSize(QSize(40, 40))
        self.label_82.setPixmap(QPixmap(u"image/usermacho.png"))
        self.label_82.setScaledContents(True)

        self.verticalLayout_54.addWidget(self.label_82)

        self.label_83 = QLabel(self.frame_46)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(0, 28))
        self.label_83.setMaximumSize(QSize(16777215, 20))
        self.label_83.setPixmap(QPixmap(u"image/alejandro.png"))
        self.label_83.setScaledContents(True)

        self.verticalLayout_54.addWidget(self.label_83)


        self.horizontalLayout_29.addWidget(self.frame_46)


        self.verticalLayout_51.addWidget(self.frame_42)

        self.frame_43 = QFrame(self.page_nosotros)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_47)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.frame_47)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(286, 166))
        self.label_84.setMaximumSize(QSize(16777215, 166))
        self.label_84.setWordWrap(True)

        self.verticalLayout_55.addWidget(self.label_84)


        self.horizontalLayout_30.addWidget(self.frame_47)

        self.frame_49 = QFrame(self.frame_43)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(286, 166))
        self.frame_49.setMaximumSize(QSize(16777215, 166))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_49)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 40))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_85 = QLabel(self.frame_50)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_31.addWidget(self.label_85)


        self.verticalLayout_57.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_49)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_26 = QPushButton(self.frame_51)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(40, 40))
        self.pushButton_26.setMaximumSize(QSize(40, 40))
        icon12 = QIcon()
        icon12.addFile(u"image/telefono.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_26.setIcon(icon12)
        self.pushButton_26.setIconSize(QSize(30, 30))

        self.horizontalLayout_32.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame_51)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(40, 40))
        self.pushButton_27.setMaximumSize(QSize(40, 40))
        icon13 = QIcon()
        icon13.addFile(u"image/correo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon13)
        self.pushButton_27.setIconSize(QSize(30, 30))

        self.horizontalLayout_32.addWidget(self.pushButton_27)


        self.verticalLayout_57.addWidget(self.frame_51)


        self.horizontalLayout_30.addWidget(self.frame_49)


        self.verticalLayout_51.addWidget(self.frame_43)

        self.paginas_menu.addWidget(self.page_nosotros)
        self.page_buscar = QWidget()
        self.page_buscar.setObjectName(u"page_buscar")
        self.verticalLayout_19 = QVBoxLayout(self.page_buscar)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.page_buscar)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 40))
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.btn_regresar_buscar_home = QPushButton(self.frame_14)
        self.btn_regresar_buscar_home.setObjectName(u"btn_regresar_buscar_home")
        self.btn_regresar_buscar_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_buscar_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_buscar_home.setIcon(icon10)
        self.btn_regresar_buscar_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_64.addWidget(self.btn_regresar_buscar_home)

        self.horizontalSpacer_46 = QSpacerItem(1257, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_46)


        self.verticalLayout_19.addWidget(self.frame_14)

        self.scrollArea = QScrollArea(self.page_buscar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1314, 407))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.grid_buscar = QGridLayout()
        self.grid_buscar.setObjectName(u"grid_buscar")
        self.grid_buscar.setHorizontalSpacing(6)
        self.grid_buscar.setVerticalSpacing(10)

        self.verticalLayout_25.addLayout(self.grid_buscar)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_19.addWidget(self.scrollArea)

        self.paginas_menu.addWidget(self.page_buscar)
        self.page_editar_info = QWidget()
        self.page_editar_info.setObjectName(u"page_editar_info")
        self.verticalLayout_21 = QVBoxLayout(self.page_editar_info)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.page_editar_info)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 120))
        self.widget_16.setMaximumSize(QSize(16777215, 120))
        self.horizontalLayout_47 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.lbl_id_mod = QLabel(self.widget_16)
        self.lbl_id_mod.setObjectName(u"lbl_id_mod")
        self.lbl_id_mod.setMinimumSize(QSize(70, 70))
        self.lbl_id_mod.setMaximumSize(QSize(70, 70))

        self.horizontalLayout_47.addWidget(self.lbl_id_mod)

        self.horizontalSpacer_38 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_38)

        self.lbl_user_2 = QLabel(self.widget_16)
        self.lbl_user_2.setObjectName(u"lbl_user_2")
        self.lbl_user_2.setMinimumSize(QSize(90, 90))
        self.lbl_user_2.setMaximumSize(QSize(90, 90))
        self.lbl_user_2.setPixmap(QPixmap(u"image/usuario.png"))
        self.lbl_user_2.setScaledContents(True)

        self.horizontalLayout_47.addWidget(self.lbl_user_2)

        self.horizontalSpacer_39 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_39)


        self.verticalLayout_21.addWidget(self.widget_16)

        self.frame_11 = QFrame(self.page_editar_info)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(557, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_12)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(50)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_telefono_mod = QPushButton(self.frame_12)
        self.btn_telefono_mod.setObjectName(u"btn_telefono_mod")

        self.gridLayout.addWidget(self.btn_telefono_mod, 0, 1, 1, 1)

        self.btn_nombre_mod = QPushButton(self.frame_12)
        self.btn_nombre_mod.setObjectName(u"btn_nombre_mod")

        self.gridLayout.addWidget(self.btn_nombre_mod, 0, 0, 1, 1)

        self.btn_correo_mod = QPushButton(self.frame_12)
        self.btn_correo_mod.setObjectName(u"btn_correo_mod")

        self.gridLayout.addWidget(self.btn_correo_mod, 1, 0, 1, 1)

        self.btn_password_mod = QPushButton(self.frame_12)
        self.btn_password_mod.setObjectName(u"btn_password_mod")

        self.gridLayout.addWidget(self.btn_password_mod, 1, 1, 1, 1)


        self.verticalLayout_22.addLayout(self.gridLayout)


        self.horizontalLayout_59.addWidget(self.frame_12)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.paginas_menu.addWidget(self.page_editar_info)
        self.page_hitorial = QWidget()
        self.page_hitorial.setObjectName(u"page_hitorial")
        self.verticalLayout_26 = QVBoxLayout(self.page_hitorial)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.page_hitorial)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 60))
        self.frame_15.setMaximumSize(QSize(16777215, 60))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_67 = QSpacerItem(614, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_67)

        self.lbl_img_buscar = QLabel(self.frame_15)
        self.lbl_img_buscar.setObjectName(u"lbl_img_buscar")
        self.lbl_img_buscar.setMinimumSize(QSize(50, 50))
        self.lbl_img_buscar.setMaximumSize(QSize(50, 50))
        self.lbl_img_buscar.setPixmap(QPixmap(u"image/historial.png"))
        self.lbl_img_buscar.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.lbl_img_buscar)

        self.horizontalSpacer_68 = QSpacerItem(614, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_68)


        self.verticalLayout_26.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.page_hitorial)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalSpacer_55 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_55)

        self.tabl_historial = QTableWidget(self.frame_16)
        if (self.tabl_historial.columnCount() < 3):
            self.tabl_historial.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabl_historial.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabl_historial.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabl_historial.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabl_historial.setObjectName(u"tabl_historial")
        self.tabl_historial.setMinimumSize(QSize(311, 351))
        self.tabl_historial.setMaximumSize(QSize(311, 351))

        self.horizontalLayout_76.addWidget(self.tabl_historial)

        self.horizontalSpacer_66 = QSpacerItem(483, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_66)


        self.verticalLayout_26.addWidget(self.frame_16)

        self.paginas_menu.addWidget(self.page_hitorial)

        self.verticalLayout_9.addWidget(self.paginas_menu)


        self.horizontalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.paginas_usuarios.addWidget(self.page_user)
        self.page_registro = QWidget()
        self.page_registro.setObjectName(u"page_registro")
        self.verticalLayout_2 = QVBoxLayout(self.page_registro)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.page_registro)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lbl_user_regis = QLabel(self.widget)
        self.lbl_user_regis.setObjectName(u"lbl_user_regis")
        self.lbl_user_regis.setMinimumSize(QSize(90, 90))
        self.lbl_user_regis.setMaximumSize(QSize(90, 90))
        self.lbl_user_regis.setPixmap(QPixmap(u"image/usuario.png"))
        self.lbl_user_regis.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lbl_user_regis)

        self.horizontalSpacer_2 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_regresar_regis_inicio = QPushButton(self.widget)
        self.btn_regresar_regis_inicio.setObjectName(u"btn_regresar_regis_inicio")
        self.btn_regresar_regis_inicio.setMinimumSize(QSize(30, 30))
        self.btn_regresar_regis_inicio.setMaximumSize(QSize(30, 30))
        self.btn_regresar_regis_inicio.setIcon(icon10)
        self.btn_regresar_regis_inicio.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_regresar_regis_inicio)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.page_registro)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.ln_Nombre = QLineEdit(self.widget_5)
        self.ln_Nombre.setObjectName(u"ln_Nombre")

        self.verticalLayout_3.addWidget(self.ln_Nombre)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.ln_cod = QLineEdit(self.widget_5)
        self.ln_cod.setObjectName(u"ln_cod")

        self.verticalLayout_3.addWidget(self.ln_cod)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.ln_tel = QLineEdit(self.widget_5)
        self.ln_tel.setObjectName(u"ln_tel")

        self.verticalLayout_3.addWidget(self.ln_tel)

        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.ln_correo = QLineEdit(self.widget_5)
        self.ln_correo.setObjectName(u"ln_correo")

        self.verticalLayout_3.addWidget(self.ln_correo)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.ln_Username = QLineEdit(self.widget_6)
        self.ln_Username.setObjectName(u"ln_Username")

        self.verticalLayout_4.addWidget(self.ln_Username)

        self.label_7 = QLabel(self.widget_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.ln_Password = QLineEdit(self.widget_6)
        self.ln_Password.setObjectName(u"ln_Password")

        self.verticalLayout_4.addWidget(self.ln_Password)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.ln_Confirm = QLineEdit(self.widget_6)
        self.ln_Confirm.setObjectName(u"ln_Confirm")

        self.verticalLayout_4.addWidget(self.ln_Confirm)

        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 23))
        self.label_9.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page_registro)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(304, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_registrar = QPushButton(self.widget_4)
        self.btn_registrar.setObjectName(u"btn_registrar")
        self.btn_registrar.setMinimumSize(QSize(120, 40))

        self.horizontalLayout_4.addWidget(self.btn_registrar)

        self.horizontalSpacer_4 = QSpacerItem(304, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.paginas_usuarios.addWidget(self.page_registro)
        self.page_recuperar = QWidget()
        self.page_recuperar.setObjectName(u"page_recuperar")
        self.verticalLayout_49 = QVBoxLayout(self.page_recuperar)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.page_recuperar)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(0, 120))
        self.widget_14.setMaximumSize(QSize(16777215, 120))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_17 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_17)

        self.lbl_user_recu = QLabel(self.widget_14)
        self.lbl_user_recu.setObjectName(u"lbl_user_recu")
        self.lbl_user_recu.setMinimumSize(QSize(90, 90))
        self.lbl_user_recu.setMaximumSize(QSize(90, 90))
        self.lbl_user_recu.setPixmap(QPixmap(u"image/usuario.png"))
        self.lbl_user_recu.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.lbl_user_recu)

        self.horizontalSpacer_18 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_18)

        self.btn_regresar_recu_inicio = QPushButton(self.widget_14)
        self.btn_regresar_recu_inicio.setObjectName(u"btn_regresar_recu_inicio")
        self.btn_regresar_recu_inicio.setMinimumSize(QSize(30, 30))
        self.btn_regresar_recu_inicio.setMaximumSize(QSize(30, 30))
        self.btn_regresar_recu_inicio.setIcon(icon10)
        self.btn_regresar_recu_inicio.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.btn_regresar_recu_inicio)


        self.verticalLayout_49.addWidget(self.widget_14)

        self.frame_40 = QFrame(self.page_recuperar)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_19 = QSpacerItem(257, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_19)

        self.widget_15 = QWidget(self.frame_40)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_50 = QVBoxLayout(self.widget_15)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_73 = QLabel(self.widget_15)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_50.addWidget(self.label_73)

        self.ln_correo_recu = QLineEdit(self.widget_15)
        self.ln_correo_recu.setObjectName(u"ln_correo_recu")

        self.verticalLayout_50.addWidget(self.ln_correo_recu)

        self.label_74 = QLabel(self.widget_15)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_50.addWidget(self.label_74)

        self.ln_user_recu = QLineEdit(self.widget_15)
        self.ln_user_recu.setObjectName(u"ln_user_recu")

        self.verticalLayout_50.addWidget(self.ln_user_recu)

        self.btn_verificar_contra = QPushButton(self.widget_15)
        self.btn_verificar_contra.setObjectName(u"btn_verificar_contra")
        self.btn_verificar_contra.setMinimumSize(QSize(120, 30))
        self.btn_verificar_contra.setMaximumSize(QSize(120, 30))
        self.btn_verificar_contra.setStyleSheet(u"font: 12px")

        self.verticalLayout_50.addWidget(self.btn_verificar_contra)

        self.label_22 = QLabel(self.widget_15)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_50.addWidget(self.label_22)

        self.line_veri_cod = QLineEdit(self.widget_15)
        self.line_veri_cod.setObjectName(u"line_veri_cod")

        self.verticalLayout_50.addWidget(self.line_veri_cod)

        self.btn_veri_cod = QPushButton(self.widget_15)
        self.btn_veri_cod.setObjectName(u"btn_veri_cod")
        self.btn_veri_cod.setMinimumSize(QSize(120, 30))
        self.btn_veri_cod.setMaximumSize(QSize(120, 30))
        self.btn_veri_cod.setStyleSheet(u"font: 9pt \"Times New Roman\";")

        self.verticalLayout_50.addWidget(self.btn_veri_cod)

        self.label_75 = QLabel(self.widget_15)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_50.addWidget(self.label_75)

        self.ln_pass_new = QLineEdit(self.widget_15)
        self.ln_pass_new.setObjectName(u"ln_pass_new")
        self.ln_pass_new.setEnabled(False)

        self.verticalLayout_50.addWidget(self.ln_pass_new)

        self.label_78 = QLabel(self.widget_15)
        self.label_78.setObjectName(u"label_78")

        self.verticalLayout_50.addWidget(self.label_78)

        self.ln_pass_confirm = QLineEdit(self.widget_15)
        self.ln_pass_confirm.setObjectName(u"ln_pass_confirm")
        self.ln_pass_confirm.setEnabled(False)

        self.verticalLayout_50.addWidget(self.ln_pass_confirm)

        self.btn_confirmar_pass = QPushButton(self.widget_15)
        self.btn_confirmar_pass.setObjectName(u"btn_confirmar_pass")
        self.btn_confirmar_pass.setMinimumSize(QSize(120, 30))
        self.btn_confirmar_pass.setMaximumSize(QSize(120, 30))
        self.btn_confirmar_pass.setStyleSheet(u"font: 12px")

        self.verticalLayout_50.addWidget(self.btn_confirmar_pass)


        self.horizontalLayout_27.addWidget(self.widget_15)

        self.horizontalSpacer_20 = QSpacerItem(257, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_20)


        self.verticalLayout_49.addWidget(self.frame_40)

        self.paginas_usuarios.addWidget(self.page_recuperar)
        self.page_sesion = QWidget()
        self.page_sesion.setObjectName(u"page_sesion")
        self.verticalLayout_5 = QVBoxLayout(self.page_sesion)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.page_sesion)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 120))
        self.widget_9.setMaximumSize(QSize(16777215, 120))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_8 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)

        self.lbl_user = QLabel(self.widget_9)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setMinimumSize(QSize(90, 90))
        self.lbl_user.setMaximumSize(QSize(90, 90))
        self.lbl_user.setPixmap(QPixmap(u"image/usuario.png"))
        self.lbl_user.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lbl_user)

        self.horizontalSpacer_9 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.page_sesion)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_6 = QVBoxLayout(self.widget_10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 200))
        self.widget_11.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_10 = QSpacerItem(264, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.widget_13 = QWidget(self.widget_11)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_7 = QVBoxLayout(self.widget_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_7.addWidget(self.label_15)

        self.ln_user_inicio = QLineEdit(self.widget_13)
        self.ln_user_inicio.setObjectName(u"ln_user_inicio")

        self.verticalLayout_7.addWidget(self.ln_user_inicio)

        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_7.addWidget(self.label_16)

        self.ln_password_inicio = QLineEdit(self.widget_13)
        self.ln_password_inicio.setObjectName(u"ln_password_inicio")

        self.verticalLayout_7.addWidget(self.ln_password_inicio)


        self.horizontalLayout_8.addWidget(self.widget_13)

        self.horizontalSpacer_11 = QSpacerItem(264, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)


        self.verticalLayout_6.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_10)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_recuperar = QPushButton(self.widget_12)
        self.btn_recuperar.setObjectName(u"btn_recuperar")
        self.btn_recuperar.setMaximumSize(QSize(135, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_recuperar)

        self.btn_iniciar_sesion = QPushButton(self.widget_12)
        self.btn_iniciar_sesion.setObjectName(u"btn_iniciar_sesion")
        self.btn_iniciar_sesion.setMaximumSize(QSize(135, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_iniciar_sesion)

        self.btn_registrarse = QPushButton(self.widget_12)
        self.btn_registrarse.setObjectName(u"btn_registrarse")
        self.btn_registrarse.setMaximumSize(QSize(135, 16777215))

        self.horizontalLayout_9.addWidget(self.btn_registrarse)


        self.verticalLayout_6.addWidget(self.widget_12)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.paginas_usuarios.addWidget(self.page_sesion)
        self.page_admin = QWidget()
        self.page_admin.setObjectName(u"page_admin")
        self.verticalLayout_65 = QVBoxLayout(self.page_admin)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.page_admin)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 45))
        self.frame_3.setMaximumSize(QSize(16777215, 45))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.btn_Menu_admin = QPushButton(self.frame_3)
        self.btn_Menu_admin.setObjectName(u"btn_Menu_admin")
        self.btn_Menu_admin.setMinimumSize(QSize(35, 35))
        self.btn_Menu_admin.setMaximumSize(QSize(35, 35))
        self.btn_Menu_admin.setSizeIncrement(QSize(0, 0))
        self.btn_Menu_admin.setIcon(icon1)
        self.btn_Menu_admin.setIconSize(QSize(25, 25))

        self.horizontalLayout_34.addWidget(self.btn_Menu_admin)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_22)

        self.btn_cerrar_sesion_admin = QPushButton(self.frame_3)
        self.btn_cerrar_sesion_admin.setObjectName(u"btn_cerrar_sesion_admin")
        self.btn_cerrar_sesion_admin.setMinimumSize(QSize(30, 30))
        self.btn_cerrar_sesion_admin.setMaximumSize(QSize(30, 30))
        self.btn_cerrar_sesion_admin.setIcon(icon2)
        self.btn_cerrar_sesion_admin.setIconSize(QSize(30, 30))

        self.horizontalLayout_34.addWidget(self.btn_cerrar_sesion_admin)


        self.verticalLayout_65.addWidget(self.frame_3)

        self.frame_53 = QFrame(self.page_admin)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral_admin = QFrame(self.frame_53)
        self.frame_lateral_admin.setObjectName(u"frame_lateral_admin")
        self.frame_lateral_admin.setMinimumSize(QSize(0, 0))
        self.frame_lateral_admin.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral_admin.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral_admin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_lateral_admin)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.btn_inicio_admin = QPushButton(self.frame_lateral_admin)
        self.btn_inicio_admin.setObjectName(u"btn_inicio_admin")
        self.btn_inicio_admin.setMaximumSize(QSize(16777215, 35))
        self.btn_inicio_admin.setIcon(icon3)
        self.btn_inicio_admin.setIconSize(QSize(27, 27))

        self.verticalLayout_66.addWidget(self.btn_inicio_admin)

        self.btn_recursos_admin = QPushButton(self.frame_lateral_admin)
        self.btn_recursos_admin.setObjectName(u"btn_recursos_admin")
        self.btn_recursos_admin.setMaximumSize(QSize(16777215, 35))
        self.btn_recursos_admin.setIcon(icon4)
        self.btn_recursos_admin.setIconSize(QSize(27, 27))

        self.verticalLayout_66.addWidget(self.btn_recursos_admin)

        self.btn_recetas_admin = QPushButton(self.frame_lateral_admin)
        self.btn_recetas_admin.setObjectName(u"btn_recetas_admin")
        self.btn_recetas_admin.setMaximumSize(QSize(16777215, 35))
        self.btn_recetas_admin.setIcon(icon5)
        self.btn_recetas_admin.setIconSize(QSize(30, 30))

        self.verticalLayout_66.addWidget(self.btn_recetas_admin)

        self.btn_provedores_admin = QPushButton(self.frame_lateral_admin)
        self.btn_provedores_admin.setObjectName(u"btn_provedores_admin")
        self.btn_provedores_admin.setMaximumSize(QSize(16777215, 35))
        self.btn_provedores_admin.setIcon(icon6)
        self.btn_provedores_admin.setIconSize(QSize(30, 30))

        self.verticalLayout_66.addWidget(self.btn_provedores_admin)


        self.horizontalLayout_35.addWidget(self.frame_lateral_admin)

        self.paginas_menu_admin = QStackedWidget(self.frame_53)
        self.paginas_menu_admin.setObjectName(u"paginas_menu_admin")
        self.page_inicio_admin = QWidget()
        self.page_inicio_admin.setObjectName(u"page_inicio_admin")
        self.horizontalLayout_48 = QHBoxLayout(self.page_inicio_admin)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_74 = QFrame(self.page_inicio_admin)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_74)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.frame_74)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalSpacer_30 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_30)

        self.lbl_recu_admin = QLabel(self.frame_77)
        self.lbl_recu_admin.setObjectName(u"lbl_recu_admin")
        self.lbl_recu_admin.setMinimumSize(QSize(200, 50))
        self.lbl_recu_admin.setMaximumSize(QSize(200, 50))
        self.lbl_recu_admin.setPixmap(QPixmap(u"image/recurso.png"))
        self.lbl_recu_admin.setScaledContents(True)

        self.horizontalLayout_50.addWidget(self.lbl_recu_admin)

        self.horizontalSpacer_31 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_31)


        self.verticalLayout_86.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_74)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_78)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalSpacer_36 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_36)

        self.btn_ingresar_recu = QPushButton(self.frame_78)
        self.btn_ingresar_recu.setObjectName(u"btn_ingresar_recu")
        self.btn_ingresar_recu.setMinimumSize(QSize(150, 34))
        self.btn_ingresar_recu.setMaximumSize(QSize(150, 34))

        self.horizontalLayout_54.addWidget(self.btn_ingresar_recu)

        self.horizontalSpacer_37 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_37)


        self.verticalLayout_86.addWidget(self.frame_78)

        self.frame_80 = QFrame(self.frame_74)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSpacer_40 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_40)

        self.btn_modificar_recu = QPushButton(self.frame_80)
        self.btn_modificar_recu.setObjectName(u"btn_modificar_recu")
        self.btn_modificar_recu.setMinimumSize(QSize(150, 34))
        self.btn_modificar_recu.setMaximumSize(QSize(150, 34))

        self.horizontalLayout_52.addWidget(self.btn_modificar_recu)

        self.horizontalSpacer_41 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_41)


        self.verticalLayout_86.addWidget(self.frame_80)


        self.horizontalLayout_48.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.page_inicio_admin)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_75)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame_81 = QFrame(self.frame_75)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_33 = QSpacerItem(62, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_33)

        self.lbl_rece_admin = QLabel(self.frame_81)
        self.lbl_rece_admin.setObjectName(u"lbl_rece_admin")
        self.lbl_rece_admin.setMinimumSize(QSize(200, 50))
        self.lbl_rece_admin.setMaximumSize(QSize(200, 50))
        self.lbl_rece_admin.setPixmap(QPixmap(u"image/rece.png"))
        self.lbl_rece_admin.setScaledContents(True)

        self.horizontalLayout_51.addWidget(self.lbl_rece_admin)

        self.horizontalSpacer_32 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_32)


        self.verticalLayout_87.addWidget(self.frame_81)

        self.frame_84 = QFrame(self.frame_75)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_43 = QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_43)

        self.btn_ingresar_rece = QPushButton(self.frame_84)
        self.btn_ingresar_rece.setObjectName(u"btn_ingresar_rece")
        self.btn_ingresar_rece.setMinimumSize(QSize(150, 34))
        self.btn_ingresar_rece.setMaximumSize(QSize(150, 34))

        self.horizontalLayout_55.addWidget(self.btn_ingresar_rece)

        self.horizontalSpacer_42 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_42)


        self.verticalLayout_87.addWidget(self.frame_84)

        self.frame_83 = QFrame(self.frame_75)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer_51 = QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_51)

        self.btn_modificar_rece = QPushButton(self.frame_83)
        self.btn_modificar_rece.setObjectName(u"btn_modificar_rece")
        self.btn_modificar_rece.setMinimumSize(QSize(150, 34))
        self.btn_modificar_rece.setMaximumSize(QSize(150, 34))

        self.horizontalLayout_57.addWidget(self.btn_modificar_rece)

        self.horizontalSpacer_50 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_50)


        self.verticalLayout_87.addWidget(self.frame_83)


        self.horizontalLayout_48.addWidget(self.frame_75)

        self.frame_76 = QFrame(self.page_inicio_admin)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_76)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_76)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalSpacer_34 = QSpacerItem(62, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_34)

        self.lbl_prove_Admin = QLabel(self.frame_85)
        self.lbl_prove_Admin.setObjectName(u"lbl_prove_Admin")
        self.lbl_prove_Admin.setMinimumSize(QSize(200, 50))
        self.lbl_prove_Admin.setMaximumSize(QSize(200, 50))
        self.lbl_prove_Admin.setPixmap(QPixmap(u"image/provedo.png"))
        self.lbl_prove_Admin.setScaledContents(True)

        self.horizontalLayout_49.addWidget(self.lbl_prove_Admin)

        self.horizontalSpacer_35 = QSpacerItem(61, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_35)


        self.verticalLayout_88.addWidget(self.frame_85)

        self.frame_88 = QFrame(self.frame_76)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalSpacer_49 = QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_49)

        self.btn_ingresar_prove = QPushButton(self.frame_88)
        self.btn_ingresar_prove.setObjectName(u"btn_ingresar_prove")
        self.btn_ingresar_prove.setMinimumSize(QSize(150, 34))
        self.btn_ingresar_prove.setMaximumSize(QSize(150, 34))

        self.horizontalLayout_58.addWidget(self.btn_ingresar_prove)

        self.horizontalSpacer_48 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_48)


        self.verticalLayout_88.addWidget(self.frame_88)

        self.frame_87 = QFrame(self.frame_76)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_53 = QSpacerItem(87, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_53)

        self.btn_modificar_prove = QPushButton(self.frame_87)
        self.btn_modificar_prove.setObjectName(u"btn_modificar_prove")
        self.btn_modificar_prove.setMinimumSize(QSize(150, 34))
        self.btn_modificar_prove.setMaximumSize(QSize(150, 34))

        self.horizontalLayout_60.addWidget(self.btn_modificar_prove)

        self.horizontalSpacer_52 = QSpacerItem(86, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_52)


        self.verticalLayout_88.addWidget(self.frame_87)


        self.horizontalLayout_48.addWidget(self.frame_76)

        self.paginas_menu_admin.addWidget(self.page_inicio_admin)
        self.page_recursos_admin = QWidget()
        self.page_recursos_admin.setObjectName(u"page_recursos_admin")
        self.verticalLayout_73 = QVBoxLayout(self.page_recursos_admin)
        self.verticalLayout_73.setSpacing(0)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.verticalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.page_recursos_admin)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 90))
        self.frame_54.setMaximumSize(QSize(16777215, 90))
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.lbl_img_recurso_admin = QLabel(self.frame_54)
        self.lbl_img_recurso_admin.setObjectName(u"lbl_img_recurso_admin")
        self.lbl_img_recurso_admin.setMinimumSize(QSize(90, 90))
        self.lbl_img_recurso_admin.setMaximumSize(QSize(90, 90))
        self.lbl_img_recurso_admin.setPixmap(QPixmap(u"hoja.png"))
        self.lbl_img_recurso_admin.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.lbl_img_recurso_admin)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(6)
        self.formLayout_7.setVerticalSpacing(7)
        self.formLayout_7.setContentsMargins(-1, -1, 5, 5)
        self.label_30 = QLabel(self.frame_54)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_30)

        self.label_35 = QLabel(self.frame_54)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_35)

        self.ln_idrecurso_admin = QLineEdit(self.frame_54)
        self.ln_idrecurso_admin.setObjectName(u"ln_idrecurso_admin")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.ln_idrecurso_admin)

        self.label_36 = QLabel(self.frame_54)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_36)

        self.ln_nombrecomun_admin = QLineEdit(self.frame_54)
        self.ln_nombrecomun_admin.setObjectName(u"ln_nombrecomun_admin")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.ln_nombrecomun_admin)

        self.label_38 = QLabel(self.frame_54)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_38)

        self.ln_nombrecient_admin = QLineEdit(self.frame_54)
        self.ln_nombrecient_admin.setObjectName(u"ln_nombrecient_admin")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.ln_nombrecient_admin)

        self.lbl_numero_recurso = QLabel(self.frame_54)
        self.lbl_numero_recurso.setObjectName(u"lbl_numero_recurso")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lbl_numero_recurso)


        self.horizontalLayout_36.addLayout(self.formLayout_7)


        self.verticalLayout_73.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.page_recursos_admin)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(0, 40))
        self.frame_55.setMaximumSize(QSize(16777215, 40))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_55)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.btn_select_img_recurso = QPushButton(self.frame_55)
        self.btn_select_img_recurso.setObjectName(u"btn_select_img_recurso")
        self.btn_select_img_recurso.setMinimumSize(QSize(120, 30))
        self.btn_select_img_recurso.setMaximumSize(QSize(120, 30))
        self.btn_select_img_recurso.setStyleSheet(u"font-size: 13px")
        self.btn_select_img_recurso.setIconSize(QSize(25, 25))

        self.horizontalLayout_37.addWidget(self.btn_select_img_recurso)

        self.horizontalSpacer_23 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_23)


        self.verticalLayout_73.addWidget(self.frame_55)

        self.frame_57 = QFrame(self.page_recursos_admin)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_57)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_57)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(0, 20))
        self.label_41.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_67.addWidget(self.label_41)

        self.scrollArea_12 = QScrollArea(self.frame_57)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setMinimumSize(QSize(0, 82))
        self.scrollArea_12.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1297, 89))
        self.verticalLayout_68 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.text_descripcion_recurso = QTextEdit(self.scrollAreaWidgetContents_11)
        self.text_descripcion_recurso.setObjectName(u"text_descripcion_recurso")

        self.verticalLayout_68.addWidget(self.text_descripcion_recurso)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_67.addWidget(self.scrollArea_12)


        self.verticalLayout_73.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.page_recursos_admin)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_59)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_59)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(0, 20))
        self.label_47.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_69.addWidget(self.label_47)

        self.scrollArea_13 = QScrollArea(self.frame_59)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setMinimumSize(QSize(0, 82))
        self.scrollArea_13.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 637, 89))
        self.verticalLayout_70 = QVBoxLayout(self.scrollAreaWidgetContents_13)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.text_usos_recurso = QTextEdit(self.scrollAreaWidgetContents_13)
        self.text_usos_recurso.setObjectName(u"text_usos_recurso")

        self.verticalLayout_70.addWidget(self.text_usos_recurso)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)

        self.verticalLayout_69.addWidget(self.scrollArea_13)


        self.horizontalLayout_39.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_60)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_60)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(0, 20))
        self.label_49.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_71.addWidget(self.label_49)

        self.scrollArea_14 = QScrollArea(self.frame_60)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setMinimumSize(QSize(0, 82))
        self.scrollArea_14.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 637, 89))
        self.verticalLayout_72 = QVBoxLayout(self.scrollAreaWidgetContents_14)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.text_contradic_recurso = QTextEdit(self.scrollAreaWidgetContents_14)
        self.text_contradic_recurso.setObjectName(u"text_contradic_recurso")

        self.verticalLayout_72.addWidget(self.text_contradic_recurso)

        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_14)

        self.verticalLayout_71.addWidget(self.scrollArea_14)


        self.horizontalLayout_39.addWidget(self.frame_60)


        self.verticalLayout_73.addWidget(self.frame_58)

        self.frame_56 = QFrame(self.page_recursos_admin)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(0, 40))
        self.frame_56.setMaximumSize(QSize(16777215, 40))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.btn_regresar_recu_home = QPushButton(self.frame_56)
        self.btn_regresar_recu_home.setObjectName(u"btn_regresar_recu_home")
        self.btn_regresar_recu_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_recu_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_recu_home.setIcon(icon10)
        self.btn_regresar_recu_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_38.addWidget(self.btn_regresar_recu_home)

        self.horizontalSpacer_24 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_24)

        self.btn_guardar_recurso = QPushButton(self.frame_56)
        self.btn_guardar_recurso.setObjectName(u"btn_guardar_recurso")
        self.btn_guardar_recurso.setMinimumSize(QSize(120, 30))
        self.btn_guardar_recurso.setMaximumSize(QSize(120, 30))
        self.btn_guardar_recurso.setStyleSheet(u"font-size: 13px")
        self.btn_guardar_recurso.setIconSize(QSize(25, 25))

        self.horizontalLayout_38.addWidget(self.btn_guardar_recurso)


        self.verticalLayout_73.addWidget(self.frame_56)

        self.paginas_menu_admin.addWidget(self.page_recursos_admin)
        self.page_recetas_admin = QWidget()
        self.page_recetas_admin.setObjectName(u"page_recetas_admin")
        self.verticalLayout_82 = QVBoxLayout(self.page_recetas_admin)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.formLayout_15.setHorizontalSpacing(8)
        self.formLayout_15.setVerticalSpacing(9)
        self.formLayout_15.setContentsMargins(0, 0, -1, -1)
        self.label_12 = QLabel(self.page_recetas_admin)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.ln_nombre_receta = QLineEdit(self.page_recetas_admin)
        self.ln_nombre_receta.setObjectName(u"ln_nombre_receta")

        self.formLayout_15.setWidget(0, QFormLayout.FieldRole, self.ln_nombre_receta)

        self.label_13 = QLabel(self.page_recetas_admin)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_15.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.ln_id_receta = QLineEdit(self.page_recetas_admin)
        self.ln_id_receta.setObjectName(u"ln_id_receta")

        self.formLayout_15.setWidget(1, QFormLayout.FieldRole, self.ln_id_receta)


        self.verticalLayout_82.addLayout(self.formLayout_15)

        self.frame_61 = QFrame(self.page_recetas_admin)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(0, 90))
        self.frame_61.setMaximumSize(QSize(16777215, 90))
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(90, 90))
        self.frame_62.setMaximumSize(QSize(90, 90))
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.lbl_img_receta_admin = QLabel(self.frame_62)
        self.lbl_img_receta_admin.setObjectName(u"lbl_img_receta_admin")
        self.lbl_img_receta_admin.setMinimumSize(QSize(90, 90))
        self.lbl_img_receta_admin.setMaximumSize(QSize(90, 90))
        self.lbl_img_receta_admin.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.lbl_img_receta_admin)


        self.horizontalLayout_40.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_63)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.label_53 = QLabel(self.frame_63)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(0, 20))
        self.label_53.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_74.addWidget(self.label_53)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_44)

        self.cbox_agr_rece = QComboBox(self.frame_63)
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.addItem("")
        self.cbox_agr_rece.setObjectName(u"cbox_agr_rece")

        self.horizontalLayout_62.addWidget(self.cbox_agr_rece)

        self.horizontalLayout_62.setStretch(0, 2)
        self.horizontalLayout_62.setStretch(1, 1)

        self.verticalLayout_74.addLayout(self.horizontalLayout_62)


        self.horizontalLayout_40.addWidget(self.frame_63)


        self.verticalLayout_82.addWidget(self.frame_61)

        self.frame_64 = QFrame(self.page_recetas_admin)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(0, 40))
        self.frame_64.setMaximumSize(QSize(16777215, 40))
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.btn_select_img_receta = QPushButton(self.frame_64)
        self.btn_select_img_receta.setObjectName(u"btn_select_img_receta")
        self.btn_select_img_receta.setMinimumSize(QSize(120, 30))
        self.btn_select_img_receta.setMaximumSize(QSize(120, 30))
        self.btn_select_img_receta.setStyleSheet(u"font-size: 13px")
        self.btn_select_img_receta.setIconSize(QSize(25, 25))

        self.horizontalLayout_42.addWidget(self.btn_select_img_receta)

        self.horizontalSpacer_25 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_25)


        self.verticalLayout_82.addWidget(self.frame_64)

        self.frame_65 = QFrame(self.page_recetas_admin)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_65)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.frame_65)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 20))
        self.label_72.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_76.addWidget(self.label_72)

        self.scrollArea_16 = QScrollArea(self.frame_65)
        self.scrollArea_16.setObjectName(u"scrollArea_16")
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollAreaWidgetContents_16 = QWidget()
        self.scrollAreaWidgetContents_16.setObjectName(u"scrollAreaWidgetContents_16")
        self.scrollAreaWidgetContents_16.setGeometry(QRect(0, 0, 1314, 89))
        self.verticalLayout_77 = QVBoxLayout(self.scrollAreaWidgetContents_16)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.text_ingredi_recetas = QTextEdit(self.scrollAreaWidgetContents_16)
        self.text_ingredi_recetas.setObjectName(u"text_ingredi_recetas")

        self.verticalLayout_77.addWidget(self.text_ingredi_recetas)

        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_16)

        self.verticalLayout_76.addWidget(self.scrollArea_16)


        self.verticalLayout_82.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.page_recetas_admin)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_66)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_67)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.label_88 = QLabel(self.frame_67)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(0, 20))
        self.label_88.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_78.addWidget(self.label_88)

        self.scrollArea_17 = QScrollArea(self.frame_67)
        self.scrollArea_17.setObjectName(u"scrollArea_17")
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollAreaWidgetContents_17 = QWidget()
        self.scrollAreaWidgetContents_17.setObjectName(u"scrollAreaWidgetContents_17")
        self.scrollAreaWidgetContents_17.setGeometry(QRect(0, 0, 654, 89))
        self.verticalLayout_79 = QVBoxLayout(self.scrollAreaWidgetContents_17)
        self.verticalLayout_79.setSpacing(0)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.verticalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.text_prepa_recetas = QTextEdit(self.scrollAreaWidgetContents_17)
        self.text_prepa_recetas.setObjectName(u"text_prepa_recetas")

        self.verticalLayout_79.addWidget(self.text_prepa_recetas)

        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_17)

        self.verticalLayout_78.addWidget(self.scrollArea_17)


        self.horizontalLayout_43.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_66)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_68)
        self.verticalLayout_80.setSpacing(0)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.verticalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_89 = QLabel(self.frame_68)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(0, 20))
        self.label_89.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_80.addWidget(self.label_89)

        self.scrollArea_18 = QScrollArea(self.frame_68)
        self.scrollArea_18.setObjectName(u"scrollArea_18")
        self.scrollArea_18.setWidgetResizable(True)
        self.scrollAreaWidgetContents_18 = QWidget()
        self.scrollAreaWidgetContents_18.setObjectName(u"scrollAreaWidgetContents_18")
        self.scrollAreaWidgetContents_18.setGeometry(QRect(0, 0, 654, 89))
        self.verticalLayout_81 = QVBoxLayout(self.scrollAreaWidgetContents_18)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.text_contra_recetas = QTextEdit(self.scrollAreaWidgetContents_18)
        self.text_contra_recetas.setObjectName(u"text_contra_recetas")

        self.verticalLayout_81.addWidget(self.text_contra_recetas)

        self.scrollArea_18.setWidget(self.scrollAreaWidgetContents_18)

        self.verticalLayout_80.addWidget(self.scrollArea_18)


        self.horizontalLayout_43.addWidget(self.frame_68)


        self.verticalLayout_82.addWidget(self.frame_66)

        self.frame_69 = QFrame(self.page_recetas_admin)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(0, 40))
        self.frame_69.setMaximumSize(QSize(16777215, 40))
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.btn_regresar_rece_home = QPushButton(self.frame_69)
        self.btn_regresar_rece_home.setObjectName(u"btn_regresar_rece_home")
        self.btn_regresar_rece_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_rece_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_rece_home.setIcon(icon10)
        self.btn_regresar_rece_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_44.addWidget(self.btn_regresar_rece_home)

        self.horizontalSpacer_26 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_26)

        self.btn_guardar_recetas = QPushButton(self.frame_69)
        self.btn_guardar_recetas.setObjectName(u"btn_guardar_recetas")
        self.btn_guardar_recetas.setMinimumSize(QSize(120, 30))
        self.btn_guardar_recetas.setMaximumSize(QSize(120, 30))
        self.btn_guardar_recetas.setStyleSheet(u"font-size: 13px")
        self.btn_guardar_recetas.setIconSize(QSize(25, 25))

        self.horizontalLayout_44.addWidget(self.btn_guardar_recetas)


        self.verticalLayout_82.addWidget(self.frame_69)

        self.paginas_menu_admin.addWidget(self.page_recetas_admin)
        self.page_prove_admin = QWidget()
        self.page_prove_admin.setObjectName(u"page_prove_admin")
        self.verticalLayout_84 = QVBoxLayout(self.page_prove_admin)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.frame_71 = QFrame(self.page_prove_admin)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_27 = QSpacerItem(331, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_27)

        self.frame_70 = QFrame(self.frame_71)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(400, 160))
        self.frame_70.setMaximumSize(QSize(400, 16777215))
        self.frame_70.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #000000; /* Establece el borde de 2 p\u00edxeles de ancho y color negro. Puedes ajustar el grosor y el color seg\u00fan tus preferencias. */\n"
"}")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_70)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.formLayout_16 = QFormLayout()
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.formLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.label = QLabel(self.frame_70)
        self.label.setObjectName(u"label")

        self.formLayout_16.setWidget(0, QFormLayout.LabelRole, self.label)

        self.ln_nombre_prove = QLineEdit(self.frame_70)
        self.ln_nombre_prove.setObjectName(u"ln_nombre_prove")

        self.formLayout_16.setWidget(0, QFormLayout.FieldRole, self.ln_nombre_prove)

        self.label_14 = QLabel(self.frame_70)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_16.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.ln_id_prove = QLineEdit(self.frame_70)
        self.ln_id_prove.setObjectName(u"ln_id_prove")

        self.formLayout_16.setWidget(1, QFormLayout.FieldRole, self.ln_id_prove)


        self.verticalLayout_83.addLayout(self.formLayout_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_83.addItem(self.verticalSpacer_2)

        self.scrollArea_19 = QScrollArea(self.frame_70)
        self.scrollArea_19.setObjectName(u"scrollArea_19")
        self.scrollArea_19.setMinimumSize(QSize(378, 123))
        self.scrollArea_19.setMaximumSize(QSize(378, 123))
        self.scrollArea_19.setWidgetResizable(True)
        self.scrollAreaWidgetContents_19 = QWidget()
        self.scrollAreaWidgetContents_19.setObjectName(u"scrollAreaWidgetContents_19")
        self.scrollAreaWidgetContents_19.setGeometry(QRect(0, 0, 374, 119))
        self.scrollAreaWidgetContents_19.setMinimumSize(QSize(374, 119))
        self.scrollAreaWidgetContents_19.setMaximumSize(QSize(374, 16777215))
        self.verticalLayout_85 = QVBoxLayout(self.scrollAreaWidgetContents_19)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.text_info_prove = QTextEdit(self.scrollAreaWidgetContents_19)
        self.text_info_prove.setObjectName(u"text_info_prove")

        self.verticalLayout_85.addWidget(self.text_info_prove)

        self.scrollArea_19.setWidget(self.scrollAreaWidgetContents_19)

        self.verticalLayout_83.addWidget(self.scrollArea_19)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_83.addItem(self.verticalSpacer)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_92 = QLabel(self.frame_70)
        self.label_92.setObjectName(u"label_92")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_92)

        self.label_93 = QLabel(self.frame_70)
        self.label_93.setObjectName(u"label_93")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_93)

        self.label_94 = QLabel(self.frame_70)
        self.label_94.setObjectName(u"label_94")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_94)

        self.ln_direc_prove = QLineEdit(self.frame_70)
        self.ln_direc_prove.setObjectName(u"ln_direc_prove")

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.ln_direc_prove)

        self.ln_tele_prove = QLineEdit(self.frame_70)
        self.ln_tele_prove.setObjectName(u"ln_tele_prove")

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.ln_tele_prove)

        self.ln_correo_prove = QLineEdit(self.frame_70)
        self.ln_correo_prove.setObjectName(u"ln_correo_prove")

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.ln_correo_prove)


        self.verticalLayout_83.addLayout(self.formLayout_8)


        self.horizontalLayout_45.addWidget(self.frame_70)

        self.horizontalSpacer_28 = QSpacerItem(331, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_28)


        self.verticalLayout_84.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.page_prove_admin)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 40))
        self.frame_72.setMaximumSize(QSize(16777215, 40))
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.btn_regresar_prove_home = QPushButton(self.frame_72)
        self.btn_regresar_prove_home.setObjectName(u"btn_regresar_prove_home")
        self.btn_regresar_prove_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_prove_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_prove_home.setIcon(icon10)
        self.btn_regresar_prove_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_46.addWidget(self.btn_regresar_prove_home)

        self.horizontalSpacer_29 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_29)

        self.btn_guardar_prove = QPushButton(self.frame_72)
        self.btn_guardar_prove.setObjectName(u"btn_guardar_prove")
        self.btn_guardar_prove.setMinimumSize(QSize(120, 30))
        self.btn_guardar_prove.setMaximumSize(QSize(120, 30))
        self.btn_guardar_prove.setStyleSheet(u"font-size: 13px")
        self.btn_guardar_prove.setIconSize(QSize(25, 25))

        self.horizontalLayout_46.addWidget(self.btn_guardar_prove)


        self.verticalLayout_84.addWidget(self.frame_72)

        self.paginas_menu_admin.addWidget(self.page_prove_admin)
        self.page_modificar_recu = QWidget()
        self.page_modificar_recu.setObjectName(u"page_modificar_recu")
        self.verticalLayout_101 = QVBoxLayout(self.page_modificar_recu)
        self.verticalLayout_101.setSpacing(0)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.verticalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.frame_89 = QFrame(self.page_modificar_recu)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 40))
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.btn_regresar_modrecu_home = QPushButton(self.frame_89)
        self.btn_regresar_modrecu_home.setObjectName(u"btn_regresar_modrecu_home")
        self.btn_regresar_modrecu_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_modrecu_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_modrecu_home.setIcon(icon10)
        self.btn_regresar_modrecu_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_61.addWidget(self.btn_regresar_modrecu_home)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_58)

        self.cbox_recurso = QComboBox(self.frame_89)
        self.cbox_recurso.setObjectName(u"cbox_recurso")

        self.horizontalLayout_61.addWidget(self.cbox_recurso)

        self.btn_buscar_recu_mod = QPushButton(self.frame_89)
        self.btn_buscar_recu_mod.setObjectName(u"btn_buscar_recu_mod")
        self.btn_buscar_recu_mod.setMinimumSize(QSize(30, 30))
        self.btn_buscar_recu_mod.setMaximumSize(QSize(30, 30))
        self.btn_buscar_recu_mod.setIcon(icon9)
        self.btn_buscar_recu_mod.setIconSize(QSize(20, 20))

        self.horizontalLayout_61.addWidget(self.btn_buscar_recu_mod)

        self.horizontalLayout_61.setStretch(1, 1)
        self.horizontalLayout_61.setStretch(2, 1)

        self.verticalLayout_101.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.page_modificar_recu)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(0, 90))
        self.frame_90.setMaximumSize(QSize(16777215, 90))
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.lbl_img_recurso_admin_mod = QLabel(self.frame_90)
        self.lbl_img_recurso_admin_mod.setObjectName(u"lbl_img_recurso_admin_mod")
        self.lbl_img_recurso_admin_mod.setMinimumSize(QSize(90, 90))
        self.lbl_img_recurso_admin_mod.setMaximumSize(QSize(90, 90))
        self.lbl_img_recurso_admin_mod.setPixmap(QPixmap(u"hoja.png"))
        self.lbl_img_recurso_admin_mod.setScaledContents(True)

        self.horizontalLayout_65.addWidget(self.lbl_img_recurso_admin_mod)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setHorizontalSpacing(6)
        self.formLayout_10.setVerticalSpacing(7)
        self.formLayout_10.setContentsMargins(-1, -1, 5, 5)
        self.label_98 = QLabel(self.frame_90)
        self.label_98.setObjectName(u"label_98")

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_98)

        self.label_99 = QLabel(self.frame_90)
        self.label_99.setObjectName(u"label_99")

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_99)

        self.ln_idrecurso_admin_mod = QLineEdit(self.frame_90)
        self.ln_idrecurso_admin_mod.setObjectName(u"ln_idrecurso_admin_mod")

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.ln_idrecurso_admin_mod)

        self.label_100 = QLabel(self.frame_90)
        self.label_100.setObjectName(u"label_100")

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_100)

        self.ln_nombrecomun_admin_mod = QLineEdit(self.frame_90)
        self.ln_nombrecomun_admin_mod.setObjectName(u"ln_nombrecomun_admin_mod")

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.ln_nombrecomun_admin_mod)

        self.label_101 = QLabel(self.frame_90)
        self.label_101.setObjectName(u"label_101")

        self.formLayout_10.setWidget(3, QFormLayout.LabelRole, self.label_101)

        self.ln_nombrecient_admin_mod = QLineEdit(self.frame_90)
        self.ln_nombrecient_admin_mod.setObjectName(u"ln_nombrecient_admin_mod")

        self.formLayout_10.setWidget(3, QFormLayout.FieldRole, self.ln_nombrecient_admin_mod)

        self.lbl_num_recu_mod = QLabel(self.frame_90)
        self.lbl_num_recu_mod.setObjectName(u"lbl_num_recu_mod")

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.lbl_num_recu_mod)


        self.horizontalLayout_65.addLayout(self.formLayout_10)


        self.verticalLayout_101.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.page_modificar_recu)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 40))
        self.frame_91.setMaximumSize(QSize(16777215, 40))
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.btn_select_img_recurso_mod = QPushButton(self.frame_91)
        self.btn_select_img_recurso_mod.setObjectName(u"btn_select_img_recurso_mod")
        self.btn_select_img_recurso_mod.setMinimumSize(QSize(120, 30))
        self.btn_select_img_recurso_mod.setMaximumSize(QSize(120, 30))
        self.btn_select_img_recurso_mod.setStyleSheet(u"font-size: 13px")
        self.btn_select_img_recurso_mod.setIconSize(QSize(25, 25))

        self.horizontalLayout_66.addWidget(self.btn_select_img_recurso_mod)

        self.horizontalSpacer_56 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_56)


        self.verticalLayout_101.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.page_modificar_recu)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_92)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.verticalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_102 = QLabel(self.frame_92)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(0, 20))
        self.label_102.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_95.addWidget(self.label_102)

        self.scrollArea_23 = QScrollArea(self.frame_92)
        self.scrollArea_23.setObjectName(u"scrollArea_23")
        self.scrollArea_23.setMinimumSize(QSize(0, 82))
        self.scrollArea_23.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_23.setWidgetResizable(True)
        self.scrollAreaWidgetContents_23 = QWidget()
        self.scrollAreaWidgetContents_23.setObjectName(u"scrollAreaWidgetContents_23")
        self.scrollAreaWidgetContents_23.setGeometry(QRect(0, 0, 1297, 89))
        self.verticalLayout_96 = QVBoxLayout(self.scrollAreaWidgetContents_23)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.text_descripcion_recurso_mod = QTextEdit(self.scrollAreaWidgetContents_23)
        self.text_descripcion_recurso_mod.setObjectName(u"text_descripcion_recurso_mod")

        self.verticalLayout_96.addWidget(self.text_descripcion_recurso_mod)

        self.scrollArea_23.setWidget(self.scrollAreaWidgetContents_23)

        self.verticalLayout_95.addWidget(self.scrollArea_23)


        self.verticalLayout_101.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.page_modificar_recu)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.frame_94 = QFrame(self.frame_93)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_94)
        self.verticalLayout_97.setSpacing(0)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.verticalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_103 = QLabel(self.frame_94)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setMinimumSize(QSize(0, 20))
        self.label_103.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_97.addWidget(self.label_103)

        self.scrollArea_24 = QScrollArea(self.frame_94)
        self.scrollArea_24.setObjectName(u"scrollArea_24")
        self.scrollArea_24.setMinimumSize(QSize(0, 82))
        self.scrollArea_24.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_24.setWidgetResizable(True)
        self.scrollAreaWidgetContents_24 = QWidget()
        self.scrollAreaWidgetContents_24.setObjectName(u"scrollAreaWidgetContents_24")
        self.scrollAreaWidgetContents_24.setGeometry(QRect(0, 0, 637, 89))
        self.verticalLayout_98 = QVBoxLayout(self.scrollAreaWidgetContents_24)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.text_usos_recurso_mod = QTextEdit(self.scrollAreaWidgetContents_24)
        self.text_usos_recurso_mod.setObjectName(u"text_usos_recurso_mod")

        self.verticalLayout_98.addWidget(self.text_usos_recurso_mod)

        self.scrollArea_24.setWidget(self.scrollAreaWidgetContents_24)

        self.verticalLayout_97.addWidget(self.scrollArea_24)


        self.horizontalLayout_67.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_93)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_95)
        self.verticalLayout_99.setSpacing(0)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.verticalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.label_104 = QLabel(self.frame_95)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setMinimumSize(QSize(0, 20))
        self.label_104.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_99.addWidget(self.label_104)

        self.scrollArea_25 = QScrollArea(self.frame_95)
        self.scrollArea_25.setObjectName(u"scrollArea_25")
        self.scrollArea_25.setMinimumSize(QSize(0, 82))
        self.scrollArea_25.setMaximumSize(QSize(16777215, 82))
        self.scrollArea_25.setWidgetResizable(True)
        self.scrollAreaWidgetContents_25 = QWidget()
        self.scrollAreaWidgetContents_25.setObjectName(u"scrollAreaWidgetContents_25")
        self.scrollAreaWidgetContents_25.setGeometry(QRect(0, 0, 637, 89))
        self.verticalLayout_100 = QVBoxLayout(self.scrollAreaWidgetContents_25)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.text_contradic_recurso_mod = QTextEdit(self.scrollAreaWidgetContents_25)
        self.text_contradic_recurso_mod.setObjectName(u"text_contradic_recurso_mod")

        self.verticalLayout_100.addWidget(self.text_contradic_recurso_mod)

        self.scrollArea_25.setWidget(self.scrollAreaWidgetContents_25)

        self.verticalLayout_99.addWidget(self.scrollArea_25)


        self.horizontalLayout_67.addWidget(self.frame_95)


        self.verticalLayout_101.addWidget(self.frame_93)

        self.frame_96 = QFrame(self.page_modificar_recu)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(0, 40))
        self.frame_96.setMaximumSize(QSize(16777215, 40))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.btn_eliminar_recur = QPushButton(self.frame_96)
        self.btn_eliminar_recur.setObjectName(u"btn_eliminar_recur")
        self.btn_eliminar_recur.setMinimumSize(QSize(120, 30))
        self.btn_eliminar_recur.setStyleSheet(u"font-size: 13px")

        self.horizontalLayout_68.addWidget(self.btn_eliminar_recur)

        self.horizontalSpacer_57 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_68.addItem(self.horizontalSpacer_57)

        self.btn_modificar_recurso = QPushButton(self.frame_96)
        self.btn_modificar_recurso.setObjectName(u"btn_modificar_recurso")
        self.btn_modificar_recurso.setMinimumSize(QSize(120, 30))
        self.btn_modificar_recurso.setMaximumSize(QSize(120, 30))
        self.btn_modificar_recurso.setStyleSheet(u"font-size: 13px")
        self.btn_modificar_recurso.setIconSize(QSize(25, 25))

        self.horizontalLayout_68.addWidget(self.btn_modificar_recurso)


        self.verticalLayout_101.addWidget(self.frame_96)

        self.paginas_menu_admin.addWidget(self.page_modificar_recu)
        self.page_modificar_rece = QWidget()
        self.page_modificar_rece.setObjectName(u"page_modificar_rece")
        self.verticalLayout_110 = QVBoxLayout(self.page_modificar_rece)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.frame_97 = QFrame(self.page_modificar_rece)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMaximumSize(QSize(16777215, 40))
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_97)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.btn_regresar_modrece_home = QPushButton(self.frame_97)
        self.btn_regresar_modrece_home.setObjectName(u"btn_regresar_modrece_home")
        self.btn_regresar_modrece_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_modrece_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_modrece_home.setIcon(icon10)
        self.btn_regresar_modrece_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_69.addWidget(self.btn_regresar_modrece_home)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_69.addItem(self.horizontalSpacer_59)

        self.cbox_mod_rec = QComboBox(self.frame_97)
        self.cbox_mod_rec.setObjectName(u"cbox_mod_rec")

        self.horizontalLayout_69.addWidget(self.cbox_mod_rec)

        self.btn_buscar_rece_mod = QPushButton(self.frame_97)
        self.btn_buscar_rece_mod.setObjectName(u"btn_buscar_rece_mod")
        self.btn_buscar_rece_mod.setMinimumSize(QSize(30, 30))
        self.btn_buscar_rece_mod.setMaximumSize(QSize(30, 30))
        self.btn_buscar_rece_mod.setIcon(icon9)
        self.btn_buscar_rece_mod.setIconSize(QSize(20, 20))

        self.horizontalLayout_69.addWidget(self.btn_buscar_rece_mod)

        self.horizontalLayout_69.setStretch(1, 2)
        self.horizontalLayout_69.setStretch(2, 1)

        self.verticalLayout_110.addWidget(self.frame_97)

        self.formLayout_18 = QFormLayout()
        self.formLayout_18.setObjectName(u"formLayout_18")
        self.formLayout_18.setHorizontalSpacing(8)
        self.formLayout_18.setVerticalSpacing(9)
        self.formLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.label_18 = QLabel(self.page_modificar_rece)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_18.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.label_28 = QLabel(self.page_modificar_rece)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_18.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.ln_nombre_receta_mod = QLineEdit(self.page_modificar_rece)
        self.ln_nombre_receta_mod.setObjectName(u"ln_nombre_receta_mod")

        self.formLayout_18.setWidget(0, QFormLayout.FieldRole, self.ln_nombre_receta_mod)

        self.ln_id_receta_mod = QLineEdit(self.page_modificar_rece)
        self.ln_id_receta_mod.setObjectName(u"ln_id_receta_mod")

        self.formLayout_18.setWidget(1, QFormLayout.FieldRole, self.ln_id_receta_mod)


        self.verticalLayout_110.addLayout(self.formLayout_18)

        self.frame_99 = QFrame(self.page_modificar_rece)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 90))
        self.frame_99.setMaximumSize(QSize(16777215, 90))
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_99)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMinimumSize(QSize(90, 90))
        self.frame_100.setMaximumSize(QSize(90, 90))
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.lbl_img_receta_admin_mod = QLabel(self.frame_100)
        self.lbl_img_receta_admin_mod.setObjectName(u"lbl_img_receta_admin_mod")
        self.lbl_img_receta_admin_mod.setMinimumSize(QSize(90, 90))
        self.lbl_img_receta_admin_mod.setMaximumSize(QSize(90, 90))
        self.lbl_img_receta_admin_mod.setScaledContents(True)

        self.horizontalLayout_71.addWidget(self.lbl_img_receta_admin_mod)


        self.horizontalLayout_70.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_99)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_101)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.label_106 = QLabel(self.frame_101)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setMinimumSize(QSize(0, 20))
        self.label_106.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_104.addWidget(self.label_106)

        self.scrollArea_27 = QScrollArea(self.frame_101)
        self.scrollArea_27.setObjectName(u"scrollArea_27")
        self.scrollArea_27.setWidgetResizable(True)
        self.scrollAreaWidgetContents_27 = QWidget()
        self.scrollAreaWidgetContents_27.setObjectName(u"scrollAreaWidgetContents_27")
        self.scrollAreaWidgetContents_27.setGeometry(QRect(0, 0, 1187, 71))
        self.verticalLayout_105 = QVBoxLayout(self.scrollAreaWidgetContents_27)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.text_afec_receta_mod = QTextEdit(self.scrollAreaWidgetContents_27)
        self.text_afec_receta_mod.setObjectName(u"text_afec_receta_mod")

        self.verticalLayout_105.addWidget(self.text_afec_receta_mod)

        self.scrollArea_27.setWidget(self.scrollAreaWidgetContents_27)

        self.verticalLayout_104.addWidget(self.scrollArea_27)


        self.horizontalLayout_70.addWidget(self.frame_101)


        self.verticalLayout_110.addWidget(self.frame_99)

        self.frame_102 = QFrame(self.page_modificar_rece)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setMinimumSize(QSize(0, 40))
        self.frame_102.setMaximumSize(QSize(16777215, 40))
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.btn_select_img_receta_mod = QPushButton(self.frame_102)
        self.btn_select_img_receta_mod.setObjectName(u"btn_select_img_receta_mod")
        self.btn_select_img_receta_mod.setMinimumSize(QSize(120, 30))
        self.btn_select_img_receta_mod.setMaximumSize(QSize(120, 30))
        self.btn_select_img_receta_mod.setStyleSheet(u"font-size: 13px")
        self.btn_select_img_receta_mod.setIconSize(QSize(25, 25))

        self.horizontalLayout_72.addWidget(self.btn_select_img_receta_mod)

        self.horizontalSpacer_60 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_60)


        self.verticalLayout_110.addWidget(self.frame_102)

        self.frame_98 = QFrame(self.page_modificar_rece)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_98)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_105 = QLabel(self.frame_98)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setMinimumSize(QSize(0, 20))
        self.label_105.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_102.addWidget(self.label_105)

        self.scrollArea_26 = QScrollArea(self.frame_98)
        self.scrollArea_26.setObjectName(u"scrollArea_26")
        self.scrollArea_26.setWidgetResizable(True)
        self.scrollAreaWidgetContents_26 = QWidget()
        self.scrollAreaWidgetContents_26.setObjectName(u"scrollAreaWidgetContents_26")
        self.scrollAreaWidgetContents_26.setGeometry(QRect(0, 0, 1297, 71))
        self.verticalLayout_103 = QVBoxLayout(self.scrollAreaWidgetContents_26)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.text_ingredi_recetas_mod = QTextEdit(self.scrollAreaWidgetContents_26)
        self.text_ingredi_recetas_mod.setObjectName(u"text_ingredi_recetas_mod")

        self.verticalLayout_103.addWidget(self.text_ingredi_recetas_mod)

        self.scrollArea_26.setWidget(self.scrollAreaWidgetContents_26)

        self.verticalLayout_102.addWidget(self.scrollArea_26)


        self.verticalLayout_110.addWidget(self.frame_98)

        self.frame_104 = QFrame(self.page_modificar_rece)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_105)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.frame_105)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setMinimumSize(QSize(0, 20))
        self.label_107.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_106.addWidget(self.label_107)

        self.scrollArea_28 = QScrollArea(self.frame_105)
        self.scrollArea_28.setObjectName(u"scrollArea_28")
        self.scrollArea_28.setWidgetResizable(True)
        self.scrollAreaWidgetContents_28 = QWidget()
        self.scrollAreaWidgetContents_28.setObjectName(u"scrollAreaWidgetContents_28")
        self.scrollAreaWidgetContents_28.setGeometry(QRect(0, 0, 637, 71))
        self.verticalLayout_107 = QVBoxLayout(self.scrollAreaWidgetContents_28)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.text_prepa_recetas_mod = QTextEdit(self.scrollAreaWidgetContents_28)
        self.text_prepa_recetas_mod.setObjectName(u"text_prepa_recetas_mod")

        self.verticalLayout_107.addWidget(self.text_prepa_recetas_mod)

        self.scrollArea_28.setWidget(self.scrollAreaWidgetContents_28)

        self.verticalLayout_106.addWidget(self.scrollArea_28)


        self.horizontalLayout_74.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_106)
        self.verticalLayout_108.setSpacing(0)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.label_108 = QLabel(self.frame_106)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setMinimumSize(QSize(0, 20))
        self.label_108.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_108.addWidget(self.label_108)

        self.scrollArea_29 = QScrollArea(self.frame_106)
        self.scrollArea_29.setObjectName(u"scrollArea_29")
        self.scrollArea_29.setWidgetResizable(True)
        self.scrollAreaWidgetContents_29 = QWidget()
        self.scrollAreaWidgetContents_29.setObjectName(u"scrollAreaWidgetContents_29")
        self.scrollAreaWidgetContents_29.setGeometry(QRect(0, 0, 637, 71))
        self.verticalLayout_109 = QVBoxLayout(self.scrollAreaWidgetContents_29)
        self.verticalLayout_109.setSpacing(0)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.verticalLayout_109.setContentsMargins(0, 0, 0, 0)
        self.text_contra_recetas_mod = QTextEdit(self.scrollAreaWidgetContents_29)
        self.text_contra_recetas_mod.setObjectName(u"text_contra_recetas_mod")

        self.verticalLayout_109.addWidget(self.text_contra_recetas_mod)

        self.scrollArea_29.setWidget(self.scrollAreaWidgetContents_29)

        self.verticalLayout_108.addWidget(self.scrollArea_29)


        self.horizontalLayout_74.addWidget(self.frame_106)


        self.verticalLayout_110.addWidget(self.frame_104)

        self.frame_103 = QFrame(self.page_modificar_rece)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMinimumSize(QSize(0, 40))
        self.frame_103.setMaximumSize(QSize(16777215, 40))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_103)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.btn_eliminar_rece = QPushButton(self.frame_103)
        self.btn_eliminar_rece.setObjectName(u"btn_eliminar_rece")
        self.btn_eliminar_rece.setMinimumSize(QSize(120, 30))
        self.btn_eliminar_rece.setStyleSheet(u"font-size: 13px")

        self.horizontalLayout_53.addWidget(self.btn_eliminar_rece)

        self.horizontalSpacer_61 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_61)

        self.btn_modificar_recetas = QPushButton(self.frame_103)
        self.btn_modificar_recetas.setObjectName(u"btn_modificar_recetas")
        self.btn_modificar_recetas.setMinimumSize(QSize(120, 30))
        self.btn_modificar_recetas.setMaximumSize(QSize(120, 30))
        self.btn_modificar_recetas.setStyleSheet(u"font-size: 13px")
        self.btn_modificar_recetas.setIconSize(QSize(25, 25))

        self.horizontalLayout_53.addWidget(self.btn_modificar_recetas)


        self.verticalLayout_110.addWidget(self.frame_103)

        self.paginas_menu_admin.addWidget(self.page_modificar_rece)
        self.page_modificar_prove = QWidget()
        self.page_modificar_prove.setObjectName(u"page_modificar_prove")
        self.verticalLayout_113 = QVBoxLayout(self.page_modificar_prove)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.frame_107 = QFrame(self.page_modificar_prove)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMaximumSize(QSize(16777215, 40))
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.btn_regresar_modprove_home = QPushButton(self.frame_107)
        self.btn_regresar_modprove_home.setObjectName(u"btn_regresar_modprove_home")
        self.btn_regresar_modprove_home.setMinimumSize(QSize(30, 30))
        self.btn_regresar_modprove_home.setMaximumSize(QSize(30, 30))
        self.btn_regresar_modprove_home.setIcon(icon10)
        self.btn_regresar_modprove_home.setIconSize(QSize(20, 20))

        self.horizontalLayout_75.addWidget(self.btn_regresar_modprove_home)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_62)

        self.comboBox = QComboBox(self.frame_107)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_75.addWidget(self.comboBox)

        self.btn_buscar_prove_mod = QPushButton(self.frame_107)
        self.btn_buscar_prove_mod.setObjectName(u"btn_buscar_prove_mod")
        self.btn_buscar_prove_mod.setMinimumSize(QSize(30, 30))
        self.btn_buscar_prove_mod.setMaximumSize(QSize(30, 30))
        self.btn_buscar_prove_mod.setIcon(icon9)
        self.btn_buscar_prove_mod.setIconSize(QSize(20, 20))

        self.horizontalLayout_75.addWidget(self.btn_buscar_prove_mod)

        self.horizontalLayout_75.setStretch(1, 2)
        self.horizontalLayout_75.setStretch(2, 1)

        self.verticalLayout_113.addWidget(self.frame_107)

        self.frame_109 = QFrame(self.page_modificar_prove)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalSpacer_64 = QSpacerItem(331, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_64)

        self.frame_110 = QFrame(self.frame_109)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(400, 160))
        self.frame_110.setMaximumSize(QSize(400, 16777215))
        self.frame_110.setStyleSheet(u"QFrame {\n"
"    border: 2px solid #000000; /* Establece el borde de 2 p\u00edxeles de ancho y color negro. Puedes ajustar el grosor y el color seg\u00fan tus preferencias. */\n"
"}")
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_110)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.formLayout_19 = QFormLayout()
        self.formLayout_19.setObjectName(u"formLayout_19")
        self.formLayout_19.setContentsMargins(-1, 7, 0, -1)
        self.label_11 = QLabel(self.frame_110)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_19.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.ln_nombre_prove_mod = QLineEdit(self.frame_110)
        self.ln_nombre_prove_mod.setObjectName(u"ln_nombre_prove_mod")

        self.formLayout_19.setWidget(0, QFormLayout.FieldRole, self.ln_nombre_prove_mod)

        self.label_40 = QLabel(self.frame_110)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_19.setWidget(1, QFormLayout.LabelRole, self.label_40)

        self.ln_id_prove_mod = QLineEdit(self.frame_110)
        self.ln_id_prove_mod.setObjectName(u"ln_id_prove_mod")

        self.formLayout_19.setWidget(1, QFormLayout.FieldRole, self.ln_id_prove_mod)


        self.verticalLayout_111.addLayout(self.formLayout_19)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_111.addItem(self.verticalSpacer_3)

        self.scrollArea_30 = QScrollArea(self.frame_110)
        self.scrollArea_30.setObjectName(u"scrollArea_30")
        self.scrollArea_30.setMinimumSize(QSize(378, 123))
        self.scrollArea_30.setMaximumSize(QSize(378, 123))
        self.scrollArea_30.setWidgetResizable(True)
        self.scrollAreaWidgetContents_30 = QWidget()
        self.scrollAreaWidgetContents_30.setObjectName(u"scrollAreaWidgetContents_30")
        self.scrollAreaWidgetContents_30.setGeometry(QRect(0, 0, 374, 119))
        self.scrollAreaWidgetContents_30.setMinimumSize(QSize(374, 119))
        self.scrollAreaWidgetContents_30.setMaximumSize(QSize(374, 16777215))
        self.verticalLayout_112 = QVBoxLayout(self.scrollAreaWidgetContents_30)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.text_info_prove_mod = QTextEdit(self.scrollAreaWidgetContents_30)
        self.text_info_prove_mod.setObjectName(u"text_info_prove_mod")

        self.verticalLayout_112.addWidget(self.text_info_prove_mod)

        self.scrollArea_30.setWidget(self.scrollAreaWidgetContents_30)

        self.verticalLayout_111.addWidget(self.scrollArea_30)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_111.addItem(self.verticalSpacer_4)

        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.label_109 = QLabel(self.frame_110)
        self.label_109.setObjectName(u"label_109")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_109)

        self.label_110 = QLabel(self.frame_110)
        self.label_110.setObjectName(u"label_110")

        self.formLayout_11.setWidget(1, QFormLayout.LabelRole, self.label_110)

        self.label_111 = QLabel(self.frame_110)
        self.label_111.setObjectName(u"label_111")

        self.formLayout_11.setWidget(2, QFormLayout.LabelRole, self.label_111)

        self.ln_direc_prove_mod = QLineEdit(self.frame_110)
        self.ln_direc_prove_mod.setObjectName(u"ln_direc_prove_mod")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.ln_direc_prove_mod)

        self.ln_tele_prove_mod = QLineEdit(self.frame_110)
        self.ln_tele_prove_mod.setObjectName(u"ln_tele_prove_mod")

        self.formLayout_11.setWidget(1, QFormLayout.FieldRole, self.ln_tele_prove_mod)

        self.ln_correo_prove_mod = QLineEdit(self.frame_110)
        self.ln_correo_prove_mod.setObjectName(u"ln_correo_prove_mod")

        self.formLayout_11.setWidget(2, QFormLayout.FieldRole, self.ln_correo_prove_mod)


        self.verticalLayout_111.addLayout(self.formLayout_11)


        self.horizontalLayout_77.addWidget(self.frame_110)

        self.horizontalSpacer_65 = QSpacerItem(331, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_65)


        self.verticalLayout_113.addWidget(self.frame_109)

        self.frame_108 = QFrame(self.page_modificar_prove)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(0, 40))
        self.frame_108.setMaximumSize(QSize(16777215, 40))
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_108)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.btn_eliminar_prove = QPushButton(self.frame_108)
        self.btn_eliminar_prove.setObjectName(u"btn_eliminar_prove")
        self.btn_eliminar_prove.setMinimumSize(QSize(120, 30))
        self.btn_eliminar_prove.setStyleSheet(u"font-size: 13px")

        self.horizontalLayout_56.addWidget(self.btn_eliminar_prove)

        self.horizontalSpacer_63 = QSpacerItem(513, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_63)

        self.btn_modificar_provedores = QPushButton(self.frame_108)
        self.btn_modificar_provedores.setObjectName(u"btn_modificar_provedores")
        self.btn_modificar_provedores.setMinimumSize(QSize(120, 30))
        self.btn_modificar_provedores.setMaximumSize(QSize(120, 30))
        self.btn_modificar_provedores.setStyleSheet(u"font-size: 13px")
        self.btn_modificar_provedores.setIconSize(QSize(25, 25))

        self.horizontalLayout_56.addWidget(self.btn_modificar_provedores)


        self.verticalLayout_113.addWidget(self.frame_108)

        self.paginas_menu_admin.addWidget(self.page_modificar_prove)

        self.horizontalLayout_35.addWidget(self.paginas_menu_admin)


        self.verticalLayout_65.addWidget(self.frame_53)

        self.paginas_usuarios.addWidget(self.page_admin)

        self.horizontalLayout_2.addWidget(self.paginas_usuarios)


        self.verticalLayout_28.addWidget(self.widget_2)

        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 90))
        self.widget_8.setMaximumSize(QSize(16777215, 90))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.lbl_heremedcol = QLabel(self.widget_8)
        self.lbl_heremedcol.setObjectName(u"lbl_heremedcol")
        self.lbl_heremedcol.setMinimumSize(QSize(400, 50))
        self.lbl_heremedcol.setMaximumSize(QSize(400, 50))
        self.lbl_heremedcol.setPixmap(QPixmap(u"image/titule.png"))
        self.lbl_heremedcol.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.lbl_heremedcol)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_28.addWidget(self.widget_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.paginas_usuarios.setCurrentIndex(0)
        self.paginas_menu.setCurrentIndex(0)
        self.paginas_menu_admin.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HerMedCol", None))
        self.lbl_hermedcol.setText("")
        self.lbl_icono.setText("")
        self.btn_Menu.setText("")
        self.btn_cerrar_sesion.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"    Inicio", None))
        self.btn_recursos.setText(QCoreApplication.translate("MainWindow", u"   Recursos", None))
        self.btn_recetas.setText(QCoreApplication.translate("MainWindow", u"    Recetas", None))
        self.btn_provedores.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.btn_nosotros.setText(QCoreApplication.translate("MainWindow", u"   Nosotros", None))
        self.btn_actualizacion.setText(QCoreApplication.translate("MainWindow", u" Actualizaci\u00f3n", None))
        self.btn_buscar.setText("")
        self.lbl_img4.setText(QCoreApplication.translate("MainWindow", u"Img4", None))
        self.lbl_info4.setText(QCoreApplication.translate("MainWindow", u"Info4", None))
        self.lbl_img5.setText(QCoreApplication.translate("MainWindow", u"Img5", None))
        self.lbl_info5.setText(QCoreApplication.translate("MainWindow", u"Info5", None))
        self.lbl_img6.setText(QCoreApplication.translate("MainWindow", u"Img6", None))
        self.lbl_info6.setText(QCoreApplication.translate("MainWindow", u"Info6", None))
        self.btn_historial.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.lbl_img1.setText("")
        self.lbl_info1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Info1</p></body></html>", None))
        self.lbl_img2.setText(QCoreApplication.translate("MainWindow", u"Img2", None))
        self.lbl_info2.setText(QCoreApplication.translate("MainWindow", u"Info2", None))
        self.lbl_img3.setText(QCoreApplication.translate("MainWindow", u"Img3", None))
        self.lbl_info3.setText(QCoreApplication.translate("MainWindow", u"Info3", None))
        self.btn_regresar_recurso.setText("")
        self.lbl_img_recurso.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Recurso", None))
        self.lbl_recurso.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Id Producto", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Nombre Com\u00fan", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Nombre Cient\u00edfico", None))
        self.lbl_id_recurso.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_nombre_recur.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.lbl_cienti_recur.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Descripcion Producto</span></p></body></html>", None))
        self.lbl_info_produc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Posibles Usos</span></p></body></html>", None))
        self.lbl_usos_produc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contradicciones</span></p></body></html>", None))
        self.lbl_contra_produc.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.cbox_filtro_receta.setItemText(0, "")
        self.cbox_filtro_receta.setItemText(1, QCoreApplication.translate("MainWindow", u"Dolor de estomago", None))
        self.cbox_filtro_receta.setItemText(2, QCoreApplication.translate("MainWindow", u"Dolor de cabeza", None))
        self.cbox_filtro_receta.setItemText(3, QCoreApplication.translate("MainWindow", u"Dolor de garganta", None))
        self.cbox_filtro_receta.setItemText(4, QCoreApplication.translate("MainWindow", u"Dolor de piernas", None))
        self.cbox_filtro_receta.setItemText(5, QCoreApplication.translate("MainWindow", u"Fiebre", None))
        self.cbox_filtro_receta.setItemText(6, QCoreApplication.translate("MainWindow", u"Resfriado", None))
        self.cbox_filtro_receta.setItemText(7, QCoreApplication.translate("MainWindow", u"Tos seca", None))
        self.cbox_filtro_receta.setItemText(8, QCoreApplication.translate("MainWindow", u"Gastritis", None))
        self.cbox_filtro_receta.setItemText(9, QCoreApplication.translate("MainWindow", u"Estres", None))
        self.cbox_filtro_receta.setItemText(10, QCoreApplication.translate("MainWindow", u"Insolaci\u00f3n", None))
        self.cbox_filtro_receta.setItemText(11, QCoreApplication.translate("MainWindow", u"Quemadura", None))
        self.cbox_filtro_receta.setItemText(12, QCoreApplication.translate("MainWindow", u"Dolor de cuerpo", None))

        self.cbox_filtro_receta.setCurrentText("")
        self.btn_regresar_receta.setText("")
        self.lbl_receta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_img_receta.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Afecciones tratadas con esta receta</span></p></body></html>", None))
        self.lbl_afecci_recetas.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Ingredientes</span></p></body></html>", None))
        self.lbl_ingredientes_rece.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Modo de preparaci\u00f3n</span></p></body></html>", None))
        self.lbl_prepara_rece.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contraindicaciones</span></p></body></html>", None))
        self.lbl_contra_rece.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Calificaci\u00f3n</span></p></body></html>", None))
        self.pushButton_19.setText("")
        self.pushButton_20.setText("")
        self.pushButton_21.setText("")
        self.pushButton_22.setText("")
        self.pushButton_23.setText("")
        self.lbl_prom_rec.setText(QCoreApplication.translate("MainWindow", u"Sin calificar", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Proveedores Disponibles</span></p></body></html>", None))
        self.cbox_filtro_prove.setItemText(0, "")
        self.cbox_filtro_prove.setItemText(1, QCoreApplication.translate("MainWindow", u"Tumaco", None))
        self.cbox_filtro_prove.setItemText(2, QCoreApplication.translate("MainWindow", u"Pasto", None))
        self.cbox_filtro_prove.setItemText(3, QCoreApplication.translate("MainWindow", u"Bogot\u00e1", None))
        self.cbox_filtro_prove.setItemText(4, QCoreApplication.translate("MainWindow", u"Cali", None))
        self.cbox_filtro_prove.setItemText(5, QCoreApplication.translate("MainWindow", u"Medell\u00edn", None))
        self.cbox_filtro_prove.setItemText(6, QCoreApplication.translate("MainWindow", u"Barranquilla", None))
        self.cbox_filtro_prove.setItemText(7, QCoreApplication.translate("MainWindow", u"Bucaramanga", None))
        self.cbox_filtro_prove.setItemText(8, QCoreApplication.translate("MainWindow", u"Tolima", None))
        self.cbox_filtro_prove.setItemText(9, QCoreApplication.translate("MainWindow", u"Sibundoy", None))
        self.cbox_filtro_prove.setItemText(10, QCoreApplication.translate("MainWindow", u"Sincelejo", None))
        self.cbox_filtro_prove.setItemText(11, QCoreApplication.translate("MainWindow", u"Boyac\u00e1", None))
        self.cbox_filtro_prove.setItemText(12, QCoreApplication.translate("MainWindow", u"Pop\u00e1yan", None))

        self.cbox_filtro_prove.setCurrentText("")
        self.label_76.setText("")
        self.label_77.setText("")
        self.label_79.setText("")
        self.label_86.setText("")
        self.label_87.setText("")
        self.label_80.setText("")
        self.label_81.setText("")
        self.label_82.setText("")
        self.label_83.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">El material almacenado tiene la intenci\u00f3n de brindar</span></p><p align=\"center\"><span style=\" font-size:14pt;\">informaci\u00f3n relevante sobre los beneficios</span></p><p align=\"center\"><span style=\" font-size:14pt;\">medicinales de plantas, hierbas, frutos en </span></p><p align=\"center\"><span style=\" font-size:14pt;\">nuestra vida diaria.</span></p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">CONTACTANOS</span></p></body></html>", None))
        self.pushButton_26.setText("")
        self.pushButton_27.setText("")
        self.btn_regresar_buscar_home.setText("")
        self.lbl_id_mod.setText(QCoreApplication.translate("MainWindow", u"Id_User", None))
        self.lbl_user_2.setText("")
        self.btn_telefono_mod.setText(QCoreApplication.translate("MainWindow", u"Modificar Tel\u00e9fono", None))
        self.btn_nombre_mod.setText(QCoreApplication.translate("MainWindow", u"Modificar Nombre", None))
        self.btn_correo_mod.setText(QCoreApplication.translate("MainWindow", u"Modificar Correo", None))
        self.btn_password_mod.setText(QCoreApplication.translate("MainWindow", u"Modificar Password", None))
        self.lbl_img_buscar.setText("")
        ___qtablewidgetitem = self.tabl_historial.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Concepto", None));
        ___qtablewidgetitem1 = self.tabl_historial.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.tabl_historial.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        self.lbl_user_regis.setText("")
        self.btn_regresar_regis_inicio.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Confirmar Password", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.btn_registrar.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.lbl_user_recu.setText("")
        self.btn_regresar_recu_inicio.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.btn_verificar_contra.setText(QCoreApplication.translate("MainWindow", u"Verificar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.btn_veri_cod.setText(QCoreApplication.translate("MainWindow", u"Verificar Codigo", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Nuevo Password", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Confirmar Password", None))
        self.btn_confirmar_pass.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.lbl_user.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_recuperar.setText(QCoreApplication.translate("MainWindow", u"Recuperar", None))
        self.btn_iniciar_sesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesi\u00f3n", None))
        self.btn_registrarse.setText(QCoreApplication.translate("MainWindow", u"Registrarse", None))
        self.btn_Menu_admin.setText("")
        self.btn_cerrar_sesion_admin.setText("")
        self.btn_inicio_admin.setText(QCoreApplication.translate("MainWindow", u"   Inicio", None))
        self.btn_recursos_admin.setText(QCoreApplication.translate("MainWindow", u"   Recursos", None))
        self.btn_recetas_admin.setText(QCoreApplication.translate("MainWindow", u"    Recetas", None))
        self.btn_provedores_admin.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.lbl_recu_admin.setText("")
        self.btn_ingresar_recu.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.btn_modificar_recu.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.lbl_rece_admin.setText("")
        self.btn_ingresar_rece.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.btn_modificar_rece.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.lbl_prove_Admin.setText("")
        self.btn_ingresar_prove.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.btn_modificar_prove.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.lbl_img_recurso_admin.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Recurso", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Id Producto", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Nombre Com\u00fan", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Nombre Cient\u00edfico", None))
        self.lbl_numero_recurso.setText("")
        self.btn_select_img_recurso.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Descripcion Producto</span></p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Posibles Usos</span></p></body></html>", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contradicciones</span></p></body></html>", None))
        self.btn_regresar_recu_home.setText("")
        self.btn_guardar_recurso.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Id Receta", None))
        self.lbl_img_receta_admin.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Afecciones tratadas con esta receta</span></p></body></html>", None))
        self.cbox_agr_rece.setItemText(0, "")
        self.cbox_agr_rece.setItemText(1, QCoreApplication.translate("MainWindow", u"Dolor de estomago", None))
        self.cbox_agr_rece.setItemText(2, QCoreApplication.translate("MainWindow", u"Dolor de cabeza", None))
        self.cbox_agr_rece.setItemText(3, QCoreApplication.translate("MainWindow", u"Dolor de garganta", None))
        self.cbox_agr_rece.setItemText(4, QCoreApplication.translate("MainWindow", u"Dolor de piernas", None))
        self.cbox_agr_rece.setItemText(5, QCoreApplication.translate("MainWindow", u"Fiebre", None))
        self.cbox_agr_rece.setItemText(6, QCoreApplication.translate("MainWindow", u"Resfriado", None))
        self.cbox_agr_rece.setItemText(7, QCoreApplication.translate("MainWindow", u"Tos seca", None))
        self.cbox_agr_rece.setItemText(8, QCoreApplication.translate("MainWindow", u"Gatritis", None))
        self.cbox_agr_rece.setItemText(9, QCoreApplication.translate("MainWindow", u"Estres", None))
        self.cbox_agr_rece.setItemText(10, QCoreApplication.translate("MainWindow", u"Insolaci\u00f3n", None))
        self.cbox_agr_rece.setItemText(11, QCoreApplication.translate("MainWindow", u"Quemadura", None))
        self.cbox_agr_rece.setItemText(12, QCoreApplication.translate("MainWindow", u"Dolor de cuerpo", None))

        self.btn_select_img_receta.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Ingredientes</span></p></body></html>", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Modo de preparaci\u00f3n</span></p></body></html>", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contraindicaciones</span></p></body></html>", None))
        self.btn_regresar_rece_home.setText("")
        self.btn_guardar_recetas.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Id Proveedor", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.btn_regresar_prove_home.setText("")
        self.btn_guardar_prove.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btn_regresar_modrecu_home.setText("")
        self.btn_buscar_recu_mod.setText("")
        self.lbl_img_recurso_admin_mod.setText("")
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Recurso", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Id Producto", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Nombre Com\u00fan", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Nombre Cient\u00edfico", None))
        self.lbl_num_recu_mod.setText("")
        self.btn_select_img_recurso_mod.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Descripcion Producto</span></p></body></html>", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Posibles Usos</span></p></body></html>", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contradicciones</span></p></body></html>", None))
        self.btn_eliminar_recur.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btn_modificar_recurso.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btn_regresar_modrece_home.setText("")
        self.btn_buscar_rece_mod.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Id Receta", None))
        self.lbl_img_receta_admin_mod.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Afecciones tratadas con esta receta</span></p></body></html>", None))
        self.btn_select_img_receta_mod.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Ingredientes</span></p></body></html>", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Modo de preparaci\u00f3n</span></p></body></html>", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contraindicaciones</span></p></body></html>", None))
        self.btn_eliminar_rece.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btn_modificar_recetas.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btn_regresar_modprove_home.setText("")
        self.btn_buscar_prove_mod.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Id Proveedor", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.btn_eliminar_prove.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btn_modificar_provedores.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.lbl_heremedcol.setText("")
    # retranslateUi

