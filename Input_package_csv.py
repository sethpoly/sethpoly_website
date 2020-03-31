import csv
from random import randint

from HashTable import HashTable
from Truck import Truck

# Create separate truck objects to begin loading packages
truck_one = Truck("Truck One")
truck_two = Truck("Truck Two")
truck_three = Truck("Truck Three")


def main():
    # Opens the package.csv file, and converts it into a hash table
    with open('package_csv.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Creates empty hash table
        package_hash_table = HashTable()

        # Add each package to the hash table as key/value pair
        # Complexity is O(N)
        for row in csv_reader:
            package_id = row[0]
            package_address = row[1]
            package_city = row[2]
            package_state = row[3]
            package_zip = row[4]
            package_deadline = row[5]
            package_weight = row[6]
            package_note = row[7]
            package_status = ''  # [delivered] or [in-route]
            package_current_distance = 0    # The distance the truck travels from the last location to deliver

            package_key = package_id  # Unique key for each package is the ID
            package_details = [package_id, package_address, package_city, package_state, package_zip,
                               package_deadline, package_weight, package_note, package_status, package_current_distance]

            # Adheres to requirements put upon each package
            # Assigns each package to one of the trucks
            if "Delayed" in package_details[7] or "only be on truck 2" in package_details[7]:
                truck_two.load_package(package_key, package_details)
            elif package_details[5] != "EOD" and package_details[7] == "" or "Must" in package_details[7]:
                truck_one.load_package(package_key, package_details)
            elif "Wrong address" in package_details[7]:
                package_details[1] = '410 S State St'
                package_details[4] = '84111'
                truck_three.load_package(package_key, package_details)
            elif package_details[5] == "EOD" and package_details[7] == "":
                if truck_two.package_limit > len(truck_two.check_packages().hashTable) > len(
                        truck_three.check_packages().hashTable):
                    truck_three.load_package(package_key, package_details)
                else:
                    truck_two.load_package(package_key, package_details)

            # Insert each package into a master hash table
            package_hash_table.insert(package_key, package_details)

        truck_one.to_string()
        truck_two.to_string()
        truck_three.to_string()

        # print(package_hash_table.retrieve('1')[2])


main()
