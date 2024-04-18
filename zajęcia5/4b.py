class Postac:
    def __init__(self, imie, wiek, zdrowie):
        self.imie = imie
        self.wiek = wiek
        self.zdrowie = zdrowie

    def przedstawienie(self):
        print(f"Czesc jestem {self.imie} i mam {self.wiek} lat")

    def atak(self):
        print(f"{self.imie} boi się i ucieka")

class Wojownik(Postac):
    def __init__(self, imie, wiek, zdrowie, sila):
        self.sila = sila
        self.imie = imie
        self.wiek = wiek
        self.zdrowie = zdrowie

    def staty(self):
        print(f"{self.imie}(Wojownik) Hp: {self.zdrowie} Sila: {self.sila}")

    def atak(self):
        print(f"{self.imie} rusza do ataku z pięściami")

class Mag(Postac):
    def __init__(self, imie, wiek, zdrowie, mana):
        self.mana = mana
        self.imie = imie
        self.wiek = wiek
        self.zdrowie = zdrowie

    def staty(self):
        print(f"{self.imie}(Mag) Hp: {self.zdrowie} Mana: {self.mana}")

    def atak(self):
        print(f"{self.imie} zaczyna pokazywać magiczne sztuczki")

class Berserker(Wojownik):
    def atak(self):
        print(f"{self.imie} rusza do ataku z dwoma toporami")

class Rycerz(Wojownik):
    def atak(self):
        print(f"{self.imie} rusza do ataku z mieczem")

    def blok(self):
        print(f"{self.imie} blokuje się tarczą")

olaf = Berserker("Olaf", 33, 90, 50)
olaf.przedstawienie()
olaf.staty()
olaf.atak()
print("\n")
zawisza = Rycerz("Zawisza Czarny", 40, 150, 30)
zawisza.przedstawienie()
zawisza.staty()
zawisza.atak()
zawisza.blok()
