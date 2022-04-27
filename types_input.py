
def input_variable(variable) -> object:
    while True:
        try:
            if type(variable) is str:
                return input().strip()
            elif type(variable) is int:
                return int(input())
            elif type(variable) is list:
                variable: list
                ans = ''
                while ans != '0':
                    print('1 - добавить элемент, 2 - удалить элемент по индексу, 0 - выйти')
                    ans = input().strip()
                    match ans:
                        case '1':
                            print("Новый элемент: ", end='')
                            variable.append(input().strip())
                        case '2':
                            print('Индекс: ', end='')
                            index = int(input())
                            del variable[index]
                return variable
            elif type(variable) is dict:
                variable: dict
                ans = ''
                while ans != '0':
                    print('1 - добавить ключ, 2 - удалить ключ, 0 - выйти')
                    ans = input().strip()
                    match ans:
                        case '1':
                            print("Ключ: ", end='')
                            key = input().strip()
                            print('Значение: ', end='')
                            value = input().strip()
                            variable[key] = value
                        case '2':
                            print('Ключ: ', end='')
                            key = input().strip()
                            del variable[key]
                    return variable
            else:
                raise TypeError
        except ValueError:
            print('НЕВЕРНЫЙ ТИП ДАННЫХ')
        except TypeError:
            print('ДАННЫЙ ТИП ДАННЫХ НЕ ПОДДЕРЖИВАЕТСЯ')
            break
