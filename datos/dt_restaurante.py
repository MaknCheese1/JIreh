import  sys
from .conexion import Conexion
from entidades.restaurante import Restaurante

class Dt_Restaurante:
    _SELECT = 'SELECT * FROM JirehDB.Restaurante WHERE Estado <> 3 '
    _INSERT = "INSERT INTO JirehDB.Restaurante (Nombre_restaurante,Telefono_restaurante,Correo_restaurante,Direccion,Numero_ruc,Pagina_web,Estado) values (%s,%s,%s,%s,%s,%s,1)"
    _UPDATE = "UPDATE Restaurante set Nombre_restaurante=%s,Telefono_restaurante=%s,Correo_restaurante=%s,Direccion=%s,Numero_ruc=%s,Pagina_web=%s where RestauranteID=%s"
    _DELETE = 'UPDATE JirehDB.Restaurante SET Estado=3 WHERE RestauranteID=%s '
    @classmethod
    def listarRestaurante(cls):
        cursor = Conexion.getConnection().cursor()
        cursor.execute(cls._SELECT)
        resultado = cursor.fetchall()
        Restaurantes = []

        for x in resultado:
            r = Restaurante(x['RestauranteID'],x['Nombre_restaurante'],x['Telefono_restaurante'],x['Correo_restaurante'],
                            x['Direccion'],x['Numero_ruc'],x['Pagina_web'])
            Restaurantes.append(r)
            print('Restauranntes',Restaurantes)
        return Restaurantes

    @classmethod
    def guardarRestaurante(cls, restaurante):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()
        try:

            valores = (restaurante.Nombre_restaurante, restaurante.Telefono_restaurante, restaurante.Correo_restaurante,
                       restaurante.Direccion, restaurante.Numero_ruc, restaurante.Pagina_web)
            cursor.execute(cls._INSERT, valores)
            print(f'Restaurante insertaado: {restaurante}')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception {e}')

    @classmethod
    def actualizarRestaurante(cls,Restaurante):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            print(f'Restaurante al actualizar: {Restaurante}')
            valores = (Restaurante.Nombre_restaurante, Restaurante.Telefono_restaurante, Restaurante.Correo_restaurante,
                       Restaurante.Direccion, Restaurante.Numero_ruc, Restaurante.Pagina_web, Restaurante.RestauranteID)
            cursor.execute(cls._UPDATE,valores)
            print(f'Actualizando Restaurante:   {Restaurante} ')
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Exception al editar: {e.__traceback__}')

    @classmethod
    def eliminarRestaurante(cls,Restaurante):
        cursor = Conexion.getConnection().cursor()
        conexion = Conexion.getConnection()

        try:
            valores = (Restaurante.RestauranteID,)
            print('Eliminando Restaurante')
            cursor.execute(cls._DELETE, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ocurrió un error al eliminar el Restaurante: {e}')
            sys.exit()






















