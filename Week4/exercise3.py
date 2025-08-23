import queue
import json
import sys

def json_to_dict_array(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    # If the JSON is a list, return as is; if it's a dict, wrap in a list
    if isinstance(data, list):
        return data
    else:
        return [data]

def process_people(people: list[dict]):
    queue_VIP = queue.Queue()
    queue_Normal = queue.Queue()
    queue_BULK = queue.Queue()
    result = queue.Queue()
    
    for person in people:
        if person["tipo"] == "VIP":
            queue_VIP.put(person)
        elif person["tipo"] == "NORM":
            queue_Normal.put(person)
        elif person["tipo"] == "BULK":
            queue_BULK.put(person)

    while not queue_VIP.empty():
        result.put(queue_VIP.get())
    while not queue_Normal.empty():
        result.put(queue_Normal.get())
    while not queue_BULK.empty():
        result.put(queue_BULK.get())

    return list(result.queue)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please provide a JSON file.")
        exit(code = 1)

    json_file = sys.argv[1]
    people = json_to_dict_array(json_file)
    processed_people = process_people(people)
    for person in processed_people:
        print(person["nombre"], end=" ")