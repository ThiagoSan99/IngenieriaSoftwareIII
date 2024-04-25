# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogocontra.ui'
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
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)



class Ui_DialogContra(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
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
"color: white;\n"
"	font: 700 10pt \"Times New Roman\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPlainTextEdit:disabled {\n"
"    background-color: #FFFFFF; /* Establece el color de fondo a blanco */\n"
"    color: #FFFFFF; /* Establece el color del texto a negro */\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line_contra_act = QLineEdit(Dialog)
        self.line_contra_act.setObjectName(u"line_contra_act")

        self.verticalLayout_2.addWidget(self.line_contra_act)

        self.line_contra_nueva = QLineEdit(Dialog)
        self.line_contra_nueva.setObjectName(u"line_contra_nueva")

        self.verticalLayout_2.addWidget(self.line_contra_nueva)

        self.line_contra_veri = QLineEdit(Dialog)
        self.line_contra_veri.setObjectName(u"line_contra_veri")

        self.verticalLayout_2.addWidget(self.line_contra_veri)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Actualizar contraseña", None))
        self.line_contra_act.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese Contrase\u00f1a actual", None))
        self.line_contra_nueva.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese nueva contrase\u00f1a", None))
        self.line_contra_veri.setPlaceholderText(QCoreApplication.translate("Dialog", u"Verifique contrase\u00f1a", None))
    # retranslateUi

class DialogoContraseña(QDialog, Ui_DialogContra):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

