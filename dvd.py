from disk import *


class DVD(Disk):
    def __init__(self, name: str, genre: str = '', price: int = 0, director: str = '', company: str = '',
                 main_roles_actors={}):
        Disk.__init__(self, name, genre, price)
        self.director = director
        self.properties['Режиссер'] = ('director', self.get_director)

        self.company = company
        self.properties['Кинокомпания'] = ('company', self.get_company)

        self.main_roles_actors = main_roles_actors
        self.properties['Главные роли'] = ('main_roles_actors', self.get_main_roles_actors)

    def get_main_roles_actors(self):
        return self.main_roles_actors

    def set_director(self, director: str):
        self.director = director

    def get_director(self):
        return self.director

    def get_company(self):
        return self.company

    def write_main_role(self, role: str, actor: str):
        if self.main_roles_actors is None:
            self.main_roles_actors = {}
        self.main_roles_actors[role] = actor

    def del_main_role(self, role: str):
        del self.main_roles_actors[role]
        if self.main_roles_actors == {}:
            self.main_roles_actors = None

    def __str__(self):
        value = super().__str__() + ' ('
        if self.main_roles_actors is not None:
            for main_role_actor in self.main_roles_actors.items():
                value += '{} : {};'.format(main_role_actor[0], main_role_actor[1])
            value += ')'
        else:
            value += ' Список ролей пуст'
        return value
