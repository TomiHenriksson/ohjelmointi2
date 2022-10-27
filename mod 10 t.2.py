
"""Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi."""


class Hissi:

    def __init__(self, alin_kerros, ylin_kerros, kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = kerros

    def siirrykerrokseen(self, kerros1):

        for i in range(kerros1):
            if kerros1 > self.kerros:
                hissi.kerros_ylös()
            elif kerros1 < self.kerros:
                hissi.kerros_alas()

    def kerros_ylös(self):
        print(f"Hissi menee kerroksen ylöspäin...")
        self.kerros += 1
        print(f"Hissi on kerroksessa: {self.kerros}")

    def kerros_alas(self):
        print(f"Hissi menee kerroksen alaspäin...")
        self.kerros -= 1
        print(f"Hissi on kerroksessa: {self.kerros}")

class Talo:

    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_lukumaara = hissien_lukumaara
        self.hissit = []
        for x in range(hissien_lukumaara):
            hissi = Hissi(1, 100, 1)
            self.hissit.append(hissi)

    def aja_hissia(self, hissin_numero, kohde_kerros):
        hissin_nro = hissin_numero
        if hissin_nro == 1:
            print(f"Hissisi numero on: {self.hissit[0]}")
        elif hissin_nro == 2:
            print(f"Hissisi numero on: {self.hissit[1]}")
        elif hissin_nro == 3:
            print(f"Hissisi numero on: {self.hissit[2]}")
        elif hissin_nro == 4:
            print(f"Hissisi numero on: {self.hissit[3]}")
        elif hissin_nro == 5:
            print(f"Hissisi numero on: {self.hissit[4]}")
        elif hissin_nro == 6:
            print(f"Hissisi numero on: {self.hissit[5]}")
        hissi.kerros = kohde_kerros
        print(f"Kohdekerros on {hissi.kerros}")




hissi = Hissi(1, 100, 1)
print(f"Hissi on kerroksessa: {hissi.kerros} ")
hissi.siirrykerrokseen(5)
hissi.kerros_alas()
hissi.kerros_alas()
hissi.kerros_alas()
hissi.kerros_alas()

talo = Talo(1, 100, 5)

talo.aja_hissia(1, 10)

