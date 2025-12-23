import requests

auth_url = "https://tb.piltismart.com/api/auth/login"
auth_data = {
    "username": "n18naveen@gmail.com",
    "password": "nav8024"
}

response = requests.post(auth_url, json=auth_data)
print(response)

if response.status_code == 200:
    token = response.json().get("token")
    print(f"Authentication Token: {token}")
else:
    print(f"Failed to obtain token. Status code: {response.status_code}")
    print(response.text)

customer_id = "c2b483d0-d995-11f0-a3f5-8b520a8e06f7"

token= response.json("")

api_url = f"https://tb.piltismart.com/api/pilti/{customer_id}/getCustomerAssetDeviceTree"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json"
}

response = requests.get(api_url, headers=headers)
response.raise_for_status()

print(response.json())
   
 


    
    
