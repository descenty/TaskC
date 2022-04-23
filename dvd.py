from disk import *


class DVD (Disk):
    def __init__(self, name: str, genre: str, price: int, director: str, company: str, main_roles_actors: dict):
        Disk.__init__(self, name, genre, price)
        self.director = director
        self.company = company
        self.main_roles_actors = main_roles_actors

    def set_director(self, director: str):
        self.director = director

    def write_main_role(self, role: str, actor: str):
        self.main_roles_actors[role] = actor

    def del_main_role(self, role: str):
        del self.main_roles_actors[role]

    def __str__(self):
        return '{} - {} (Жанр: {}, Кинокомпания - , Цена -  {})'.format(self.director, self.name, self.genre, self.company, self.price)


