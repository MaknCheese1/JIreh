import random
import string

import PyQt6
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QAbstractItemView, QTableWidgetItem

from datos.dt_usuario import DT_Usuario
from entidades.usuario import Usuario
from vistas import vw_lista_usuarios


class vw_lista_usuarios_Widget(QtWidgets.QMainWindow, vw_lista_usuarios.Ui_frmListaUsuarios):
    def __init__(self, parent=None):
        super(vw_lista_usuarios_Widget,self).__init__(parent)
        self.setupUi(self)
        self.listarUsuario()
        self.txtIdUsuarioEdit.hide()
        self.btnBuscar.clicked.connect(self.buscarUsuario)
        self.tw_usuarios.clicked.connect(self.clickTablaCelda)
        self.btnEditarUsuario.clicked.connect(self.actualizarUsuarioClick)
        self.btnEliminarUsuario.clicked.connect(self.eliminarUsuario)



    def buscarUsuario(self, s):
        self.tw_usuarios.setCurrentItem(None)
        busqueda = self.txtBuscar.text()
        users = DT_Usuario.buscarUsuarios(busqueda)
        indexes = len(users)
        self.tw_usuarios.setRowCount(indexes)
        tablerow = 0

        for res in users:
            self.tw_usuarios.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(res.idusuario)))
            self.tw_usuarios.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(res.nombre))
            self.tw_usuarios.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(res.apellido))
            self.tw_usuarios.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(res.nombreusuario))
            self.tw_usuarios.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(res.fecha_creacion)))
            tablerow += 1


    def listarUsuario(self):
        usuarios = DT_Usuario.listarUsuario()
        indexes = len(usuarios)
        self.tw_usuarios.setRowCount(indexes)
        tablerow = 0
        for usuario in usuarios:
            self.tw_usuarios.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(usuario.idusuario)))
            self.tw_usuarios.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(usuario.nombre)))
            self.tw_usuarios.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(usuario.apellido)))
            self.tw_usuarios.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(usuario.nombreusuario)))
            self.tw_usuarios.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(usuario.fecha_creacion)))
            tablerow += 1

    def clickTablaCelda(self):
        #Se obtiene la fila actual
        row = self.tw_usuarios.currentRow()
        #Se obtienen los valores de la tabla
        id = self.tw_usuarios.item(row, 0).text()
        nombre = self.tw_usuarios.item(row, 1).text()
        apellido = self.tw_usuarios.item(row, 2).text()
        nombre_usuario = self.tw_usuarios.item(row, 3).text()

        #Se muestra en el formulario
        self.txtIdUsuarioEdit.setText(id)
        self.txtNombreEdit.setText(nombre)
        self.txtApellidoEdit.setText(apellido)
        self.txtNombreUsuarioEdit.setText(nombre_usuario)


    def actualizarUsuarioClick(self):
        nombre = self.txtNombreEdit.text()
        apellido = self.txtApellidoEdit.text()
        nombre_usuario = self.txtNombreUsuarioEdit.text()
        clave = self.txtClaveEdit.text()
        id_usuario = self.txtIdUsuarioEdit.text()

        usuario = Usuario()
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.nombreusuario = nombre_usuario
        usuario.clave = clave
        usuario.idusuario = id_usuario
        DT_Usuario.actualizarUsuario(usuario)

        self.listarUsuario()
        # Limpiar campos
        self.limpiarcampos()

    def eliminarUsuario(self):
        Usuario.idusuario = self.txtIdUsuarioEdit.text()
        DT_Usuario.eliminarUsuario(Usuario)
        self.listarUsuario()
        self.limpiarcampos()


    def limpiarcampos(self):
        self.txtNombreEdit.setText("")
        self.txtApellidoEdit.setText("")
        self.txtNombreUsuarioEdit.setText("")
        self.txtClaveEdit.setText("")
        self.txtIdUsuarioEdit.setText("")
