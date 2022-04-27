import class_properties


class Disk:
    def change_property(self, property_name: str):
        class_properties.change_property(self, property_name)

    def get_name(self):
        return self.name

    def get_genre(self):
        return self.genre

    def get_price(self):
        return self.price

    def __init__(self, name='', genre='', price: int = 0):
        self.properties = {}

        self.name = name
        self.properties['Имя'] = ('name', self.get_name)

        self.genre = genre
        self.properties['Жанр'] = ('genre', self.get_genre)

        self.price = price
        self.properties['Цена'] = ('price', self.get_price)

    def __str__(self):
        props = {x[0]: x[1][1]() for x in self.properties.items() if x[0] != 'Имя' and type(x[1][1]()) in [str, int]}
        return '{} {}'.format(self.name, props)
