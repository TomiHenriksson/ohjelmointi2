"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
 Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
  Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.

 Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
 Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
 Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""
import random


class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinenNopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        self.kuljettuMatka = kuljettu_matka

    # def __str__(self):
        # return "\nRekisteritunnus: " + self.rekisteritunnus + "\nHuippunopeus: " + self.huippunopeus + "\nTämänhetkinen nopeus: " + self.tamanhetkinenNopeus + "\nKuljettu matka: " + self.kuljettuMatka



    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinenNopeus = self.tamanhetkinenNopeus + nopeuden_muutos
        if self.tamanhetkinenNopeus < 0:
            self.tamanhetkinenNopeus = 0
        elif self.tamanhetkinenNopeus > 142:
            print(f"Autosi maksiminopeutesi on {self.huippunopeus} KM/H ")
            self.tamanhetkinenNopeus = 142


    def kulje(self, tuntimaara):
        tuntimaara = tuntimaara * self.tamanhetkinenNopeus
        return tuntimaara




rekisteritunnukset = ["ABC-1", "ABC-2", "ABC-3", "ABC-4", "ABC-5", "ABC-6", "ABC-7", "ABC-8", "ABC-9", "ABC-10"]
kilpailijat1 = []
for i in range(10):
    kilpailijat = Auto(rekisteritunnukset[random.randint(0, len(rekisteritunnukset) -1 )], random.randint(100, 200), 0, 0)
    kilpailijat1.append(kilpailijat)

print(kilpailijat1)  # 9.4 kesken










auto1 = Auto("ABC-123", 142, 0, 0)
print(f"Auto1 \n rekisteritunnus: {auto1.rekisteritunnus:s} \n huippunopeus: {auto1.huippunopeus} \n tämänhetkinen nopeus: {auto1.tamanhetkinenNopeus} \n kuljettu matka: {auto1.kuljettuMatka} ")

print(f"Auto kiihdyttää vauhtiaan 30 KM/H... ")
auto1.kiihdyta(30)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print(f"Auto kiihdyttää vauhtiaan 70 KM/H... ")
auto1.kiihdyta(70)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
# print(f"Jos autoilija jatkaisi matkaa nopeudella {auto1.tamanhetkinenNopeus}KM/H 1 tunnin ja 30 minuutin ajan autoilija kulkisi yhteensä {auto1.kulje(1.5)} KM")
print(f"Auto kiihdyttää vauhtiaan 50 KM/H... ")
auto1.kiihdyta(50)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print("AUTOILIJA TEKEE HÄTÄJARRUTUKSEN...")
auto1.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto1.tamanhetkinenNopeus} KM/H")








