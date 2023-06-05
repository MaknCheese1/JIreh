import sys

from entidades.usuario_rol import Usuario_Rol
from .conexion import Conexion


class DT_UsuarioRol:
    _SELECT = "SELECT * FROM JirehDB.usuario_rol"
    _INSERT = "INSERT INTO JirehDB.usuario_rol (idUsuario, idRol) values (%s,%s)"
    _DELETE = "DELETE FROM JirehDB.usuario_rol where idRol=%s, idUsuario=%s)"

    _cursor = None

    @classmethod
    def listarUsuarioRol(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        usuario_rol = []
        for ur in resultado:
            usuario_roles = Usuario_Rol(ur['idUsuarioRol'],ur['idUsuario'], ur['idRol'])
            usuario_rol.append(usuario_roles)
        print('Roles por usuario', usuario_rol)
        return usuario_rol

    @classmethod
    def asignarRol(cls, usuario_rol):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            print(f'Rol asignado: {usuario_rol.idUsuario, usuario_rol.idRol}')
            valores = (usuario_rol.idUsuario, usuario_rol.idRol)
            cursor.execute(cls._INSERT, valores)
            print(f'Rol insertado: {usuario_rol.idUsuario, usuario_rol.idRol}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')




    @classmethod
    def eliminarUsuarioRol(cls, usuario_rol):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            valores = (usuario_rol.idRol, usuario_rol.idUsuario)
            print("Eliminando Rol")
            cursor.execute(cls._DELETE,valores)
            print("Rol eliminado")
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar el rol: {e}')
            sys.exit()

if __name__ == '__main__':
    roles = DT_UsuarioRol.listarRol()
    for r in roles:
        print(r)
