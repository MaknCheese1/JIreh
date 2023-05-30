import sys
from .conexion import Conexion
from entidades.cliente import Cliente

class Dt_Cliente:
    _SELECT = 'SELECT * FROM JirehBD.Cliente where estado <> 3'
    _INSERT = 'insert into JirehBD.Cliente(RestauranteID,Nombre_cliente,Telefono_cliente,Direccion,Tipo_cliente,Estado) values(RestauranteID=%s,Nombre_cliente=%s,Telefono_cliente=%s,Direccion=%s,Tipo_cliente=%s,1)'
    _UPDATE = "UPDATE Cliente set RestauranteID=%s,Nombre_cliente=%s,Telefono_cliente=%s,Direccion=%s,Tipo_cliente=%s where ClienteID=%s"
    _DELETE = "UPDATE Cliente set Estado=3 where ClienteID=%s"
    @classmethod
    def listarCliente(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        clientes = []

        for x in resultado:
            c = Cliente(x['ClienteID'], x['RestauranteID'], x['Nombre_cliente'], x['Telefono_cliente'], x['Direccion'],
                        x['Tipo_cliente'])
            clientes.append(c)
            print('clientes', clientes)
            return clientes

    @classmethod
    def guardarClient(cls,cliente):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Clientes al insertar: {cliente}')
            valores = (cliente.RestauranteID,cliente.Nombre_cliente,cliente.Telefono_cliente,cliente.Direccion,
                       cliente.Tipo_cliente)
            cursor.execute(cls._INSERT,valores)
            print(f'Clientes insertado: {cliente}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarCliente(cls,cliente):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Cliente al actualizar')
            valores = (cliente.RestauranteID,cliente.Nombre_cliente,cliente.Telefono_cliente,cliente.Direccion,
                       cliente.Tipo_cliente,cliente.ClienteID)
            cursor.execute(cls._UPDATE,valores)
            print(f'Actualizando cliente')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')



    @classmethod
    def eliminarCliente(cls,cliente):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (cliente.ClienteID)
            print('Eliminando cliente')
            cursor.execute(cls._DELETE,valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocuriio un error al eliminar el restaurante: {e}')
            sys.exit()



