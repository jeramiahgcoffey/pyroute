class Map:
    """Hash map implementation"""

    def __init__(self, size=40):
        """
        Initialize Map object.

        Time Complexity: O(N)
        Space Complexity: O(N)

        :param size: Integer. The initial size of the hash map.
        """

        self.count = 0
        self.size = size
        self.map = [None] * self.size

    def _calc_hash(self, key):
        """
        Calculate the hashed key value.

        Time Complexity: O(N)
        Space Complexity: O(1)

        :param key: Any. The key to be hashed
        :return: Integer. The hashed key value.
        """

        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def _check_for_resize(self):
        """
        Check if map needs to resize based on the current count.

        Time Complexity: O(1)
        Space Complexity: O(1)

        :return: Boolean. Represents if a resize is needed.
        """

        if self.count == self.size - 1:
            self._resize(self.size * 2)
            return True
        return False

    def _resize(self, size):
        # TODO: Refactor this method to be less than O(N^3)
        """
        Create new map, and rehash the current values.

        Time Complexity: Average - O(N^2)  Worst - O(N^2+M)
        Space Complexity: O(N)

        :param size: Integer. The new size of the map.
        """

        new_map = [None] * size
        self.size = size
        for bucket in self.map:
            if bucket is not None:
                for pair in bucket:
                    index = self._calc_hash(pair[0])
                    item = [pair[0], pair[1]]
                    if new_map[index] is None:
                        new_map[index] = list([item])
                    else:
                        for key_value in new_map[index]:
                            if key_value[0] == pair[0]:
                                key_value[1] = item
                        new_map[index].append(item)
        self.map = new_map

    def add(self, key, value):
        """
        Add new key value pair to the map.

        Time Complexity: Average - O(N)  Worst - O(N+M)
        Space Complexity: O(1)

        :param key: Any. The key which is hashed.
        :param value: Any. The value which is stored.
        """

        self.count += 1
        index = self._calc_hash(key)
        item = [key, value]

        if self.map[index] is None:
            self.map[index] = list([item])
        else:
            for pair in self.map[index]:
                if pair[0] == key:
                    pair[1] = value
                    self._check_for_resize()
                    return
            self.map[index].append(item)

        self._check_for_resize()

    def get(self, key):
        """
        Get the value associated with the key passed in.

        Time Complexity: Average - O(1)  Worst - O(N)
        Space Complexity: O(1)

        :param key: Any. The key which the value is associated with.
        :return: Any. The value which is associated with the key passed in, or None if not found
        """

        index = self._calc_hash(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
        Delete the key value pair which is associated with the key passed in.

        Time Complexity: Average - O(1)  Worst - O(N)
        Space Complexity: O(1)

        :param key: Any. The key which the pair is associated with.
        :return: Any. The deleted key value pair, or None if not found.
        """

        self.count -= 1
        index = self._calc_hash(key)

        if self.map[index] is not None:
            for i in range(0, len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index].pop(i)
        return None



