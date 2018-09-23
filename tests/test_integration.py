import pytest

@pytest.mark.usefixtures('use_fake_timestamps')
def test_report_generation(default_store):
    s = default_store.store
    s.sell('banana', 100)
    s.buy_from_wholesale('apple', 50)
    s.sell('apple', 10)

    expected = ('time                    product  qty  unit-price\n'
                '2000-01-01 10:00:00      banana  100   1\n'
                '2000-01-01 11:00:00       apple   50   -0.6\n'
                '2000-01-01 12:00:00       apple   10   0.7')
    res = s.get_sales_report()
    assert res == expected