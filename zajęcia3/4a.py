import math

def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

if a + b > c and a + c > b and b + c > a:
    print(f"Pole trójkąta wynosi: {heron(a, b, c)}")
else:
    print("Błędne dane")

