"""Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
Uusi hissi on aina alimmassa kerroksessa.
 Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
  metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
 että hissi päätyy viidenteen kerrokseen.
 Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
  missä kerroksessa hissi sen jälkeen on.
 Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
 ja sen jälkeen takaisin alimpaan kerrokseen."""


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


hissi = Hissi(1, 100, 1)
print(f"Hissi on kerroksessa: {hissi.kerros} ")
hissi.siirrykerrokseen(5)
hissi.kerros_alas()
hissi.kerros_alas()
hissi.kerros_alas()
hissi.kerros_alas()

