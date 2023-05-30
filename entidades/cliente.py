import  copy
class Cliente:
    def __init__(self,ClienteID=None,RestauranteID=None,Nombre_cliente=None,
                 Telefono_cliente=None,Direccion=None,Tipo_cliente=None,
                 Estado=None):
        self._ClienteID=ClienteID
        self._RestauranteID=RestauranteID
        self._Nombre_cliente=Nombre_cliente
        self._Telefono_cliente=Telefono_cliente
        self._Direccion=Direccion
        self._Tipo_cliente=Tipo_cliente
        self._Estado=Estado

    def __str__(self):
        return f'''
        ClienteID:{self._ClienteID},
        RestauranteID: {self._RestauranteID},
        Nombre_cliente: {self._Nombre_cliente},
        Telefono_cliente: {self._Telefono_cliente}
        Direccion: {self._Direccion}
        Tipo_Cliente: {self._Tipo_cliente}
        Estado: {self._Estado}
        
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.ClienteID = u._ClienteID
        u.RestauranteID = u._RestauranteID
        u.Nombre_cliente = u._Nombre_cliente
        u.Telefono_cliente = u._Telefono_cliente
        u.Direccion = u._Direccion
        u.Tipo_cliente = u._Tipo_cliente
        u.Estado = u._Estado
        return u

    @property
    def ClienteID(self):
        return self._ClienteID

    @ClienteID.setter
    def ClienteID(self,ClienteID):
        self._ClienteID=ClienteID

    @property
    def RestauranteID(self):
        return self._RestauranteID

    @RestauranteID.setter
    def RestauranteID(self, RestauranteID):
        self._RestauranteID = RestauranteID

    @property
    def Nombre_cliente(self):
        return self._Nombre_cliente

    @Nombre_cliente.setter
    def Nombre_cliente(self, Nombre_cliente):
        self._Nombre_cliente = Nombre_cliente

    @property
    def Telefono_cliente(self):
        return self._Telefono_cliente

    @Telefono_cliente.setter
    def Telefono_cliente(self,Telefono_cliente):
        self._Telefono_cliente = Telefono_cliente

    @property
    def Direccion(self):
        return self._Direccion

    @Direccion.setter
    def Direccion(self, Direccion):
        self._Direccion = Direccion

    @property
    def Tipo_cliente(self):
        return self._Tipo_cliente

    @Tipo_cliente.setter
    def Tipo_cliente(self, Tipo_cliente):
        self._Tipo_cliente = Tipo_cliente

    @property
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, Estado):
        self._Estado = Estado



if __name__ == '__main__':
    cliente1  = Cliente(Nombre_cliente='Freedman Rodriguez',Telefono_cliente='77470702',Direccion='Monimbo',Tipo_cliente='Compra frecuente')
    print(cliente1)
