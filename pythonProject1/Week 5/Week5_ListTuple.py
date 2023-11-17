


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

run_task2()

def list_tasks():
    run_task1()


list_tasks()


