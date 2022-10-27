
class Auto:

    def __init__(self, rekisteritunnus, huippunopeus, tamanhetkinenNopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinenNopeus = tamanhetkinenNopeus
        self.kuljettuMatka = kuljettu_matka
auto1 = Auto("ABC-123", 142)
print(f"Auto1 \n rekisteritunnus: {auto1.rekisteritunnus:s} \n huippunopeus: {auto1.huippunopeus} \n tämänhetkinen nopeus: {auto1.tamanhetkinenNopeus} \n kuljettu matka: {auto1.kuljettuMatka} ")