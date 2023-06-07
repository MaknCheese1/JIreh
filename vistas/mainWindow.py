import  sys
from PyQt6 import (QtWidgets)
from PyQt6.QtWidgets import QApplication
from vistas import vw_FrmPrincipal
import vw_cliente
import vw_restuarante
import vw_menuDetalle
import  vw_menuTipo
import  vw_proveedor
import vw_menu
import vw_lista_usuariosW
import  vw_frmGuardarUsuario
import  vw_frmAsignarRol
class MainWindow(QtWidgets.QMainWindow,vw_FrmPrincipal.Ui_vw_principal):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        # Validando None a mis variables
        self.showWindows = None
        self.lista_client = None
        self.lista_rest = None
        self.lista_MenuDet = None
        self.lista_MenuTip = None
        self.lista_Proveedor = None
        self.lista_Menu = None
        self.lista_lstUSuarioW = None
        self.lista_Guardaruser = None
        self.lista_Guardarol = None


        # Llamando el formulario cliente
        self.actionGestionar_Clientes.triggered.connect(self.loadClient)
        # Llamando el formulario restaurante
        self.actionGestionar_Restaurantes.triggered.connect(self.loadRest)
        # Llamando el formulario MenuDetalle
        self.actionConfigurar_Menu_Detalle.triggered.connect(self.loadMenuDet)
        # Llamando el formulario MenuTipo
        self.actionConfigurar_Menu_Tipo.triggered.connect(self.loadMenuTip)
        # Llamando el formulario Proveedor
        self.actionGestionar_Proveedores.triggered.connect(self.loadProveedor)
        # Llamando el formulario Menu
        self.actionConfigurar_Menu.triggered.connect(self.loadMenu)
        # Llamando el forrmulario listar usuario
        self.actionListar_Usuario.triggered.connect(self.loadLstUsuarioW)
        # Llamando el forrmulario guardar usuario
        self.actionGestionar_Usuario.triggered.connect(self.LoadGuardarUser)
        # Llamando el forrmulario guardar Rol
        self.actionGestionar_Rol.triggered.connect(self.LoadGuardarRol)






    def loadClient(self):
        if self.showWindows is None:
            self.lista_client = vw_cliente.vw_listar_cliente_Widget()
            self.verticalLayout.addWidget(self.lista_client)
            self.showWindows = self.lista_client
        else:
            if self.showWindows == self.lista_client:
                return self.lista_client
            else:
                self.showWindows.close()
                self.lista_client = vw_cliente.vw_listar_cliente_Widget()
                self.verticalLayout.addWidget(self.lista_client)
                self.showWindows = self.lista_client

    def loadRest(self):
        if self.showWindows is None:
            self.lista_rest = vw_restuarante.vw_listar_Restaurante_Widget()
            self.verticalLayout.addWidget(self.lista_rest)
            self.showWindows = self.lista_rest
        else:
            if self.showWindows == self.lista_rest:
                return self.lista_rest
            else:
                self.showWindows.close()
                self.lista_rest = vw_restuarante.vw_listar_Restaurante_Widget()
                self.verticalLayout.addWidget(self.lista_rest)
                self.showWindows = self.lista_rest

    def loadMenuDet(self):
        if self.showWindows is None:
            self.lista_MenuDet = vw_menuDetalle.vw_listar_MenuDetalle_Widget()
            self.verticalLayout.addWidget(self.lista_MenuDet)
            self.showWindows = self.lista_MenuDet
        else:
            if self.showWindows == self.lista_MenuDet:
                return  self.lista_MenuDet
            else:
                self.showWindows.close()
                self.lista_MenuDet = vw_menuDetalle.vw_listar_MenuDetalle_Widget()
                self.verticalLayout.addWidget(self.lista_MenuDet)
                self.showWindows = self.lista_MenuDet
    
    def loadMenuTip(self):
        if self.showWindows is None:
            self.lista_MenuTip = vw_menuTipo.vw_listar_MenuTipo_Widget()
            self.verticalLayout.addWidget(self.lista_MenuTip)
            self.showWindows = self.lista_MenuTip
        else:
            if self.showWindows == self.lista_MenuTip:
                return self.lista_MenuTip
            else:
                self.showWindows.close()
                self.lista_MenuTip = vw_menuTipo.vw_listar_MenuTipo_Widget()
                self.verticalLayout.addWidget(self.lista_MenuTip)
                self.showWindows = self.lista_MenuTip

    def loadProveedor(self):
        if self.showWindows is None:
            self.lista_Proveedor = vw_proveedor.vw_listar_proveedor_Widget()
            self.verticalLayout.addWidget(self.lista_Proveedor)
            self.showWindows = self.lista_Proveedor
        else:
            if self.showWindows == self.lista_Proveedor:
                return self.lista_Proveedor
            else:
                self.showWindows.close()
                self.lista_Proveedor = vw_proveedor.vw_listar_proveedor_Widget()
                self.verticalLayout.addWidget(self.lista_Proveedor)
                self.showWindows = self.lista_Proveedor

    def loadMenu(self):
        if self.showWindows is None:
            self.lista_Menu = vw_menu.vw_listar_menu_Widget()
            self.verticalLayout.addWidget(self.lista_Menu)
            self.showWindows = self.lista_Menu
        else:
            if self.showWindows == self.lista_Menu:
                return self.lista_Menu
            else:
                self.showWindows.close()
                self.lista_Menu = vw_menu.vw_listar_menu_Widget()
                self.verticalLayout.addWidget(self.lista_Menu)
                self.showWindows = self.lista_Menu

    def loadLstUsuarioW(self):
        if self.showWindows is None:
            self.lista_lstUSuarioW = vw_lista_usuariosW.vw_lista_usuarios_Widget()
            self.verticalLayout.addWidget(self.lista_lstUSuarioW)
            self.showWindows = self.lista_lstUSuarioW
        else:
            if self.showWindows == self.lista_lstUSuarioW:
                return self.lista_lstUSuarioW
            else:
                self.showWindows.close()
                self.lista_lstUSuarioW = vw_lista_usuariosW.vw_lista_usuarios_Widget()
                self.verticalLayout.addWidget(self.lista_lstUSuarioW)
                self.showWindows = self.lista_lstUSuarioW

    def LoadGuardarUser(self):
        if self.showWindows is None:
            self.lista_Guardaruser = vw_frmGuardarUsuario.VW_frmGuardarUsuario()
            self.verticalLayout.addWidget(self.lista_Guardaruser)
            self.showWindows = self.lista_Guardaruser
        else:
            if self.showWindows == self.lista_Guardaruser:
                return self.lista_Guardaruser
            else:
                self.showWindows.close()
                self.lista_Guardaruser = vw_frmGuardarUsuario.VW_frmGuardarUsuario()
                self.verticalLayout.addWidget(self.lista_Guardaruser)
                self.showWindows = self.lista_Guardaruser

    def LoadGuardarRol(self):
        if self.showWindows is None:
            self.lista_Guardarol = vw_frmAsignarRol.vw_frmAsignarRolW()
            self.verticalLayout.addWidget(self.lista_Guardarol)
            self.showWindows = self.lista_Guardarol
        else:
            if self.showWindows == self.lista_Guardarol:
                return self.lista_Guardarol
            else:
                self.showWindows.close()
                self.lista_Guardarol = vw_frmAsignarRol.vw_frmAsignarRolW()
                self.verticalLayout.addWidget(self.lista_Guardarol)
                self.showWindows = self.lista_Guardarol


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()
