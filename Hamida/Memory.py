class Memory(list):

    def __init__(self, default):
        self.default = default

    def __setitem__(self, index, value):
        while index >= len(self):
            self.append(self.default())
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        if index >= len(self):
            return self.default()
        return list.__getitem__(self, index)
