import  copy

class MenuTipo:

    def __init__(self,Menu_tipoID=None,Nombre=None,Descripcion=None,Estado=None):

        self._Menu_tipoID = Menu_tipoID
        self._Nombre = Nombre
        self._Descripcion = Descripcion
        self._Estado = Estado

    def __str__(self):
        return  f'''
        Menu_tipoID: {self._Menu_tipoID},
        Nombre: {self._Nombre},
        Descripcion: {self._Descripcion},
        Estado: {self._Estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.Menu_tipoID = u._Menu_tipoID
        u.Nombre = u._Nombre
        u.Descripcion = u._Descripcion
        u.Estado = u._Estado

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
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, Estado):
        self._Estado = Estado



if __name__ == '__main__':
    menuTipo1 = MenuTipo(Nombre='Bocadillos',Descripcion='xD')
    print(menuTipo1)