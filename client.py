import requests 
from urllib.parse import urljoin



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

if __name__ == "__main__":
    make_task("blah", "fight", "me")
