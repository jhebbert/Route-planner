import datetime


class Parcel:

    # constructor for parcel object
    def __init__(self, parcel_id, address, city, state, zip_code, deadline, mass, special_inst):
        self.parcel_id = parcel_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        if deadline != 'EOD':
            deadline = deadline[:-2]
            deadline = deadline.strip()
            if len(deadline) < 5:
                deadline = '0' + deadline
            self.deadline = datetime.datetime.strptime(deadline, '%H:%M')
        else:
            self.deadline = deadline
        self.mass = mass
        self.special_inst = special_inst
        self.is_delivered = False
        self.delivery_time = None

    # Allows printing of all class object attributes
    def __str__(self):
        return str(self.__dict__)