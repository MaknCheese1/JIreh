import PyQt6
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from datos.dt_usuario import DT_Usuario
from entidades.usuario import Usuario
from vistas import frm_GuardarUsuario


class VW_frmGuardarUsuario(QtWidgets.QMainWindow, frm_GuardarUsuario.Ui_MainWindow):
    def __init__(self, parent=None):
        super(VW_frmGuardarUsuario, self).__init__(parent)
        self.setupUi(self)
        self.btnGuardarUsuario.clicked.connect(self.btnGuardarClick)

    def btnGuardarClick(self):
        nombre = self.txtNombre.text()
        apellido = self.txtApellido.text()
        nombre_usuario = self.txtUserName.text()
        clave = self.txtClave.text()

        usuario = Usuario()
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.nombreusuario = nombre_usuario
        usuario.clave = clave
        DT_Usuario.guardarUsuario(usuario)
        #Limpiar campos
        self.limpiarcampos()

    def limpiarcampos(self):
        self.txtNombre.setText("")
        self.txtApellido.setText("")
        self.txtUserName.setText("")
        self.txtClave.setText("")



