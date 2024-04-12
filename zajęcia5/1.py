import math

class Rectangle():
    def __init__(self, a, b):
        if a<0 or b<0:
            raise ValueError("Boki prostokąta nie mogą być ujemne!")
        self.a = a
        self.b = b

    def Field(self):
        return self.a*self.b

    def Perimeter(self):
        return 2*self.a + 2*self.b

class Triangle():
    def __init__(self, a, b, c):
        if a<0 or b<0 or c<0:
            raise ValueError("Boki trójkąta nie mogą być ujemne!")
        self.a = a
        self.b = b
        self.c = c

        if Triangle.Field(self)==0:
            raise ValueError("Pole twojego trójkąta wynosi 0...")

    def Field(self):
        s = (self.a + self.b + self.c) / 2
        return round(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)),2)

    def Perimeter(self):
        return self.a + self.b + self.c

class Circle():
    def __init__(self, r):
        if r<0:
            raise ValueError("Promień koła nie może być ujemny!")
        self.r = r

    def Field(self):
        return round(math.pi * (self.r**2),2)

    def Perimeter(self):
        return round(2 * math.pi * self.r,2)


figures = ['prostokąt','trójkąt', 'koło']
input_figure = input("Podaj figurę: ")

while input_figure not in figures:
    print("Nie ma takiej figury! Napisz STOP jeśli chcesz zakończyć program.")
    input_figure = input("Podaj figurę: ")
    if input_figure == "STOP":
        exit()

if input_figure == "prostokąt":
    parameters = input("Podaj bok A i B po spacji: ").split(' ')
    while len(parameters) != 2 or not(parameters[0].isnumeric()) or not(parameters[1].isnumeric()):
        parameters = input("Podaj bok A i B po spacji: ").split(' ')

    rectangle = Rectangle(int(parameters[0]), int(parameters[1]))
    print(f'Pole prostokąta wynosi: {rectangle.Field()}, a jego obwód to: {rectangle.Perimeter()}')
elif input_figure == "trójkąt":
    parameters = input("Podaj boki a,b,c trójkąta po spacji: ").split(' ')
    while len(parameters) != 3 or not(parameters[0].isnumeric()) or not(parameters[1].isnumeric()) or not(parameters[2].isnumeric()):
        parameters = input("Podaj boki a,b,c trójkąta po spacji: ").split(' ')

    triangle = Triangle(int(parameters[0]), int(parameters[1]), int(parameters[2]))
    print(f'Pole trójkąta wynosi: {triangle.Field()}, a jego obwód to: {triangle.Perimeter()}')
elif input_figure == "koło":
    parameters = input("Podaj promień koła: ").split(' ')
    while not(parameters[0].isnumeric()):
        parameters = input("Podaj promień koła: ").split(' ')

    circle = Circle(int(parameters[0]))
    print(f'Pole koła wynosi: {circle.Field()}, a jego obwód to: {circle.Perimeter()}')
