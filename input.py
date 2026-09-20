import json
import sys


def parse_and_update_classes(raw_string: str, json_file: str = "classes.json"):
    # Split the pipe-delimited raw payload string into individual JSON strings
    json_messages = raw_string.strip().split("|")
    
    class_update = None
    aura_p = None
    s_act = None

    # Extract command payloads using the gather.py matching logic
    for msg_str in json_messages:
        if not msg_str.strip():
            continue
            
        data = json.loads(msg_str)
        obj = data.get("b", {}).get("o", {})
        cmd = obj.get("cmd")

        match cmd:
            case "updateClass":
                class_update = obj
            case "aura+p":
                aura_p = obj
            case "sAct":
                s_act = obj

    if not class_update or "sClassName" not in class_update:
        raise ValueError("The provided string does not contain a valid 'updateClass' object with an 'sClassName'.")

    class_name = class_update["sClassName"]

    # Load existing classes.json
    try:
        with open(json_file, "r") as f:
            classes_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        classes_data = {}

    # Merge payloads following process_class logic
    prev_data = classes_data.get(class_name, {})

    if class_update:
        prev_data.update(class_update)
    if aura_p:
        prev_data.update(aura_p)
    if s_act:
        prev_data.update(s_act)

    classes_data[class_name] = prev_data

    # Write merged result back to classes.json
    with open(json_file, "w") as f:
        json.dump(classes_data, f, indent=4)

    print(f"Successfully updated '{class_name}' in {json_file}")


def parse_and_update_classes_from_file(file_path: str, json_file: str = "classes.json"):
    # Split the pipe-delimited raw payload string into individual JSON strings
    with open(file_path, "r") as f:
        json_messages = json.load(f)
    
    class_update = None
    aura_p = None
    s_act = None

    # Extract command payloads using the gather.py matching logic
    for msg in json_messages:
        msg_str = json.dumps(msg)
        if not msg_str.strip():
            continue
            
        data = json.loads(msg_str)
        obj = data.get("b", {}).get("o", {})
        cmd = obj.get("cmd")

        match cmd:
            case "updateClass":
                class_update = obj
            case "aura+p":
                aura_p = obj
            case "sAct":
                s_act = obj

    if not class_update or "sClassName" not in class_update:
        raise ValueError("The provided string does not contain a valid 'updateClass' object with an 'sClassName'.")

    class_name = class_update["sClassName"]

    # Load existing classes.json
    try:
        with open(json_file, "r") as f:
            classes_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        classes_data = {}

    # Merge payloads following process_class logic
    prev_data = classes_data.get(class_name, {})

    if class_update:
        prev_data.update(class_update)
    if aura_p:
        prev_data.update(aura_p)
    if s_act:
        prev_data.update(s_act)

    classes_data[class_name] = prev_data

    # Write merged result back to classes.json
    with open(json_file, "w") as f:
        json.dump(classes_data, f, indent=4)

    print(f"Successfully updated '{class_name}' in {json_file}")

if __name__ == "__main__":
    # while True:
    #     raw_input = input("Big JSON here: ").strip()
    parse_and_update_classes_from_file("cc.json")