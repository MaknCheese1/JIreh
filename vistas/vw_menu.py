from PyQt6 import QtWidgets
from vistas import vw_FrmMenu
from datos.dt_menu import Dt_Menu
from entidades.menu import Menu

from datos.dt_restaurante import Dt_Restaurante


class vw_listar_menu_Widget(QtWidgets.QMainWindow,vw_FrmMenu.Ui_vw_menu):
    def __init__(self,parent = None):
        super(vw_listar_menu_Widget,self).__init__(parent)
        self.setupUi(self)
        self.llenarComboMenu()
        self.listarMenu()
        self.jtable_menu.clicked.connect(self.clickTablaCeldaMn)
        self.btn_guardarMenu.clicked.connect(self.btnGuardarMenuClick)
        self.btn_editarMenu.clicked.connect(self.btnActualizarMenu)
        self.btn_eliminarMenu.clicked.connect(self.btnEliminarMenu)

        self.btn_nuevoMenu.clicked.connect(self.limpiarCampos)

    def listarMenu(self):
        menus = Dt_Menu.listarMenu()
        filasMenu = len(menus)
        self.jtable_menu.setRowCount(filasMenu)
        fila = 0

        for menuRow in menus:
            self.jtable_menu.setItem(fila,0,QtWidgets.QTableWidgetItem(str(menuRow.MenuID)))
            self.jtable_menu.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(menuRow.RestauranteID)))
            self.jtable_menu.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(menuRow.Nombre_menu)))
            self.jtable_menu.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(menuRow.Descripcion)))
            fila +=1

    def btnGuardarMenuClick(self):
        nombreMenu = self.txt_nombreMenu.text()
        descMenu = self.txt_descMenu.text()

        menu = Menu()
        menu.RestauranteID = self.obtenerMenuSeleccionado()
        menu.Nombre_menu = nombreMenu
        menu.Descripcion = descMenu
        Dt_Menu.guardarMenu(menu)
        self.listarMenu()
        self.limpiarCampos()

    def llenarComboMenu(self):
        menu = Dt_Restaurante.listarRestaurante()
        try:
            for m in menu:
                self.cmb_restMenu.addItem(m.Nombre_restaurante,m.RestauranteID)
        except Exception as e:
            print(f'Ocurrio  una excepcion al recuperar usuarios: {e}')

    def obtenerMenuSeleccionado(self):
        index = self.cmb_restMenu.currentIndex()
        idMenu = self.cmb_restMenu.itemData(index)
        return  idMenu

    def btnActualizarMenu(self):
        nombreMenu = self.txt_nombreMenu.text()
        descMenu = self.txt_descMenu.text()
        menuID = self.txt_idMenu.text()

        menu = Menu()
        menu.RestauranteID = self.obtenerMenuSeleccionado()
        menu.Nombre_menu = nombreMenu
        menu.Descripcion = descMenu
        menu.MenuID = menuID
        Dt_Menu.actualizarMenu(menu)
        self.listarMenu()
        self.limpiarCampos()


    def btnEliminarMenu(self):
        menuIDdelete = self.txt_idMenu.text()
        menu = Menu()
        menu.MenuID = menuIDdelete

        Dt_Menu.eliminarMenu(menu)
        self.listarMenu()
        self.limpiarCampos()






    def limpiarCampos(self):
        self.txt_idMenu.setText("")
        self.txt_nombreMenu.setText("")
        self.txt_descMenu.setText("")

    def clickTablaCeldaMn(self):
        fila = self.jtable_menu.currentRow()
        menuID = self.jtable_menu.item(fila,0).text()
        nombreMenu = self.jtable_menu.item(fila,2).text()
        descMenu = self.jtable_menu.item(fila,3).text()

        self.txt_idMenu.setText(menuID)
        self.txt_nombreMenu.setText(nombreMenu)
        self.txt_descMenu.setText(descMenu)













































