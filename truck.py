class Truck:
    def __init__(self):
        self.packages = []
        self.miles = 0
        self.location = 'Hub'

    def add_parcel(self, parcel):
        self.packages.append(parcel)

    def __str__(self):
        return str(self.__dict__)

    def print_contents(self):
        for parcel in self.packages:
            print(parcel)

    def deliver_package(self):
        for parcel in self.packages:
            if self.location == parcel.address:
                parcel.delivered = True
                self.packages.pop(parcel)