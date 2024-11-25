def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for n in numbers:
        try:
            result += n
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {n}')
    return (result, incorrect_data)


def calculate_average(numbers):
    types = [float, int]
    try:
        numbers = list(numbers)
        digits = [i for i in numbers if type(i) in types]
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try: result = personal_sum(numbers)[0] / len(digits)
    except ZeroDivisionError:
        return 0
    return result

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
