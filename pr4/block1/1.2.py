# create a class
class Room:
    length = 0.0
    breadth = 0.0

    # method to calculate area
    def calculate_area(a,b):
        print("Area of Room =", a * b)


calculate_area = getattr(Room, 'calculate_area')
a = 5
b = 10
calculate_area(a,b)
