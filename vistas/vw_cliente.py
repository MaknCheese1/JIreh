from PyQt6 import QtWidgets
from vistas import vw_frmCliente

from datos.dt_cliente import Dt_Cliente
from entidades.cliente import Cliente


class vw_listar_cliente_Widget(QtWidgets.QMainWindow,vw_frmCliente.Ui_vw_cliente):
    def __init__(self,parent=None):
        super(vw_listar_cliente_Widget,self).__init__(parent)
        self.setupUi(self)
        # LLamando datos en la tabla
        self.listarClient()
        # LLamando la clase btnGuardar
        self.btn_guardarCliente.clicked.connect(self.btnGuardarClientClick)
        # Llamando a la clase clickTable
        self.jtable_cliente.clicked.connect(self.clickTablaCeldaC)
        # Llamando a la clase limpiarCampos
        self.btn_nuevoCliente.clicked.connect(self.limpiarCampos)




    def listarClient(self):
        clientes = Dt_Cliente.listarCliente()
        indexes = len(clientes)
        self.jtable_cliente.setRowCount(indexes)
        tablerow = 0

        for row in clientes:
            self.jtable_cliente.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.ClienteID)))
            self.jtable_cliente.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.RestauranteID)))
            self.jtable_cliente.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.Nombre_cliente)))
            self.jtable_cliente.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.Telefono_cliente)))
            self.jtable_cliente.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.Direccion)))
            self.jtable_cliente.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.Tipo_cliente)))

    def btnGuardarClientClick(self):
        nombreClient = self.txt_nombreCliente.text()
        telefonoClient = self.txt_telefonoCliente.text()
        direccionCliente = self.txt_direccionCliente.text()
        tpCliente = self.txt_tpCliente.text()

        Cliente.Nombre_cliente = nombreClient
        Cliente.Telefono_cliente = telefonoClient
        Cliente.Direccion = direccionCliente
        Cliente.Tipo_cliente = tpCliente
        Dt_Cliente.guardarClient(Cliente)

    def btnActualizarClienteClick(self):
        nombreClientedit = self.txt_nombreCliente.text()
        telefonoClientedit = self.txt_telefonoCliente.text()
        direccionClienteedit = self.txt_direccionCliente.text()
        tpClienteedit = self.txt_tpCliente.text()

        Cliente.Nombre_cliente = nombreClientedit
        Cliente.Telefono_cliente = telefonoClientedit
        Cliente.Direccion = direccionClienteedit
        Cliente.Tipo_cliente = tpClienteedit
        Dt_Cliente.actualizarCliente(Cliente)


    def eliminarClientClick(self):
        Cliente.ClienteID = self.txt_idCliente.text()
        Dt_Cliente.eliminarCliente(Cliente)


    def limpiarCampos(self):
        self.txt_nombreCliente.setText("")
        self.txt_telefonoCliente.setText("")
        self.txt_direccionCliente.setText("")
        self.txt_tpCliente.setText("")


    def clickTablaCeldaC(self):
        # Obteniendo fila
        rowC = self.jtable_cliente.currentRow()
        # Obteniendo los valores de la tabla
        Nombre_cliente = self.jtable_cliente.item(rowC,2).text()
        Telefono_cliente = self.jtable_cliente.item(rowC, 3).text()
        Direccion_cliente = self.jtable_cliente.item(rowC, 4 ).text()
        Tipo_cliente = self.jtable_cliente.item(rowC, 5).text()

        # Se muestra en el formulario
        self.txt_nombreCliente.setText(Nombre_cliente)
        self.txt_telefonoCliente.setText(Telefono_cliente)
        self.txt_direccionCliente.setText(Direccion_cliente)
        self.txt_tpCliente.setText(Tipo_cliente)


