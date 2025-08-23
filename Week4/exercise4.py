from queue import LifoQueue, Queue
import json
import sys

INVERSE_MOVES = {
    "MOVE": "MOVE_BACK",
    "TURN_LEFT": "TURN_RIGHT",
    "TURN_RIGHT": "TURN_LEFT",
    "DROP": None,
    "RETURN": None
}

def json_to_dict_array(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    # If the JSON is a list, return as is; if it's a dict, wrap in a list
    if isinstance(data, list):
        return data
    else:
        return [data]

def inverse_commands(commands: list[dict])-> LifoQueue:
    stack_inverse = LifoQueue()
    for command in commands:
        inversed_command = {}
        inversed_command ["cmd"] = INVERSE_MOVES[command["cmd"]]
        if not inversed_command["cmd"] :
            continue
        if command["cmd"] == "MOVE":
            inversed_command["x"] = command["x"]
        stack_inverse.put(inversed_command)
    return stack_inverse

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please provide a JSON file.")
        exit(code = 1)

    json_file = sys.argv[1]
    commands = json_to_dict_array(json_file)
    inversed = inverse_commands(commands)
    while not inversed.empty():
        command = inversed.get()
        print(command["cmd"], end="")
        if "x" in command:
            print(f" x {command['x']}")
        else:
            print()