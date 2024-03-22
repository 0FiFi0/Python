functions = ["-","+","*","/"]
input_function = input("Co chcesz zrobić(“+” - dodawanie, “-” - odejmowanie, “*” - mnożenie, “/” - dzielenie): ")
if input_function not in functions:
    print("Nie ma takiej opcji")
else:
    input_numbers = input("Podaj a i b (oddzielone przecinkiem)").split(",")
    if not input_numbers[0].isnumeric() or not input_numbers[1].isnumeric() :
        print("Błędne dane")
    else:
        print(input_numbers)
