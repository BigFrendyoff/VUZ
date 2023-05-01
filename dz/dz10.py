class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class Mealy:
    def __init__(self):
        self.state = "A"

    def speed(self):
        match self.state:
            case "A":
                self.state = "B"
                return 0
            case "C":
                return 3
            case "D":
                self.state = "E"
                return 4
            case "E":
                self.state = "F"
                return 7
            case _:
                raise MealyError("speed")

    def build(self):
        match self.state:
            case "B":
                self.state = "C"
                return 1
            case "D":
                self.state = "B"
                return 6
            case "E":
                self.state = "C"
                return 8
            case _:
                raise MealyError("build")

    def bend(self):
        match self.state:
            case "C":
                self.state = "D"
                return 2
            case "D":
                return 5
            case "E":
                self.state = "G"
                return 9
            case "F":
                self.state = "G"
                return 10
            case "G":
                self.state = "H"
                return 11
            case _:
                raise MealyError("bend")


def main():
    return Mealy()


def test():
    o = main()
    try:
        o.build()  # MealyError
    except MealyError:
        pass
    o.speed()  # 0
    o.build()  # 1
    o.bend()  # 2
    o.bend()  # 5
    o.build()  # 6
    o.build()  # 1
    o.speed()  # 3
    o.bend()  # 2
    o.speed()  # 4
    o.speed()  # 7
    o.bend()  # 10
    o.bend()  # 11

    o = main()
    o.speed()  # 0
    try:
        o.speed()  # MealyError
    except MealyError:
        pass
    o.build()  # 1
    o.speed()  # 3
    try:
        o.build()  # MealyError
    except MealyError:
        pass
    o.speed()  # 3
    o.bend()  # 2
    o.build()  # 6
    o.build()  # 1
    o.bend()  # 2
    o.bend()  # 5
    o.speed()  # 4
    o.speed()  # 7
    o.bend()  # 10
    try:
        o.build()  # MealyError
    except MealyError:
        pass
    o.bend()  # 11

    o = main()
    o.speed()  # 0
    try:
        o.bend()
    except MealyError:
        pass
    o.build()  # 1
    o.bend()  # 2
    o.speed()  # 4
    o.build()  # 8
    o.speed()  # 3
    o.bend()  # 2
    o.bend()  # 5
    o.speed()  # 4
    o.bend()  # 9
    o.bend()  # 11
