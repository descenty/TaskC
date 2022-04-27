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
                value += '         Список песен:\n'
                if audio.tracks is not None:
                    track: list(str)
                    for track in audio.str_tracks():
                        value += '              {}\n'.format(track)
        else:
            value += '      аудиодисков нету\n'
        value += '  Список фильмов:\n'
        if self.dvds is not None:
            dvd: DVD
            for dvd in self.dvds:
                value += '      ' + dvd.__str__() + '\n'
                value += '         Список главных ролей:\n'
                if dvd.main_roles_actors is not None:
                    for main_role_actor in dvd.str_main_roles_actors():
                        value += '              {0}\n'.format(main_role_actor)
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

    def get_disk_by_index(self, index: int):
        index -= 1
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

    def change_disks(self):
        print('Введите индекс диска: ', end='')
        try:
            index = int(input())
            self.set_disk_by_index(index)
        except ValueError:
            print('НЕВЕРНЫЙ ТИП ДАННЫХ')

    @staticmethod
    def set_disk(disk: Disk):
        ans = ''
        while ans != '0':
            print('Какое свойство вы хотите изменить? ', '(' + ' '.join(list(disk.properties.keys())) + ')')
            print('0 - выход')
            ans = input().strip().capitalize()
            if ans in disk.properties.keys():
                disk.change_property(ans)
            else:
                print('Свойство ({}) не найдено'.format(ans))

    def set_disk_by_index(self, index: int):
        disk = self.get_disk_by_index(index)
        if disk is None:
            print('ДИСК НЕ НАЙДЕН')
            return
        self.set_disk(disk)

    def delete_disk(self):
        print('Введите индекс диска для удаления:')
        ans = int(input()) - 1
        if ans in range(len(self)):
            disk = self.get_disk_by_index(ans)
            if type(disk) is Audio:
                self.audios.remove(disk)
            elif type(disk) is DVD:
                self.audios.remove(disk)
        else:
            print('ДИСК НЕ НАЙДЕН')

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
