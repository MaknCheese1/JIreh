from PyQt6 import QtCore, QtGui, QtWidgets
from vistas import vw_frmMenuTipo
from datos.dt_MenuTipo import Dt_MenuTipo
from entidades.menuTipo import MenuTipo

class vw_listar_MenuTipo_Widget(QtWidgets.QMainWindow, vw_frmMenuTipo.Ui_vw_menuTipo):
    def __init__(self, parent=None):
        super(vw_listar_MenuTipo_Widget, self).__init__(parent)
        self.setupUi(self)

        # Llamando a la función listarMenuTipo para llenar la tabla
        self.listarMenuTipo()
        # Conectando el botón "Guardar" a la función btnGuardarMenuTipoClick
        self.btn_guardarMenuTip.clicked.connect(self.btnGuardarMenuTipoClick)
        # Conectando el evento de hacer clic en una celda de la tabla a la función clickTablaCelda
        self.jtable_menuTipo.clicked.connect(self.clickTablaCelda)
        # Conectando el botón "Nuevo" a la función limpiarCampos
        self.btn_nuevoMenuTIp.clicked.connect(self.limpiarCampos)
        # Conectando el botón "Editar" a la función btnActualizarMenuTipoClick
        self.btn_editarMenuTip.clicked.connect(self.btnActualizarMenuTipoClick)
        # Conectando el botón "Eliminar" a la función eliminarMenuTipoClick
        self.btn_eliminarMenuTip.clicked.connect(self.eliminarMenuTipoClick)

    def listarMenuTipo(self):
        menuTipos = Dt_MenuTipo.listarMenuTipo()
        filas = len(menuTipos)
        self.jtable_menuTipo.setRowCount(filas)
        fila = 0

        for menuTipo in menuTipos:
            self.jtable_menuTipo.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(menuTipo.Menu_tipoID)))
            self.jtable_menuTipo.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(menuTipo.Nombre)))
            self.jtable_menuTipo.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(menuTipo.Descripcion)))
            fila += 1

    def btnGuardarMenuTipoClick(self):
        nombreMenuTipo = self.txt_nombreMenuTip.text()
        descripcionMenuTipo = self.txt_descMenuTip.text()

        menuTipo = MenuTipo()
        menuTipo.Nombre = nombreMenuTipo
        menuTipo.Descripcion = descripcionMenuTipo
        Dt_MenuTipo.guardarMenuTipo(menuTipo)

        self.listarMenuTipo()
        self.limpiarCampos()

    def btnActualizarMenuTipoClick(self):
        nombreMenuTipoedit = self.txt_nombreMenuTip.text()
        descripcionMenuTipoedit = self.txt_descMenuTip.text()
        menutipoidedit = self.txt_idMenuTip.text()

        menuTipo = MenuTipo()
        menuTipo.Nombre = nombreMenuTipoedit
        menuTipo.Descripcion = descripcionMenuTipoedit
        menuTipo.Menu_tipoID = menutipoidedit
        Dt_MenuTipo.actualizarMenuTipo(menuTipo)

        self.listarMenuTipo()
        self.limpiarCampos()

    def eliminarMenuTipoClick(self):
        menuTipoID = self.txt_idMenuTip.text()

        menuTipo = MenuTipo()
        menuTipo.Menu_tipoID = menuTipoID

        Dt_MenuTipo.eliminarMenuTipo(menuTipo)

        self.listarMenuTipo()
        self.limpiarCampos()

    def limpiarCampos(self):
        self.txt_idMenuTip.setText("")
        self.txt_nombreMenuTip.setText("")
        self.txt_descMenuTip.setText("")

    def clickTablaCelda(self):
        # Obteniendo la fila seleccionada
        fila = self.jtable_menuTipo.currentRow()
        # Obteniendo los valores de la tabla
        menuTipoID = self.jtable_menuTipo.item(fila, 0).text()
        nombreMenuTipo = self.jtable_menuTipo.item(fila, 1).text()
        descripcionMenuTipo = self.jtable_menuTipo.item(fila, 2).text()

        # Mostrando los valores en los campos de texto
        self.txt_idMenuTip.setText(menuTipoID)
        self.txt_nombreMenuTip.setText(nombreMenuTipo)
        self.txt_descMenuTip.setText(descripcionMenuTipo)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vw_menuTipo = vw_listar_MenuTipo_Widget()
    vw_menuTipo.show()
    sys.exit(app.exec())
