import sys
from .conexion import Conexion
from entidades.menuDetalle import MenuDetalle

class Dt_MenuDetalle:
    _SELECT = 'SELECT * FROM JirehBD.MenuDetalle where estado <> 3'
    _INSERT = 'insert into JirehBD.MenuDetalle(MenuID,Menu_tipoID,Nombre,Descripcion,Precio,Estado) values(MenuID=%s,Menu_tipoID=%s,Nombre_=%s,Descripcion=%s,Precio=%s,1)'
    _UPDATE = "UPDATE MenuDetalle set MenuID=%s,Menu_tipoID=%s,Nombre_=%s,Descripcion=%s,Precio=%s where Menu_detalleID=%s"
    _DELETE = "UPDATE MenuDetalle set Estado=3 where MenuDetalleID=%s"
    @classmethod
    def listarMenuDetale(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        MenuDetalles= []

        for x in resultado:
            md = MenuDetalle(x['Menu_detalleID'], x['MenuID'], x['Menu_tipoID'] ,x['Nombre'], x['Descripcion'], x['Precio'])
            MenuDetalle.append(md)
            print('MenuDetalle', MenuDetalle)
            return MenuDetalle

    @classmethod
    def guardarMenuDetalle(cls,MenuDetalle):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuDetalle al insertar: {MenuDetalle}')
            valores = (MenuDetalle.MenuID,MenuDetalle.Menu_tipoID,MenuDetalle.Nombre,MenuDetalle.Descripcion,MenuDetalle.Precio)
            cursor.execute(cls._INSERT,valores)
            print(f'MenuDetalle insertado: {MenuDetalle}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarMenuDetalle(cls,MenuDetalle):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuDetalle al actualizar')
            valores = (MenuDetalle.MenuID,MenuDetalle.Menu_tipoID,MenuDetalle.Nombre,MenuDetalle.Descripcion,MenuDetalle.Precio,MenuDetalle.Menu_detalleID)
            cursor.execute(cls._UPDATE,valores)
            print(f'Actualizando MenuDetalle')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')



    @classmethod
    def eliminarMenuDetalle(cls,MenuDetalle):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (MenuDetalle.Menu_detalleID)
            print('Eliminando MenuDetalle')
            cursor.execute(cls._DELETE,valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocuriio un error al eliminar el Menu Detalle: {e}')
            sys.exit()



