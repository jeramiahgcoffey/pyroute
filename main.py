import hash_map
import csv

with open('Package File.csv') as package_file:
    reader = csv.reader(package_file, delimiter=',')
    package_data = list(reader)

for row in package_data:
    print(row)

# with open('Distance Table.csv') as distance_file:
#     reader = csv.reader(distance_file, delimiter=',')
#     distance_data = list(reader)
#
# for row in distance_data:
#     print(row)
# h = hash_map.Map(2)
# h.add('Bob', '567-8888')
# print(h.size)
# h.add('Joe', '567-8878')
# print(h.size)
# h.add('Bill', '567-8588')
# print(h.size)
# h.add('Frannie', '577-8888')
# print(h.size)
# h.add('Jay', '512-8888')
# print(h.size)
# h.add('Jake', '567-0888')
# print(h.size)
# h.add('Boe', '567-8988')
# h.add('Ming', 'testing')
# h.print()
# h.delete('Bill')
# h.print()
# print('Joe: ', h.get('Joe'))
# print(h.size)
# h.print()
# print('Bob: ', h.get('Bob'))
