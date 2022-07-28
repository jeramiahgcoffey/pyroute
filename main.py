from csv_reader import *
from truck import Truck

package_data = load_package_data('data/Package File.csv')
address_data = load_address_data('data/distances.csv')
distance_graph = load_distance_data('data/distances.csv', address_data)

truck_1 = Truck(1, package_data, distance_graph)
truck_2 = Truck(2, package_data, distance_graph)
truck_3 = Truck(3, package_data, distance_graph)

truck_1.load_truck()
truck_2.load_truck()
truck_3.load_truck()

truck_1.deliver_packages()
truck_2.deliver_packages()
truck_3.deliver_packages()
print(len(truck_1.on_board), len(truck_2.on_board), len(truck_3.on_board))
