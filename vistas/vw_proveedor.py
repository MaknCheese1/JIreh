from PyQt6 import QtWidgets
from vistas import vw_FrmProveedor

class vw_listar_proveedor_Widget(QtWidgets.QMainWindow,vw_FrmProveedor.Ui_vw_proveedor):
    def __init__(self,parent = None):
        super(vw_listar_proveedor_Widget,self).__init__(parent)
        self.setupUi(self)