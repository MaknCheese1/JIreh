# Form implementation generated from reading ui file 'vw_FrmProveedor.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vw_proveedor(object):
    def setupUi(self, vw_proveedor):
        vw_proveedor.setObjectName("vw_proveedor")
        vw_proveedor.resize(965, 748)
        self.centralwidget = QtWidgets.QWidget(parent=vw_proveedor)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 941, 331))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 50, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 91, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(90, 210, 51, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 250, 81, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(60, 300, 81, 17))
        self.label_7.setObjectName("label_7")
        self.txt_idProveedor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_idProveedor.setGeometry(QtCore.QRect(150, 50, 291, 25))
        self.txt_idProveedor.setObjectName("txt_idProveedor")
        self.txt_nombreProveedor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_nombreProveedor.setGeometry(QtCore.QRect(150, 130, 291, 25))
        self.txt_nombreProveedor.setObjectName("txt_nombreProveedor")
        self.cmb_restauranteProv = QtWidgets.QComboBox(parent=self.groupBox)
        self.cmb_restauranteProv.setGeometry(QtCore.QRect(150, 90, 291, 25))
        self.cmb_restauranteProv.setObjectName("cmb_restauranteProv")
        self.txt_telProveedor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_telProveedor.setGeometry(QtCore.QRect(150, 170, 291, 25))
        self.txt_telProveedor.setObjectName("txt_telProveedor")
        self.txt_correoProveedor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_correoProveedor.setGeometry(QtCore.QRect(150, 210, 291, 25))
        self.txt_correoProveedor.setObjectName("txt_correoProveedor")
        self.txt_descProveedor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_descProveedor.setGeometry(QtCore.QRect(150, 250, 291, 25))
        self.txt_descProveedor.setObjectName("txt_descProveedor")
        self.txt_pagwProveedor = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_pagwProveedor.setGeometry(QtCore.QRect(150, 290, 291, 25))
        self.txt_pagwProveedor.setObjectName("txt_pagwProveedor")
        self.btn_nuevoProveedor = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_nuevoProveedor.setGeometry(QtCore.QRect(560, 60, 101, 41))
        self.btn_nuevoProveedor.setStyleSheet("QFrame{\n"
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
        self.btn_nuevoProveedor.setIcon(icon)
        self.btn_nuevoProveedor.setObjectName("btn_nuevoProveedor")
        self.btn_guardarProveedor = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_guardarProveedor.setGeometry(QtCore.QRect(560, 110, 101, 41))
        self.btn_guardarProveedor.setStyleSheet("QFrame{\n"
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
        self.btn_guardarProveedor.setIcon(icon1)
        self.btn_guardarProveedor.setObjectName("btn_guardarProveedor")
        self.btn_editarProveedor = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_editarProveedor.setGeometry(QtCore.QRect(570, 160, 101, 41))
        self.btn_editarProveedor.setStyleSheet("QFrame{\n"
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
        self.btn_editarProveedor.setIcon(icon2)
        self.btn_editarProveedor.setObjectName("btn_editarProveedor")
        self.btn_eliminarProveedor = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_eliminarProveedor.setGeometry(QtCore.QRect(570, 210, 101, 41))
        self.btn_eliminarProveedor.setStyleSheet("QFrame{\n"
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
        self.btn_eliminarProveedor.setIcon(icon3)
        self.btn_eliminarProveedor.setObjectName("btn_eliminarProveedor")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 350, 941, 361))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.jtable_proveedor = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.jtable_proveedor.setGeometry(QtCore.QRect(10, 20, 901, 291))
        self.jtable_proveedor.setObjectName("jtable_proveedor")
        self.jtable_proveedor.setColumnCount(7)
        self.jtable_proveedor.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_proveedor.setHorizontalHeaderItem(6, item)
        vw_proveedor.setCentralWidget(self.centralwidget)

        self.retranslateUi(vw_proveedor)
        QtCore.QMetaObject.connectSlotsByName(vw_proveedor)

    def retranslateUi(self, vw_proveedor):
        _translate = QtCore.QCoreApplication.translate
        vw_proveedor.setWindowTitle(_translate("vw_proveedor", "MainWindow"))
        self.groupBox.setTitle(_translate("vw_proveedor", "Registro Proveedor"))
        self.label.setText(_translate("vw_proveedor", "ID Proveedor"))
        self.label_2.setText(_translate("vw_proveedor", "Restaurante"))
        self.label_3.setText(_translate("vw_proveedor", "Nombre"))
        self.label_4.setText(_translate("vw_proveedor", "Telefono"))
        self.label_5.setText(_translate("vw_proveedor", "Correo"))
        self.label_6.setText(_translate("vw_proveedor", "Descripcion"))
        self.label_7.setText(_translate("vw_proveedor", "Pagina web"))
        self.btn_nuevoProveedor.setText(_translate("vw_proveedor", "Nuevo"))
        self.btn_guardarProveedor.setText(_translate("vw_proveedor", "Guardar"))
        self.btn_editarProveedor.setText(_translate("vw_proveedor", "Editar"))
        self.btn_eliminarProveedor.setText(_translate("vw_proveedor", "Eliminar"))
        item = self.jtable_proveedor.horizontalHeaderItem(0)
        item.setText(_translate("vw_proveedor", "ID_Proveedor"))
        item = self.jtable_proveedor.horizontalHeaderItem(1)
        item.setText(_translate("vw_proveedor", "Restaurante"))
        item = self.jtable_proveedor.horizontalHeaderItem(2)
        item.setText(_translate("vw_proveedor", "Nombre"))
        item = self.jtable_proveedor.horizontalHeaderItem(3)
        item.setText(_translate("vw_proveedor", "Telefono "))
        item = self.jtable_proveedor.horizontalHeaderItem(4)
        item.setText(_translate("vw_proveedor", "Correo"))
        item = self.jtable_proveedor.horizontalHeaderItem(5)
        item.setText(_translate("vw_proveedor", "Descripcion"))
        item = self.jtable_proveedor.horizontalHeaderItem(6)
        item.setText(_translate("vw_proveedor", "Pagina web"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_proveedor = QtWidgets.QMainWindow()
    ui = Ui_vw_proveedor()
    ui.setupUi(vw_proveedor)
    vw_proveedor.show()
    sys.exit(app.exec())
