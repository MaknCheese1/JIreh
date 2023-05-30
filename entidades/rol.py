import  copy

class Rol:
    def __init__(self,RolID=None,Rol_nombre=None,Estado=None):
        self._RolID = RolID
        self._Rol_nombre = Rol_nombre
        self._Estado = Estado

    def __str__(self):
        return f'''
        RolID: {self._RolID},
        Rol_nombre: {self._Rol_nombre},
        Estado: {self._Estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.RolID = u._RolID
        u.Rol_nombre = u._Rol_nombre
        u.Estado = u._Estado

    @property
    def RolID(self):
        return self._RolID

    @RolID.setter
    def RolID(self, RolID):
        self._RolID = RolID

    @property
    def Rol_nombre(self):
        return self._Rol_nombre

    @Rol_nombre.setter
    def Rol_nombre(self, Rol_nombre):
        self._Rol_nombre = Rol_nombre

    @property
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, Estado):
        self._Estado = Estado


if __name__ == '__main__':
    rol1 = Rol(Rol_nombre='Cajero')
    print(rol1)