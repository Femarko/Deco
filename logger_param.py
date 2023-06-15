import os
import datetime

def logger(path):
    def __logger(old_function):
        call_count = 0
        def new_function(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            result = old_function(*args, **kwargs)
            result_str = str(result) + '\n' + '\n'
            call_time = str(datetime.datetime.now()) + '\n'
            func_name = str(old_function) + '\n'
            func_args = str([args, kwargs]) + '\n'
            file_name = 'log_' + str(call_count) + '.log'
            # current_dir = os.path.curdir()
            path_to_the_file = os.path.dirname(path)
            full_path = os.path.join(path_to_the_file, file_name)
            with open(full_path, 'a', encoding='utf-8') as log_file:
                log_file.write(call_time)
                log_file.write(func_name)
                log_file.write(func_args)
                log_file.write(result_str)
            return result
        return new_function
    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':

    test_2()