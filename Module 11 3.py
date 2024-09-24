import sys, inspect
from pprint import pprint

class Basis:
    def __init__(self):
        self.modification = ['Ту-154', 'Ту-154А']
        self.value_of_planes = [49, 63]
        super().__init__()


def print_info(func):
    '''
    Тряхнём стариной и вспомним декоратор, так как pprint почему-то не всегда работает корректно.
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):
        info = func(*args, **kwargs)
        for key, value in info.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for val in value.items():
                    print(f'\t{val}')
            elif isinstance(value, list):
                print(f'{key}:')
                for val in value:
                    print(f'\t{val}')
            else:
                print(f'{key}: \n\t{value}')
    return wrapper

@print_info
def introspection_info(obj):
    object_info = {}
    if inspect.isfunction(obj) or inspect.isclass(obj):
        object_info.update({'Имя объекта': obj.__name__})

    if inspect.isfunction(obj) and (obj.__name__ == 'wrapper' or 'surrogate'):
        object_info.update({'Тип объекта': f'{type(obj)} (скорее всего применён декоратор.)'})
    else:
        object_info.update({'Тип объекта': type(obj)})

    if inspect.isfunction(obj) and obj.__doc__ is not None:
        object_info.update({'Комментарий к функции': obj.__doc__})

    if not isinstance(obj, (int, str, list, tuple, set, float, complex)) and not (inspect.isfunction(obj), inspect.isgenerator(obj)):
        object_info.update({'Атрибуты объекта и их значения': obj.__dict__})
    if inspect.isclass(obj):
        object_info.update({'Атрибуты объекта и методы (Класса)': [element for element in dir(obj)]})
        object_info.update({'Цепочка наследования класса': obj.__mro__})
    else:
        if '__main__' in str(type(obj)):
            object_info.update({'Атрибуты и методы объекта класса:':[element for element in dir(obj)]})
        else:
            method_list = [element for element in dir(obj) if '__' not in element]
            object_info.update({'Атрибуты объекта': method_list})
            if not method_list:
                object_info.update({'Методы объекта': 'Отсутствуют'})
            else:
                object_info.update({'Методы объекта': [element for element in dir(obj) if '__' not in element]})

    if not isinstance(obj, (int, str, list, tuple, set, float, complex)) and not inspect.isgenerator(obj):
        object_info.update({f'Объект находится в модуле': obj.__module__})
    object_info.update({'Пути к каталогам для поиска модулей': sys.path})

    return object_info

class Info(Basis):
    type_of_plane = 'Ту-154'
    def make_dict(self):
        self.dict_of_planes = {}
        for i in range(len(self.modification)):
            self.dict_of_planes.update({self.modification[i]: self.value_of_planes[i]})
        return self.dict_of_planes


# obj = introspection_info(45)
# obj = introspection_info(45.23)
# obj = introspection_info(45+6j)
# obj = introspection_info('Ratio')
# obj = introspection_info(Info)
planes = Info()
obj = introspection_info(planes)
# obj = introspection_info({1,2,54,3467,2322,'Я множество! Поклоняйтесь мне!', 342})
# obj = introspection_info([2,54, 2322,'А я список! Поклоняйтесь мне тоже!', 65])
# obj = introspection_info((2,54, 2322,'А вообще кортеж! Все поклоняйтесь только мне!', 65))
# obj = introspection_info(print_info)
# obj = introspection_info((a, a**2) for a in range(100))
# obj = introspection_info(introspection_info)
#
# pprint(obj)
# obj = Info()
# print(obj.make_dict())

















import sys, inspect
from pprint import pprint

def print_info(func):
    def wrapper(*args, **kwargs):
        info = func(*args, **kwargs)
        for key, value in info.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for val in value.items():
                    print(f'\t{val}')
            elif isinstance(value, list):
                print(f'{key}:')
                for val in value:
                    print(f'\t{val}')
            else:
                print(f'{key}: \n\t{value}')
    return wrapper

@print_info
def introspection_info(obj):
    object_info = {}
    if inspect.isfunction(obj) or inspect.isclass(obj):
        object_info.update({'Имя объекта': obj.__name__})
    if inspect.isfunction(obj) and (obj.__name__ == 'wrapper' or 'surrogate'):
        object_info.update({'Тип объекта': f'{type(obj)} (скорее всего функция-декоратор)'})
    else:
        object_info.update({'Тип объекта': type(obj)})
    if not isinstance(obj, (int, str, list, tuple, set)) and not (inspect.isfunction(obj), inspect.isgenerator(obj)):
        object_info.update({'Атрибуты объекта и их значения': obj.__dict__})
    object_info.update({'Методы объекта:': dir(obj)})
    if not isinstance(obj, (int, str, list, tuple, set)) and not inspect.isgenerator(obj):
        object_info.update({f'Объект находится в модуле': obj.__module__})
    object_info.update({'Пути к каталогам для поиска модулей': sys.path})
    return object_info

class Info:
    def __init__(self):
        self.modification = ['Ту-154', 'Ту-154А']
        self.value_of_planes = [49, 63]
    def make_dict(self):
        self.dict_of_planes = {}
        for i in range(len(self.modification)):
            self.dict_of_planes.update({self.modification[i]: self.value_of_planes[i]})
        return self.dict_of_planes


# obj = introspection_info(45)
# obj = introspection_info('Ratio')
# obj = introspection_info(Info)
obj = introspection_info({1,2,54,3467,2322,'Я множество! Поклоняйтесь мне!', 342, })
# obj = introspection_info(print_info)
# obj = introspection_info((a, a**2) for a in range(100))
# obj = introspection_info(introspection_info)

#pprint(obj)
