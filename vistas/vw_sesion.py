from PyQt6 import QtWidgets
from vistas import vw_FrmSesion
from PyQt6.QtWidgets import QApplication
import sys
from vistas import mainWindow
from datos.conexion import Conexion
from PyQt6.QtWidgets import QMessageBox
class vw_sesion_Widget(QtWidgets.QMainWindow,vw_FrmSesion.Ui_vw_sesion):
    def __init__(self,parent=None):
        super(vw_sesion_Widget,self).__init__(parent)
        self.setupUi(self)
        # LLamando la clase btn_iniciarSesion
        self.btn_iniciarSesion.clicked.connect(self.btnIniciarSesionClick)

    def btnIniciarSesionClick(self):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            username = self.txt_usuarioSesion.text()
            password = self.txt_passworSesion.text()
            # Verificar las credenciales en la base de datos
            query = "SELECT * FROM usuario WHERE nombreusuario=%s AND clave=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            if result:
                self.main = mainWindow.MainWindow()
                self.main.show()
                self.close()
            else:
                QMessageBox.warning(self, "Login", "Credenciales inválidas.")
        except Exception as e:
            print(f'Ocurrio una exception {e}')
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    vws = vw_sesion_Widget()
    vws.show()
    app.exec()
