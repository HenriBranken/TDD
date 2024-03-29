class Checkout:
    class Discount:
        def __init__(self, num_of_items, price):
            self.num_of_items = num_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def add_item_price(self, item, price):
        self.prices[item] = price

    def add_item(self, item):
        if item not in self.prices:
            raise Exception("Bad Item with no price!")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculate_total(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculate_item_total(item=item, count=count)
        return total

    def add_discount(self, item, num_of_items, discounted_price):
        discount = self.Discount(num_of_items=num_of_items,
                                 price=discounted_price)
        self.discounts[item] = discount

    def calculate_item_total(self, item, count):
        dummy = 0
        if item in self.discounts.keys():
            dummy += self.calculate_discounted_total(item, count,
                                                     self.discounts[item])
        else:
            dummy += self.prices[item] * count
        return dummy

    def calculate_discounted_total(self, item, count, discount):
        dummy = 0
        n_discounts = count // discount.num_of_items
        dummy += discount.price * n_discounts
        dummy += (count % discount.num_of_items) * self.prices[item]
        return dummy
