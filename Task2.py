import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, encoding="UTF-8")


def division(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zd:
        logging.error(f'Вы делите на ноль. Ошибка: {zd}')


if __name__ == '__main__':
    division(1, 0)
