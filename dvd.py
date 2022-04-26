from disk import *


class DVD(Disk):
    def __init__(self, name: str, genre: str = '', price: int = 0, director: str = '', company: str = '',
                 main_roles_actors: dict = {}):
        Disk.__init__(self, name, genre, price)
        self.director = director
        self.properties['Режиссер'] = (self.director, 'self.set_director(input().strip())')

        self.company = company
        self.properties['Кинокомпания'] = (self.company, 'self.company = input().strip()')

        self.main_roles_actors = main_roles_actors
        self.properties['Главные роли'] = (self.main_roles_actors, self.change_main_roles)

    def change_main_roles(self):
        ans = ''
        while ans != '3':
            print('1 - добавить роль, 2 - удалить роль, 3 - выйти')
            ans = input().strip()
            match ans:
                case '1':
                    print('Название роли:')
                    main_role_name = input().strip()
                    print('ФИ актера:')
                    main_role_actor = input().strip()
                    self.write_main_role(main_role_name, main_role_actor)
                case '2':
                    print('Название роли для удаления: ')
                    main_role_name = input().strip()
                    if main_role_name in self.main_roles_actors.keys():
                        self.del_main_role(main_role_name)

    def set_director(self, director: str):
        self.director = director

    def write_main_role(self, role: str, actor: str):
        self.main_roles_actors[role] = actor

    def del_main_role(self, role: str):
        del self.main_roles_actors[role]

    def str_main_roles_actors(self):
        value = ''
        for main_role_actor in self.main_roles_actors:
            value += '{} : {}'.format(main_role_actor[0], main_role_actor[1]) + '\n'
