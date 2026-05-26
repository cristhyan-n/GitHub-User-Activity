import urllib.request, json

def get_activity(username):
    request = urllib.request.Request(f"https://api.github.com/users/{username}/events", headers={"User-Agent": "app"})
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    data = json.loads(content)
    return data