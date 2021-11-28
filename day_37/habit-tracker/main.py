import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "eNLH6EzZrKaJ6o2T2tkw",
    "username": "thoma",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# "message":"Success. Let's visit https://pixe.la/@thoma , it is your profile page!","isSuccess":true
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

