class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Imie: {self.name}\nWiek: {self.age}")

    def sound(self):
        print("Default sound")

class Fish(Animal):
    def sound(self):
        print("bul bul")

class Bird(Animal):
    def sound(self):
        print("Default bird sound")

    def fly(self):
        print(f"{self.name} wzbił się w powietrze")

class Pigeon(Bird):
    def sound(self):
        print("gru gru")

jacek = Animal("Jacek", 4)
jacek.introduce()
jacek.sound()
print("\n")
marek = Bird("Marek", 2)
marek.introduce()
marek.fly()
marek.sound()
print("\n")
wojtek = Pigeon("Wojtek",5)
wojtek.introduce()
wojtek.fly()
wojtek.sound()
