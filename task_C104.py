import datetime

from logger import Logger, LogEventTypes
from store import *
import pickle

stores = []
logger = Logger('logs.txt')


def time_now():
    return datetime.datetime.now()


def manage_stores():
    global stores
    ans = ''
    while ans != '0':
        print('Магазины:')
        if len(stores) == 0:
            print("магазинов нету")
        for i in range(len(stores)):
            print(str(i + 1) + '.', stores[i].get_main_info())
        print('команды: 1 - управлять магазином, 2 - создать магазин, 3 - удалить магазин, '
              '4 - загрузить данные, 5 - сохранить данные, 0 - выйти')
        try:
            ans = input().strip()
            match ans:
                case '1':
                    print('Введите индекс магазина: ', end='')
                    ans = int(input()) - 1
                    if ans in range(len(stores)):
                        manage_store(stores[ans])
                    else:
                        print('Магазин с индексом {} не найден'.format(ans))
                case '2':
                    print('Введите название магазина: ', end='')
                    name = input().strip()
                    store = Store(name)
                    stores.append(store)
                    logger.write_event(LogEventTypes.CRE, time_now(), f"создан магазин с именем '{name}'")
                case '3':
                    print('Введите индекс магазина: ', end='')
                    ans = int(input()) - 1
                    if ans in range(len(stores)):
                        logger.write_event(LogEventTypes.INF, time_now(), f"удален магазин с "
                                                                          f"именем '{stores[ans].name}'")
                        del stores[ans]
                    else:
                        print('МАГАЗИН НЕ НАЙДЕН')
                case '4':
                    print('Введите название файла: ', end='')
                    filename = input()
                    try:
                        with open(filename, 'rb') as f:
                            stores = pickle.load(f)
                    except IOError:
                        print('FILE NOT FOUND')
                        logger.write_event(LogEventTypes.ERR, time_now(), f"не удалось найти файл '{filename}'")
                case '5':
                    print('Введите название файла: ', end='')
                    filename = input()
                    try:
                        with open(filename, 'wb') as f:
                            pickle.dump(stores, f)
                    except IOError:
                        print('FILE NOT FOUND')
                        logger.write_event(LogEventTypes.ERR, time_now(), f"не удалось найти файл '{filename}'")

        except ValueError:
            print('НЕВЕРНЫЙ ТИП ДАННЫХ')
            logger.write_event(LogEventTypes.ERR, time_now(), f'введены неверные данные')
        print()


def manage_store(store: Store):
    ans = ''
    while ans != '0':
        print('-' * 20)
        print(store)
        print('-' * 20)
        print('команды: 1 - добавить диск, 2 - изменить диск, 3 - удалить диск, 4 - изменить адрес магазина, '
              '5 - изменить имя магазина, 6 - записать в файл, 0 - выйти')
        ans = input().strip()
        match ans:
            case '1':
                print('Диск какого типа вы хотите добавить (1 - аудиодиск, 2 - фильм)')
                ans2 = input().strip()
                disk = Disk('')
                match ans2:
                    case '1':
                        disk = Audio('')
                        store += disk
                        for prop in list(disk.properties.keys()):
                            disk.change_property(prop)
                    case '2':
                        disk = DVD('')
                        store += disk
                        for prop in list(disk.properties.keys()):
                            disk.change_property(prop)
                logger.write_event(LogEventTypes.CRE, time_now(), f"в магазин '{store.name}' "
                                                                  f"добавлен новый диск '{disk.name}'")
            case '2':
                print('Введите индекс диска: ', end='')
                try:
                    index = int(input()) - 1
                    disk = store[index]
                    if disk is None:
                        print('ДИСК НЕ НАЙДЕН')
                        return
                    ans = ''
                    while ans != '0':
                        print('Какое свойство вы хотите изменить?', '(' + ' '.join(list(disk.properties.keys())) + ')')
                        print('0 - выход')
                        ans = input().strip().capitalize()
                        if ans in disk.properties.keys():
                            disk.change_property(ans)
                        else:
                            print('Свойство ({}) не найдено'.format(ans))
                except ValueError:
                    print('НЕВЕРНЫЙ ТИП ДАННЫХ')
                    logger.write_event(LogEventTypes.ERR, time_now(), f'введены неверные данные')

            case '3':
                print('Введите индекс диска для удаления:')
                ans = int(input()) - 1
                if ans in range(len(store)):
                    disk: Disk = store[ans]
                    if type(disk) is Audio:
                        store.audios.remove(disk)
                    elif type(disk) is DVD:
                        store.audios.remove(disk)
                    logger.write_event(LogEventTypes.INF, time_now(), f"из магазина '{store.name}' "
                                                                      f"удален диск с именем '{disk.name}'")
                else:
                    print('ДИСК НЕ НАЙДЕН')
            case '4':
                store.change_property('адрес')
                logger.write_event(LogEventTypes.INF, time_now(), f"изменен адрес магазина '{store.name}'")
            case '5':
                temp_name = store.name
                store.change_property('имя')
                logger.write_event(LogEventTypes.INF, time_now(), f"изменено имя магазина c "
                                                                  f"'{temp_name}' на '{store.name}'")
            case '6':
                print('Введите имя файла (.txt)')
                path = input().strip()
                store.write_txt(path)
                print('Информация записана')
                logger.write_event(LogEventTypes.INF, time_now(), f"информация о магазине '{store.name}' "
                                                                  f"выгружена в файл '{path}'")


def main():
    manage_stores()


main()
