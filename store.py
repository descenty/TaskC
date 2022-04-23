from dvd import *
from audio import *

class Store:
    name: str
    address: str
    audios: list
    dvds: list

    def __init__(self, name: str, address: str, audios: list, dvds: list):
        self.set_name()
        self.set_address()
        self.set_audios()
        self.dvds = dvds

    def set_name(self, name: str):
        self.name = name

    def set_address(self, address: str):
        self.address = address

    def set_audios(self, audios: list):
        self.audios = audios

    def set_dvds(self, dvds: list):
        self.dvds = dvds

    def __str__(self):
        value = '{}, {}'.format(self.name, self.address)
        value += 'Список аудиодисков: \n'
        item: Audio
        for item in self.audios:
            value += item.__str__() + '\n'
        item: DVD
        for item in self.dvds:
            value += item.__str__() + '\n'
        return value

    def __len__(self):
        return len(self.audios + self.dvds)

    def get_disk_by_index(self, index: int):
        curr = 0
        for item in self.audios:
            if curr == index:
                return item
            else:
                curr += 1
        for item in self.dvds:
            if curr == index:
                return item
            else:
                curr += 1
        return None

    def set_disk_by_index(self, index: int):
        item = self.get_disk_by_index(index)
        if type(item) is Audio:
            print("Какое поле вы хотите изменить (название, жанр, цена?")
            print
            a = input()
     #       while input() != 'q'

    # Реализовать в виде делегатов
    # https://qna.habr.com/q/237887
    properties = {'имя': set_name, 'адрес': set_address}
    #


