import requests

url="http://localhost:8000/askgemini"

json_data={"prompt":"who is virat kohli"}

try:
    res=requests.post(url,json=json_data)
    print(f"status code: {res.status_code}")
    print("Response JSON :")
    print(res.json())
except requests.exceptions.RequestException as e:
    print(f"An error occured:{e}")