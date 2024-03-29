import sys

from .conexion import Conexion
from entidades.usuario import Usuario


class DT_Usuario:
    _SELECT = "SELECT * FROM JirehDB.usuario where estado <> 3"
    _INSERT = "INSERT INTO JirehDB.usuario (nombre,apellido,nombreusuario,clave,fecha_creacion,estado) values (%s,%s,%s,%s,now(),1)"
    _UPDATE = "UPDATE usuario set nombre=%s,apellido=%s,nombreusuario=%s,clave=%s where idusuario=%s"
    _DELETE = "UPDATE usuario set estado=3 where idusuario=%s"
    _BUSCAR = "SELECT * FROM JirehDB.usuario where nombreusuario like %s and estado<>3"
    _cursor = None

    @classmethod
    def listarUsuario(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        usuarios = []
        for x in resultado:
            u = Usuario(x['idusuario'], x['nombre'], x['apellido'], x['nombreusuario'],
                x['clave'], x['fecha_creacion'], x['estado'])
            usuarios.append(u)
            print('usuarios', usuarios)
        return usuarios

    @classmethod
    def buscarUsuarios(cls, busqueda):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._BUSCAR, busqueda)
        resultado = cursor.fetchall()
        usuarios = []
        for x in resultado:
            u = Usuario(x['idusuario'], x['nombre'], x['apellido'], x['nombreusuario'],
                x['clave'], x['fecha_creacion'], x['estado'])
            usuarios.append(u)
            print('usuarios', usuarios)
        return usuarios

    @classmethod
    def guardarUsuario(cls, usuario):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:

            print(f'Usuario a insertar: {usuario}')
            valores = (usuario.nombre, usuario.apellido, usuario.nombreusuario, usuario.clave)
            cursor.execute(cls._INSERT, valores)
            print(f'Usuario insertado: {usuario}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')


    @classmethod
    def actualizarUsuario(cls, usuario):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            valores = (usuario.nombre, usuario.apellido, usuario.nombreusuario, usuario.clave, usuario.idusuario)
            cursor.execute(cls._UPDATE, valores)
            print('Actualizando usuario')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Excepción al editar: {e.__traceback__}')

    @classmethod
    def eliminarUsuario(cls, usuario):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            valores = (usuario.idusuario)
            print("Eliminando Usuario")
            cursor.execute(cls._DELETE,valores)
            print("Usuario eliminado")
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar el usuario: {e}')
            sys.exit()

if __name__ == '__main__':
    users = DT_Usuario.listarUsuario()
    for u in users:
        print(u)

