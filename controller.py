from truck import Truck


class Controller:

    def __init__(self):
        self.fleet = []

    def add_truck(self, truck):
        self.fleet.append(truck)

    def run(self):
        for truck in self.fleet:
            while truck.packages:
                truck.move_to(truck.find_next_stop())
                truck.deliver_package()
