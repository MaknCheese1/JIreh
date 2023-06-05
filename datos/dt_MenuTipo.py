import sys
from .conexion import Conexion
from entidades.menuTipo import MenuTipo

class Dt_MenuTipo:
    _SELECT = 'SELECT * FROM JirehDB.Menu_tipo WHERE Estado <> 3'
    _INSERT = 'INSERT INTO JirehDB.Menu_tipo(Menu_tipoID, Nombre, Descripcion, Estado) VALUES (%s, %s, %s, 1)'
    _UPDATE = "UPDATE JirehDB.Menu_tipo SET Menu_tipoID=%s, Nombre=%s, Descripcion=%s WHERE Menu_tipoID=%s"
    _DELETE = "UPDATE JirehDB.Menu_tipo SET Estado=3 WHERE Menu_tipoID=%s"

    @classmethod
    def listarMenuTipo(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        MenuTipos = []

        for x in resultado:
            mt = MenuTipo(x['Menu_tipoID'], x['Nombre'], x['Descripcion'])
            MenuTipos.append(mt)
            print('MenuTipos', MenuTipos)

        return MenuTipos

    @classmethod
    def guardarMenuTipo(cls, MenuTipo):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuTipo al insertar: {MenuTipo}')
            valores = (MenuTipo.Menu_tipoID, MenuTipo.Nombre, MenuTipo.Descripcion)
            cursor.execute(cls._INSERT, valores)
            print(f'MenuTipo insertado: {MenuTipo}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarMenuTipo(cls, MenuTipo):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuTipo al actualizar: {MenuTipo}')
            valores = (MenuTipo.Menu_tipoID, MenuTipo.Nombre, MenuTipo.Descripcion, MenuTipo.Menu_tipoID)
            cursor.execute(cls._UPDATE, valores)
            print(f'Actualizando MenuTipo: {MenuTipo}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')

    @classmethod
    def eliminarMenuTipo(cls, MenuTipo):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (MenuTipo.Menu_tipoID,)
            print('Eliminando MenuTipo')
            cursor.execute(cls._DELETE, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrió un error al eliminar el Menu Tipo: {e}')
            sys.exit()
