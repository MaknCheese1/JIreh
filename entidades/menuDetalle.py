import  copy
class MenuDetalle:

    def __init__(self,Menu_detalleID=None,MenuID=None,Menu_tipoID=None,Nombre=None,Descripcion=None,Precio=None):

        self._Menu_detalleID = Menu_detalleID
        self._MenuID = MenuID
        self._Menu_tipoID = Menu_tipoID
        self._Nombre = Nombre
        self._Descripcion = Descripcion
        self._Precio = Precio

    def __str__(self):
        return  f'''
        Menu_detalleID: {self._Menu_detalleID},
        MenuID: {self._MenuID},
        Menu_tipoID: {self._Menu_tipoID},
        Nombre: {self._Nombre},
        Descripcion: {self._Descripcion},
        Precio: {self._Precio} 
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.Menu_detalleID = u._Menu_detalleID
        u.MenuID = u._MenuID
        u.Menu_tipoID = u._Menu_tipoID
        u.Nombre = u._Nombre
        u.Descripcion = u._Descripcion
        u.Precio = u._Precio

    @property
    def Menu_detalleID(self):
        return self._Menu_detalleID

    @Menu_detalleID.setter
    def Menu_detalleID(self, Menu_detalleID):
        self._Menu_detalleID = Menu_detalleID

    @property
    def MenuID(self):
        return self._MenuID

    @MenuID.setter
    def MenuID(self, MenuID):
        self._MenuID = MenuID

    @property
    def Menu_tipoID(self):
        return self._Menu_tipoID

    @Menu_tipoID.setter
    def Menu_tipoID(self, Menu_tipoID):
        self._Menu_tipoID = Menu_tipoID

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre

    @property
    def Descripcion(self):
        return self._Descripcion

    @Descripcion.setter
    def Descripcion(self, Descripcion):
        self._Descripcion = Descripcion

    @property
    def Precio(self):
        return self._Precio

    @Precio.setter
    def Precio(self, Precio):
        self._Precio = Precio

if __name__ == '__main__':
    menuDetalle1 = MenuDetalle(Nombre='Carne Asada', Descripcion='Arroz con cerveza',Precio=200.00)
    print(menuDetalle1)