from PyQt6 import QtWidgets
from vistas import  vw_FrmMenuDetalle

from datos.dt_MenuDetalle import Dt_MenuDetalle
from entidades.menuDetalle import MenuDetalle
from datos.dt_menu import Dt_Menu
from datos.dt_MenuTipo import Dt_MenuTipo


class vw_listar_MenuDetalle_Widget(QtWidgets.QMainWindow,vw_FrmMenuDetalle.Ui_vw_menuDetalle):
    def __init__(self,parent = None):
        super(vw_listar_MenuDetalle_Widget, self).__init__(parent)
        self.setupUi(self)
        self.txt_idMenuDet.setEnabled(False)

        self.llenarComboMenu()
        self.llenarComboMenuTipo()

        self.listarMenuDetalle()
        self.jtable_MenuDet.clicked.connect(self.clickTablaCeldaMt)
        self.btn_nuevoMenuDet.clicked.connect(self.limpiarCampos)
        self.btn_guardarMenuDet.clicked.connect(self.btnGuardarMenuDetalleClick)
        self.btn_editarMenuDet.clicked.connect(self.btnActualizarMenuDetalleClick)
        self.btn_eliminarMenuDet.clicked.connect(self.eliminarMenuDetClick)

    def listarMenuDetalle(self):
        menuDetalles = Dt_MenuDetalle.listarMenuDetalle()
        indices = len(menuDetalles)
        self.jtable_MenuDet.setRowCount(indices)
        fila = 0

        for filaMenu in menuDetalles:
            self.jtable_MenuDet.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(filaMenu.Menu_detalleID)))
            self.jtable_MenuDet.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(filaMenu.MenuID)))
            self.jtable_MenuDet.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(filaMenu.Menu_tipoID)))
            self.jtable_MenuDet.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(filaMenu.Nombre)))
            self.jtable_MenuDet.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(filaMenu.Descripcion)))
            self.jtable_MenuDet.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(filaMenu.Precio)))
            fila += 1


    def btnGuardarMenuDetalleClick(self):
        nombreMenuDetalle = self.txt_nombreMenuDet.text()
        descripcionMenuDetalle = self.txt_descMenuDet.text()
        precioMenuDetalle = self.txt_precioMenuDet.text()


        menuDet = MenuDetalle()
        menuDet.MenuID = self.obtenerMenuSeleccionado()
        menuDet.Menu_tipoID = self.obtenerMenuTipo()
        menuDet.Nombre = nombreMenuDetalle
        menuDet.Descripcion = descripcionMenuDetalle
        menuDet.Precio = precioMenuDetalle
        Dt_MenuDetalle.guardarMenuDetalle(menuDet)
        self.listarMenuDetalle()
        self.limpiarCampos()

    def btnActualizarMenuDetalleClick(self):
        nombreMenuDetalleedit = self.txt_nombreMenuDet.text()
        descripcionMenuDetalledit = self.txt_descMenuDet.text()
        precioMenuDetalleedit = self.txt_precioMenuDet.text()
        idMenuDet = self.txt_idMenuDet


        menuDet = MenuDetalle()
        menuDet.MenuID = self.obtenerMenuSeleccionado()
        menuDet.Menu_tipoID = self.obtenerMenuTipo()
        menuDet.Nombre = nombreMenuDetalleedit
        menuDet.Descripcion = descripcionMenuDetalledit
        menuDet.Precio = precioMenuDetalleedit
        menuDet.Menu_detalleID = idMenuDet
        Dt_MenuDetalle.actualizarMenuDetalle(menuDet)
        self.listarMenuDetalle()
        self.limpiarCampos()

    def eliminarMenuDetClick(self):
        menuDetalle = MenuDetalle()
        menuDetalle.Menu_detalleID = self.txt_idMenuDet.text()
        Dt_MenuDetalle.eliminarMenuDetalle(menuDetalle)
        self.listarMenuDetalle()
        self.limpiarCampos()

    def llenarComboMenu(self):
        menu = Dt_Menu.listarMenu()
        try:
            for mu in menu:
                self.cmb_menuDetalle.addItem(mu.Nombre_menu,mu.MenuID)
        except Exception as e:
            print(f'Ocurrio  una excepcion al recuperar usuarios: {e}')

    def obtenerMenuSeleccionado(self):
        index = self.cmb_menuDetalle.currentIndex()
        idMenu = self.cmb_menuDetalle.itemData(index)
        return idMenu

    def llenarComboMenuTipo(self):
        menuDet = Dt_MenuDetalle.listarMenuDetalle()
        try:
            for mt in menuDet:
                self.cmb_MenutipoDet.addItem(mt.Nombre,mt.Menu_tipoID)
        except Exception as e:
            print(f'Ocurrio una excepcion al recuperar menudetalle: {e}')

    def obtenerMenuTipo(self):
        index = self.cmb_MenutipoDet.currentIndex()
        idMenuTip = self.cmb_MenutipoDet.itemData(index)
        return idMenuTip

    def limpiarCampos(self):
        self.txt_idMenuDet.setText("")
        self.txt_nombreMenuDet.setText("")
        self.txt_descMenuDet.setText("")
        self.txt_precioMenuDet.setText("")

    def clickTablaCeldaMt(self):
        # Obteniendo fila
        fila = self.jtable_MenuDet.currentRow()
        # Obteniendo los valores de la tabla
        menu_detalleID = self.jtable_MenuDet.item(fila, 0).text()
        nombre = self.jtable_MenuDet.item(fila, 3).text()
        descripcion = self.jtable_MenuDet.item(fila, 4).text()
        precio = self.jtable_MenuDet.item(fila, 5).text()

        # Mostrando los valores en los campos de texto
        self.txt_idMenuDet.setText(menu_detalleID)
        self.txt_nombreMenuDet.setText(nombre)
        self.txt_descMenuDet.setText(descripcion)
        self.txt_precioMenuDet.setText(precio)




