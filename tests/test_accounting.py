from supermarket.accounting import Receipt, Cashier
import pytest


@pytest.mark.usefixtures("use_fake_timestamps")
class TestReceipt:
    def test_it_str_presentation(self):
        res = str(Receipt('milk', amount=10, price=1.2))
        assert res == '2000-01-01 10:00:00        milk   10   1.2'