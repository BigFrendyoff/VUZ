# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)



print( [k for k, v in Room.__dict__.items()
     if not (k.startswith('__') and k.endswith('__'))])

