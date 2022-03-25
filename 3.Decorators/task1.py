
# Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.

import time

def decor(old_function):
    def new_function(a, b, c):
        print(f'Вызвана функция {old_function}')
        print(f'с аргументами {a} {b} {c}')
        result = old_function()
        print(f'получен результат {result}')
        return result
    return new_function

@decor
def summ(a=1, b=2, c=3):
    return a + b + c


if __name__ == "__main__":

    summ(1, 2, 3)

