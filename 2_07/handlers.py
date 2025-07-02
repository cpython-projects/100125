from log_exceptions import log_error


@log_error(False)
def handler_search_by_category(keyword: str):
    """

    :param keyword:
    :return: 
    """
    res = f'Serach by {keyword}'
    return res


@log_error(True)
def handler_search_by_years(start: int, stop: int):
    """

    :param start:
    :param stop:
    :return:
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError('Дорогой пользователь! Когда вводишь года - используй положительные целые числа!')
    res = range(start, stop + 1)
    return res
