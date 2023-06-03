from PyQt6 import QtWidgets
from vistas import vw_FrmSesion

class vw_sesion_Widget(QtWidgets.QMainWindow,vw_FrmSesion.Ui_vw_sesion):
    def __init__(self,parent=None):
        super(vw_sesion_Widget,self).__init__(parent)
        self.setupUi(self)
        # LLamando la clase btn_iniciarSesion
        self.btn_iniciarSesion.clicked.connect(self.btnIniciarSesionClick)
        
    def btnIniciarSesionClick(self):
        username = self.txt_usuarioSesion.text()
        password = self.txt_passworSesion.text()

        try:
            with Conexion.cursor() as cursor:
                # Verificar las credenciales en la base de datos
                query = "SELECT * FROM usuario WHERE nombreusuario=%s AND clave=%s"
                cursor.execute(query, (username, password))
                result = cursor.fetchone()

                if result:
                    QMessageBox.information(self, "Login", "Inicio de sesión exitoso.")
                else:
                    QMessageBox.warning(self, "Login", "Credenciales inválidas.")

        except pymysql.Error as e:
            print(f"Error al realizar la consulta: {e}")
