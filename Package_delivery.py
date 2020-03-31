# This class will handle the simulated delivery of all packages on each truck
from Input_package_csv import truck_one, truck_two, truck_three
import Distance_setup


# Simulates a truck's route delivery for a day - will iterate through the optimized package list
# and deliver each package in order of the sorted route, it will save the timestamp of each delivered package to the Truck obj.
# @Param: the truck obj to simulate
# Complexity:
def simulate_truck_route(truck):
    miles = 0  # Var to hold the distance the truck travelled to deliver each package
    optimized_list = truck.check_optimized_packages()  # Optimized ordered route list

    # Iterate through route list
    for package in optimized_list.hashTable:
        # Update the current distance of each package to the total distance the truck travelled to deliver it
        miles += optimized_list.retrieve(package)[9]
        optimized_list.retrieve(package)[9] = miles
        #print(package)
        #print(optimized_list.retrieve(package)[9])

simulate_truck_route(truck_one)
