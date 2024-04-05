def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero."

while True:
    functions = input("Wybierz operację (+, -, *, /). Wpisz 'stop' aby zakończyć działanie: ").lower()

    if functions == "stop":
        print("Koniec programu.")
        break

    if functions not in ["+", "-", "*", "/"]:
        print("Nieprawidłowa operacja. Spróbuj ponownie.")
        continue

    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj drugą liczbę: ")

    if not a.isnumeric() or not b.isnumeric() :
        print("Błędne dane")
        continue
    a = float(a)
    b = float(b)
    if functions == "+":
        print(f"Wynik dodawania: {add(a, b)}")
    elif functions == "-":
        print(f"Wynik odejmowania: {sub(a, b)}")
    elif functions == "*":
        print(f"Wynik mnożenia: {mul(a, b)}")
    elif functions == "/":
        print(f"Wynik dzielenia: {div(a, b)}")
