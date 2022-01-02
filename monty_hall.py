import random


def initialize_doors(number_of_doors):
    list_of_doors = [bool]*number_of_doors
    door_with_car = random.randint(0, number_of_doors-1)
    for i in range(len(list_of_doors)):
        if i == door_with_car:
            list_of_doors[i] = True
        else:
            list_of_doors[i] = False
    return list_of_doors


def remove_wrong_doors(chosen_door, doors):
    if doors[chosen_door-1]:
        return random.randint(1,len(doors))  # returns random door number (not index) if chosen door has car behind it
    else:
        return doors.index(True)+1  # returns number (not index) of door with car behind it


def print_doors(doors, dont_open):
    n = len(doors)
    if len(doors) == len(dont_open):
        print("{:^3s} ".format("_") * n)
        print("{:^3s} ".format("| |") * n)
        print("{:^3s} ".format("|_|") * n)
        for i in range(n):
            if i == n-1:
                print("{:^3d} ".format(i+1))
            else:
                print("{:^3d} ".format(i + 1), end="")
    else:
        print("{:^3s} ".format("_") * n)
        for i in range(n):
            if i+1 in dont_open:
                print("{:^3s} ".format("| |"), end="")
            elif not doors[i]:
                print("{:^3s} ".format("|G|"), end="")
            else:
                print("{:^3s} ".format("|C|"), end="")
        print("")
        print("{:^3s} ".format("|_|") * n)
        for i in range(n-1):
            print("{:^3d} ".format(i + 1), end="")
        print("{:^3d} ".format(n))


def main():
    seed = int(input("Set seed:\n"))
    random.seed(seed)

    num_of_doors = int(input("How many doors?\n"))
    while num_of_doors < 3 or num_of_doors > 999:
        print("The number of doors must be between 3-999!")
        num_of_doors = int(input("How many doors?\n"))
    doors = initialize_doors(num_of_doors)
    dont_open = []
    for i in range(num_of_doors):
        dont_open.append(i+1)
    print_doors(doors, dont_open)

    chosen_door = int(input(f"Choose a door 1-{num_of_doors}.\n"))
    while chosen_door < 1 or chosen_door > num_of_doors:
        chosen_door = int(input(f"Choose a door 1-{num_of_doors}.\n"))
    print(f"You chose the door number {chosen_door}.\n...")

    door_to_remove = remove_wrong_doors(chosen_door, doors) #door to not show
    dont_open = [chosen_door, door_to_remove]

    print_doors(doors, dont_open)

    print(f"{num_of_doors-2} certainly wrong doors were opened. The door number {door_to_remove} was left.")
    new_chosen_door = int(input(f"Choose {chosen_door} if you want to keep the door you first chose and choose {door_to_remove} if you want to change the door.\n"))
    while new_chosen_door != chosen_door and new_chosen_door != door_to_remove:
        new_chosen_door = int(input(f"Choose {chosen_door} if you want to keep the door you first chose and choose {door_to_remove} if you want to change the door.\n"))
    dont_open = []
    print_doors(doors, dont_open)

    if new_chosen_door-1 == doors.index(True):
        print("Congratulations! The car was behind the door you chose!")
    else:
        print("A goat emerged from the door you chose! The car was behind the other door :(")

main()