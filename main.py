'''
Домашнее задание 9
1) Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.
2) Создайте декоратор, который зарегистрирует декорируемую функцию в
списке функций, для обработки последовательности.
3) Предположим, в классе определен метод __str__, который возвращает
строку на основании класса. Создайте такой декоратор для этого метода,
чтобы полученная строка сохранялась в текстовый файл, имя которого
совпадает с именем класса, метод которого вы декорировали.
4) Создайте декоратор с параметрами для проведения хронометража работы
той или иной функции. Параметрами должны выступать то, сколько раз нужно
запустить декорируемую функцию и в какой файл сохранить результаты
хронометража. Цель - провести хронометраж декорируемой функции.
'''
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

    @LogDecorator  # HW 9.4
    @tags('b')
    def get_text(name):
        return f'Hello {name}'

    @LogDecorator  # HW 9.4
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
class LogDecorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **name_args):
        self.__log_str = self.f(*args, **name_args)
        self.add_to_txt()
        return self.__log_str

    def add_to_txt(self):
        file_name = 'txt.txt' # як отримати __name__ классу?
        with open(file_name, 'a') as text_file:
            text_file.write(f"{self.__log_str}\n")
        # log = my_logger.MyLoger(__name__)
        # log.add_info(self.__log_str)


if __name__ == '__main__':
    main()


