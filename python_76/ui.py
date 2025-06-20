def main_menu():
    prompt = """
        Меню:
        1. Поиск информации о книгах
        2. Поиск информации о клиентах
        0. Выход
        Выберите пункт меню (1, 2 или 0):
    """
    return int(input(prompt))


def author_name():
    return input('Введите имя автора или часть имени>>')
    
def customer_name():
    return input('Введите имя клиента или часть имени>>')


def print_table_data(data: list[tuple]):
    for items in data:
        items = map(str, items)
        print('\t| '.join(items))