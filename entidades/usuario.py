import copy

class Usuario:
    def __init__(self,UsuarioID=None,RolID=None,Nombre_usuario=None,Clave=None,Estado=None):

        self._UsuarioID = UsuarioID
        self._RolID = RolID
        self._Nombre_usuario = Nombre_usuario
        self._Clave = Clave
        self._Estado = Estado

    def __str__(self):
        return f'''
        UsuarioID: {self._UsuarioID},
        RolID: {self._RolID},
        Nombre_usuario: {self._Nombre_usuario},
        Clave: {self._Clave},
        Estado: {self._Estado}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.UsuarioID = u._UsuarioID
        u.RolID = u._RolID
        u.Nombre_usuario = u._Nombre_usuario
        u.Clave = u._Clave
        u.Estado = u._Estado

    @property
    def UsuarioID(self):
        return self._UsuarioID

    @UsuarioID.setter
    def UsuarioID(self, UsuarioID):
        self._UsuarioID = UsuarioID

    @property
    def RolID(self):
        return self._RolID

    @RolID.setter
    def RolID(self, RolID):
        self._RolID = RolID

    @property
    def Nombre_usuario(self):
        return self._Nombre_usuario

    @Nombre_usuario.setter
    def Nombre_usuario(self, Nombre_usuario):
        self._Nombre_usuario = Nombre_usuario

    @property
    def Clave(self):
        return self._Clave

    @Clave.setter
    def Clave(self, Clave):
        self._Clave = Clave

    @property
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, Estado):
        self._Estado = Estado

if __name__ == '__main__':
    usuario1 = Usuario(Nombre_usuario='Freedman',Clave='freedgt5')
    print(usuario1)
