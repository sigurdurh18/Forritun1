'''
this code is sadly kek'less.
Your complaints of variable names of single letters ('a','b','c'...) and 'kek' has not gone unnoticed.
For this oppression of free variable naming it will be temporarily discontinued.
Doomed to return to plague the readers of my codes for ever more.
'''

class Vehicle(object):
    license=""
    year=int(0)
    weight=float(0)
    fee=float(0)

    def __init__(self,the_license, the_year):
        self.license=the_license
        self.year=the_year

    def set_weight(self,the_weight):
        self.weight=the_weight

    def get_weight(self):
        return self.weight

    def get_fee(self):
        return self.fee

    def get_license(self):
        return self.license

    def get_year(self):
        return self.year

    def __str__(self):
        return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.license,self.year,self.weight,self.fee)

class Car(Vehicle):
    style=""
    def __init__(self,the_license, the_year, the_style):
        Vehicle.__init__(self,the_license, the_year)
        self.style=the_style

    def set_weight(self,the_weight):
        self.weight=the_weight
        if the_weight<3000:
            self.fee=30
        elif the_weight < 5000:
            self.fee=40
        else:
            self.fee=50

    def get_style(self):
        return self.style

    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.license,self.year,self.style,self.weight,self.fee)

class Truck(Vehicle):
    wheels=int(0)
    def __init__(self,the_license, the_year, the_wheels):
        Vehicle.__init__(self,the_license, the_year)
        self.wheels=the_wheels

    def set_weight(self,the_weight):
        self.weight=the_weight
        if the_weight<3000:
            self.fee=40
        elif the_weight < 5000:
            self.fee=50
        elif the_weight < 10000:
            self.fee=60
        else:
            self.fee = 70

    def get_wheels(self):
        return self.wheels

    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.license,self.year,self.wheels,self.weight,self.fee)

class Motorbike(Vehicle):
    cc=int(0)
    def __init__(self,the_license, the_year):
        Vehicle.__init__(self,the_license, the_year)

    def set_CC(self,the_cc):
        self.cc=the_cc
        if the_cc<50:
            self.fee=10
        elif the_cc < 200:
            self.fee=20
        else:
            self.fee=35

    def get_CC(self):
        return self.cc

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.license,self.year,self.cc,self.fee)
def main():
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)
    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
    print()
    #Put the four vehicles into a list.
    # Then loop through the list and call the print function for each of the
    # vehicles.
    # You have to implement this part of the main program!
    # YOUR CODE GOES HERE
    # MY CODE STARTS
    the_garage = [v1, c1, t1, b1]
    for transport in the_garage:
        print(transport)
    # MY CODE ENDS

    v1 = c1
    print(v1)
    print()