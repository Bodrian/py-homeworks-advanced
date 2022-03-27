
# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

from time import asctime

def decor(log_path = '/log'):
    def _decor(old_function):
        def new_function(*args, **kwargs):
            print(f'Вызвана функция {old_function}')
            print(f'с аргументами {args} {kwargs}')
            result = old_function(*args, **kwargs)
            print(f'получен результат {result}')
            print(f'Время вызова {asctime()}')
            print(f'Путь к логу {log_path}')
            return result
        return new_function
    return _decor

decor_log = decor('/log1')

@decor_log
def summ(a = 1, b = 2, c = 3):
    return a + b + c


if __name__ == "__main__":

    summ(1, 2, 3)

