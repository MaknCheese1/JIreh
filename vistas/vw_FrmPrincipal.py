# Form implementation generated from reading ui file 'vw_FrmPrincipal.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_vw_principal(object):
    def setupUi(self, vw_principal):
        vw_principal.setObjectName("vw_principal")
        vw_principal.resize(983, 715)
        self.centralwidget = QtWidgets.QWidget(parent=vw_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        vw_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=vw_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 22))
        self.menubar.setObjectName("menubar")
        self.menuUsuario = QtWidgets.QMenu(parent=self.menubar)
        self.menuUsuario.setObjectName("menuUsuario")
        self.menuRestaurante = QtWidgets.QMenu(parent=self.menubar)
        self.menuRestaurante.setObjectName("menuRestaurante")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        vw_principal.setMenuBar(self.menubar)
        self.actionGestionar_Usuario = QtGui.QAction(parent=vw_principal)
        self.actionGestionar_Usuario.setObjectName("actionGestionar_Usuario")
        self.actionGestionar_Proveedores = QtGui.QAction(parent=vw_principal)
        self.actionGestionar_Proveedores.setObjectName("actionGestionar_Proveedores")
        self.actionGestionar_Restaurantes = QtGui.QAction(parent=vw_principal)
        self.actionGestionar_Restaurantes.setObjectName("actionGestionar_Restaurantes")
        self.actionGestionar_Clientes = QtGui.QAction(parent=vw_principal)
        self.actionGestionar_Clientes.setObjectName("actionGestionar_Clientes")
        self.actionConfigurar_Menu = QtGui.QAction(parent=vw_principal)
        self.actionConfigurar_Menu.setObjectName("actionConfigurar_Menu")
        self.actionConfigurar_Menu_Detalle = QtGui.QAction(parent=vw_principal)
        self.actionConfigurar_Menu_Detalle.setObjectName("actionConfigurar_Menu_Detalle")
        self.actionConfigurar_Menu_Tipo = QtGui.QAction(parent=vw_principal)
        self.actionConfigurar_Menu_Tipo.setObjectName("actionConfigurar_Menu_Tipo")
        self.menuUsuario.addAction(self.actionGestionar_Usuario)
        self.menuRestaurante.addAction(self.actionGestionar_Proveedores)
        self.menuRestaurante.addAction(self.actionGestionar_Restaurantes)
        self.menuRestaurante.addAction(self.actionGestionar_Clientes)
        self.menuMenu.addAction(self.actionConfigurar_Menu)
        self.menuMenu.addAction(self.actionConfigurar_Menu_Detalle)
        self.menuMenu.addAction(self.actionConfigurar_Menu_Tipo)
        self.menubar.addAction(self.menuUsuario.menuAction())
        self.menubar.addAction(self.menuRestaurante.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(vw_principal)
        QtCore.QMetaObject.connectSlotsByName(vw_principal)

    def retranslateUi(self, vw_principal):
        _translate = QtCore.QCoreApplication.translate
        vw_principal.setWindowTitle(_translate("vw_principal", "MainWindow"))
        self.menuUsuario.setTitle(_translate("vw_principal", "Usuario"))
        self.menuRestaurante.setTitle(_translate("vw_principal", "Restaurante"))
        self.menuMenu.setTitle(_translate("vw_principal", "Menu"))
        self.actionGestionar_Usuario.setText(_translate("vw_principal", "Gestionar Usuario"))
        self.actionGestionar_Proveedores.setText(_translate("vw_principal", "Gestionar Proveedores"))
        self.actionGestionar_Restaurantes.setText(_translate("vw_principal", "Gestionar Restaurantes"))
        self.actionGestionar_Clientes.setText(_translate("vw_principal", "Gestionar Clientes"))
        self.actionConfigurar_Menu.setText(_translate("vw_principal", "Configurar Menu"))
        self.actionConfigurar_Menu_Detalle.setText(_translate("vw_principal", "Configurar Menu Detalle"))
        self.actionConfigurar_Menu_Tipo.setText(_translate("vw_principal", "Configurar Menu Tipo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_principal = QtWidgets.QMainWindow()
    ui = Ui_vw_principal()
    ui.setupUi(vw_principal)
    vw_principal.show()
    sys.exit(app.exec())