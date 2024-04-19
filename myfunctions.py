"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""

#   Функция создает красивый резделитель из 10-и звездочек (**********)
#    :return: **********


def simple_separator():
    separator = "*" * 10
    return separator
    pass

print(simple_separator() == '**********')  # True


#    Функция создает разделитель из звездочек число которых можно регулировать параметром count
#    :param count: количество звездочек
#    :return: строка разделитель, примеры использования ниже


def long_separator(count):
    separator = "*" * count
    return separator
    pass

# Пример использования функции

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
    separator = simbol * count
    return separator
    pass

#    """
#    Функция создает разделитель из любых символов любого количества
#    :param simbol: символ разделителя
#    :param count: количество повторений
#    :return: строка разделитель примеры использования ниже
#    """


# Пример использования функции

print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    separator = "*" * 10
    greeting = "Hello World!"
    underline = "#" * 10

    print(separator)  # Печатаем верхний разделитель
    print()           # Печатаем пустую строку
    print(greeting)   # Печатаем приветствие "Hello World!"
    print()           # Печатаем пустую строку
    print(underline)  # Печатаем нижний разделитель
    pass
    # Вызов функции для печати Hello World в указанном формате
hello_world()

#    """
#    Функция печатает Hello World в формате:
#    **********

#    Hello World!

#    ##########
#    :return: None
#    """



'''
**********

Hello World!

##########
'''
hello_world()


def hello_who(who='World'):
    """
    Функция печатает приветствие в красивом формате
    **********

    Hello {who}!

    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
    pass

def hello_who(who="World"):
    separator = "*" * 10
    greeting = f"Hello {who}!"
    underline = "#" * 10

    print(separator)
    print()
    print(greeting)
    print()
    print(underline)
    pass

hello_who(who="P0ll")


'''
**********

Hello World!

##########
'''
hello_who()
'''
**********

Hello Max!

##########
'''
hello_who('Max')
'''
**********

Hello Kate!

##########
'''
hello_who('Kate')


#def pow_many(power, *args):
#    """
#    Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
#    :param power: степень
#    :param args: любое количество цифр
#    :return: результат вычисления # True -> (1 + 2)**1
#    """


def pow_many(power, *args):
    total = sum(args)
    result = total ** power
    return result
    pass

print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


#def print_key_val(**kwargs):
#    """
#    Функция выводит переданные параметры в виде key --> value
#    key - имя параметра
#    value - значение параметра
#    :param kwargs: любое количество именованных параметров
#    :return: None
#    """
#    pass

def print_key_val(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} --> {value}")
    pass

"""
name --> Max
age --> 21
"""
print_key_val(name='Max', age=21)
"""
animal --> Cat
is_animal --> True
"""
print_key_val(animal='Cat', is_animal=True)


#def my_filter(iterable, function):
#    """
#    (Усложненое задание со *)
#    Функция фильтрует последовательность iterable и возвращает новую
#    Если function от элемента последовательности возвращает True, то элемент входит в новую последовательность иначе нет
#    (примеры ниже)
#    :param iterable: входаня последовательности
#    :param function: функция фильтрации
#    :return: новая отфильтрованная последовательность
#    """
#    pass

def my_filter(iterable, function):
    return [element for element in iterable if function(element)]
    pass

print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
