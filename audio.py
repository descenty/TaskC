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


    def add_track(self, track_name: str, length: int):
        if self.tracks is None:
            self.tracks = {}
        self.tracks[track_name] = length

    def delete_track(self, track_name: str):
        del self.tracks[track_name]

    def __str__(self):
        value = super().__str__() + ' ('
        if self.tracks is not None:
            for track in self.tracks.items():
                value += '{} : {};'.format(track[0], track[1])
            value += ')'
        else:
            value += ' Список песен пуст'
        return value
