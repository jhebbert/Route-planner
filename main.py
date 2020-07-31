import csv
from parcel import Parcel
from hash_table import HashTable
from truck import Truck
from location import Location

test_table = HashTable()
test_truck = Truck()
locations = []

with open('distance-table.csv') as csvfile:
    read_distance_csv = csv.reader(csvfile, delimiter=',')

    row = next(read_distance_csv)

    for address in row:
        location = Location(address)
        locations.append(location)

    distance_data = []
    for row in read_distance_csv:
        distance_values = []
        for col in row:
            distance_values.append(float(col))
        distance_data.append(distance_values)

    for i in range(len(distance_data)):

        for j in range(len(distance_data[i])):
            distance = distance_data[i][j]
            loc_A = locations[i]
            loc_B = locations[j]
            loc_A.distance_dic[loc_B.address] = distance
            loc_B.distance_dic[loc_A.address] = distance

for location in locations:
    print(location.address, ': ', location.distance_dic)

with open('parcels.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        parcel_id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        mass = int(row[6])
        special = row[7]

        parcel = Parcel(parcel_id, address, city, state, zip_code, deadline, mass, special)
        test_table.add(parcel)

test_truck.add_parcel(test_table.search_parcel(5))

