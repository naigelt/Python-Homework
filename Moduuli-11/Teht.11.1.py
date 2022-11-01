# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Publish:

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f" Name of the piece is {self.name}")

class Book(Publish):

    def __init__(self, name, writer, pages):
        super().__init__(name)
        self.writer = writer
        self.pages = pages

    def print_info(self):
        super().print_info()
        print(f" The writes is {self.writer}, and it has {self.pages} pages.")

class Magazine(Publish):

    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def print_info(self):
        super().print_info()
        print(f" The Editor in chief is {self.editor_in_chief}")

book = Book(" Hytti n:o 6", "Rosa Liksom", 200)
magazine = Magazine(" Aku Ankka", "Aki Hyyppä")
book.print_info()
magazine.print_info()




