import  copy

class Rol:
    def __init__(self,idrol=None,descripcion=None):
        self._RolID = idrol
        self._Rol_nombre = descripcion


    def __str__(self):
        return f'''
        idrol: {self._RolID},
        descripcion: {self._Rol_nombre},
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.idrol = u._RolID
        u.descripcion = u._Rol_nombre


    @property
    def idrol(self):
        return self._RolID

    @idrol.setter
    def idrol(self, idrol):
        self._RolID = idrol

    @property
    def descripcion(self):
        return self._Rol_nombre

    @descripcion.setter
    def descripcion(self, descripcion):
        self._Rol_nombre = descripcion


if __name__ == '__main__':
    rol1 = Rol(descripcion='Cajero')
    print(rol1)