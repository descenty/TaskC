from disk import *


class Audio(Disk):
    def __init__(self, name: str, genre: str = '', price: int = 0, performer: str = 'no_name', studio: str = '', tracks: dict = {}):
        Disk.__init__(self, name, genre, price)

        self.performer = performer
        self.properties['Исполнитель'] = (self.performer, 'self.performer = input().strip()')

        self.studio = studio
        self.properties['Студия звукозаписи'] = (self.studio, 'self.studio = input().strip()')

        self.tracks = tracks
        self.properties['Список песен'] = (self.tracks, self.change_tracks)

    def change_tracks(self):
        ans = ''
        while ans != '3':
            print('1 - добавить песню, 2 - удалить песню, 3 - выйти')
            ans = input().strip()
            match ans:
                case '1':
                    print('Название песни:')
                    track_name = input().strip()
                    print('Длительность (с):')
                    track_length = int(input())
                    self.add_track(track_name, track_length)
                case '2':
                    print('Название песни для удаления:')
                    track_name = input().strip()
                    self.delete_track(track_name)

    def add_track(self, track_name: str, length: int):
        self.tracks[track_name] = length

    def delete_track(self, track_name: str):
        del self.tracks[track_name]

    def str_tracks(self):
        value = ''
        if self.tracks is not None:
            for track in self.tracks:
                value += '{} : {}'.format(track[0], track[1]) + '\n'
        return value
