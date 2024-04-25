# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogonombre.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)



class Ui_DialogDatos(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(246, 240)
        Dialog.setStyleSheet(u"QPushButton {\n"
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
"color: rgb(0, 0, 0);\n"
"}\n"
"QPlainTextEdit:disabled {\n"
"    background-color: #FFFFFF; /* Establece el color de fondo a blanco */\n"
"    color: #FFFFFF; /* Establece el color del texto a negro */\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.line_actualizacion = QLineEdit(Dialog)
        self.line_actualizacion.setObjectName(u"line_actualizacion")
        self.line_actualizacion.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 5px; /* El valor 10px puede ser ajustado seg\u00fan el radio deseado */\n"
"background-color: #556B2F; /* Verde m\u00e1s oscuro */\n"
"color: white;\n"
"	font: 700 10pt \"Times New Roman\";\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout.addWidget(self.line_actualizacion)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Actualizar Datos", None))
        #self.line_actualizacion.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese texto", None))
    # retranslateUi

class DialogoDatos(QDialog, Ui_DialogDatos):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
