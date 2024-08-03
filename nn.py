class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock
        self.scores = []
    
    def average_score(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

class Products:
    def __init__(self):
        self.kalaha = []
        
    def add_product(self, product):
        self.kalaha.append(product)
    
    def search_by_name(self, name):
        tmp =  [i for i in self.kalaha if i.name == name]
        for i in tmp :
            i:Product
            print(f"name:{i.name} price:{i.price} category:{i.category} average score:{i.average_score()}")
    def search_by_price(self, min_price, max_price):
        tmp = [i for i in self.kalaha if min_price <= i.price <= max_price]
        for i in tmp :
            i:Product
            print(f"name:{i.name} price:{i.price} category:{i.category} average score:{i.average_score()}",end = "\n")
    def search_by_category(self, category):
        tmp =  [i for i in self.kalaha if i.category == category]
        for i in tmp :
            i:Product
            print(f"name:{i.name} price:{i.price} category:{i.category} average score:{i.average_score()}")
    def show_all(self):
        tmp =  self.kalaha
        for i in tmp :
            i : Product
            print(f"name:{i.name} price:{i.price} category:{i.category} average score:{i.average_score()}",end = "\n")

class Customer:
    def __init__(self):
        self.sabad_kharid = []
        self.buyed_item = []
    
    def add_to_sabad(self, name):
        pass
    def see_what_in_sabad(self):
        for i in self.sabad_kharid:
            i:Product
            print(i.name,i.category,i.price,i.average_score())
    def delete_from_sabad(self, product):
        if product in self.sabad_kharid:
            self.sabad_kharid.remove(product)
            product.stock += 1
    
    def finalize_order(self):
        self.buyed_item.extend(self.sabad_kharid)
        self.sabad_kharid = []
    
    def show_last_kharid(self):
        for i in self.buyed_item:
            i:Product
            print(i.name,i.category,i.price,i.average_score())
    def set_score_for_kharid(self, product, score):
        if product in self.buyed_item:
            if 1 <= score <= 5:
                product.scores.append(score)
            else:
                print("enter score from 1 to 5")
        else:
            print("you must buy this product first")
product1 = Product("harry potter", 100, "amozeshi", 10)
product2 = Product("pen" , 10, "books and needs", 50)
product3 = Product("lebas", 200, "poshak", 20)
product4 = Product("leili majnon", 300, "amozeshi", 30)
product5 = Product("khosro shirin", 300, "amozeshi", 30)
product6 = Product("divan of hafez", 300, "amozeshi", 30)
product7 = Product("saba", 300, "amozeshi", 30)
products = Products()
products.add_product(product1)
products.add_product(product2)
products.add_product(product3)
products.add_product(product4)
products.add_product(product5)
products.add_product(product6)
products.add_product(product7)
while True:
    print("""
    """"welcome too pishikala""""
    1. search product name
    2. search product price
    3. search product category
    4. show all products
    5. see what in cart
    6. delete from cart
    7. finalize order
    8. show last order
    9. set score for product
          """)
    n = int(input())
    if n == 1:
        tmp = input("enter product name")
        products.search_by_name(tmp)
    if n == 2 :
        tmp1,tmp2 = map(int,input("enter power of your buy a-b").split())
        products.search_by_price(tmp1,tmp2)
    if n == 3:
        tmp = input("enter product category")
        products.search_by_category(tmp)
    if n == 4:
        print("""
                here all the product aff pishikala
              """)
        products.show_all()
    



            

    
