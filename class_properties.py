import types_input


def change_property(self, property_name: str):
    property_name = property_name.capitalize()
    value = self.properties[property_name]
    if value is not None:
        flag = True
        while flag:
            flag = False
            print(property_name + ': ', end='')
            setattr(self, value[0], types_input.input_variable(value[1]()))
    else:
        print('Поле не найдено')