import  copy
class Proveedor:
    def __init__(self,ProveedorID=None,RestauranteID=None,Nombre_proveedor=None,Telefono_proveedor=None,
                 Correo_proveedor=None,Descripcion=None,Pagina_web=None):

        self._ProveedorID = ProveedorID
        self._RestauranteID = RestauranteID
        self._Nombre_proveedor = Nombre_proveedor
        self._Telefono_proveedor = Telefono_proveedor
        self._Correo_proveedor = Correo_proveedor
        self._Descripcion = Descripcion
        self._Pagina_web = Pagina_web

    def __str__(self):
        return f'''
        ProveedorID: {self._ProveedorID},
        RestauranteID: {self._RestauranteID},
        Nombre_proveedor: {self._Nombre_proveedor},
        Telefono_proveedor: {self._Telefono_proveedor},
        Correo_proveedor: {self._Correo_proveedor},
        Descripcion: {self._Descripcion},
        Pagina_web: {self._Pagina_web}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.ProveedorID = u._ProveedorID
        u.RestauranteID = u._RestauranteID
        u.Nombre_proveedor = u._Nombre_proveedor
        u.Telefono_proveedor = u._Telefono_proveedor
        u.Correo_proveedor = u._Correo_proveedor
        u.Descripcion = u._Descripcion
        u.Pagina_web = u._Pagina_web

    @property
    def ProveedorID(self):
        return self._ProveedorID

    @ProveedorID.setter
    def ProveedorID(self, ProveedorID):
        self._ProveedorID = ProveedorID

    @property
    def RestauranteID(self):
        return self._RestauranteID

    @RestauranteID.setter
    def RestauranteID(self, RestauranteID):
        self._RestauranteID = RestauranteID

    @property
    def Nombre_proveedor(self):
        return self._Nombre_proveedor

    @Nombre_proveedor.setter
    def Nombre_proveedor(self, Nombre_proveedor):
        self._Nombre_proveedor = Nombre_proveedor

    @property
    def Telefono_proveedor(self):
        return self._Telefono_proveedor

    @Telefono_proveedor.setter
    def Telefono_proveedor(self, Telefono_proveedor):
        self._Telefono_proveedor = Telefono_proveedor

    @property
    def Correo_proveedor(self):
        return self._Correo_proveedor

    @Correo_proveedor.setter
    def Correo_proveedor(self, Correo_proveedor):
        self._Correo_proveedor = Correo_proveedor

    @property
    def Descripcion(self):
        return self._Descripcion

    @Descripcion.setter
    def Descripcion(self, Descripcion):
        self._Descripcion = Descripcion

    @property
    def Pagina_web(self):
        return self._Pagina_web

    @Pagina_web.setter
    def Pagina_web(self, Pagina_web):
        self._Pagina_web = Pagina_web


if __name__ == '__main__':
    proveedor1 = Proveedor(Nombre_proveedor='Cainsa',Telefono_proveedor='88557892',Correo_proveedor='Cansa.gmail',
                           Descripcion='Embutidos',Pagina_web='Cainsa.com')
    print(proveedor1)