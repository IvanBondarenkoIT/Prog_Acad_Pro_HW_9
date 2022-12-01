# Домашнее задание 9
# 1) Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.
# 2) Создайте декоратор, который зарегистрирует декорируемую функцию в
# списке функций, для обработки последовательности.

import time
import my_logger


def main():

    func_list = []  # HW 9.2

    def tags(tag):
        def decorator(func):
            count = 0  # HW 9.1

            def inner(*args, **kwargs):
                nonlocal count  # HW 9.1
                count += 1  # HW 9.1
                func_list.append(func)  # HW 9.2
                return f'<{tag}>{func(*args, **kwargs)}</{tag}> cnt:{count}'
            return inner
        return decorator

    @LogDecorator  # HW 9.3 test
    @tags('b')
    def get_text(name):
        return f'Hello {name}'

    @LogDecorator  # HW 9.3 test
    @tags('i')
    def get_text_1(name):
        return f'Hello {name}'

    print(get_text('Ivan'))
    print(get_text('Ivan'))
    print(get_text('Ivan'))

    print(get_text_1('Ivan'))
    print(get_text_1('Ivan'))

    for item in func_list:
        print(item)  # HW 9.2

# HW 9.4
# 4) Создайте декоратор с параметрами для проведения хронометража работы
# той или иной функции. Параметрами должны выступать то, сколько раз нужно
# запустить декорируемую функцию и в какой файл сохранить результаты
# хронометража. Цель - провести хронометраж декорируемой функции.
    def chrono(qty_lunches, file_name):
        def decorator(func):
            start = 0
            end = 0

            def inner(*args, **kwargs):
                nonlocal start, end
                start = time.time()
                for i in range(qty_lunches):
                    func(*args, **kwargs)
                end = time.time()
                log = my_logger.MyLoger(file_name)
                log.add_info(f"start:{start} - finish:{end}")
            return inner

        return decorator

    @chrono(qty_lunches=100, file_name='my_log_file')
    def get_text3():
        return 'Hello!'

    get_text3()


# HW 9.3
# 3) Предположим, в классе определен метод __str__, который возвращает
# строку на основании класса. Создайте такой декоратор для этого метода,
# чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.
class LogDecorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **name_args):
        self.__log_str = self.f(*args, **name_args)
        self.add_to_txt()
        return self.__log_str

    def add_to_txt(self):
        file_name = 'txt.txt'  # як отримати __name__ классу?
        with open(file_name, 'a') as text_file:
            text_file.write(f"{self.__log_str}\n")


if __name__ == '__main__':
    main()

