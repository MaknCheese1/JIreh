import  sys
from PyQt6 import (QtWidgets)
from PyQt6.QtWidgets import QApplication
from vistas import vw_FrmPrincipal
import vw_cliente
import vw_restaurante

class MainWindow(QtWidgets.QMainWindow,vw_FrmPrincipal.Ui_vw_principal):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        # Validando None a mis variables
        self.showWindows = None
        self.lista_client = None
        self.lista_rest = None
        # Llamando el formulario cliente
        self.actionGestionar_Clientes.triggered.connect(self.loadClient)
        # Llamando el formulario restaurante
        self.actionGestionar_Restaurantes.triggered.connect(self.loadRest)

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
            self.lista_rest = vw_restaurante.vw_listar_restaurantes_Widget()
            self.verticalLayout.addWidget(self.lista_rest)
            self.showWindows = self.lista_rest
        else:
            if self.showWindows == self.lista_rest:
                return self.lista_rest
            else:
                self.showWindows.close()
                self.lista_rest = vw_restaurante.vw_listar_restaurantes_Widget()
                self.verticalLayout.addWidget(self.lista_rest)
                self.showWindows = self.lista_rest


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    app.exec()