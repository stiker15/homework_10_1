import pytest
from io import StringIO
import logging


def error_function(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        logger = logging.getLogger('decorators')
        logger.error(f"error_function error: {e}")
        raise


# Тест для случая с ошибкой
def test_error_function_with_error():
    log_stream = StringIO()
    handler = logging.StreamHandler(log_stream)
    logger = logging.getLogger('decorators')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)

    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)

    handler.flush()
    log_contents = log_stream.getvalue()
    handler.close()
    logger.removeHandler(handler)

    assert "error_function error: division by zero" in log_contents


# Тест для случая без ошибки
def test_error_function_without_error():
    result = error_function(4, 2)
    assert result == 2

    # Логирование успешного результата в mylog.txt
    log_file = 'mylog.txt'
    file_handler = logging.FileHandler(log_file)
    logger = logging.getLogger('decorators')
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    logger.info(f"Successful result: {result}")

    file_handler.close()
    logger.removeHandler(file_handler)

    # Проверка наличия записи в файле
    with open(log_file, 'r') as f:
        log_contents = f.read()

    assert "Successful result: 2" in log_contents
