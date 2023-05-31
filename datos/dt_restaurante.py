import sys

from .conexion import  Conexion
from entidades.restaurante import Restaurante

class Dt_Restaurante:
    _SELECT = "SELECT * FROM JirehDB.Restaurante where estado <> 3"
    _INSERT = "INSERT INTO JirehDB.Restaurante (Nombre_restaurante,Telefono_restaurante,Correo_restaurante,Direccion,Numero_ruc,Pagina_web,Estado) values (%s,%s,%s,%s,%s,%s,1)"
    _UPDATE = "UPDATE Restaurante set Nombre_restaurante=%s,Telefono_restaurante=%s,Correo_restaurante=%s,Direccion=%s,Numero_ruc=%s,Pagina_web=%s where RestauranteID=%s"
    _DELETE = "UPDATE Restaurante set Estado=3 where RestauranteID=%s"
    @classmethod
    def listarRestaurante(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        restaurantes = []

        for x in resultado:
            r = Restaurante(x['RestauranteID'], x['Nombre_restaurante'], x['Telefono_restaurante'],
                            x['Correo_restaurante'], x['Direccion'], x['Numero_ruc'], x['Pagina_web'])
            restaurantes.append(r)
            print('restaurantes', restaurantes)
        return restaurantes

    @classmethod
    def guardarRestaurante(cls, restaurante):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            print(f'Restaurante a insertar:{restaurante}')
            valores = (restaurante.Nombre_restaurante, restaurante.Telefono_restaurante, restaurante.Correo_restaurante,
                       restaurante.Direccion, restaurante.Numero_ruc, restaurante.Pagina_web)
            cursor.execute(cls._INSERT, valores)
            print(f'Restaurante insertaado: {restaurante}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarRestaurante(cls, restaurante):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            print(f'Restaurante al actualizar')
            valores = (restaurante.Nombre_restaurante, restaurante.Telefono_restaurante, restaurante.Correo_restaurante,
                       restaurante.Direccion, restaurante.Numero_ruc, restaurante.Pagina_web, restaurante.RestauranteID)
            cursor.execute(cls._UPDATE, valores)
            print(f'Actualizando restaurante')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')

    @classmethod
    def eliminarRestaurante(cls, restaurante):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:
            valores = (restaurante.RestauranteID)
            print('Eliminando Restaurante')
            cursor.execute(cls._DELETE, valores)
            print(f'Restaurante eliminado')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocuriio un error al eliminar el restaurante: {e}')
            sys.exit()




