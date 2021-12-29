class Car(object):
    def __init__(self,modal,color,company,speedlimit):
        self.modal=modal
        self.color=color
        self.company=company
        self.speedlimit=speedlimit

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")    

    def gearchange(self):
        print("Gear Changed")

car1=Car("Fortuner","white","Toyota",180)
print(car1.start())
