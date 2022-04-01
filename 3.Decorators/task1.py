from time import asctime

def decor(log_path):
    def _decor(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(f'{log_path}log.txt', 'a', encoding='UTF-8') as f:
                f.write(f'Вызвана функция: {old_function}\nC аргументами: {args} {kwargs}\n'
                        f'Получен результат: {result}\nВремя вызова: {asctime()}\nПуть к логу: {log_path}')
            return result
        return new_function
    return _decor

decor_log = decor('log1/')

@decor_log # task1 + task2
def summ(a, b, c):
    return a + b + c

if __name__ == "__main__":

    summ(1, 2, 3)

