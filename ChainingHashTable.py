# This class is the hash table that will hold the package list.
# This hash table uses chaining to resolve collisions.
# The chaining will allow each bucket to be a list so multiple items can be stored.
# ie this table will be an array of lists that where any bucket contains a list.

# Hashtable class that uses chaining to resolve collision.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # This function will also be used to update existing keys.
    def insert(self, key, item):
        # Uses the key to get the bucket in the hashtable where the key/item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Searches for the key in the bucket_list
        # and updates the value if the key is found.
        for keyValue in bucket_list:
            if keyValue[0] == key:
                keyValue[1] = item
                return True

        # If key is not already in the bucket_list
        # then insert appends the key and value to the list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search is used to find an item with the matching key in the hash table.
    # This function will return the item if it is found or NONE if it isn't found.
    def search(self, key):
        # Uses the key to get the bucket in the hashtable where the key/item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # Search for the key in the bucket_list.
        for keyValue in bucket_list:
            if keyValue[0] == key:  # This is the key in the key value pair.
                return keyValue[1]  # This is the value in the key value pair.
        return None

    # Remove will remove an item from the hash table based on a matching key.
    # This function requires the key as input and then will remove any matching item.
    def remove(self, key):
        # Uses the key to get the bucket in the hashtable where the key/item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # This for loop goes through the bucket_list and compares the key against all the keys in the list,
        # if a match is found it removes it.
        for keyValue in bucket_list:
            if keyValue[0] == key:
                bucket_list.remove([keyValue[0], keyValue[1]])

