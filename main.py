import csv
import datetime
from parcel import Parcel
from hash_table import HashTable
from truck import Truck
from location import Location
from controller import Controller

package_table = HashTable()
locations = []

# Read in the distance table as a csvfile
with open('distance-table.csv') as csvfile:
    read_distance_csv = csv.reader(csvfile, delimiter=',')

    row = next(read_distance_csv)

    # Reads the first line of the CSV file and creates a new
    # Location object for each address and adds the location
    # to the locations list
    for address in row:
        location = Location(address)
        locations.append(location)

    # Reads the distance values from the CSV and creates a two
    # dimensional array. Each row represents a location and the
    # values in each column of the row hold the distance.
    distance_data = []
    for row in read_distance_csv:
        distance_values = []
        for col in row:
            distance_values.append(float(col))
        distance_data.append(distance_values)

    # Adds the distance data to each Location object in the
    # locations list.
    for i in range(len(distance_data)):
        for j in range(len(distance_data[i])):
            distance = distance_data[i][j]
            loc_A = locations[i]
            loc_B = locations[j]
            loc_A.distance_dic[loc_B.address] = distance
            loc_B.distance_dic[loc_A.address] = distance

# Reads the parcel information from a CSV file and creates a
# new Parcel object with the values from the current row.
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
        package_table.insert(parcel)

# Updating the address for the package that had the wrong address.
package_table.table[9].address = '410 S State St'

# Create the Controller, truck_1 and truck_2
# Loads the trucks
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

# Starts the delivery run for both trucks
WGUPS_controller.run()

# Load the second run for truck_2
truck_2.add_parcel(package_table.search_parcel(9))
truck_2.add_parcel(package_table.search_parcel(2))
truck_2.add_parcel(package_table.search_parcel(33))
truck_2.add_parcel(package_table.search_parcel(28))

# Load the second run for truck_1
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

# Start the second run
WGUPS_controller.run()

# Print the combined total miles for both trucks
print('Total Miles: ', WGUPS_controller.calculate_miles())


# Print the details of all packages at the entered time
def print_report():
    print('\n Please enter a time in HH:MM format (24hr time) to view a status report. \n Or Enter "Exit".')
    input_str = input()
    if input_str.lower() == 'exit':
        print('Have a great day!')
    else:
        user_time_input = 'Aug 04 2020 ' + input_str
        user_time = datetime.datetime.strptime(user_time_input, '%b %d %Y %H:%M')
        for parcel in package_table.table:
            parcel.print_status_at_time(user_time, package_table.table)
        print_report()


print_report()

