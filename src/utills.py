import os

from develop_project.config import ROOT_DIR

"""
Функция считывает данные из json
"""


def read_data():
    OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'operation.json')


"""

Функция фильтрует executed 
из полученного списка и
далее использует только эти данные

"""


def filter_executed():
    ...

    """

    Функция фильтрует данные по датам 
    и сортирует их от старого к новому


    """


def picking_data():
    ...

    """

    Функция возвращает 
    последние 5 полученных данных 

    """


def use_last_five():
    ...

    """

    Функция показывает результат 


    """


def show_result():
    format_operation = ...

    print(f"{format_operation}")
