import math


def get_player_pos():
    print("Get a first set of coordinates")
    while True:
        coord = input("Enter new coordinates as floats in format ’x,y,z’:")
        coord = coord.split(",")
        try:
            if len(coord) != 3:
                raise IndexError()
            x = float(coord[0])
            y = float(coord[1])
            z = float(coord[2])
            tu = (x, y, z)
            break
        except IndexError:
            print("Invalid syntax")
        except ValueError as e:
            print(f"Error on parameter  : {e}")

    print(f"Got a first tuple: {tu}")
    print(f"It includes: X={x} , Y={y} , Z={z}")
    x0 = 0
    y0 = 0
    z0 = 0
    distance = math.sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2)
    print(f"Distance to center: {round(distance, 4)}\n")

    print("Get a second set of coordinates")
    while True:
        coord2 = input("Enter new coordinates as floats in format ’x,y,z’:")
        coord2 = coord2.split(",")
        test = ""
        try:
            if len(coord2) != 3:
                raise IndexError()
            test = coord2[0]
            x1 = float(coord2[0])
            test = coord2[1]
            y1 = float(coord2[1])
            test = coord2[2]
            z1 = float(coord2[2])
            tu2 = (x1, y1, z1)
            break
        except ValueError as e:
            print(f"Error on parameter '{test}' : {e}")
        except IndexError:
            print("Invalid syntax")

    distance2 = math.sqrt((x1 - x)**2 + (y1 - y)**2 + (z1 - z)**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance2, 4)}")
    return tu
    return tu2


def ft_coordinate_system():
    print("=== Game Coordinate System ===\n")
    get_player_pos()


if __name__ == "__main__":
    ft_coordinate_system()
