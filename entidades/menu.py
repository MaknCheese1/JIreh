import copy
class Menu:
    def __init__(self,MenuID=None,RestauranteID=None,Nombre_menu=None,Descripcion=None):

        self._MenuID = MenuID
        self._RestauranteID = RestauranteID
        self._Nombre_menu = Nombre_menu
        self._Descripcion = Descripcion

    def __str__(self):
        return  f'''
        MenuID: {self._MenuID},
        RestauranteID: {self._RestauranteID},
        Nombre_menu: {self._Nombre_menu},
        Descripcion: {self._Descripcion}
        '''

    def __getitem__(self, item):
        u = copy.copy(self)
        u.MenuID = u._MenuID
        u.RestauranteID = u._RestauranteID
        u.Nombre_menu = u._Nombre_menu
        u.Descripcion = u._Descripcion

    @property
    def MenuID(self):
        return self._MenuID

    @MenuID.setter
    def MenuID(self, MenuID):
        self._MenuID = MenuID

    @property
    def RestauranteID(self):
        return self._RestauranteID

    @RestauranteID.setter
    def RestauranteID(self, RestauranteID):
        self._RestauranteID = RestauranteID

    @property
    def Nombre_menu(self):
        return self._Nombre_menu

    @Nombre_menu.setter
    def Nombre_menu(self, Nombre_menu):
        self._Nombre_menu = Nombre_menu

    @property
    def Descripcion(self):
        return self._Descripcion

    @Descripcion.setter
    def Descripcion(self,Descripcion):
        self._Descripcion = Descripcion

if __name__ == '__main__':
    menu1 = Menu(Nombre_menu='Bebida',Descripcion='Bebida alcoholica')
    print(menu1)


