__author__ = "on line source, Sam Haakenstad"

from abc import ABCMeta, abstractmethod
class Vehicle(object):
    """A vehicle for sale by Jeffco Car Dealership.


    Attributes:
        wheels: An integer representing the number of wheels the vehicle has.
        miles: The integral number of miles driven on the vehicle.
        make: The make of the vehicle as a string.
        model: The model of the vehicle as a string.
        year: The integral year the vehicle was built.
        sold_on: The date the vehicle was sold.
    """

    __metaclass__ = ABCMeta

    base_sale_price = 0
    wheels = 0

    repairs = 0 #number of repairs starts at zero
    cost_of_repair_list = [] #assumes cost cost of repair to start is 0, but then can add costs
    date_of_repair_list = [] #starts empty because a car could never need to be repaired
    

    def __init__(self, miles, make, model, year, sold_on,repaired):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on
        self.repaired_on = repaired_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)
        
    def repair_cost(self,cost_of_repair,date_of_repair):
    """" set up local variables cost_of_repair, date_of_repair
    ... make these variables of type list so that each time 
    ... a repair occurs, the fact can be retained.""""

        self.cost_of_repair_list.add(cost_of_repair)
        self.date_of_repair_list.add(date_of_repair)
        self.repairs = self.repairs + 1
        
        total_cost = sum(cost_of_repairs_list)
            return total_cost
 
class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'
    def vehicle_size(self):
            """returns a string representing the number of passengers the vehicle can hold""""
            return '4'

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'
    def vehicle_size(self):
            """returns a string representing the number of passengers the vehicle can hold""""
            return '2'
        
class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'

    def vehicle_size(self):
            """returns a string representing the number of passengers the vehicle can hold""""
            return '1 or 2'
        
