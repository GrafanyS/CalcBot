def get_ints():
    """
    Проверка на ввод числа
    """
    while True:
        try:
            num = int(input('value = '))
            return num
        except ValueError:
            print('Ошибка. Ожидалось вещественное число.')


def test_division(x, y):
    """Проверка деление на 0 """
