def rectangle_area(side_a, side_b):
    return side_a*side_b

def trapeze_area(side_a, side_b, height):
    return (side_a+side_b) * height / 2

def triangle_area(side_a , height):
    return side_a * height / 2



while True:
    figures = ["prostokąt", "trapez", "trójkąt"]
    input_figure = input("Podaj figurę (prostokąt, trapez, trójkąt). Wpisz 'stop' aby zakończyć działanie: ").lower()

    if input_figure == "stop":
        print("Koniec programu.")
        break

    if input_figure not in figures:
        print("Błędna figura")
        continue

    elif input_figure == "prostokąt":
        while True:
            rectangle = input("Podaj boki(a b): ").split(" ")
            if len(rectangle) == 2 and float(rectangle[0]) > 0 and float(rectangle[1]) > 0:
                print(f"Pole twojego prostokąta wynosi: {rectangle_area(float(rectangle[0]),float(rectangle[1]))}")
                break
            else:
                print("Błędne dane")
    elif input_figure == "trapez":
        while True:
            trapeze = input("Podaj podstawy oraz wysokośc(a b h): ").split(" ")
            if len(trapeze) == 3 and float(trapeze[0]) > 0 and float(trapeze[1]) > 0 and float(trapeze[2]) > 0:
                print(f"Pole twojego trapezu wynosi: {trapeze_area(float(trapeze[0]), float(trapeze[1]), float(trapeze[2]))}")
                break
            else:
                print("Błędne dane")
    elif input_figure == "trójkąt":
        while True:
            triangle = input("Podaj podstawę oraz wysokośc(a h): ").split(" ")
            if len(triangle) == 2 and float(triangle[0]) > 0 and float(triangle[1]) > 0 :
                print(f"Pole twojego trójkąta wynosi: {triangle_area(float(triangle[0]), float(triangle[1]))}")
                break
            else:
                print("Błędne dane")
