from PyQt6 import QtWidgets
from vistas import vw_FrmMenu

class vw_listar_menu_Widget(QtWidgets.QMainWindow,vw_FrmMenu.Ui_vw_menu):
    def __init__(self,parent = None):
        super(vw_listar_menu_Widget,self).__init__(parent)
        self.setupUi(self)