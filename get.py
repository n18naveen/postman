import requests

url = "https://tb.piltismart.com/api/pilti/c2b483d0-d995-11f0-a3f5-8b520a8e06f7/getCustomerAssetDeviceTree"

headers = {
    "Authorization": f"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhamF5ZGV2YWFqYXlkZXZhMUBnbWFpbC5jb20iLCJ1c2VySWQiOiIyM2RhODI5MC1kOTk2LTExZjAtYTNmNS04YjUyMGE4ZTA2ZjciLCJzY29wZXMiOlsiQ1VTVE9NRVJfVVNFUiJdLCJzZXNzaW9uSWQiOiJiYTI5YjQzMy1jMGUzLTRmNWEtODBmNi1kZmFlOGYzNThhNmIiLCJleHAiOjE3NjU4ODg4MjIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNzY1ODc5ODIyLCJmaXJzdE5hbWUiOiJqb2UiLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiODhlNzgyNDAtY2ZmNy0xMWVmLWI5OTMtMjVlNmYyZjY0ZDJiIiwiY3VzdG9tZXJJZCI6ImMyYjQ4M2QwLWQ5OTUtMTFmMC1hM2Y1LThiNTIwYThlMDZmNyJ9.5JAtm1ESJgJzGNRcpkbFSse9vb0K_vRTqWdvwKi9ZFHQmfGWZzlIlAjw4f7RTzXxlGm6kjHbiQbedT0C0gYKEw",
    "Accept": "application/json"
}

api_response = requests.get(url, headers=headers)

print("Status:", api_response.status_code)
print("Response:", api_response.text)



if not token:
    print("Token not found")
    exit()

print("Login success")