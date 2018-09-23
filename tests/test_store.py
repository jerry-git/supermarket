

def test_sell(default_store):
    s = default_store.store
    s.sell('banana', 10)
    assert s.balance == 1010
    assert s.available_products[default_store.banana] == 90



def test_buy_from_wholesale(default_store):
    s = default_store.store
    s.buy_from_wholesale('banana', 15)
    assert s.balance == 988
    assert s.available_products[default_store.banana] == 115





