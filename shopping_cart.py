class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name]['quantity'] += quantity
        else:
            self.products[name] = {'quantity': quantity, 'price': price}
        print(f'{quantity} item(s) with name {name} added')

    def remove_product(self,name):
        if name in self.products:
            del self.products[name]
        else:
            raise ValueError(f'{name} not found')
        
    def calculate_total(self):
        total = 0
        for name in self.products:
            total += self.products[name]['quantity'] * self.products[name]['price']
        return total
    
    def view_products(self):
        if not self.products:
            print('Shopping cart is empty')
        else:
            print("In shopping cart: ")
            for name,info in self.products.items():
                print(f"{info['quantity']} - {info['price']} ")



obj = ShoppingCart()
obj.add_product('Table', 1, 10000)
#obj.view_products()
obj.add_product('Chair', 3, 5000)
obj.add_product('Puff', 4, 7000)
obj.view_products()
#obj.remove_product('Chair')
#obj.view_products()
total = obj.calculate_total()
print('The total is: ', total)
