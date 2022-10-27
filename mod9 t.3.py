"""Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km."""

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
        tuntimaara = tuntimaara * self.tamanhetkinenNopeus
        return tuntimaara





auto1 = Auto("ABC-123", 142)
print(f"Auto1 \n rekisteritunnus: {auto1.rekisteritunnus:s} \n huippunopeus: {auto1.huippunopeus} \n tämänhetkinen nopeus: {auto1.tamanhetkinenNopeus} \n kuljettu matka: {auto1.kuljettuMatka} ")

print(f"Auto kiihdyttää vauhtiaan 30 KM/H... ")
auto1.kiihdyta(30)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print(f"Auto kiihdyttää vauhtiaan 70 KM/H... ")
auto1.kiihdyta(70)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print(f"Jos autoilija jatkaisi matkaa nopeudella {auto1.tamanhetkinenNopeus}KM/H 1 tunnin ja 30 minuutin ajan autoilija kulkisi yhteensä {auto1.kulje(1.5)} KM")
print(f"Auto kiihdyttää vauhtiaan 50 KM/H... ")
auto1.kiihdyta(50)
print(f"Auton nopeus tällä hetkellä on {auto1.tamanhetkinenNopeus} KM/H")
print("AUTOILIJA TEKEE HÄTÄJARRUTUKSEN...")
auto1.kiihdyta(-200)
print(f"Auton nopeus hätäjarrutuksen jälkeen on {auto1.tamanhetkinenNopeus} KM/H")








