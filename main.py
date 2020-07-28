from parcel import Parcel
from hash_table import HashTable

test_parcel = Parcel(1, 'address', 'city', 'state', 'zip_code', 'deadline', 'second', 'special_inst')
test_parcel_1 = Parcel(80, 'address', 'city', 'state', 'zip_code', 'deadline', 'first', 'special_inst')
test_parcel_2 = Parcel(0, 'address', 'city', 'state', 'zip_code', 'deadline', 'last', 'special_inst')
test_parcel_3 = Parcel(1, 'address', 'city', 'state', 'zip_code', 'deadline', 'should not be printed', 'special_inst')
testTable = HashTable()

testTable.add(test_parcel)
testTable.add(test_parcel_1)
testTable.add(test_parcel_2)

for parcel in testTable.table:
    print(parcel)