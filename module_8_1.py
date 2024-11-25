def add_everything_up(a, b):
    types = [int, float, str]
    if type(a) in types and type(b) in types:
        try:
            result = a + b
        except TypeError as exc:
            result = f'{a}{b}'
        finally:
            return result
    else:
        return 'a и b должны быть строками, целыми или дробными числами!'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(False, 7))