import copy
class Restaurante:
    def __init__(self,RestauranteID=None,Nombre_restaurante=None,Telefono_restaurante=None,
                 Correo_restaurante=None,Direccion=None,Numero_ruc=None,
                 Pagina_web=None,Estado=None):
        self._RestauranteID = RestauranteID
        self._Nombre_restaurante = Nombre_restaurante
        self._Telefono_restaurante = Telefono_restaurante
        self._Correo_restaurante = Correo_restaurante
        self._Direccion = Direccion
        self._Numero_ruc = Numero_ruc
        self._Pagina_web = Pagina_web
        self._Estado = Estado

    def __str__(self):
        return f'''
        RestauranteID: {self._RestauranteID},
        Nombre_restaurante: {self._Nombre_restaurante},
        Telefono_restaurante: {self._Telefono_restaurante},
        Correo_restaurante: {self._Correo_restaurante}
        Direccion: {self._Direccion}
        Numero_ruc: {self._Numero_ruc}
        Pagina_web: {self._Pagina_web}
        Estado: {self._Estado}
        
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.RestauranteID = u._RestauranteID
        u.Nombre_restaurante = u._Nombre_restaurante
        u.Telefono_restaurante = u._Telefono_restaurante
        u.Correo_restaurante = u._Correo_restaurante
        u.Direccion = u.Direccion
        u.Numero_ruc = u._Numero_ruc
        u.Pagina_web = u._Pagina_web
        u.Estado = u._Estado


    @property
    def RestauranteID(self):
        return self._RestauranteID

    @RestauranteID.setter
    def RestauranteID(self, RestauranteID):
        self._RestauranteID = RestauranteID

    @property
    def Nombre_restaurante(self):
        return self._Nombre_restaurante

    @Nombre_restaurante.setter
    def Nombre_restaurante(self, Nombre_restaurante):
        self._Nombre_restaurante = Nombre_restaurante

    @property
    def Telefono_restaurante(self):
        return self._Telefono_restaurante

    @Telefono_restaurante.setter
    def Telefono_restaurante(self, Telefono_restaurante):
        self._Telefono_restaurante = Telefono_restaurante

    @property
    def Correo_restaurante(self):
        return self._Correo_restaurante

    @Correo_restaurante.setter
    def Correo_restaurante(self, Correo_restaurante):
        self._Correo_restaurante = Correo_restaurante

    @property
    def Direccion(self):
        return self._Direccion

    @Direccion.setter
    def Direccion(self, Direccion):
        self._Direccion = Direccion

    @property
    def Numero_ruc(self):
        return self._Numero_ruc

    @Numero_ruc.setter
    def Numero_ruc(self, Numero_ruc):
        self._Numero_ruc = Numero_ruc

    @property
    def Pagina_web(self):
        return self._Pagina_web

    @Pagina_web.setter
    def Pagina_web(self, Pagina_web):
        self._Pagina_web = Pagina_web

    @property
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, Estado):
        self._Estado = Estado


if __name__ == '__main__':
    restaurante1 = Restaurante(Nombre_restaurante='Jireh',Telefono_restaurante='55778892',
                               Correo_restaurante='JIreh.gmail',Direccion='Metrocentro',Numero_ruc='007-23M',
                               Pagina_web='Jireh.com.ni')
    print(restaurante1)








