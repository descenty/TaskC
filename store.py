from dvd import *
from audio import *
import class_properties


class Store:
    def change_property(self, property_name: str):
        class_properties.change_property(self, property_name)

    def __init__(self, name: str, address: str = '', audios: list = None, dvds: list = None, disks: list = None):
        self.properties = {}

        self.name = name
        self.properties['Имя'] = ('name', self.get_name)

        self.address = address
        self.properties['Адрес'] = ('address', self.get_address)

        self.audios = audios
        self.properties['Аудиодиски'] = ('audios', self.get_audios)

        self.dvds = dvds
        self.properties['Фильмы'] = ('dvds', self.get_dvds)

        self.disks = disks

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_audios(self):
        return self.audios

    def get_dvds(self):
        return self.dvds

    def get_main_info(self):
        return '{} ({})'.format(self.name, self.address)

    def __str__(self):
        value = '{} ({})\n'.format(self.name, self.address)
        value += '  Список аудиодисков:\n'
        if self.audios is not None:
            audio: Audio
            for audio in self.audios:
                value += '      ' + audio.__str__() + '\n'
        else:
            value += '      аудиодисков нету\n'
        value += '  Список фильмов:\n'
        if self.dvds is not None:
            dvd: DVD
            for dvd in self.dvds:
                value += '      ' + dvd.__str__() + '\n'
        else:
            value += '      фильмов нету'
        return value

    def __len__(self):
        value = 0
        if self.audios is not None:
            value += len(self.audios)
        if self.dvds is not None:
            value += len(self.dvds)
        return value

    def __getitem__(self, index):
        curr = 0
        if self.audios is not None:
            for item in self.audios:
                if curr == index:
                    return item
                else:
                    curr += 1
        if self.dvds is not None:
            for item in self.dvds:
                if curr == index:
                    return item
                else:
                    curr += 1
        return None

    def __setitem__(self, key, value):
        self[key] = value

    def __add__(self, other):
        if type(other) is Audio:
            if self.audios is None:
                self.audios = []
            self.audios.append(other)
        elif type(other) is DVD:
            if self.dvds is None:
                self.dvds = []
            self.dvds.append(other)
        return self

    def __sub__(self, other):
        if type(other) is Audio:
            self.audios.remove(other)
        elif type(other) is DVD:
            self.audios.remove(other)
        return self

    def write_txt(self, path: str):
        f = open(path + '.txt', 'w')
        f.write(self.__str__())
        f.close()
