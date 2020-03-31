class HashTable:
    def __init__(self):
        self.hashTable = {}

    # Insert a new entry by key/value pair
    # Complexity is O(1)
    def insert(self, key, value):
        self.hashTable[key] = value

    # Retrieve a value in the hash table by using the corresponding key
    # Complexity is O(1)
    def retrieve(self, key):
        return self.hashTable.get(key)

    # Delete an entry in the hash table by specifying a key
    # Complexity is O(1)
    def delete(self, key):
        self.hashTable.pop(key, None)

    # Return the length of the hashtable
    # Complexity: O(1)
    def length(self):
        return len(self.hashTable)