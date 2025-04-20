import requests
from config.settings import YANDEX_API_KEY

def get_location_from_address(address):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": YANDEX_API_KEY,
        "geocode": address,
        "format": "json",
        "lang": "uz_UZ"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            pos = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            lon, lat = map(float, pos.split())
            return {"lat": lat, "lon": lon}
        except (IndexError, KeyError):
            return None
    return None
