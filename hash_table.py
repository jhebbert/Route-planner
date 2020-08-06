from parcel import Parcel

class HashTable:

    def __init__(self):
        self.size = 40
        self.table = [None] * 40

    # Gets the index to be used for insertion into the hash table.
    # This is redundant for the given scenario since package ids run from 1 to 40
    # but having this would allow the program to be used with package ids that
    # are larger than 40
    def get_index(self, parcel):
        index = int(parcel.parcel_id) % 40
        return index

    def is_duplicate(self, index):
        found = False
        for parcel in self.table:
            if parcel is not None:
                id = parcel.parcel_id
                if id == index:
                    found = True
        return found

    # Add parcel to table and handle collisions
    def insert(self, parcel):
        index = self.get_index(parcel)
        if not self.is_duplicate(parcel.parcel_id):
            if self.table[index] is None:
                self.table[index] = parcel
            else:
                counter = 0
                while self.table[index] is not None and counter < 40:
                    index = index + 1
                    counter = counter + 1
                if self.table[index] is None:
                    self.table[index] = parcel

    # lookup function: returns parcel object with the
    # passed in key
    def search_parcel(self, key):
        searched = None
        for parcel in self.table:
            if parcel is not None:
                if parcel.parcel_id is key:
                    searched = parcel
        return searched

    def print_table(self):
        for parcel in self.table:
            print(parcel)
