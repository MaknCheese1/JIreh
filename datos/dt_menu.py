import sys
from .conexion import Conexion
from entidades.menu import Menu

class Dt_Menu:
    _SELECT = 'SELECT * FROM JirehDB.Menu WHERE Estado <> 3'
    _INSERT = 'INSERT INTO JirehDB.Menu(RestauranteID,Nombre_menu,Descripcion,Estado) values(%s,%s,%s,1)'
    _UPDATE = 'UPDATE Menu set RestauranteID=%s,Nombre_menu=%s,Descripcion=%s where MenuID=%s'
    _DELETE = 'UPDATE Menu set Estado=3 where MenuID=%s'

    @classmethod
    def listarMenu(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        menus = []

        for x in resultado:
            m = Menu(x['MenuID'],x['RestauranteID'],x['Nombre_menu'],x['Descripcion'])
            menus.append(m)
            print('menus',menus)
        return menus

    @classmethod
    def guardarMenu(cls,menu):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Menu al insertar: {menu}')
            valores = (menu.RestauranteID,menu.Nombre_menu,menu.Descripcion)
            cursor.execute(cls._INSERT,valores)
            print(f'Menu insertado:{menu}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarMenu(cls,menu):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Menu al actualizar')
            valores = (menu.RestauranteID,menu.Nombre_menu,menu.Descripcion,menu.MenuID)
            cursor.execute(cls._UPDATE,valores)
            print(f'Actualizando Menu')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')

    @classmethod
    def eliminarMenu(cls,menu):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (menu.MenuID)
            print('Eliminando Menu')
            cursor.execute(cls._DELETE,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocuriio un error al eliminar el restaurante: {e}')
            sys.exit()








