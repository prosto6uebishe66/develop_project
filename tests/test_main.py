import pytest
from develop_project.config import TEST_OPERATION_PATH
from develop_project.config import OPERATION_PATH
from develop_project.src.utills import format_from_account, date_show, get_sort_transaction
from develop_project.src.main import  five_transactions, get_transaction


import pytest
from develop_project.config import OPERATION_PATH
from develop_project.src.utills import format_from_account
from develop_project.src.utills import date_show
from develop_project.src.utills import get_sort_transaction


def test_five_transactions():
  transactions = get_sort_transaction(OPERATION_PATH)
  expected_transactions = [
    {'id': 863064926},
    {'id': 114832369},
    {'id': 154927927},
    {'id': 482520625},
    {'id': 801684332},
  ]
  actual_transactions = []
  for t in transactions[:5]:
    actual_transactions.append({'id': t['id']})
  assert actual_transactions == expected_transactions
