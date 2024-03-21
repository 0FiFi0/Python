# Tutaj pisz swój kod, młody padawanie ;-)

figures = ["prostokąt", "trapez", "trójkąt"]

input_figure = input("Podaj figurę (prostokąt, trapez, trójkąt): ").lower()
if input_figure not in figures:
    print("Błędna figura")
elif input_figure == "prostokąt":
    rectangle = input("Podaj boki(a b): ").split(" ")
    if len(rectangle) == 2 and float(rectangle[0]) >= 0 and float(rectangle[1]) >= 0:
        print(f"Pole twojego prostokąta wynosi: {float(rectangle[0]) * float(rectangle[1])}")
    else:
        print("Błędne dane")
elif input_figure == "trapez":
    trapeze = input("Podaj podstawy oraz wysokośc(a b h): ").split(" ")
    if len(trapeze) == 3 and float(trapeze[0]) >= 0 and float(trapeze[1]) >= 0 and float(trapeze[2]) >= 0:
        print(f"Pole twojego trapezu wynosi: {(float(trapeze[0]) + float(trapeze[1])) * float(trapeze[2]) / 2}")
    else:
        print("Błędne dane")
elif input_figure == "trójkąt":
    triangle = input("Podaj podstawę oraz wysokośc(a h): ").split(" ")
    if len(triangle) == 2 and float(triangle[0]) >= 0 and float(triangle[1]) >= 0 :
        print(f"Pole twojego trójkąta wynosi: {float(triangle[0]) * float(triangle[1]) / 2}")
    else:
        print("Błędne dane")

