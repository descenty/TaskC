from disk import *


class Audio(Disk):
    def __init__(self, name='', genre='', price=0, performer='', studio='',
                 tracks={}):
        Disk.__init__(self, name, genre, price)

        self.performer = performer
        self.properties['Исполнитель'] = ('performer', self.get_performer)

        self.studio = studio
        self.properties['Студия звукозаписи'] = ('studio', self.get_studio)

        self.tracks = tracks
        self.properties['Список песен'] = ('tracks', self.get_tracks)

    def get_performer(self):
        return self.performer

    def get_studio(self):
        return self.studio

    def get_tracks(self):
        return self.tracks

    def change_tracks(self):
        ans = ''
        while ans != '0':
            if self.tracks is not None:
                for track in self.str_tracks():
                    print('              {}'.format(track))
            print('1 - добавить песню, 2 - удалить песню, 0 - выйти')
            ans = input().strip()
            match ans:
                case '1':
                    print('Название песни: ', end='')
                    track_name = input().strip()
                    print('Длительность (с): ', end='')
                    track_length = int(input())
                    self.add_track(track_name, track_length)
                case '2':
                    print('Название песни для удаления: ', end='')
                    track_name = input().strip()
                    self.delete_track(track_name)

    def add_track(self, track_name: str, length: int):
        if self.tracks is None:
            self.tracks = {}
        self.tracks[track_name] = length

    def delete_track(self, track_name: str):
        del self.tracks[track_name]

    def str_tracks(self):
        value = []
        if self.tracks is not None:
            for track in self.tracks.items():
                value.append('{} : {}'.format(track[0], track[1]))
        else:
            value.append('Список песен пуст')
        return value
