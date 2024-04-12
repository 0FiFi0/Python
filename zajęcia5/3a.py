class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, placa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = placa
        self.stanowisko = stanowisko
    def przedstaw(self):
        print("Imię: " +str(self.imie)+"\nNazwisko: "+str(self.nazwisko)+ "\nStanowisko: "+str(self.stanowisko)+"\nZarobki: "+ str(self.placa))
    def podwyzka(self, podwyzka):
        self.placa+=podwyzka
    def zmien_stanowisko(self, nowe_stanowisko):
        self.stanowisko = nowe_stanowisko

pracownik1 = Pracownik("Filip","Oskwarek","kierownik",7000)
pracownik1.przedstaw()
pracownik1.podwyzka(1000)
pracownik1.zmien_stanowisko("prezes")
print("")
pracownik1.przedstaw()

