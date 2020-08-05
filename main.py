import csv
from parcel import Parcel
from hash_table import HashTable
from truck import Truck
from location import Location
from controller import Controller

package_table = HashTable()
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
        package_table.add(parcel)


package_table.table[9].address = '410 S State St'

WGUPS_controller = Controller()
truck_1 = Truck(locations[0], locations, 8, 0)
truck_2 = Truck(locations[0], locations, 8, 0)
WGUPS_controller.add_truck(truck_1)
WGUPS_controller.add_truck(truck_2)
truck_2.add_parcel(package_table.search_parcel(15))
truck_2.add_parcel(package_table.search_parcel(16))
truck_2.add_parcel(package_table.search_parcel(34))
truck_2.add_parcel(package_table.search_parcel(20))
truck_2.add_parcel(package_table.search_parcel(21))
truck_2.add_parcel(package_table.search_parcel(1))
truck_2.add_parcel(package_table.search_parcel(13))
truck_2.add_parcel(package_table.search_parcel(39))
truck_2.add_parcel(package_table.search_parcel(3))
truck_2.add_parcel(package_table.search_parcel(10))
truck_2.add_parcel(package_table.search_parcel(24))
truck_2.add_parcel(package_table.search_parcel(36))
truck_2.add_parcel(package_table.search_parcel(35))
truck_2.add_parcel(package_table.search_parcel(14))
truck_2.add_parcel(package_table.search_parcel(19))
truck_2.add_parcel(package_table.search_parcel(27))

truck_1.add_parcel(package_table.search_parcel(29))
truck_1.add_parcel(package_table.search_parcel(37))
truck_1.add_parcel(package_table.search_parcel(40))
truck_1.add_parcel(package_table.search_parcel(8))
truck_1.add_parcel(package_table.search_parcel(30))
truck_1.add_parcel(package_table.search_parcel(7))
truck_1.add_parcel(package_table.search_parcel(38))
truck_1.add_parcel(package_table.search_parcel(5))
truck_1.add_parcel(package_table.search_parcel(4))
# # truck_1.add_parcel(package_table.search_parcel())
# # truck_1.add_parcel(package_table.search_parcel())
# # truck_1.add_parcel(package_table.search_parcel())
# # truck_1.add_parcel(package_table.search_parcel())
# truck_1.add_parcel(package_table.search_parcel())
# truck_1.add_parcel(package_table.search_parcel())


WGUPS_controller.run()


truck_2.add_parcel(package_table.search_parcel(9))
truck_2.add_parcel(package_table.search_parcel(2))
truck_2.add_parcel(package_table.search_parcel(33))
truck_2.add_parcel(package_table.search_parcel(28))
# truck_2.add_parcel(package_table.search_parcel())
# truck_2.add_parcel(package_table.search_parcel())
# truck_2.add_parcel(package_table.search_parcel())
# truck_2.add_parcel(package_table.search_parcel())

truck_1.add_parcel(package_table.search_parcel(6))
truck_1.add_parcel(package_table.search_parcel(25))
truck_1.add_parcel(package_table.search_parcel(26))
truck_1.add_parcel(package_table.search_parcel(31))
truck_1.add_parcel(package_table.search_parcel(32))
truck_1.add_parcel(package_table.search_parcel(11))
truck_1.add_parcel(package_table.search_parcel(12))
truck_1.add_parcel(package_table.search_parcel(17))
truck_1.add_parcel(package_table.search_parcel(18))
truck_1.add_parcel(package_table.search_parcel(23))
truck_1.add_parcel(package_table.search_parcel(22))

WGUPS_controller.run()

for package in package_table.table:
    print(package.parcel_id, ':', package.is_delivered)
print(WGUPS_controller.calculate_miles())



