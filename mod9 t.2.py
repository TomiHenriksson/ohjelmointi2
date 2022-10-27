"""Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää."""


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





auto1 = Auto("ABC-123", 142)
print(f"Auto1 \n rekisteritunnus: {auto1.rekisteritunnus:s} \n huippunopeus: {auto1.huippunopeus} \n tämänhetkinen nopeus: {auto1.tamanhetkinenNopeus} \n kuljettu matka: {auto1.kuljettuMatka} ")

print(f"Auto kiihdyttää vauhtiaan 30 KM/H... ")
auto1.kiihdyta(30)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print(f"Auto kiihdyttää vauhtiaan 70 KM/H... ")
auto1.kiihdyta(70)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print(f"Auto kiihdyttää vauhtiaan 50 KM/H... ")
auto1.kiihdyta(50)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print("AUTOILIJA TEKEE HÄTÄJARRUTUKSEN...")
auto1.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto1.tamanhetkinenNopeus} KM/H")




