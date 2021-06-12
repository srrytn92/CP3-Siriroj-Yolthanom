class Vehicle:
    tag: ''
    chassis_no = ''
    def turn_on_air(self):
        print('turn on air')

class Car(Vehicle):
    color = ''
class Pickup(Vehicle):
    color = ''
class Van(Vehicle):
    color = ''
class Estate_Car(Vehicle):
    color = ''

car1 = Car()
car1.turn_on_air()
pickup1 = Pickup()
pickup1.turn_on_air()
van1 = Van()
van1.turn_on_air()
estatecar1 = Estate_Car()
estatecar1.turn_on_air()