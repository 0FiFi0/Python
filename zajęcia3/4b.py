import math
def row_kwadratowe(a, b, c):
    if a == 0:
        return None
    else:
        delta = b**2 - 4 * a * c
        if delta > 0:
             x1 = (-b - math.sqrt(delta)) / (2 * a)
             x2 = (-b + math.sqrt(delta)) / (2 * a)
             return x1, x2
        elif delta == 0:
              x0 = -(b / 2 * a)
              return x0
        elif delta < 0:
               return None

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

if row_kwadratowe(a, b, c) is None:
    print("Brak rozwiązań")
else:
    print(f"Pierwiastki: {row_kwadratowe(a, b, c)}")
