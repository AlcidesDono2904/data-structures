import sys
import json

def json_to_dict_array(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    # If the JSON is a list, return as is; if it's a dict, wrap in a list
    if isinstance(data, list):
        return data
    else:
        return [data]

def parse_time (time: str):
    time_splited = time.split(sep = ':')
    time_splited = list(int(x) for x in time_splited)
    result = ((time_splited[0])*60) + time_splited[1]
    return result

def compress_agenda(events: list[dict]):
    i=0
    while (i < len(events)-1):
        current_event = events[i]
        next_event = events[i+1]
        if current_event["sala"] != next_event["sala"]:
            i += 1
            continue
        start_current = parse_time(current_event["inicio"])
        end_current = start_current + current_event["duracion"]
        start_next = parse_time(next_event["inicio"])
        if end_current == start_next:
            current_event["duracion"] += next_event["duracion"]
            events.remove(next_event)
        else:
            i += 1

    print(events)
    with open("compressed_agenda.json", "w") as file:
        json.dump(events, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Please provide a JSON file.")
        exit(code = 1)
    
    json_file = sys.argv[1]
    events = json_to_dict_array(json_file)
    compress_agenda(events)