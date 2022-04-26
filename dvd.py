from disk import *


class DVD(Disk):
    def __init__(self, name: str, genre: str = '', price: int = 0, director: str = '', company: str = '',
                 main_roles_actors: dict = None):
        Disk.__init__(self, name, genre, price)
        self.director = director
        self.properties['Режиссер'] = (self.get_director, 'self.set_director(input().strip())')

        self.company = company
        self.properties['Кинокомпания'] = (self.get_company, 'self.company = input().strip()')

        self.main_roles_actors = main_roles_actors
        self.properties['Главные роли'] = (self.get_main_roles_actors, self.change_main_roles)

    def change_main_roles(self):
        ans = ''
        while ans != '0':
            if self.main_roles_actors is not None:
                for main_role_actor in self.str_main_roles_actors():
                    print('              {}'.format(main_role_actor))
            print('1 - добавить роль, 2 - удалить роль, 0 - выйти')
            ans = input().strip()
            match ans:
                case '1':
                    print('Название роли: ', end='')
                    main_role_name = input().strip()
                    print('ФИ актера: ', end='')
                    main_role_actor = input().strip()
                    self.write_main_role(main_role_name, main_role_actor)
                case '2':
                    if self.main_roles_actors is not None:
                        print('Название роли для удаления: ', end='')
                        main_role_name = input().strip()
                        if main_role_name in self.main_roles_actors.keys():
                            self.del_main_role(main_role_name)

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

    def str_main_roles_actors(self):
        value = []
        if self.main_roles_actors is not None:
            for main_role_actor in self.main_roles_actors.items():
                value.append('{} : {}'.format(main_role_actor[0], main_role_actor[1]))
        else:
            value.append('Список ролей пуст')
        return value
