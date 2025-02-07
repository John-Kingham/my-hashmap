class HashMap:
    """
    A hashmap that uses a simple implementation of open addressing to resolve address conflicts.
    It doesn't use linked lists, so if the underlying array fills up, the hashmap will fill up.
    """

    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]

    def get_hash(self, key, collisions):
        hash_code = sum(key.encode()) + collisions
        return hash_code % self.array_size

    def assign(self, key, value):

        # keep trying until assignment is successful
        collisions = 0
        while True:

            # Use a hash to choose an index to store the key-value pair
            index = self.get_hash(key, collisions)

            # if the index is empty or if the keys match, store the key-value pair and exit
            if self.array[index] is None or self.array[index][0] == key:
                self.array[index] = [key, value]
                return

            # the index holds a different key, so use open addressing to select another index
            collisions += 1

    def retrieve(self, key):

        # keep trying until the key is definitely in or not in the hashmap
        collisions = 0
        while True:

            # Use a hash to find the index for the key
            index = self.get_hash(key, collisions)

            # if the index is empty, the key isn't in the hashmap so return nothing
            if self.array[index] is None:
                return None

            # if the keys match, return the value mapped to the key
            if self.array[index][0] == key:
                return self.array[index][1]

            # the index holds a different key, so use open addressing to select another index
            collisions += 1
