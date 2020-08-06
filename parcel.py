import datetime
import copy


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
            self.deadline = datetime.datetime.strptime(deadline, '%H:%M').strftime('%H:%M')
        else:
            self.deadline = deadline
        self.mass = mass
        self.special_inst = special_inst
        self.status = 'Hub'
        self.delivery_time = None
        self.load_time = None

    # Prints the details for each package in the passed in table
    def print_status_at_time(self, time, table):
        parcel_copy = copy.copy(self)
        if parcel_copy.load_time > time:
            parcel_copy.status = 'Hub'
        elif parcel_copy.load_time < time < parcel_copy.delivery_time:
            parcel_copy.status = 'On Truck'
        else:
            parcel_copy.status = 'Delivered'
        print('ID:', parcel_copy.parcel_id, '   ' 'Address:', parcel_copy.address, parcel_copy.city,
              parcel_copy.zip_code, '   ' 'Deadline:', parcel_copy.deadline, '  ' 'Weight:', parcel_copy.mass,
              ' ', 'Status:', parcel_copy.status)

    # Allows printing of all class object attributes
    def __str__(self):
        return str(self.__dict__)