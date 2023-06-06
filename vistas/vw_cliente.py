from PyQt6 import QtWidgets
from vistas import vw_frmCliente

from datos.dt_cliente import Dt_Cliente
from entidades.cliente import Cliente
from datos.dt_restaurante import Dt_Restaurante
from entidades.restaurante import  Restaurante




class vw_listar_cliente_Widget(QtWidgets.QMainWindow,vw_frmCliente.Ui_vw_cliente):
    def __init__(self,parent=None):
        super(vw_listar_cliente_Widget,self).__init__(parent)
        self.setupUi(self)
        self.llenarComboClient()


        # dtr de guardarRest
        self.dtr = Dt_Restaurante
        # LLamando datos en la tabla
        self.listarClient()
        # LLamando la clase btnGuardar
        self.btn_guardarCliente.clicked.connect(self.btnGuardarClientClick)
        # LLamando la clase btnEditar
        self.btn_editarCliente.clicked.connect(self.btnActualizarClienteClick)
        self.btn_eliminarCliente.clicked.connect(self.eliminarClientClick)
        # Llamando a la clase clickTable
        self.jtable_cliente.clicked.connect(self.clickTablaCeldaC)
        # Llamando a la clase limpiarCampos
        self.btn_nuevoCliente.clicked.connect(self.limpiarCampos)




    def listarClient(self):
        clientes = Dt_Cliente.listarCliente()
        filaClient = len(clientes)
        self.jtable_cliente.setRowCount(filaClient)
        fila = 0
        for rowClient in clientes:
            self.jtable_cliente.setItem(fila,0,QtWidgets.QTableWidgetItem(str(rowClient.ClienteID)))
            self.jtable_cliente.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(rowClient.RestauranteID)))
            self.jtable_cliente.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(rowClient.Nombre_cliente)))
            self.jtable_cliente.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(rowClient.Telefono_cliente)))
            self.jtable_cliente.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(rowClient.Direccion)))
            self.jtable_cliente.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(rowClient.Tipo_cliente)))
            fila +=1





    def btnGuardarClientClick(self):

        nombreClient = self.txt_nombreCliente.text()
        telefonoClient = self.txt_telefonoCliente.text()
        direccionCliente = self.txt_direccionCliente.text()
        tpCliente = self.txt_tpCliente.text()

        cliente = Cliente()
        cliente.RestauranteID = self.obtenerClientSeleccionado()
        cliente.Nombre_cliente = nombreClient
        cliente.Telefono_cliente = telefonoClient
        cliente.Direccion = direccionCliente
        cliente.Tipo_cliente = tpCliente
        Dt_Cliente.guardarClient(cliente)


        self.listarClient()
        self.limpiarCampos()


    def llenarComboClient(self):
        client = Dt_Restaurante.listarRestaurante()
        try:
            for c in client:
                self.cmb_idRestaurante.addItem(c.Nombre_restaurante,c.RestauranteID)
        except Exception as e:
            print(f'Ocurrio  una excepcion al recuperar usuarios: {e}')


    def obtenerClientSeleccionado(self):
        index = self.cmb_idRestaurante.currentIndex()
        idRest = self.cmb_idRestaurante.itemData(index)
        return idRest


    def btnActualizarClienteClick(self):
        nombreClientedit = self.txt_nombreCliente.text()
        telefonoClientedit = self.txt_telefonoCliente.text()
        direccionClienteedit = self.txt_direccionCliente.text()
        tpClienteedit = self.txt_tpCliente.text()
        clientIDedit = self.txt_idCliente.text()

        cliente = Cliente()
        cliente.RestauranteID = self.obtenerClientSeleccionado()
        cliente.Nombre_cliente = nombreClientedit
        cliente.Telefono_cliente = telefonoClientedit
        cliente.Direccion = direccionClienteedit
        cliente.Tipo_cliente = tpClienteedit
        cliente.ClienteID = clientIDedit
        Dt_Cliente.actualizarCliente(cliente)
        self.listarClient()
        self.limpiarCampos()


    def eliminarClientClick(self):
        clienteIDdelete = self.txt_idCliente.text()
        cliente = Cliente()
        cliente.ClienteID = clienteIDdelete

        Dt_Cliente.eliminarCliente(cliente)
        self.listarClient()
        self.limpiarCampos()


    def limpiarCampos(self):
        self.txt_idCliente.setText("")
        self.txt_nombreCliente.setText("")
        self.txt_telefonoCliente.setText("")
        self.txt_direccionCliente.setText("")
        self.txt_tpCliente.setText("")


    def clickTablaCeldaC(self):
        # Obteniendo fila
        rowC = self.jtable_cliente.currentRow()
        # Obteniendo los valores de la tabla
        id_cliente = self.jtable_cliente.item(rowC,0).text()
        Nombre_cliente = self.jtable_cliente.item(rowC,2).text()
        Telefono_cliente = self.jtable_cliente.item(rowC, 3).text()
        Direccion_cliente = self.jtable_cliente.item(rowC, 4 ).text()
        Tipo_cliente = self.jtable_cliente.item(rowC, 5).text()

        # Se muestra en el formulario
        self.txt_idCliente.setText(id_cliente)
        self.txt_nombreCliente.setText(Nombre_cliente)
        self.txt_telefonoCliente.setText(Telefono_cliente)
        self.txt_direccionCliente.setText(Direccion_cliente)
        self.txt_tpCliente.setText(Tipo_cliente)



