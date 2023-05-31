from PyQt6 import QtWidgets
from vistas import vw_frmMenuTipo

from datos.dt_MenuTipo import Dt_MenuTipo
from entidades.menuTipo import MenuTipo

class vw_listar_MenuTipo_Widget(QtWidgets.QMainWindow,vw_frmMenuTipo.Ui_vw_menuTipo):
    def __init__(self,parent = None):
        super(vw_listar_MenuTipo_Widget,self).__init__(parent)
        self.setupUi(self)

        # LLamando datos en la tabla
        self.listarMenuDetalle()
        # LLamando la clase btnGuardar
        self.btn_guardarMenuTipo.clicked.connect(self.btnGuardarClientClick)
        # Llamando a la clase clickTable
        self.jtable_MenuTipo.clicked.connect(self.clickTablaCeldaC)
        # Llamando a la clase limpiarCampos
        self.btn_nuevoMenuTipo.clicked.connect(self.limpiarCampos)

    def listarMenuTipo(self):
        MenuTipo = Dt_MenuTipo.listarMenuTipo()
        indexes = len(MenuTipo)
        self.jtable_MenuTipo.setRowCount(indexes)
        tablerow = 0

        for row in MenuTipo:
            self.jtable_MenuTipo.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.Menu_tipoID)))
            self.jtable_MenuTipo.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.Nombre)))
            self.jtable_MenuTipo.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.Descripcion)))

    def btnGuardarMenuTipClick(self):
        nombreMenuTipo = self.txt_nombreMenuTip.text()
        descripcionMenuTipo = self.txt_descMenuTip.text()

        MenuTipo.Nombre = nombreMenuTipo
        MenuTipo.Descripcion = descripcionMenuTipo
        Dt_MenuTipo.guardarMenuTipo(MenuTipo)

    def btnActualizarMenuTipClick(self):
        nombreMenuTipoedit = self.txt_nombreMenuTip.text()
        descripcionMenuTipoedit = self.txt_descrpcionMenuTip.text()

        MenuTipo.Nombre = nombreMenuTipoedit
        MenuTipo.Descripcion = descripcionMenuTipoedit
        Dt_MenuTipo.actualizarMenuTipo(MenuTipo)

    def eliminarMenuTipClick(self):
        MenuTipo.Menu_tipoID = self.txt_idMenuTip.text()
        Dt_MenuTipo.eliminarMenuTipo(MenuTipo)

    def limpiarCampos(self):
        self.txt_nombreMenuTip.setText("")
        self.txt_descrpcionMenuTip.setText("")

    def clickTablaCeldaC(self):
        # Obteniendo fila
        rowC = self.jtable_MenuTipo.currentRow()
        # Obteniendo los valores de la tabla
        Nombre = self.jtable_MenuTipo.item(rowC, 1).text()
        Descripcion = self.jtable_MenuTipo.item(rowC, 2).text()

        # Se muestra en el formulario
        self.txt_nombreMenuTip.setText(Nombre)
        self.txt_descripcionMenuTip.setText(Descripcion)

