# You need to simulate a shopping cart in Python. This involves:
# Adding items
#   Each item has a name and a price.
#   Store these in some kind of data structure, like a dictionary or a list of tuples.
# Removing items
#   User should be able to remove an item from the cart.
#   Update the cart after removal.
# Viewing total bill
#   Calculate the sum of prices of all items in the cart.
#   Optionally, show the list of items and prices.

class shoppingCart:
    def __init__(self):
        self.cart={}
    def add_item(self,name,price):
        self.cart[name]=float(price)
        #print(self.cart)
    def remove_item(self,name):
        del self.cart[name]
        print(self.cart)
    def bill(self):
        total=0
        for p in self.cart.values():
            total +=p
        print(total)



SC=shoppingCart()
SC.add_item("orange","20.30")
SC.add_item("apple","30.30")
SC.add_item("banana","07.30")
SC.remove_item("orange")
SC.bill()


