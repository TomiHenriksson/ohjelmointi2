"""Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin
 sekä lämpötilan Celsius-asteina.
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen,
jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi."""
import requests

kysy_paikkakunta = input("Syötä paikkakunta: ").lower()
pyynto = "http://api.openweathermap.org/geo/1.0/direct?q=" + kysy_paikkakunta + "&appid=153cafab2c4dec53bb5c58705a69c8ea"

vastaus1 = requests.get(pyynto).json()
lat = (vastaus1["lat"])
lon = (vastaus1["lon"])
nimi = (vastaus1["name"])

saa_tiedot = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly&appid=153cafab2c4dec53bb5c58705a69c8ea"
vastaus2 = requests.get(saa_tiedot).json()
temp = (vastaus2["temp"])
temp_to_c = temp - 273.15
print(f"{nimi}\n lämpötila (K):{temp}\nlämpötila(C): {temp_to_c}")