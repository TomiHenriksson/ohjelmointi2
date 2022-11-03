"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
Kirjoita aliluokille alustajat.
Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
huippunopeuden ja akkukapasiteetin.
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi
sekä asettaa oman kapasiteettinsa.
Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
Aseta kummallekin autolle haluamasi nopeus,
käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
"""


import random


class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinenNopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        self.kuljettuMatka = kuljettu_matka


    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinenNopeus = self.tamanhetkinenNopeus + nopeuden_muutos
        if self.tamanhetkinenNopeus < 0:
            self.tamanhetkinenNopeus = 0
        elif self.tamanhetkinenNopeus > 142:
            print(f"Autosi maksiminopeutesi on {self.huippunopeus} KM/H ")
            self.tamanhetkinenNopeus = 142


    def kulje(self, tuntimaara):
        self.kuljettuMatka += tuntimaara * self.tamanhetkinenNopeus
        return self.kuljettuMatka


class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinenNopeus, kuljettu_matka, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        super().__init__(rekisteritunnus, huippunopeus, tamanhetkinenNopeus, kuljettu_matka)

    def kulje(self, tuntimaara):
        super().kulje(tuntimaara)


class Polttomoottoriauto(Auto):


    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinenNopeus, kuljettu_matka, bensatankinkoko):
        self.bensatankinkoko = bensatankinkoko
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        super().__init__(rekisteritunnus, huippunopeus, tamanhetkinenNopeus, kuljettu_matka)

    def kulje(self, tuntimaara):
        super().kulje(tuntimaara)


# autot = []
# for i in range(10):
    # uusi_auto = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    # autot.append(uusi_auto)

sahkoauto = Sähköauto("ABC-15", "180 km/h", 22, 0,"52.5 kWh")
polttomoottoriauto = Polttomoottoriauto("ACD-123", "165 km/h", 44, 0, "32.3 l")

sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)


print(f"Sähköauto\nrekisteritunnus:{sahkoauto.rekisteritunnus}\nhuippunopeus:{sahkoauto.huippunopeus}\nkuljettumatka:{sahkoauto.kuljettuMatka}\nakkukapasiteetti:{sahkoauto.akkukapasiteetti}\ntämänhetkinen nopeus:{sahkoauto.tamanhetkinenNopeus}")
print()
print(f"Polttomoottoriauto\nrekisteritunnus:{polttomoottoriauto.rekisteritunnus}\nhuippunopeus:{polttomoottoriauto.huippunopeus}\nkuljettumatka:{polttomoottoriauto.kuljettuMatka}\nbensatankin koko:{polttomoottoriauto.bensatankinkoko}\ntämänhetkinen nopeus:{polttomoottoriauto.tamanhetkinenNopeus}")