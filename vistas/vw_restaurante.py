from PyQt6 import QtWidgets
from vistas import vw_frmRestaurante

from datos.dt_restaurante import Dt_Restaurante
from entidades.restaurante import Restaurante



class vw_listar_restaurantes_Widget(QtWidgets.QMainWindow,vw_frmRestaurante.Ui_vw_restaurante):
    def __init__(self,parent=None):
        super(vw_listar_restaurantes_Widget,self).__init__(parent)
        self.setupUi(self)
        # LLamando datos en la tabla
        self.listarRest()
        # LLamando la clase btnGuardar
        self.btn_guardarRest.clicked.connect(self.btnGuardarRestClick)
        # LLamando la clase btnEditar
        self.btn_editarRest.clicked.connect(self.btnActualizarRestClick)
        # LLamando la clase btnEliminar
        self.btn_eliminarRest.clicked.connect(self.eliminarRestClick)
        # Llamando a la clase clickTable
        self.jtable_Restaurante.clicked.connect(self.clickTablaCeldaR)
        # Llamando a la clase limpiarCampos
        self.btn_nuevoRest.clicked.connect(self.limpiarCampos)

    def btnGuardarRestClick(self):
        nombreRest = self.txt_nombreRest.text()
        telefonoRest = self.txt_telefonoRest.text()
        correoRest = self.txt_correoRest.text()
        direccionRest = self.txt_direccionRest.text()
        nrucRest = self.txt_rucRest.text()
        pwebRest = self.txt_pagWebrest.text()

        Restaurante.Nombre_restaurante = nombreRest
        Restaurante.Telefono_restaurante = telefonoRest
        Restaurante.Correo_restaurante = correoRest
        Restaurante.Direccion = direccionRest
        Restaurante.Numero_ruc = nrucRest
        Restaurante.Pagina_web = pwebRest
        Dt_Restaurante.guardarRestaurante(Restaurante)



    def btnActualizarRestClick(self):
        nombreRestedit = self.txt_nombreRest.text()
        telefonoRestedit = self.txt_telefonoRest.text()
        correoRestedit = self.txt_correoRest.text()
        direccionRestedit = self.txt_direccionRest.text()
        nrucRestedit = self.txt_rucRest.text()
        pwebRestedit = self.txt_pagWebrest.text()

        Restaurante.Nombre_restaurante = nombreRestedit
        Restaurante.Telefono_restaurante = telefonoRestedit
        Restaurante.Correo_restaurante = correoRestedit
        Restaurante.Direccion = direccionRestedit
        Restaurante.Numero_ruc = nrucRestedit
        Restaurante.Pagina_web = pwebRestedit
        Dt_Restaurante.actualizarRestaurante(Restaurante)

    def eliminarRestClick(self):
        Restaurante.RestauranteID = self.txt_idRest.text()
        Dt_Restaurante.eliminarRestaurante(Restaurante)

    def listarRest(self):
        restaurantes = Dt_Restaurante.listarRestaurante()
        indixes = len(restaurantes)
        self.jtable_Restaurante.setRowCount(indixes)
        tablerow = 0

        for row in restaurantes:
            self.jtable_Restaurante.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.RestauranteID)))
            self.jtable_Restaurante.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.Nombre_restaurante)))
            self.jtable_Restaurante.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.Telefono_restaurante)))
            self.jtable_Restaurante.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.Correo_restaurante)))
            self.jtable_Restaurante.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.Direccion)))
            self.jtable_Restaurante.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.Numero_ruc)))
            self.jtable_Restaurante.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row.Pagina_web)))
            self.jtable_Restaurante.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row.Estado)))
            tablerow += 1


    def limpiarCampos(self):
        self.txt_idRest.setText("")
        self.txt_nombreRest.setText("")
        self.txt_telefonoRest.setText("")
        self.txt_correoRest.setText("")
        self.txt_direccionRest.setText("")
        self.txt_rucRest.setText("")
        self.txt_pagWebrest.setText("")

    def clickTablaCeldaR(self):
        # Obteniendo fila
        rowR = self.jtable_Restaurante.currentRow()
        # Obteniendo los valores de la tabla
        RestauranteID = self.jtable_Restaurante.item(rowR, 0).text()
        Nombre_restaurante = self.jtable_Restaurante.item(rowR, 1).text()
        Telefono_restaurante = self.jtable_Restaurante.item(rowR, 2).text()
        Correo_restaurante = self.jtable_Restaurante.item(rowR, 3).text()
        Direecion_restaurante = self.jtable_Restaurante.item(rowR, 4).text()
        Numero_ruc = self.jtable_Restaurante.item(rowR, 5).text()
        pagina_web = self.jtable_Restaurante.item(rowR, 6).text()


        # Se muestra en el formulario
        self.txt_idRest.setText(RestauranteID)
        self.txt_nombreRest.setText(Nombre_restaurante)
        self.txt_telefonoRest.setText(Telefono_restaurante)
        self.txt_correoRest.setText(Correo_restaurante)
        self.txt_direccionRest.setText(Direecion_restaurante)
        self.txt_rucRest.setText(Numero_ruc)
        self.txt_pagWebrest.setText(pagina_web)







