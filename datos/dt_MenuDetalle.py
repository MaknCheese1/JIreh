import sys
from .conexion import Conexion
from entidades.menuDetalle import MenuDetalle

class Dt_MenuDetalle:
    _SELECT = 'SELECT * FROM JirehDB.Menu_detalle WHERE estado <> 3'
    _INSERT = 'INSERT INTO JirehDB.Menu_detalle(MenuID, Menu_tipoID, Nombre, Descripcion, Precio, Estado) VALUES (%s, %s, %s, %s, %s, 1)'
    _UPDATE = "UPDATE JirehDB.Menu_detalle SET MenuID=%s, Menu_tipoID=%s, Nombre=%s, Descripcion=%s, Precio=%s WHERE Menu_detalleID=%s"
    _DELETE = "UPDATE JirehDB.Menu_detalle SET Estado=3 WHERE Menu_detalleID=%s"

    @classmethod
    def listarMenuDetalle(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        MenuDetalles = []

        for x in resultado:
            md = MenuDetalle(x['Menu_detalleID'], x['MenuID'], x['Menu_tipoID'], x['Nombre'], x['Descripcion'], x['Precio'])
            MenuDetalles.append(md)
            print('MenuDetalles', MenuDetalles)

        return MenuDetalles

    @classmethod
    def guardarMenuDetalle(cls, MenuDetalle):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuDetalle al insertar: {MenuDetalle}')
            valores = (MenuDetalle.MenuID, MenuDetalle.Menu_tipoID, MenuDetalle.Nombre, MenuDetalle.Descripcion, MenuDetalle.Precio)
            cursor.execute(cls._INSERT, valores)
            print(f'MenuDetalle insertado: {MenuDetalle}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarMenuDetalle(cls, MenuDetalle):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuDetalle al actualizar')
            valores = (MenuDetalle.MenuID, MenuDetalle.Menu_tipoID, MenuDetalle.Nombre, MenuDetalle.Descripcion,
                       MenuDetalle.Precio, MenuDetalle.Menu_detalleID)
            cursor.execute(cls._UPDATE, valores)
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
            print(f'Ocurrió un error al eliminar el MenuDetalle: {e}')
            sys.exit()
