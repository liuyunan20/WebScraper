import requests
print("Input the URL:")
url = input()
r = requests.get(url)
if r.status_code == 200:
    print(r.json().get("content", "Invalid quote resource!"))
else:
    print("Invalid quote resource!")
# ["content"]
