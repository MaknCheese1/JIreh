import sys

from entidades.rol import Rol
from .conexion import Conexion


class DT_Rol:
    _SELECT = "SELECT * FROM JirehDB.rol"
    _INSERT = "INSERT INTO JirehDB.rol (descripcion) values (%s)"
    _UPDATE = "UPDATE JirehDB.rol set descripcion=%s where idrol=%s"
    _DELETE = "DELETE FROM JirehDB.rol where idrol=%s"
    _cursor = None

    @classmethod
    def listarRol(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        roles = []
        for z in resultado:
            a = Rol(z['idrol'], z['descripcion'])
            roles.append(a)
        print('roles', roles)
        return roles

    @classmethod
    def guardarRol(cls, rol):
        with Conexion.getConnection() as conexion:
            with Conexion.getCursor() as cursor:

                try:

                    print(f'Usuario a insertar: {rol}')
                    valores = (rol.descripcion)
                    cursor.execute(cls._INSERT, valores)
                    print(f'Rol insertado: {rol}')
                    Conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Exception {e}')
                finally:
                    cursor.close()


    @classmethod
    def actualizarRol(cls, rol):

        with Conexion.getConnection() as conexion:
            with Conexion.getCursor() as cursor:
                try:
                    valores = (rol.descripcion)
                    cursor.execute(cls._UPDATE, valores)
                    print('Actualizando rol')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Excepción al editar: {e.__traceback__}')
                finally:
                    cursor.close()

    @classmethod
    def eliminarRol(cls, rol):
        with Conexion.getConnection() as conexion:
            with Conexion.getCursor() as cursor:
                try:
                    valores = (rol.idrol)
                    print("Eliminando Rol")
                    cursor.execute(cls._DELETE,valores)
                    print("Rol eliminado")
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Ocurrió un error al eliminar el rol: {e}')
                    sys.exit()
                finally:
                    cursor.close()



if __name__ == '__main__':
    rols = DT_Rol.listarRol()
    for a in rols:
        print(a)
    #INSERTAR REGISTRO
    # usuario1 = Usuario(nombre='miguel', apellido='cervantes', nombreusuario='elQuijote', clave='123', fecha_creacion='2023-03-10')
    # insertar = DT_Usuario.guardarUsuario(usuario1)
    # print(f'Usuario insertado : {insertar}')
