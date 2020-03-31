# TESTING DIJKSTRA'S ALGORITHM
def dijkstra_test():
    # Represents the cities
    nodes = ('WGU', 'International', 'Taylorsville', 'Sugar')
    print(nodes)
    # Represents distances between the nodes (nodes)
    distances = {
        'WGU': {'International': 7.2, 'Taylorsville': 11.0, 'Sugar': 3.8},
        'International': {'WGU': 7.2, 'Taylorsville': 6.4, 'Sugar': 1},
        'Taylorsville': {'WGU': 11.0, 'International': 6.4, 'Sugar': 9.2},
        'Sugar': {'WGU': 3.8, 'Taylorsville': 9.2, 'International': 7.1}
    }

    print('Hard-coded distance dict values in DIJKSTRAS_TEST(): ')
    print(distances)
    print()

    # distances = complete_distance_list

    # Creates a dictionary of all unvisited nodes (City: None)
    unvisited = {node: None for node in nodes}  # Using None as infinity

    # Dictionary that will hold the visited nodes
    visited = {}

    current = 'WGU'  # The starting node is the hub WGU
    # current = 0
    current_distance = 0  # It is 0 miles away from itself
    unvisited[current] = current_distance  # The starting location (WGU) is assigned it's current distance which is 0
    while True:
        # For current city (neighbor): loop through each connecting city (distances[current].items())
        for neighbor, distance in distances[current].items():
            if neighbor not in unvisited: continue  # if the city was visited, restart loop
            new_distance = current_distance + distance  # Calculate distance of connected city from current city
            # If the city has not been assigned a new distance OR the new distance is shorter than the city being compared
            # Set the current city to the new distance
            # If calculated distance is lower than known distance, update it in the dict
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance

        visited[current] = current_distance  # Add the current distance to the visited dict
        del unvisited[current]  # Delete the city from the unvisited dict bc it has been visited
        if not unvisited: break  # BASE CASE: if unvisited is empty: break from while loop
        candidates = [city for city in unvisited.items() if
                      city[1]]  # The updated unvisited list (only if the city distance is not NONE)

        def get_second_element(x):
            return x[1]

        # Sort the unvisited items that have a calculated distance (sort by distance)
        # Assign the current city and current distance of that city to first item in the new sorted list
        # unvisited[] loses an element each  iteration because cities get visited
        current, current_distance = sorted(candidates, key=get_second_element)[0]

    print('Result from DIJKSTRAS_TEST(): ')
    print(visited)

# TESTING DIJKSTRA'S ALGORITHM with imported distance CSV data
def calculate_shortest_distances():
    # Represents the cities
    nodes = address_indices

    # Represents distances between the nodes (nodes)
    distances = complete_distance_list

    # Creates a dictionary of all unvisited nodes (City: None)
    unvisited = {node: None for node in nodes}  # Using None as infinity

    # Dictionary that will hold the visited nodes
    visited = {}

    current = 0  # The starting node is the hub WGU
    current_distance = 0.0  # It is 0 miles away from itself
    unvisited[current] = current_distance  # The starting location (WGU) is assigned it's current distance which is 0
    while True:
        # For current city (neighbor): loop through each connecting city (distances[current].items())
        for neighbor, distance in distances[current].items():
            if neighbor not in unvisited: continue  # if the city was visited, restart loop
            new_distance = current_distance + distance  # Calculate distance of connected city in loop iteration from
            # current city

            # If the city has not been assigned a new distance OR the new distance is shorter than the city being
            # compared
            # Set the current city to the new distance
            # If calculated distance is lower than known distance, update it in the dict
            if unvisited[neighbor] is None or unvisited[neighbor] > new_distance:
                unvisited[neighbor] = new_distance

        visited[current] = current_distance  # Add the current distance to the visited dict
        del unvisited[current]  # Delete the city from the unvisited dict bc it has been visited
        if not unvisited: break  # BASE CASE: if unvisited is empty: break from while loop
        candidates = [city for city in unvisited.items() if
                      city[1]]  # The updated unvisited list (only if the city distance is not NONE)

        def get_second_element(x_):
            return x_[1]

        # Sort the unvisited items that have a calculated distance (sort by distance)
        # Assign the current city and current distance of that city to first item in the new sorted list
        # unvisited[] loses an element each  iteration because cities get visited
        current, current_distance = sorted(candidates, key=get_second_element)[0]

    print('Result from CALCULATE_SHORTEST_DISTANCE() test: ')
    print(visited)

def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        # reverses the array, to display the path nicely
        readable=path[0]
        for index in range(1,len(path)):
            readable = path[index]+readable
        #prints it
            print('shortest path - array: ')
            print(path)
            #print(readable)
            print(distances[dest])
    else :
        # if it is the initial  run, initializes the cost
        if not visited:
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)