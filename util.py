import json

DATA_FILE="data/task_data.json"

def read_json():
    try:
        with open(DATA_FILE) as f:
            return json.load(f)
    except:
        data={
            "tasks":[]
        }
        return data

def write_json(data):
    try:
        with open(DATA_FILE,"w") as f:
            json.dump(data,f,indent=3)
    except:
        print("Unable to write data")