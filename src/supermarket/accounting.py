import datetime as dt

TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S'

class NotEnoughMoney(Exception):
    pass

class Receipt:
    def __init__(self, name, price, amount):
        self._name = name
        self._price = price
        self._amount = amount
        self._time_stamp = self._create_time_stamp()

    @staticmethod
    def _create_time_stamp():
        return dt.datetime.utcnow().strftime(TIMESTAMP_FORMAT)


    def __str__(self):
        return '{}  {:>10}  {:3}   {}'.format(self._time_stamp, self._name, self._amount, self._price)


class Cashier:
    def __init__(self, balance):
        self._balance = balance
        self._receipts = []

    @property
    def balance(self):
        return self._balance

    def add_sales(self, product, amount):
        self._balance += product.sell_price * amount
        r = Receipt(product.name, product.sell_price, amount)
        self._receipts.append(r)

    def make_purchase(self, product, amount):
        if product.buy_price * amount > self.balance:
            raise NotEnoughMoney()
        r = Receipt(product.name, -product.buy_price, amount)
        self._receipts.append(r)
        self._balance -= product.buy_price * amount


    def get_sales_report(self):
        header = 'time                    product  qty  unit-price'
        receipts = '\n'.join(str(r) for r in self._receipts)
        return '\n'.join([header, receipts])
