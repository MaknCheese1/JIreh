# Form implementation generated from reading ui file 'vw_frmRestaurante.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vw_restaurante(object):
    def setupUi(self, vw_restaurante):
        vw_restaurante.setObjectName("vw_restaurante")
        vw_restaurante.resize(894, 614)
        self.centralwidget = QtWidgets.QWidget(parent=vw_restaurante)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 941, 361))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 60, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 61, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(100, 220, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(120, 260, 41, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(80, 300, 81, 17))
        self.label_7.setObjectName("label_7")
        self.txt_idRest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_idRest.setGeometry(QtCore.QRect(170, 60, 291, 25))
        self.txt_idRest.setObjectName("txt_idRest")
        self.txt_nombreRest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_nombreRest.setGeometry(QtCore.QRect(170, 100, 291, 25))
        self.txt_nombreRest.setObjectName("txt_nombreRest")
        self.txt_telefonoRest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_telefonoRest.setGeometry(QtCore.QRect(170, 140, 291, 25))
        self.txt_telefonoRest.setObjectName("txt_telefonoRest")
        self.txt_correoRest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_correoRest.setGeometry(QtCore.QRect(170, 180, 291, 25))
        self.txt_correoRest.setObjectName("txt_correoRest")
        self.txt_direccionRest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_direccionRest.setGeometry(QtCore.QRect(170, 220, 291, 25))
        self.txt_direccionRest.setObjectName("txt_direccionRest")
        self.txt_rucRest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_rucRest.setGeometry(QtCore.QRect(170, 260, 291, 25))
        self.txt_rucRest.setObjectName("txt_rucRest")
        self.txt_pagWebrest = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_pagWebrest.setGeometry(QtCore.QRect(170, 300, 291, 25))
        self.txt_pagWebrest.setObjectName("txt_pagWebrest")
        self.btn_nuevoRest = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_nuevoRest.setGeometry(QtCore.QRect(580, 90, 101, 41))
        self.btn_nuevoRest.setStyleSheet("QFrame{\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Descargas/CRUD Iconos-20230506T130125Z-001/CRUD Iconos/agregar-documento.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_nuevoRest.setIcon(icon)
        self.btn_nuevoRest.setObjectName("btn_nuevoRest")
        self.btn_guardarRest = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_guardarRest.setGeometry(QtCore.QRect(580, 140, 101, 41))
        self.btn_guardarRest.setStyleSheet("QFrame{\n"
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Descargas/CRUD Iconos-20230506T130125Z-001/CRUD Iconos/flecha-de-circulo-de-disquete-a-la-derecha.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_guardarRest.setIcon(icon1)
        self.btn_guardarRest.setObjectName("btn_guardarRest")
        self.btn_editarRest = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_editarRest.setGeometry(QtCore.QRect(580, 190, 101, 41))
        self.btn_editarRest.setStyleSheet("QFrame{\n"
"background-color:#aa5ff;\n"
"}\n"
"QPushButton{\n"
"background-color:#aa5ff;\n"
"border-top-left:20px;\n"
"border-bottom-left-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:yellow;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../Descargas/CRUD Iconos-20230506T130125Z-001/CRUD Iconos/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_editarRest.setIcon(icon2)
        self.btn_editarRest.setObjectName("btn_editarRest")
        self.btn_eliminarRest = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_eliminarRest.setGeometry(QtCore.QRect(580, 240, 101, 41))
        self.btn_eliminarRest.setStyleSheet("QFrame{\n"
"background-color:#aa5ff;\n"
"}\n"
"QPushButton{\n"
"background-color:#aa5ff;\n"
"border-top-left:20px;\n"
"border-bottom-left-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:red;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../Descargas/CRUD Iconos-20230506T130125Z-001/CRUD Iconos/eliminar-documento.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_eliminarRest.setIcon(icon3)
        self.btn_eliminarRest.setObjectName("btn_eliminarRest")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 380, 941, 361))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.jtable_Restaurante = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.jtable_Restaurante.setGeometry(QtCore.QRect(20, 10, 781, 291))
        self.jtable_Restaurante.setObjectName("jtable_Restaurante")
        self.jtable_Restaurante.setColumnCount(7)
        self.jtable_Restaurante.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_Restaurante.setHorizontalHeaderItem(6, item)
        vw_restaurante.setCentralWidget(self.centralwidget)

        self.retranslateUi(vw_restaurante)
        QtCore.QMetaObject.connectSlotsByName(vw_restaurante)

    def retranslateUi(self, vw_restaurante):
        _translate = QtCore.QCoreApplication.translate
        vw_restaurante.setWindowTitle(_translate("vw_restaurante", "Restaurante"))
        self.groupBox.setTitle(_translate("vw_restaurante", "Registro Restaurante"))
        self.label.setText(_translate("vw_restaurante", "ID_Restaurante"))
        self.label_2.setText(_translate("vw_restaurante", "Nombre"))
        self.label_3.setText(_translate("vw_restaurante", "Telefono"))
        self.label_4.setText(_translate("vw_restaurante", "Correo"))
        self.label_5.setText(_translate("vw_restaurante", "Direccion"))
        self.label_6.setText(_translate("vw_restaurante", "Ruc"))
        self.label_7.setText(_translate("vw_restaurante", "Pagina web"))
        self.btn_nuevoRest.setText(_translate("vw_restaurante", "Nuevo"))
        self.btn_guardarRest.setText(_translate("vw_restaurante", "Guardar"))
        self.btn_editarRest.setText(_translate("vw_restaurante", "Editar"))
        self.btn_eliminarRest.setText(_translate("vw_restaurante", "Eliminar"))
        item = self.jtable_Restaurante.horizontalHeaderItem(0)
        item.setText(_translate("vw_restaurante", "ID_Rest"))
        item = self.jtable_Restaurante.horizontalHeaderItem(1)
        item.setText(_translate("vw_restaurante", "Nombre"))
        item = self.jtable_Restaurante.horizontalHeaderItem(2)
        item.setText(_translate("vw_restaurante", "Telefono"))
        item = self.jtable_Restaurante.horizontalHeaderItem(3)
        item.setText(_translate("vw_restaurante", "Correo"))
        item = self.jtable_Restaurante.horizontalHeaderItem(4)
        item.setText(_translate("vw_restaurante", "Direccion"))
        item = self.jtable_Restaurante.horizontalHeaderItem(5)
        item.setText(_translate("vw_restaurante", "RUC"))
        item = self.jtable_Restaurante.horizontalHeaderItem(6)
        item.setText(_translate("vw_restaurante", "Pagina web"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_restaurante = QtWidgets.QMainWindow()
    ui = Ui_vw_restaurante()
    ui.setupUi(vw_restaurante)
    vw_restaurante.show()
    sys.exit(app.exec())