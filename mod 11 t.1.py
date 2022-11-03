"""Toteuta seuraava luokkahierarkia Python-kielellä:
Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat.
Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla."""


class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi


    def print_info(self):
        print(f"Julkaisun nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara ):
        self.sivumaara = sivumaara
        self.kirjoittaja = kirjoittaja
        super().__init__(nimi)


    def print_info(self):
        super().print_info()
        print(f"Kirja on {self.sivumaara}-sivuinen")


class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)
    # LISÄÄ PRINT INFO METODI

    def print_info(self):
        super().print_info()
        print(f"Lehden päätoimittaja on {self.paatoimittaja}")



julkaisu1 = Lehti("Aku Ankka", "Aki Hyppää")
julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
julkaisu1.print_info()
julkaisu2.print_info()