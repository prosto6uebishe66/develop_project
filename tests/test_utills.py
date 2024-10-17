import json
import os
import tempfile
from datetime import datetime

import pytest
from develop_project.src.utills import date_format
from develop_project.src.utills import date_show
from develop_project.src.utills import format_from_account
from develop_project.src.utills import get_sort_transaction


#Проверка для функции `date_format`
@pytest.mark.parametrize(
    "input_date, expected_date",
    [
        ("2023-01-01T12:34:56.789", datetime(2023, 1, 1, 12, 34, 56, 789000)),
        ("2003-02-26T01:50:12.78", datetime(2003, 2, 26, 1, 50, 12, 780000)),
        ("2023-12-31T12:34:56.5", datetime(2023, 12, 31, 12, 34, 56, 500000)),
    ],
)
def test_date_format(input_date, expected_date):
    formatted_date = date_format(input_date)
    assert formatted_date == expected_date


# Проверка для функции `date_show`
def test_date_show():
    expected_result = "07.01.2023"
    result = date_show("2023-01-07T18:29:34.123")
    assert result == expected_result


# Проверка для функции `format_from_account`
def test_format_from_account():
    # Проверка №1
    result = format_from_account("Счет 86655182730188443980")
    assert result == "Счет **3980"
    #Проверка №2
    result = format_from_account("МИР 6381702861749111")
    assert result == "МИР 6381 70** **** 9111"


def test_get_sort_transaction():
    mock_data = [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T10:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2023-10-02T09:00:00.000000"},
        {"id": 3, "state": "PENDING", "date": "2023-10-03T08:00:00.000000"},
        {"id": 4, "state": "EXECUTED", "date": "2023-10-04T07:00:00.000000"},
        {"id": 5, "state": "FAILED", "date": "2023-10-05T06:00:00.000000"},
    ]

    # Создаем временный файл
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        json.dump(mock_data, temp_file)

    temp_file_path = temp_file.name

    try:
        # Вызываем тестируемую функцию
        result = get_sort_transaction(temp_file_path)

        expected_result = [
            {"id": 4, "state": "EXECUTED", "date": "2023-10-04T07:00:00.000000"},
            {"id": 2, "state": "EXECUTED", "date": "2023-10-02T09:00:00.000000"},
            {"id": 1, "state": "EXECUTED", "date": "2023-10-01T10:00:00.000000"},
        ]

        assert result == expected_result
    finally:
        # Удаляем временный файл
        os.remove(temp_file_path)
