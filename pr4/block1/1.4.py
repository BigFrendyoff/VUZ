class A:
    pass
class B(A):
    pass

class Room(B):
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

def classlookup(cls):
    print(cls.__name__,end = " <- ")
    for base in list(cls.__bases__):
        classlookup(base)



print(classlookup(Room))