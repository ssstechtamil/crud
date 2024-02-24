from util import *

def addtask(task):
    data=read_json()
    task_json={
        "sno": len(data["tasks"])+1,
        "task":task,
        "status":"Open"
    }
    data["tasks"].append(task_json)
    write_json(data)
    print("task added successfully!!")

def mark_done(id):
    data=read_json()
    for task in data["tasks"]:
        if task["sno"]==int(id):
            task["status"]="Done"
            write_json(data)
            print(f"{id} marked done ")
    
    

def update_task(id,task_update):
    data=read_json()
    for task in data["tasks"]:
        if task["sno"]==int(id):
            task["task"]=task_update
            write_json(data)
            print(f"{id} updated successfully ")
    

def delete_task(id):
    data=read_json()
    for task in data["tasks"]:
        if task["sno"]==int(id):
            data["tasks"].remove(task)
    counter=1
    for task in data["tasks"]:
        task["sno"]=counter
        counter+=1
    write_json(data)
    print("data deleted successfully!")

