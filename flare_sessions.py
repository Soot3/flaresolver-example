import requests
import time
# session created
url = "http://localhost:8191/v1"
headers = {"Content-Type": "application/json"}
first_request = {
    "cmd": "sessions.create",
    }

first_response = requests.post(url, headers=headers, json=first_request)
session_id = first_response.json().get('session', {})

# using the session id

second_request = {
    "cmd": "request.get",
    "url": "https://www.datanearme.co/",
    "maxTimeout": 60000,
    "session":f"{session_id}"
}
second_response = requests.post(url, headers=headers, json=second_request)
print("Status:", second_response.json().get('status', {}))
