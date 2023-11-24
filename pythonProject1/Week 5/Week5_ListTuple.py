


def directions():
    steps =["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def run_task1():
    returned_steps = directions()
    print(returned_steps)
def movements():
    path = ["Move Forward", 10,
            "Move Backward", 5,
            "Turn Left", 3,
            "Turn Right", 1]
    return path

def run_task2():
    print("Moving...")
    returned_path = movements()


    """
        for value in returned_path:
            if type(value) == int:
                print(f"{value} steps")
            else:
                print(f"{value}", end = "!! ")
    """
    for each_item in range(0, len(returned_path), 2):
        print(f"{returned_path[each_item]} for {returned_path[each_item+1]} steps")

def menu():
    print("Please select a direction:")
    returned_list = directions()

    for i in range(len(returned_list)):
        print(f"{i}:{returned_list[i]}")


def run_task3():
    menu()

def menu_and_input():
    print("Please select a direction:")
    returned_list = directions()

    for i in range(len(returned_list)):
        print(f"{i}:{returned_list[i]}")

    direction = int(input())
    return returned_list[direction]

def run_task4():
    route = []
    print("Working out display route: ")

    for each_time in range(5):
        route.append(menu_and_input())

    print(route)


#run_task1()
#run_task2()
#run_task3()
run_task4()


