# Form implementation generated from reading ui file 'vw_frmCliente.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vw_cliente(object):
    def setupUi(self, vw_cliente):
        vw_cliente.setObjectName("vw_cliente")
        vw_cliente.resize(934, 621)
        self.centralwidget = QtWidgets.QWidget(parent=vw_cliente)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 941, 321))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 80, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 200, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(80, 240, 67, 17))
        self.label_5.setObjectName("label_5")
        self.txt_idCliente = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_idCliente.setGeometry(QtCore.QRect(160, 70, 291, 25))
        self.txt_idCliente.setObjectName("txt_idCliente")
        self.txt_nombreCliente = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_nombreCliente.setGeometry(QtCore.QRect(160, 150, 291, 25))
        self.txt_nombreCliente.setObjectName("txt_nombreCliente")
        self.txt_telefonoCliente = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_telefonoCliente.setGeometry(QtCore.QRect(160, 190, 291, 25))
        self.txt_telefonoCliente.setObjectName("txt_telefonoCliente")
        self.txt_direccionCliente = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_direccionCliente.setGeometry(QtCore.QRect(160, 230, 291, 25))
        self.txt_direccionCliente.setObjectName("txt_direccionCliente")
        self.cmb_idRestaurante = QtWidgets.QComboBox(parent=self.groupBox)
        self.cmb_idRestaurante.setGeometry(QtCore.QRect(160, 110, 291, 25))
        self.cmb_idRestaurante.setObjectName("cmb_idRestaurante")
        self.btn_nuevoCliente = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_nuevoCliente.setGeometry(QtCore.QRect(540, 80, 101, 41))
        self.btn_nuevoCliente.setStyleSheet("QFrame{\n"
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
        self.btn_nuevoCliente.setIcon(icon)
        self.btn_nuevoCliente.setObjectName("btn_nuevoCliente")
        self.btn_guardarCliente = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_guardarCliente.setGeometry(QtCore.QRect(540, 130, 101, 41))
        self.btn_guardarCliente.setStyleSheet("QFrame{\n"
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
        self.btn_guardarCliente.setIcon(icon1)
        self.btn_guardarCliente.setObjectName("btn_guardarCliente")
        self.btn_editarCliente = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_editarCliente.setGeometry(QtCore.QRect(540, 180, 101, 41))
        self.btn_editarCliente.setStyleSheet("QFrame{\n"
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
        self.btn_editarCliente.setIcon(icon2)
        self.btn_editarCliente.setObjectName("btn_editarCliente")
        self.btn_eliminarCliente = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_eliminarCliente.setGeometry(QtCore.QRect(540, 230, 101, 41))
        self.btn_eliminarCliente.setStyleSheet("QFrame{\n"
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
        self.btn_eliminarCliente.setIcon(icon3)
        self.btn_eliminarCliente.setObjectName("btn_eliminarCliente")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(40, 270, 111, 16))
        self.label_6.setObjectName("label_6")
        self.txt_tpCliente = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_tpCliente.setGeometry(QtCore.QRect(160, 270, 291, 25))
        self.txt_tpCliente.setObjectName("txt_tpCliente")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 340, 941, 351))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.jtable_cliente = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.jtable_cliente.setGeometry(QtCore.QRect(20, 20, 791, 301))
        self.jtable_cliente.setObjectName("jtable_cliente")
        self.jtable_cliente.setColumnCount(6)
        self.jtable_cliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_cliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_cliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_cliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_cliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_cliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_cliente.setHorizontalHeaderItem(5, item)
        vw_cliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(vw_cliente)
        QtCore.QMetaObject.connectSlotsByName(vw_cliente)

    def retranslateUi(self, vw_cliente):
        _translate = QtCore.QCoreApplication.translate
        vw_cliente.setWindowTitle(_translate("vw_cliente", "Cliente"))
        self.groupBox.setTitle(_translate("vw_cliente", "Registro Usuario"))
        self.label.setText(_translate("vw_cliente", "ID Cliente"))
        self.label_2.setText(_translate("vw_cliente", "ID Restaurante"))
        self.label_3.setText(_translate("vw_cliente", "Nombre"))
        self.label_4.setText(_translate("vw_cliente", "Telefono"))
        self.label_5.setText(_translate("vw_cliente", "Direccion"))
        self.btn_nuevoCliente.setText(_translate("vw_cliente", "Nuevo"))
        self.btn_guardarCliente.setText(_translate("vw_cliente", "Guardar"))
        self.btn_editarCliente.setText(_translate("vw_cliente", "Editar"))
        self.btn_eliminarCliente.setText(_translate("vw_cliente", "Eliminar"))
        self.label_6.setText(_translate("vw_cliente", "Tipo de cliente"))
        item = self.jtable_cliente.horizontalHeaderItem(0)
        item.setText(_translate("vw_cliente", "ID_Cliente"))
        item = self.jtable_cliente.horizontalHeaderItem(1)
        item.setText(_translate("vw_cliente", "ID_Restaurante"))
        item = self.jtable_cliente.horizontalHeaderItem(2)
        item.setText(_translate("vw_cliente", "Nombre"))
        item = self.jtable_cliente.horizontalHeaderItem(3)
        item.setText(_translate("vw_cliente", "Telefono"))
        item = self.jtable_cliente.horizontalHeaderItem(4)
        item.setText(_translate("vw_cliente", "Direccion"))
        item = self.jtable_cliente.horizontalHeaderItem(5)
        item.setText(_translate("vw_cliente", "Tipo Cliente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_cliente = QtWidgets.QMainWindow()
    ui = Ui_vw_cliente()
    ui.setupUi(vw_cliente)
    vw_cliente.show()
    sys.exit(app.exec())