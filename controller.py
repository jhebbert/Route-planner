from truck import Truck


class Controller:

    def __init__(self):
        self.fleet = []
        self.fleet_miles = 0

    def add_truck(self, truck):
        self.fleet.append(truck)

    def run(self):
        for truck in self.fleet:
            truck.find_priority()
            truck.deliver_priority()
            while truck.packages:
                truck.move_to(truck.find_next_stop(truck.packages))
                truck.deliver_package()

    def calculate_miles(self):
        miles = 0
        for truck in self.fleet:
            miles = miles + truck.miles
        return miles
