import pytest
from develop_project.src.utills import format_from_account, date_show, get_sort_transaction
from develop_project.src.main import  five_transactions, get_transaction


# Моковые данные для тестирования
MOCK_TRANSACTIONS = [
  {
    "date": "2023-03-15T12:00:00.000Z",
    "description": "Перевод с карты",
    "from": {
      "account": "40817810918318571582"
    },
    "to": {
      "account": "40817810918318571583"
    },
    "operationAmount": {
      "amount": "1000.00",
      "currency": {
        "name": "RUB"
      }
    }
  },
  {
    "date": "2023-03-14T10:00:00.000Z",
    "description": "Покупка в магазине",
    "from": {
      "account": "40817810918318571582"
    },
    "to": None,
    "operationAmount": {
      "amount": "500.00",
      "currency": {
        "name": "RUB"
      }
    }
  }
]

# Тесты для get_transaction
def test_get_transaction_empty():
  assert get_transaction([]) == ''

def test_get_transaction_one_transaction():
  expected_output = "2023-03-15T12:00:00.000Z Перевод с карты\n40817810918318571582 -> 40817810918318571583\n1000.00 RUB\n"
  assert get_transaction([MOCK_TRANSACTIONS[0]]) == expected_output

def test_get_transaction_multiple_transactions():
  expected_output = "2023-03-15T12:00:00.000Z Перевод с карты\n40817810918318571582 -> 40817810918318571583\n1000.00 RUB\n2023-03-14T10:00:00.000Z Покупка в магазине\n40817810918318571582 -> \n500.00 RUB\n"
  assert get_transaction(MOCK_TRANSACTIONS) == expected_output