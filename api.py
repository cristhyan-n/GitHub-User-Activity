import urllib.request, json, sys

def get_activity(username):
    request = urllib.request.Request(f"https://api.github.com/users/{username}/events", headers={"User-Agent": "app"})
    try:
        response = urllib.request.urlopen(request)
        content = response.read().decode("utf-8")
        data = json.loads(content)
        return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("usuário não encontrado")
        elif e.code == 403:
            print("acesso negado")
        elif e.code == 500:
            print("erro interno no servidor")
        else:
            print("erro")
        sys.exit(1)
            
    except urllib.error.URLError:
        print("Falha na conexão")
        sys.exit(1)
    