import pytest
from supermarket.facility import Store, Product
from supermarket.accounting import TIMESTAMP_FORMAT
from unittest.mock import MagicMock
from collections import namedtuple
import datetime as dt



def fake_timestamp():
    '''
    Returns timestamp strings starting from 2000-01-01 10:00:00
    Hours are increased by one every time this is called during a single test
    '''
    stamp = dt.datetime(2000,1,1,10)
    while True:
        yield stamp.strftime(TIMESTAMP_FORMAT)
        stamp += dt.timedelta(hours=1)




@pytest.fixture
def use_fake_timestamps(monkeypatch):
    mock_stamps = MagicMock(side_effect=fake_timestamp())
    monkeypatch.setattr('supermarket.accounting.Receipt._create_time_stamp', mock_stamps)

@pytest.fixture
def default_store():
    DefaultStore = namedtuple('Store', ['store', 'banana', 'apple'])
    banana = Product('banana', sell_price=1, buy_price=0.8)
    apple = Product('apple', sell_price=0.7, buy_price=0.6)
    s = Store(cash=1000, products_and_amounts=[(banana, 100), (apple, 50)])
    return DefaultStore(s, banana, apple)
