import datetime


# Construcktor
class Truck:
    def __init__(self, location, possible_locations, hour, min):
        self.packages = []
        self.miles = 0
        self.location = location
        self.possible_locations = possible_locations
        self.time = datetime.datetime(2020, 8, 4, hour, min, 0)
        self.speed = 18
        self.priority_del = []

    # Searches the possible_locations list for a location that
    # matches the passed in address.
    def set_location(self, address):
        for location in self.possible_locations:
            if location.address == address:
                self.location = location

    # Adds a parcel to the trucks packages list
    def add_parcel(self, parcel):
        self.packages.append(parcel)
        parcel.status = 'On Truck'
        parcel.load_time = self.time

    # Finds all the packages with a delivery deadline and
    # adds them to the priority delivery list
    def find_priority(self):
        for package in self.packages:
            if package.deadline != 'EOD':
                self.priority_del.append(package)
        # print(len(self.priority_del))

    # Handles the delivery of all priority parcels and
    # any packages on the truck with the same address as
    # a priority parcel
    def deliver_priority(self):
        while self.priority_del:
            for package in self.priority_del:
                self.move_to(self.find_next_stop(self.priority_del))
                self.deliver_package()
        # print('Priority deliveries done.')

    # Allows printing of truck objects in a human readable format
    def __str__(self):
        return str(self.__dict__)

    # Prints all the parcels in the trucks packages list
    def print_contents(self):
        for parcel in self.packages:
            print(parcel)

    # Searches the trucks packages list for packages that
    # match the current location, updates the packages status
    # and removes the package from the packages list and the
    # priority_del list if applicable.
    def deliver_package(self):
        for parcel in self.packages:
            if self.location.address == parcel.address and parcel.status != 'Delivered':
                parcel.status = 'Delivered'
                parcel.delivery_time = self.time
                # print(parcel.status)
                # print(parcel.delivery_time.time())
                self.packages.remove(parcel)
                if parcel in self.priority_del:
                    self.priority_del.remove(parcel)
        if not self.packages:
            # print('Empty!!!!!')
            self.return_to_hub()

    # Updates the trucks location, miles and time.
    def move_to(self, address):
        dist_traveled = self.location.distance_dic.get(address)
        min_elapsed = int((dist_traveled / self.speed) * 60)
        self.set_location(address)
        self.miles = self.miles + dist_traveled
        self.time = self.time + datetime.timedelta(minutes=min_elapsed)
        # print(self.location.address)
        # print(self.miles)

    # Finds the package who's address is closest to the trucks current
    # location and returns that address.
    def find_next_stop(self, package_list):
        address = package_list[0].address
        dist = self.location.distance_dic.get(address)
        for package in package_list:
            cur_dist = self.location.distance_dic.get(package.address)
            if cur_dist < dist:
                address = package.address
        return address

    # Moves the truck back to the hub location 
    def return_to_hub(self):
        self.move_to('4001 South 700 East')





