# Form implementation generated from reading ui file 'vw_FrmMenu.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vw_menu(object):
    def setupUi(self, vw_menu):
        vw_menu.setObjectName("vw_menu")
        vw_menu.resize(965, 748)
        self.centralwidget = QtWidgets.QWidget(parent=vw_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 941, 291))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 80, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 111, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 101, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 91, 17))
        self.label_4.setObjectName("label_4")
        self.txt_idMenu = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_idMenu.setGeometry(QtCore.QRect(140, 70, 291, 25))
        self.txt_idMenu.setObjectName("txt_idMenu")
        self.cmb_restMenu = QtWidgets.QComboBox(parent=self.groupBox)
        self.cmb_restMenu.setGeometry(QtCore.QRect(140, 110, 291, 25))
        self.cmb_restMenu.setObjectName("cmb_restMenu")
        self.txt_nombreMenu = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_nombreMenu.setGeometry(QtCore.QRect(140, 150, 291, 25))
        self.txt_nombreMenu.setObjectName("txt_nombreMenu")
        self.txt_descMenu = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txt_descMenu.setGeometry(QtCore.QRect(140, 190, 291, 25))
        self.txt_descMenu.setObjectName("txt_descMenu")
        self.btn_nuevoMenu = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_nuevoMenu.setGeometry(QtCore.QRect(540, 70, 101, 41))
        self.btn_nuevoMenu.setStyleSheet("QFrame{\n"
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
        icon.addPixmap(QtGui.QPixmap("../../CRUD Iconos-20230506T130125Z-001/CRUD Iconos/agregar-documento.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_nuevoMenu.setIcon(icon)
        self.btn_nuevoMenu.setObjectName("btn_nuevoMenu")
        self.btn_guardarMenu = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_guardarMenu.setGeometry(QtCore.QRect(540, 120, 101, 41))
        self.btn_guardarMenu.setStyleSheet("QFrame{\n"
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
        icon1.addPixmap(QtGui.QPixmap("../../CRUD Iconos-20230506T130125Z-001/CRUD Iconos/flecha-de-circulo-de-disquete-a-la-derecha.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_guardarMenu.setIcon(icon1)
        self.btn_guardarMenu.setObjectName("btn_guardarMenu")
        self.btn_editarMenu = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_editarMenu.setGeometry(QtCore.QRect(540, 170, 101, 41))
        self.btn_editarMenu.setStyleSheet("QFrame{\n"
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
        icon2.addPixmap(QtGui.QPixmap("../../CRUD Iconos-20230506T130125Z-001/CRUD Iconos/editar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_editarMenu.setIcon(icon2)
        self.btn_editarMenu.setObjectName("btn_editarMenu")
        self.btn_eliminarMenu = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_eliminarMenu.setGeometry(QtCore.QRect(550, 220, 101, 41))
        self.btn_eliminarMenu.setStyleSheet("QFrame{\n"
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
        icon3.addPixmap(QtGui.QPixmap("../../CRUD Iconos-20230506T130125Z-001/CRUD Iconos/eliminar-documento.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_eliminarMenu.setIcon(icon3)
        self.btn_eliminarMenu.setObjectName("btn_eliminarMenu")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 320, 941, 411))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.jtable_menu = QtWidgets.QTableWidget(parent=self.groupBox_2)
        self.jtable_menu.setGeometry(QtCore.QRect(10, 30, 921, 341))
        self.jtable_menu.setObjectName("jtable_menu")
        self.jtable_menu.setColumnCount(4)
        self.jtable_menu.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_menu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_menu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_menu.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.jtable_menu.setHorizontalHeaderItem(3, item)
        vw_menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=vw_menu)
        self.statusbar.setObjectName("statusbar")
        vw_menu.setStatusBar(self.statusbar)

        self.retranslateUi(vw_menu)
        QtCore.QMetaObject.connectSlotsByName(vw_menu)

    def retranslateUi(self, vw_menu):
        _translate = QtCore.QCoreApplication.translate
        vw_menu.setWindowTitle(_translate("vw_menu", "Menu"))
        self.groupBox.setTitle(_translate("vw_menu", "Registro Menu"))
        self.label.setText(_translate("vw_menu", "ID menu"))
        self.label_2.setText(_translate("vw_menu", "Restaurante ID"))
        self.label_3.setText(_translate("vw_menu", "Nombre Menu"))
        self.label_4.setText(_translate("vw_menu", "Descripcion"))
        self.btn_nuevoMenu.setText(_translate("vw_menu", "Nuevo"))
        self.btn_guardarMenu.setText(_translate("vw_menu", "Guardar"))
        self.btn_editarMenu.setText(_translate("vw_menu", "Editar"))
        self.btn_eliminarMenu.setText(_translate("vw_menu", "Eliminar"))
        item = self.jtable_menu.horizontalHeaderItem(0)
        item.setText(_translate("vw_menu", "ID_Menu"))
        item = self.jtable_menu.horizontalHeaderItem(1)
        item.setText(_translate("vw_menu", "RestauranteID"))
        item = self.jtable_menu.horizontalHeaderItem(2)
        item.setText(_translate("vw_menu", "Nombre"))
        item = self.jtable_menu.horizontalHeaderItem(3)
        item.setText(_translate("vw_menu", "Descripcion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_menu = QtWidgets.QMainWindow()
    ui = Ui_vw_menu()
    ui.setupUi(vw_menu)
    vw_menu.show()
    sys.exit(app.exec())
