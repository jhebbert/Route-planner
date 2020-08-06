# A class to manage operations that do not fall directly
# under any of the other classes.


class Controller:

    # Constructor
    def __init__(self):
        self.fleet = []
        self.fleet_miles = 0

    # Brings a truck object under the controller's management
    def add_truck(self, truck):
        self.fleet.append(truck)

    # Executes the delivery process for each truck int he controller's
    # fleet.
    def run(self):
        for truck in self.fleet:
            truck.find_priority()
            truck.deliver_priority()
            while truck.packages:
                truck.move_to(truck.find_next_stop(truck.packages))
                truck.deliver_package()

    # Calculates the total miles traveled by both trucks
    def calculate_miles(self):
        miles = 0
        for truck in self.fleet:
            miles = miles + truck.miles
        return miles
