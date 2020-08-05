import datetime
from location import Location


class Truck:
    def __init__(self, location, possible_locations, hour, min):
        self.packages = []
        self.miles = 0
        self.location = location
        self.possible_locations = possible_locations
        self.time = datetime.datetime(2020, 8, 4, hour, min, 0)
        self.speed = 18
        self.priority_del = []

    def set_location(self, address):
        for location in self.possible_locations:
            if location.address == address:
                self.location = location

    def add_parcel(self, parcel):
        self.packages.append(parcel)

    def find_priority(self):
        for package in self.packages:
            if package.deadline != 'EOD':
                self.priority_del.append(package)
        print(len(self.priority_del))

    def deliver_priority(self):
        while self.priority_del:
            for package in self.priority_del:
                self.move_to(self.find_next_stop(self.priority_del))
                self.deliver_package()
        print('Priority deliveries done.')

    def __str__(self):
        return str(self.__dict__)

    def print_contents(self):
        for parcel in self.packages:
            print(parcel)

    def deliver_package(self):
        for parcel in self.packages:
            if self.location.address == parcel.address and not parcel.is_delivered:
                parcel.is_delivered = True
                parcel.delivery_time = self.time
                print(parcel.is_delivered)
                print(parcel.delivery_time.time())
                self.packages.remove(parcel)
                if parcel in self.priority_del:
                    self.priority_del.remove(parcel)
        if not self.packages:
            print('Empty!!!!!')
            self.return_to_hub()

    def move_to(self, address):
        dist_traveled = self.location.distance_dic.get(address)
        min_elapsed = int((dist_traveled / self.speed) * 60)
        self.set_location(address)
        self.miles = self.miles + dist_traveled
        self.time = self.time + datetime.timedelta(minutes=min_elapsed)
        print(self.location.address)
        print(self.miles)

    def find_next_stop(self, package_list):
        address = package_list[0].address
        dist = self.location.distance_dic.get(address)
        for package in package_list:
            cur_dist = self.location.distance_dic.get(package.address)
            if cur_dist < dist:
                address = package.address
        return address

    def return_to_hub(self):
        self.move_to('4001 South 700 East')





