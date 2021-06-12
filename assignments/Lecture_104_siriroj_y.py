class Customer :
    name = ''
    lastname = ''
    age = 0
    def addcart(self):
        print('add to cart',self.name,self.lastname,self.age)
customer1 = Customer()
customer1.name = 'siri'
customer1.lastname = 'yoltha'
customer1.age = 28
customer1.addcart()


customer2 = Customer()
customer2.name = 'saha'
customer2.lastname = 'weawngam'
customer2.age = 29
customer2.addcart()


customer3 = Customer()
customer3.name = 'pitchapa'
customer3.lastname = 'alampong'
customer3.age = 35
customer3.addcart()