#habit tracker sheet - post, put and delete
import requests
from datetime import datetime

USERNAME = "anandshankarm"
TOKEN = "askjdakj376123"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Upskilling",
    "unit" : "hours",
    "type": "float",
    "color" : "ajisai"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime(year=2026, month=1, day=7)
post_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"
post_value_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": "7"
}

# response = requests.post(url=post_value_endpoint, json=post_value_params, headers=headers)
# print(response)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{"20260108"}"

update_params = {
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{'20260107'}"

response =  requests.delete(url=delete_endpoint, headers=headers)
print(response.text)