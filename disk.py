class Disk:
    def __init_properties__(self):
        self.properties = {
            'Имя': (self.name, 'self.name = input().strip()'),
            'Жанр': (self.genre, 'self.genre = input().strip()'),
            'Цена': (self.price, 'self.price = int(input())'),
        }

    def __init__(self, name: str, genre: str = '', price: int = 0):
        self.name = name
        self.genre = genre
        self.price = price
        self.__init_properties__()

    def change_property(self, property_name: str):
        property_name = property_name.capitalize()
        value = self.properties[property_name]
        if value is not None:
            flag = True
            while flag:
                flag = False
                print(property_name + ': ', end='')
                try:
                    if type(value[1]) is str:
                        exec(value[1])
                    else:
                        value[1]()
                except ValueError:
                    print('Неправильный тип данных')
                    flag = True
        else:
            print('Поле не найдено')

    def __str__(self):
        props = {x[0]: x[1][0] for x in self.properties.items() if x[0] != 'Имя' and type(x[1][0]) is str}
        return '{} {}'.format(self.name, props)
