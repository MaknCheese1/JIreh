import sys
from PyQt6 import QtWidgets
from vistas import vw_FrmMenuDetalle
from datos.dt_MenuDetalle import Dt_MenuDetalle
from entidades.menuDetalle import MenuDetalle
from datos.dt_menu import Dt_Menu
from datos.dt_MenuTipo import Dt_MenuTipo

class vw_listar_MenuDetalle_Widget(QtWidgets.QMainWindow, vw_FrmMenuDetalle.Ui_vw_menuDetalle):
    def __init__(self, parent=None):
        super(vw_listar_MenuDetalle_Widget, self).__init__(parent)
        self.setupUi(self)
        self.llenarComboMenu()
        self.llenarComboMenuTipo()

        # Llamando datos en la tabla
        self.listarMenuDetalle()
        # Llamando a la función btnGuardar
        self.btn_guardarMenuDet.clicked.connect(self.btnGuardarMenuDetClick)
        # Llamando a la función clickTabla
        self.jtable_MenuDet.clicked.connect(self.clickTablaCeldaC)
        # Llamando a la función limpiarCampos
        self.btn_nuevoMenuDet.clicked.connect(self.limpiarCampos)

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

    def btnGuardarMenuDetClick(self):
        nombreMenuDetalle = self.txt_nombreMenuDet.text()
        descripcionMenuDetalle = self.txt_descMenuDet.text()
        precioMenuDetalle = self.txt_precioMenuDet.text()

        menuID = self.cmb_menuDetalle.currentData()
        menuTipoID = self.cmb_MenutipoDet.currentData()

        menuDetalle = MenuDetalle()
        menuDetalle.MenuID = menuID
        menuDetalle.Menu_tipoID = menuTipoID
        menuDetalle.Nombre = nombreMenuDetalle
        menuDetalle.Descripcion = descripcionMenuDetalle
        menuDetalle.Precio = precioMenuDetalle
        Dt_MenuDetalle.guardarMenuDetalle(menuDetalle)

    def llenarComboMenu(self):
        Menu = Dt_Menu.listarMenu()
        try:
            for menu in Menu:
                self.cmb_menuDetalle.addItem(menu.Nombre, menu.MenuID)
        except Exception as e:
            print(f'Ocurrió una excepción al recuperar Menu: {e}')

    def obtenermenuSeleccionado(self):
        index = self.cmb_menuDetalle.currentIndex()
        idMenu = self.cmb_menuDetalle.itemData(index)
        return idMenu

    def llenarComboMenuTipo(self):
        menuTipos = Dt_MenuTipo.listarMenuTipo()
        for mt in menuTipos:
            self.cmb_MenutipoDet.addItem(mt.Nombre, mt.Menu_tipoID)


    def obtenermenutipoSeleccionado(self):
        index = self.cmb_MenutipDet.currentIndex()
        idMenutipo = self.cmb_MenutipDet.itemData(index)
        return idMenutipo

    def btnActualizarMenuDetClick(self):
        menudetalleidEdit = self.txt_idMenuDet.text()
        nombreMenuDetalleEdit = self.txt_nombreMenuDet.text()
        descripcionMenuDetalleEdit = self.txt_descMenuDet.text()
        precioMenuDetalleEdit = self.txt_precioMenuDet.text()

        menuDetalle = MenuDetalle()
        menuDetalle.Menu_detalleID = menudetalleidEdit
        menuDetalle.Nombre = nombreMenuDetalleEdit
        menuDetalle.Descripcion = descripcionMenuDetalleEdit
        menuDetalle.Precio = precioMenuDetalleEdit
        Dt_MenuDetalle.actualizarMenuDetalle(menuDetalle)

    def eliminarMenuDetClick(self):
        menuDetalle = MenuDetalle()
        menuDetalle.Menu_detalleID = self.txt_idMenuDet.text()
        Dt_MenuDetalle.eliminarMenuDetalle(menuDetalle)

    def limpiarCampos(self):
        self.txt_idMenuDet.setText("")
        self.txt_nombreMenuDet.setText("")
        self.txt_descMenuDet.setText("")
        self.txt_precioMenuDet.setText("")

    def clickTablaCeldaC(self):
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana_menuDetalle = vw_listar_MenuDetalle_Widget()
    ventana_menuDetalle.show()
    sys.exit(app.exec())
