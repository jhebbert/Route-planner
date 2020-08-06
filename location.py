class Location:

    def __init__(self, address):
        self.address = address
        # Dictionary data structure used because the
        # distance data is stored as key-value pairs.
        # The key is the address and the value is the
        # distance to that address. This makes for an
        # efficient look up of distance information.
        self.distance_dic = {}




