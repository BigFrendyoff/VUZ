class HashTable:
    def __init__(self):
        self.table = []

    def __getitem__(self, key):
        for k, v in self.table:
            if k == key:
                return v
        raise KeyError(key)

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                self.table[i] = (key, value)
                break
        self.table.append((key, value))

    def __len__(self):
        return len(self.table)

    def iter(self):
        return [a[0] for a in self.table]

    #

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.table):
            if k == key:
                del self.table[i]
                break

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        return self

    def __next__(self):
        if not self.table:
            raise StopIteration
        key, val = self.table.pop()
        return key



import random

my_table = HashTable()
builtin_dict = {}

for i in range(10):
    key = random.randint(0, 10000)
    value = random.randint(0, 10000)
    my_table[key] = value
    builtin_dict[key] = value

print(my_table.table)
print(builtin_dict)

for key in builtin_dict:
    assert my_table[key] == builtin_dict[key]
my_table[100] = 500
builtin_dict[100] = 500
del my_table[100]
del builtin_dict[100]

for key in builtin_dict:
    assert my_table[key] == builtin_dict[key]
print(len(my_table))
print(len(builtin_dict))
assert len(my_table) == len(builtin_dict)

assert (100 in my_table) == (100 in builtin_dict)

for key in my_table:
    assert key in builtin_dict
