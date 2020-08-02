from location import Location


class Truck:
    def __init__(self, location, possible_locations):
        self.packages = []
        self.miles = 0
        self.location = location
        self.possible_locations = possible_locations

    def set_location(self, address):
        for location in self.possible_locations:
            if location.address == address:
                self.location = location

    def add_parcel(self, parcel):
        self.packages.append(parcel)

    def __str__(self):
        return str(self.__dict__)

    def print_contents(self):
        for parcel in self.packages:
            print(parcel)

    def deliver_package(self):
        i = 0
        for parcel in self.packages:
            if self.location.address == parcel.address:
                parcel.delivered = True
                self.packages.pop(i)
                print(parcel.delivered)
            i = i + 1
        if not self.packages:
            print('Empty')

    def move_to(self, address):
        dist_traveled = self.location.distance_dic.get(address)
        self.set_location(address)
        self.miles = self.miles + dist_traveled
        print(self.location.address)

    def find_next_stop(self):
        address = self.packages[0].address
        dist = self.location.distance_dic.get(address)
        for package in self.packages:
            if self.location.distance_dic.get(package.address) < dist:
                address = package.address
        return address




