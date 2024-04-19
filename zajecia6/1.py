class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def dane(self):
        print(f"Marka: {self.marka}\nModel: {self.model}")

class Elektryczny(Samochod):
    def __init__(self, zasieg):
        self.zasieg = zasieg

    def jaki_zasieg(self):
        print(f"Zasieg wynosi {self.zasieg} km")

class Sportowy(Samochod):
    def __init__(self, predkosc):
        self.predkosc = predkosc

    def max_predkosc(self):
        print(f"Maksymalna prędkosc wynosi {self.predkosc} km/h")

class ElektrycznySportowy(Elektryczny, Sportowy):
        def __init__(self, marka, model, zasieg, predkosc):
            Samochod.__init__(self, marka, model)
            Elektryczny.__init__(self, zasieg)
            Sportowy.__init__(self, predkosc)


tesla = ElektrycznySportowy("Tesla", "X", 400, 300)
tesla.dane()
tesla.jaki_zasieg()
tesla.max_predkosc()
