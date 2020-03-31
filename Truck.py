from HashTable import HashTable


class Truck:
    # Class variables - same for every instance
    speed = 18
    package_limit = 16  # The maximum amount of packages the truck can carry

    def __init__(self, name):
        self.packages_list = HashTable()  # Presorted list of packages (pre-algorithm)
        self.route_list = HashTable()  # Sorted list packages in order of route taken (post-algorithm)
        self.route_index_list = HashTable()
        self.truck_name = name  # Name of the truck <1,2,3>
        self.total_distance = 0  # Total distance travelled during route
        self.route_times = []  # Will hold all the times that each package was dropped off <Indices will
        # match the route/package order indices> (This is used when looking up specific packages at a specific timestamp in SIMULATOR)

        self.package_distances = {}  # Dict that holds the current distance of each package on truck

    # Loads a package onto the truck [appends to array]
    # Complexity: O(1)
    def load_package(self, key, value):
        self.packages_list.insert(key, value)

    # Loads pacakge to optimized package route list
    def load_optimized_package(self, key, value):
        self.route_list.insert(key, value)

    # @Return a specified package from the hash table
    # Complexity: O(1)
    def get_package(self, key):
        return self.packages_list.retrieve(key)

    # @Delete a specified package from the hash table
    # Complexity: O(1)
    def delete_package(self, key):
        self.packages_list.delete(key)

    # @Returns the list of packages currently on the truck
    # Complexity: O(1)
    def check_packages(self):
        return self.packages_list

    # @Returns the list of optimized packages on truck
    # Complexity: O(1)
    def check_optimized_packages(self):
        return self.route_list

    def print_optimized_packages(self):
        for package in self.route_list.hashTable:
            print(self.route_list.retrieve(package)[0] + ' : ' +self.route_list.retrieve(package)[1])

    # Delivers a specific package on the truck
    # Will set the 'status' of package to 'delivered'
    # Will append the timestamp of package delivery to the route list
    # Complexity: O(1)
    def deliver_package(self):
        # The time it took for package to be delivered since truck left station
        # @param: the current total distance of the truck ######
        package_time = self.get_time_of_delivery(19)
        package_time_split = package_time.split(':')  # Split package_time by hour, minute, and seconds

        # The actual <timestamp> that the last delivery was made
        last_delivery_timestamp = self.route_times[len(self.route_times) - 1]
        last_delivery_split = last_delivery_timestamp.split(':')  # Split last_delivery_timestamp by hour, minute, and seconds

        # Add together the time for package to be delivered and the last delivery timestamp
        hours = int(package_time_split[0]) + int(last_delivery_split[0])
        minutes = int(package_time_split[1]) + int(last_delivery_split[1]) % 60
        seconds = int(package_time_split[2]) + int(last_delivery_split[2]) % 60

        delivery_timestamp = "%d:%02d:%02d" % (hours, minutes, seconds) # Timestamo the package wes delivered
        print(delivery_timestamp)

        return

    # @Returns the time ('00:00:00' format) it took for a package to be delivered
    # @Param: uses the current distance of the truck to determine the 'real-world time' the package was delivered
    # Complexity: O(1)
    def get_time_of_delivery(self, distance):
        time_in_hours = round(distance / 18, 2)  # Trucks travel at 18 mph - so get hours travelled
        hours = int(time_in_hours)
        minutes = (time_in_hours * 60) % 60
        seconds = (time_in_hours * 3600) % 60
        real_time = "%d:%02d:%02d" % (hours, minutes, seconds)

        return real_time

    # Prints out the object
    # Complexity: O(1)
    def to_string(self):
        print(self.truck_name, ": ", len(self.check_packages().hashTable), " on board - ",
              self.check_packages().hashTable)


truck_ = Truck('four')
truck_.route_times.append('8:00:00')
truck_.deliver_package()
