import csv
from Input_package_csv import truck_one, truck_two, truck_three
from HashTable import HashTable


# Calculate the distances between each connecting address
# @Params: Two locations to check the distance between
# Grabs the date from the distance list created from the CSV and returns the found data
# Complexity: O(1)
def get_distance_between(location_row, location_column):
    if distance_values_list[location_row][location_column] == '':
        distance_value = distance_values_list[location_column][location_row]
    else:
        distance_value = distance_values_list[location_row][location_column]
    return distance_value


# Will return corresponding address index when passing in the String address
# Complexity: O(1)
def get_address_index(address_name):
    return address_index_list.get(address_name)


# Open & read the distance names csv file
# Complexity: O(1)
with open('distance_names.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    distance_names_list = list(csv_reader)
    print(distance_names_list)

    # Create dict of addresses using the String names as ids
    # Complexity: O(N)
    address_index_list = {}
    for address in distance_names_list:
        address_index_list[address[2]] = int(address[0])  # (Address String, address index)

    # Open & read the distance values csv file
    # Complexity: O(1)
    with open('distance_values.csv', encoding='utf-8-sig') as csv_file_values:
        csv_reader = csv.reader(csv_file_values, delimiter=',')
        distance_values_list = list(csv_reader)

        # Holds the distance value for each address to another address
        complete_distance_list = {}
        # Holds indices for each address
        address_indices = ()
        index = 0
        for address in distance_names_list:
            # Create a new dictionary for each address to hold
            # distance to other addresses
            complete_distance_list[index] = {}
            # Create new index for each city
            address_indices += (int(address[0]),)
            index += 1

        # Populate all distance between each address & store in a nested dictionary
        # Complexity: O(N^2)
        for address_dict in complete_distance_list:
            # Create nested dictionary for each address to store distances of each address
            for x in range(len(complete_distance_list)):
                complete_distance_list[address_dict][x] = float(get_distance_between(address_dict, x))

        #  Nested dictionary containing distances between each address
        print('Inputted distance CSV dictionary in OPEN_DIST_VALUES: ')
        print(complete_distance_list)
        print()


def shortest_route(truck, current_address):
    # The list of all packages on passed in truck
    truck_package_list = truck.check_packages()
    # BASE CASE: if list is empty, return it
    if truck_package_list.length() == 0:
        return truck_package_list
    else:
        shortest_distance = 100.0  # Start the default distance at arbitrarily large float
        next_location = 0  # The next address to move to

        # Iterate through each package on the truck
        # @package: the index of specific package
        for package in truck_package_list.hashTable:
            package_address_index = get_address_index(str(truck.get_package(package)[1]))  # Retrieve address index
            distance_between = complete_distance_list.get(current_address, {}).get(
                package_address_index)  # Distance between current address and compared address

            # Check distance between current address and next address in loop
            # Update the shortest distance and current address if least is found
            if distance_between <= shortest_distance:
                shortest_distance = distance_between
                current_address = package_address_index
        print(shortest_distance)
        # Iterate through packages once more to find packages addressed to same address
        # Start creating lists of package routes for each truck and pop packages off truck_package_list
        for package in list(truck_package_list.hashTable):
            # print(truck_package_list.retrieve(package)); # Prints the value of the specified package
            package_address_index = get_address_index(str(truck.get_package(package)[1]))  # Retrieve address index
            distance_between = complete_distance_list.get(current_address, {}).get(
                package_address_index)  # Distance between current address and compared address

            # Check if the distance between current address and next address index is the current shortest_distance
            # Then load the package(s) onto specific truck and recurse
            if distance_between == shortest_distance:
                truck.load_optimized_package(package,
                                             truck_package_list.retrieve(package))
                # Save the current distance of the package
                truck.check_optimized_packages().retrieve(package)[9] = shortest_distance
                truck_package_list.delete(package)
        shortest_route(truck, current_address)


shortest_route(truck_one, 0)
#shortest_route(truck_two, 0)
#shortest_route(truck_three, 0)

#print(truck_three.check_optimized_packages().retrieve('4'))  # will print <package 4> on the route list of truck_one
print(truck_one.print_optimized_packages())

# Set up the starting times for each truck to depart WGU port
truck_one.route_times.append('8:00:00')
