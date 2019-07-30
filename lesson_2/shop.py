class Shop:

    _sold = 0

    @classmethod
    def get_total_sold(self):
        return Shop._sold

    def __init__(self, name, sold):
        self.name = name
        self.sold = sold
        Shop._sold += self.sold
    
    def sell(self, qty=1):
        print("Sell {}".format(qty))
        self.sold += qty
        Shop._sold += qty

    def show_sold(self):
        return self.sold
    
    def show_total_sold(self):
        return Shop._sold

shop1 = Shop("Shop 1", 10)
shop2 = Shop("Shop 2", 20)
shop3 = Shop("Shop 3", 30)

shop1.sell(5)
shop2.sell(7)
shop3.sell(1)

print(shop1.show_sold())
print(shop1.show_total_sold())
Shop.get_total_sold()
        
