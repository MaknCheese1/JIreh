# Form implementation generated from reading ui file 'vw_FrmSesion.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vw_sesion(object):
    def setupUi(self, vw_sesion):
        vw_sesion.setObjectName("vw_sesion")
        vw_sesion.resize(791, 702)
        self.centralwidget = QtWidgets.QWidget(parent=vw_sesion)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.457, y1:0.579455, x2:0.01, y2:0.034, stop:0.233831 rgba(192, 191, 187, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radius:20px;\n"
"border:1px solid rgb(222, 221, 218);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 301, 281))
        self.label_2.setStyleSheet("background-color: rgb(0,0, 0, 0%);\n"
"border:none")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../Descargas/hamburguesa(1).png"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(300, 320, 141, 41))
        self.label.setStyleSheet("background-color: rgb(0,0, 0, 0%);\n"
"border:none;\n"
"font:75 12pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(310, 430, 141, 51))
        self.label_3.setStyleSheet("background-color: rgb(0,0, 0, 0%);\n"
"border:none;\n"
"font:75 12pt \"Arial\";")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.txt_usuarioSesion = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_usuarioSesion.setGeometry(QtCore.QRect(230, 370, 331, 41))
        self.txt_usuarioSesion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:none;\n"
"")
        self.txt_usuarioSesion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_usuarioSesion.setObjectName("txt_usuarioSesion")
        self.txt_passworSesion = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_passworSesion.setGeometry(QtCore.QRect(230, 480, 331, 41))
        self.txt_passworSesion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:none;\n"
"")
        self.txt_passworSesion.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.txt_passworSesion.setObjectName("txt_passworSesion")
        self.btn_iniciarSesion = QtWidgets.QPushButton(parent=self.frame)
        self.btn_iniciarSesion.setGeometry(QtCore.QRect(290, 560, 191, 71))
        self.btn_iniciarSesion.setStyleSheet("QFrame{\n"
"background-color:#aa5ff;\n"
"}\n"
"QPushButton{\n"
"background-color:#aa5ff;\n"
"border-top-left:20px;\n"
"border-bottom-left-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:green;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"}")
        self.btn_iniciarSesion.setObjectName("btn_iniciarSesion")
        self.horizontalLayout.addWidget(self.frame)
        vw_sesion.setCentralWidget(self.centralwidget)

        self.retranslateUi(vw_sesion)
        QtCore.QMetaObject.connectSlotsByName(vw_sesion)

    def retranslateUi(self, vw_sesion):
        _translate = QtCore.QCoreApplication.translate
        vw_sesion.setWindowTitle(_translate("vw_sesion", "Iniciar Sesion"))
        self.label.setText(_translate("vw_sesion", "Usuario"))
        self.label_3.setText(_translate("vw_sesion", "Contraseña"))
        self.txt_usuarioSesion.setPlaceholderText(_translate("vw_sesion", "Ingrese su nombre de usuario"))
        self.txt_passworSesion.setPlaceholderText(_translate("vw_sesion", "Ingrese su contraseña"))
        self.btn_iniciarSesion.setText(_translate("vw_sesion", "Iniciar Sesion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_sesion = QtWidgets.QMainWindow()
    ui = Ui_vw_sesion()
    ui.setupUi(vw_sesion)
    vw_sesion.show()
    sys.exit(app.exec())
