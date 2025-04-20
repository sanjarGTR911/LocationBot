# import requests
# from config.settings import YANDEX_API_KEY
#
# def geocode_address(address: str):
#     url = "https://geocode-maps.yandex.ru/1.x/"
#     params = {
#         "apikey": YANDEX_API_KEY,
#         "geocode": address,
#         "format": "json"
#     }
#     response = requests.get(url, params=params).json()
#     try:
#         pos = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
#         lon, lat = map(float, pos.split())
#         return lat, lon
#     except (IndexError, KeyError):
#         return None, None
