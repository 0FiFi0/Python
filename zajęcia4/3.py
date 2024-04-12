import calendar
import datetime

def ostatni_dzien_miesiaca(rok, miesiac):
    dzien = calendar.monthrange(rok, miesiac)[1]
    ostatni_dzien = datetime.date(rok, miesiac, dzien)
    while ostatni_dzien.weekday() >= 5:
        dzien -= 1
        ostatni_dzien = datetime.date(rok, miesiac, dzien)
    return ostatni_dzien

def wypisz_daty_wyplaty(rok):
    for miesiac in range(1, 13):
        ostatni_dzien = ostatni_dzien_miesiaca(rok, miesiac)
        print(calendar.month_name[miesiac], "-", ostatni_dzien.strftime("%d-%m-%Y"))


rok = int(input("Podaj rok: "))
wypisz_daty_wyplaty(rok)
