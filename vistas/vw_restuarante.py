from PyQt6 import QtCore, QtGui, QtWidgets
from vistas import vw_frmRestaurante

from datos.dt_restaurante import Dt_Restaurante
from entidades.restaurante import Restaurante

class vw_listar_Restaurante_Widget(QtWidgets.QMainWindow,vw_frmRestaurante.Ui_vw_restaurante):
    def __init__(self,parent=None):
        super(vw_listar_Restaurante_Widget,self).__init__(parent)
        self.setupUi(self)
        # Llamando a la función listarRest para llenar la tabla
        self.listarRest()
        # Llamando a la funcion para guardar
        self.btn_guardarRest.clicked.connect(self.btnGuardarRestClick)
        # Llamando a la funcion para la edicion de los datos
        self.btn_editarRest.clicked.connect(self.btnActualizarRestauranteClick)
        # Llamando a la funcion para la eliminacion de datos
        self.btn_eliminarRest.clicked.connect(self.btnEliminarRestauranteClick)
        # Llamando a la funcion para el click de la tabla
        self.jtable_Restaurante.clicked.connect(self.clickTableCeldaR)
        # Llamando a la funcion para limpiar los campos del formulario
        self.btn_nuevoRest.clicked.connect(self.limpiarCampos)





    def listarRest(self):
        restaurantes = Dt_Restaurante.listarRestaurante()
        filasRest = len(restaurantes)
        self.jtable_Restaurante.setRowCount(filasRest)
        fila = 0

        for restRow in restaurantes:
            self.jtable_Restaurante.setItem(fila,0,QtWidgets.QTableWidgetItem(str(restRow.RestauranteID)))
            self.jtable_Restaurante.setItem(fila,1, QtWidgets.QTableWidgetItem(str(restRow.Nombre_restaurante)))
            self.jtable_Restaurante.setItem(fila,2, QtWidgets.QTableWidgetItem(str(restRow.Telefono_restaurante)))
            self.jtable_Restaurante.setItem(fila,3, QtWidgets.QTableWidgetItem(str(restRow.Correo_restaurante)))
            self.jtable_Restaurante.setItem(fila,4, QtWidgets.QTableWidgetItem(str(restRow.Direccion)))
            self.jtable_Restaurante.setItem(fila,5, QtWidgets.QTableWidgetItem(str(restRow.Numero_ruc)))
            self.jtable_Restaurante.setItem(fila,6, QtWidgets.QTableWidgetItem(str(restRow.Pagina_web)))
            fila +=1

    def btnGuardarRestClick(self):
        nombreRest = self.txt_nombreRest.text()
        telefonoRest = self.txt_telefonoRest.text()
        correoRest = self.txt_correoRest.text()
        direccionRest = self.txt_direccionRest.text()
        numeroRuc = self.txt_rucRest.text()
        pagRest = self.txt_pagWebrest.text()

        restaurante = Restaurante()
        restaurante.Nombre_restaurante = nombreRest
        restaurante.Telefono_restaurante = telefonoRest
        restaurante.Correo_restaurante = correoRest
        restaurante.Direccion = direccionRest
        restaurante.Numero_ruc = numeroRuc
        restaurante.Pagina_web = pagRest
        Dt_Restaurante.guardarRestaurante(restaurante)
        self.listarRest()
        self.limpiarCampos()

    def btnActualizarRestauranteClick(self):
        nombreRestedit = self.txt_nombreRest.text()
        telefonoRestedit = self.txt_telefonoRest.text()
        correoRestedit = self.txt_correoRest.text()
        direccionRestedit = self.txt_direccionRest.text()
        numeroRucedit = self.txt_rucRest.text()
        pagRestedit = self.txt_pagWebrest.text()
        restIDedit = self.txt_idRest.text()

        restaurante = Restaurante()
        restaurante.Nombre_restaurante = nombreRestedit
        restaurante.Telefono_restaurante = telefonoRestedit
        restaurante.Correo_restaurante = correoRestedit
        restaurante.Direccion = direccionRestedit
        restaurante.Numero_ruc = numeroRucedit
        restaurante.Pagina_web = pagRestedit
        restaurante.RestauranteID = restIDedit
        Dt_Restaurante.actualizarRestaurante(restaurante)
        self.listarRest()
        self.limpiarCampos()

    def btnEliminarRestauranteClick(self):

        restauranteIDdelete = self.txt_idRest.text()
        restaurante = Restaurante()
        restaurante.RestauranteID = restauranteIDdelete

        Dt_Restaurante.eliminarRestaurante(restaurante)
        self.listarRest()
        self.limpiarCampos()



    def limpiarCampos(self):
        self.txt_idRest.setText("")
        self.txt_nombreRest.setText("")
        self.txt_telefonoRest.setText("")
        self.txt_correoRest.setText("")
        self.txt_direccionRest.setText("")
        self.txt_rucRest.setText("")
        self.txt_pagWebrest.setText("")


    def clickTableCeldaR(self):
        # Obteniendo la fila seleccionada
        fila = self.jtable_Restaurante.currentRow()
        # Obteniendo los valores de la tabla
        restID = self.jtable_Restaurante.item(fila,0).text()
        nombreRest = self.jtable_Restaurante.item(fila, 1).text()
        telefonoRest = self.jtable_Restaurante.item(fila, 2).text()
        correoRest = self.jtable_Restaurante.item(fila, 3).text()
        direccionRest = self.jtable_Restaurante.item(fila, 4).text()
        numeroRuc = self.jtable_Restaurante.item(fila, 5).text()
        paginaWrest = self.jtable_Restaurante.item(fila, 6).text()

        # Mostrando los valores en los campos de texto
        self.txt_idRest.setText(restID)
        self.txt_nombreRest.setText(nombreRest)
        self.txt_telefonoRest.setText(telefonoRest)
        self.txt_correoRest.setText(correoRest)
        self.txt_direccionRest.setText(direccionRest)
        self.txt_rucRest.setText(numeroRuc)
        self.txt_pagWebrest.setText(paginaWrest)







        
