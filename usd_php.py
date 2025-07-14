import requests

def get_usd_to_php():
    url = "https://api.frankfurter.app/latest?from=USD&to=PHP"
    res = requests.get(url)
    data = res.json()
    return data["rates"]["PHP"]
