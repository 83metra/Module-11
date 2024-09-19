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
