import pytest
from supermarket.facility import Store, Product
from unittest.mock import MagicMock
from collections import namedtuple


@pytest.fixture
def use_fake_timestamps(monkeypatch):
    fake_stamps = ['2000-01-01 10:00:00', '2000-01-01 11:00:00', '2000-01-01 12:00:00']
    mock_stamps = MagicMock(side_effect=fake_stamps)

    monkeypatch.setattr('supermarket.accounting.Receipt._create_time_stamp', mock_stamps)

@pytest.fixture
def default_store():
    DefaultStore = namedtuple('Store', ['store', 'banana', 'apple'])
    banana = Product('banana', sell_price=1, buy_price=0.8)
    apple = Product('apple', sell_price=0.7, buy_price=0.6)
    s = Store(cash=1000, products_and_amounts=[(banana, 100), (apple, 50)])
    return DefaultStore(s, banana, apple)
