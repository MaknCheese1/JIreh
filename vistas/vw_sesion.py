from PyQt6 import QtWidgets
from vistas import vw_FrmSesion
from PyQt6.QtWidgets import QApplication
import sys
from datos.conexion import Conexion
from PyQt6.QtWidgets import QMessageBox
from vistas import mainWindow
from mainWindow import MainWindow
class vw_sesion_Widget(QtWidgets.QMainWindow,vw_FrmSesion.Ui_vw_sesion):
    def __init__(self,parent=None):
        super(vw_sesion_Widget,self).__init__(parent)
        self.setupUi(self)
        # LLamando la clase btn_iniciarSesion
        self.btn_iniciarSesion.clicked.connect(self.btnIniciarSesionClick)
        self.showWindows = None
        self.main = None

    def btnIniciarSesionClick(self):

            with Conexion.getConnection() as conexion:
                with Conexion.getCursor() as cursor:
                    username = self.txt_usuarioSesion.text()
                    password = self.txt_passworSesion.text()
                    # Verificar las credenciales en la base de datos
                    query = "SELECT * FROM usuario WHERE nombreusuario=%s AND clave=%s"
                    cursor.execute(query, (username, password))
                    result = cursor.fetchone()
            if result:
                self.Entrar()
                self.Close()
            else:
                QMessageBox.warning(self, "Login", "Credenciales inválidas.")

def Entrar(self):
        if self.showWindows is None:
            self.main = mainWindow.MainWindow()
            self.verticalLayout.addWidget(self.main)
            self.showWindows = self.main
        else:
            if self.showWindows == self.main:
                return self.main
            else:
                self.showWindows.close()
                self.main = mainWindow.MainWindow()
                self.verticalLayout.addWidget(self.main)
                self.showWindows = self.main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vws = vw_sesion_Widget()
    vws.show()
    app.exec()
