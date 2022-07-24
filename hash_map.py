class Map:
    """This class implements a hash map"""

    def __init__(self, size=40):
        """
        This is the constructor for the Map class

        :param size: Integer representing the initial size of the hash map
        """

        self.count = 0
        self.size = size
        self.map = [None] * self.size

    def _calc_hash(self, key):
        """
        The method which calculates the hashed key value

        :param key: The key to be hashed
        :return: The hashed key value as an Integer
        """

        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def _check_for_resize(self):
        """
        Checks if map needs to resize based on the current count

        :return: Boolean representing if a resize is needed
        """

        if self.count == self.size - 1:
            self._resize(self.size * 2)
            return True
        return False

    def _resize(self, size):
        """
        Increases the size of the map, and rehashes the current values

        :param size: The new size of the map as an Integer
        :return: Boolean representing successful resize (always True)
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
        return True

    def add(self, key, value):
        """
        Adds new key value pair to the map

        :param key: The key which is hashed
        :param value: The value which is stored
        :return: Boolean representing successful addition (always True)
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
            self.map[index].append(item)

        self._check_for_resize()
        return True

    def get(self, key):
        """
        Gets the value associated with the key passed in

        :param key: The key which the value is associated with
        :return: The value which is associated with the key passed in, or None if not found
        """

        index = self._calc_hash(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        """
        Deletes the key value pair which is associated with the key passed in

        :param key: The key which the pair is associated with
        :return: The deleted key value pair or None if not found
        """

        self.count -= 1
        index = self._calc_hash(key)

        if self.map[index] is not None:
            for i in range(0, len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index].pop(i)
        return None

    def print(self):
        """
        Prints the key value pair in the map

        :return: None
        """

        print('---------------------------')
        for item in self.map:
            if item is not None:
                for pair in item:
                    print(str(pair))

