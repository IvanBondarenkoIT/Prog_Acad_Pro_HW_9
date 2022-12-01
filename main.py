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

    @tags('b')
    def get_text(name):
        return f'Hello {name}'

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



if __name__ == '__main__':
    main()


