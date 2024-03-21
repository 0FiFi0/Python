# Tutaj pisz swój kod, młody padawanie ;-)
name = input("Podaj imię: ").capitalize()
surname = input("Podaj nazwisko: ").capitalize()
birthdate = input("Podaj datę urodzenia w formacie dd-mm-rrrr: ")
email = input("Podaj adres e-mail: ").lower()

if '@' not in email or '.' not in email:
    print("Niepoprawny mail")
elif email[0].isdigit():
    print("E-mail nie może zaczynac się od liczby.")
elif len(birthdate) != 10 or birthdate[2] != '-' or birthdate[5] != '-':
    print("Błędny formaty daty")
else:
    date_parts = birthdate.split('-')
    if not date_parts[0].isdigit() or not date_parts[1].isdigit() or not date_parts[2].isdigit():
        print("Dzien, miesiąc, rok muszą być liczbami")
    else:
        if date_parts[0] < 1 or date_parts[0] > 31 or date_parts[1] < 1 or date_parts[1] > 12:
            print("Błędna data")
        else:
            encrypted_name = name[0] + '*' * len(name[1:])

            encrypted_surname = surname[0] + '*' * len(surname[1:])

            age = 2024 - date_parts[2]

            email_parts = email.split('@')
            encrypted_email = email[0] + '*' * (len(email_parts[0]) - 1) + '@' + email_parts[1]

            encrypted_data = {
                'Imię i nazwisko': encrypted_name + ' ' + encrypted_surname,
                'wiek': age,
                'mail': encrypted_email
            }

            print("Zaszyfrowane dane:", encrypted_data )






