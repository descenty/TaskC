from disk import *


class Audio(Disk):
    def __init__(self, name: str, genre: str, price: int, performer: str, studio: str, tracks: dict):
        Disk.__init__(self, name, genre, price)
        self.name = name
        self.genre = genre
        self.price = price
        self.performer = performer
        self.studio = studio
        self.tracks = tracks

    def add_track(self, track_name: str, length: int):
        self.tracks[track_name] = length

    def remove_track(self, track_name : str):
        del self.tracks[track_name]

    def print_tracks(self):
        for track in self.tracks:
            print('{} : {}'.format(track[0], track[1]))
            
    def __str__(self):
        return '{} - {} (Жанр: {}, Студия звукозаписи: {}) Цена: {}'.format(self.performer, self.name, self.genre, self.studio, self.price)
