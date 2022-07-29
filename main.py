from csv_reader import *
from truck import Truck
import datetime

# Read package data file and return a hash map with Package ID as keys and Package objects as values
package_data = load_package_data('data/Package File.csv')

# Read distance data file and return a Graph object with addresses as vertices and distances as edges
distance_graph = load_distance_data('data/distances.csv', load_address_data('data/distances.csv'))

# Create truck objects, passing in departure time, the ID, package data and distance graph
truck_1 = Truck(1, package_data, distance_graph)
truck_2 = Truck(2, package_data, distance_graph)
truck_3 = Truck(3, package_data, distance_graph)

# Load trucks according to the Package's truck property
truck_1.load_truck(datetime.timedelta(seconds=28800))
truck_2.load_truck(datetime.timedelta(seconds=32700))

package_data.get(9).set_notes('')
# Deliver each Truck's packages
truck_1.deliver_packages()
truck_3.load_truck(truck_1.return_time)
truck_2.deliver_packages()
truck_3.deliver_packages()

print(truck_1.distance_traveled, truck_2.distance_traveled, truck_3.distance_traveled)
print(truck_1.return_time, truck_2.return_time, truck_3.return_time)
print(truck_1.on_board, truck_2.on_board, truck_3.on_board)
print(package_data.print_all_status())
