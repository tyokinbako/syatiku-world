import requests
# APIリクエストの送信
response = requests.get("https://randomuser.me/api/")
# JSONデータの取得
data = response.json()
print(data)