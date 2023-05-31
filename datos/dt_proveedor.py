import sys
from .conexion import Conexion
from entidades.proveedor import Proveedor

class Dt_Proveedor:
    _SELECT = 'SELECT * FROM JirehDB.Proveedor where Estado <> 3'
    _INSERT ='INSERT into JirehDB.Proveedor(ProveedorID,RestauranteID,Nombre_proveedor,Telefono_proveedor,Correo_proveedor,Descripcion,Pagina_web,Estado) values(ProveedorID=%s,RestauranteID=%s,Nombre_proveedor=%s,Telefono_proveedor=%s,Correo_proveedor=%s,Descripcion=%s,Pagina_web=%s,1)'
    _UPDATE = "UPDATE Proveedor set RestauranteID=%s,Nombre_proveedor=%s,Telefono_proveedor=%s,Correo_proveedor=%s,Descripcion=%s,Pagina_web=%s where ProveedorID=%s"
    _DELETE = 'UPDATE Proveedor set Estado=3 where ProveedorID=%s'
    @classmethod
    def listarProveedor(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        proovedores = []

        for x in resultado:
            p = Proveedor(x['ProveedorID'],x['RestauranteID'],x['Nombre_proveedor'],x['Telefono_proveedor'],
                          x['Correo:proveedor'],x['Descripcion'],x['Pagina_web'])
            proovedores.append(p)
            print('proveedores',proovedores)
        return proovedores

    @classmethod
    def guardarProveedor(cls,proveedor):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Proveedor al insertar: {proveedor}')
            valores = (proveedor.ProveedorID,Proveedor.RestauranteID,proveedor.Nombre_proveedor,proveedor.Telefono_proveedor,
                       Proveedor.Correo_proveedor,Proveedor.Descripcion,proveedor.Pagina_web)
            cursor.execute(cls._INSERT,valores)
            print(f'Proveedor insertado: {proveedor}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarProveedor(cls,proveedor):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Provvedor al actualizar')
            valores = (proveedor.RestauranteID,proveedor.Nombre_proveedor,proveedor.Telefono_proveedor,Proveedor.Correo_proveedor,
                       Proveedor.Descripcion,proveedor.Pagina_web,proveedor.ProveedorID)
            cursor.execute(cls._UPDATE,valores)
            print(f'Actualizando proveedor')
            conexion.commit()
            return  cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')

    @classmethod
    def eliminarProveedor(cls,proveedor):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (proveedor.ProveedorID)
            print('Eliminando Proveedor')
            cursor.execute(cls._DELETE,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocuriio un error al eliminar el proveedor: {e}')
            sys.exit()














