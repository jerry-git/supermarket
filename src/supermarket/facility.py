from collections import namedtuple

from supermarket.accounting import Cashier

class NotEnoughProducts(Exception):
    pass

class ProductNotAvailable(Exception):
    pass

Product = namedtuple('Product', ['name', 'sell_price', 'buy_price'])


class Store:
    def __init__(self, cash, products_and_amounts):
        self._available_products = {p: amount for p, amount in products_and_amounts}
        self._cashier = Cashier(cash)

    @property
    def balance(self):
        return self._cashier.balance

    @property
    def available_products(self):
        return self._available_products

    def buy_from_wholesale(self, name, amount):
        product = self._get_product_by_name(name)
        self._cashier.make_purchase(product, amount)
        self.available_products[product] += amount

    def sell(self, name, amount):
        product = self._get_product_by_name(name)
        if self._available_products[product] < amount:
            raise NotEnoughProducts()

        self._cashier.add_sales(product, amount)
        self._available_products[product] -= amount

    def get_sales_report(self):
        return self._cashier.get_sales_report()

    def get_sales_excel_report(self):
        raise NotImplementedError()


    def _get_product_by_name(self, name):
        for product in self._available_products:
            if product.name == name:
                return product
        raise ProductNotAvailable(name)
