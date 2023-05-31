from PyQt6 import QtWidgets
from vistas import  vw_FrmMenuDetalle

from datos.dt_MenuDetalle import Dt_MenuDetalle
from entidades.menuDetalle import MenuDetalle
class vw_listar_MenuDetalle_Widget(QtWidgets.QMainWindow,vw_FrmMenuDetalle.Ui_vw_menuDetalle):
    def __init__(self,parent = None):
        super(vw_listar_MenuDetalle_Widget,self).__init__(parent)
        self.setupUi(self)
        # LLamando datos en la tabla
        self.listarMenuDetalle()
        # LLamando la clase btnGuardar
        self.btn_guardarMenuDetalle.clicked.connect(self.btnGuardarClientClick)
        # Llamando a la clase clickTable
        self.jtable_MenuDetalle.clicked.connect(self.clickTablaCeldaC)
        # Llamando a la clase limpiarCampos
        self.btn_nuevoMenuDetalle.clicked.connect(self.limpiarCampos)

    def listarMenuDetalle(self):
        MenuDetalle = Dt_MenuDetalle.listarMenuDetalle()
        indexes = len(MenuDetalle)
        self.jtable_MenuDetalle.setRowCount(indexes)
        tablerow = 0

        for row in MenuDetalle:
            self.jtable_MenuDetalle.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.Menu_detalleID)))
            self.jtable_MenuDetalle.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.MenuID)))
            self.jtable_MenuDetalle.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.Menu_tipoID)))
            self.jtable_MenuDetalle.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.Nombre)))
            self.jtable_MenuDetalle.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.Descripcion)))
            self.jtable_MenuDetalle.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.Precio)))

    def btnGuardarMenuDetClick(self):
        nombreMenuDetalle = self.txt_nombreMenuDet.text()
        descripcionMenuDetalle = self.txt_descrpcionMenuDet.text()
        precioMenuDetalle = self.txt_precioMenuDet.text()

        MenuDetalle.Nombre = nombreMenuDetalle
        MenuDetalle.Descripcion = descripcionMenuDetalle
        MenuDetalle.Precio = precioMenuDetalle
        Dt_MenuDetalle.guardarMenuDetalle(MenuDetalle)

    def btnActualizarMenuDetClick(self):
        nombreMenuDetalleedit = self.txt_nombreMenuDet.text()
        descripcionMenuDetalleedit = self.txt_descrpcionMenuDet.text()
        precioMenuDetalleedit = self.txt_precioMenuDet.text()

        MenuDetalle.Nombre = nombreMenuDetalleedit
        MenuDetalle.Descripcion = descripcionMenuDetalleedit
        MenuDetalle.Precio = precioMenuDetalleedit
        Dt_MenuDetalle.actualizarMenuDetalle(MenuDetalle)

    def eliminarMenuDetClick(self):
        MenuDetalle.Menu_detalleID = self.txt_idMenuDet.text()
        Dt_MenuDetalle.eliminarMenuDetalle(MenuDetalle)

    def limpiarCampos(self):
        self.xt_nombreMenuDet.setText("")
        self.txt_descrpcionMenuDet.setText("")
        self.txt_precioMenuDet.setText("")

    def clickTablaCeldaC(self):
        # Obteniendo fila
        rowC = self.jtable_MenuDetalle.currentRow()
        # Obteniendo los valores de la tabla
        Nombre = self.jtable_MenuDetalle.item(rowC, 3).text()
        Descripcion = self.jtable_MenuDetalle.item(rowC, 4).text()
        Precio = self.jtable_MenuDetalle.item(rowC, 5).text()

        # Se muestra en el formulario
        self.txt_nombreMenuDet.setText(Nombre)
        self.txt_descripcionMenuDet.setText(Descripcion)
        self.txt_precioMenuDet.setText(Precio)