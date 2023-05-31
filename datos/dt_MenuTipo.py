import sys
from .conexion import Conexion
from entidades.menuTipo import MenuTipo

class Dt_MenuTipo:
    _SELECT = 'SELECT * FROM JirehBD.MenuDetalle where estado <> 3'
    _INSERT = 'insert into JirehBD.MenuTipo(Menu_tipoID,Nombre,Descripcion,Estado) values(Menu_tipoID=%s,Nombre_=%s,Descripcion=%s,1)'
    _UPDATE = "UPDATE MenuTipo set Menu_tipoID=%s,Nombre_=%s,Descripcion=%s, where Menu_Tipo=%s"
    _DELETE = "UPDATE MenuTipo set Estado=3 where MenuDetalleID=%s"
    @classmethod
    def listarMenuDetale(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        MenuTipos= []

        for x in resultado:
            mt = MenuTipo(x['Menu_tipoID'],x['Nombre'], x['Descripcion'])
            MenuTipo.append(mt)
            print('MenuTipo', MenuTipo)
            return MenuTipo

    @classmethod
    def guardarMenuTipo(cls,MenuTipo):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuTipo al insertar: {MenuTipo}')
            valores = (MenuTipo.Menu_tipoID,MenuTipo.Nombre,MenuTipo.Descripcion)
            cursor.execute(cls._INSERT,valores)
            print(f'MenuTipo insertado: {MenuTipo}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarMenuTipo(cls,MenuTipo):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'MenuTipo Actualizar: {MenuTipo}')
            valores = (MenuTipo.Menu_tipoID,MenuTipo.Nombre,MenuTipo.Descripcion)
            cursor.execute(cls._INSERT,valores)
            print(f'Actualizando MenuTipo: {MenuTipo}')
            conexion.commit()
            return cursor.rowcount
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')



    @classmethod
    def eliminarMenuTipo(cls,MenuTipo):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (MenuTipo.Menu_tipoID)
            print('Eliminando MenuTipo')
            cursor.execute(cls._DELETE,valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocuriio un error al eliminar el Menu Tipo: {e}')
            sys.exit()



