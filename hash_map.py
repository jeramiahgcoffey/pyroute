class Map:
    def __init__(self, size=40):
        self.count = 0
        self.size = size
        self.map = [None] * self.size

    def _calc_hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def _check_for_resize(self):
        if self.count == self.size - 1:
            self._resize(self.size * 2)

    def _resize(self, size):
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

    def get(self, key):
        index = self._calc_hash(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]

    def delete(self, key):
        self.count -= 1
        index = self._calc_hash(key)

        if self.map[index] is not None:
            for i in range(0, len(self.map[index])):
                if self.map[index][i][0] == key:
                    return self.map[index].pop(i)

    def print(self):
        print('---------------------------')
        for item in self.map:
            if item is not None:
                for pair in item:
                    print(str(pair))

