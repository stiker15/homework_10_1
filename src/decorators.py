import functools
import logging


def log(filename=None):
    # Создаем экземпляр логгера
    logger = logging.getLogger(__name__)

    # Определяем форматер для лог-сообщений
    formatter = logging.Formatter('%(asctime)s - %(message)s')

    # Если указан filename, логи пишутся в файл, иначе в консоль
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    # Применяем форматер к обработчику
    handler.setFormatter(formatter)

    # Устанавливаем обработчик логгера
    logger.addHandler(handler)

    # Устанавливаем уровень логирования
    logger.setLevel(logging.INFO)

    def decorator(func):
        # Обертка для сохранения информации о функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)  # Выполнение самой функции
                logger.info('%s ok', func.__name__)  # Логирование успешного выполнения
                return result
            except Exception as e:
                # Логирование ошибки и параметров вызова
                logger.error('%s error: %s. Inputs: %s, %s', func.__name__, str(e), args, kwargs)
                raise
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


print(my_function(1, 1))
