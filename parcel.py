class Parcel:

    # constructor for parcel object
    def __init__(self, parcel_id, address, city, state, zip_code, deadline, mass, special_inst):
        self.parcel_id = parcel_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.mass = mass
        self.special_inst = special_inst

    # Allows printing of all class object attributes
    def __str__(self):
        return  str(self.__dict__)