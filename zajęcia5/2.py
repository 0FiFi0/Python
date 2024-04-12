class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.__x = 0
    def say_name(self):
        print("Zółw: "+str(self.name)+" szybkość: "+str(self.speed))
    def move(self, distance):
        self.__x += distance
    def get_position(self):
        return self.__x

zolw1 = Turtle("Maciek", 15)
zolw2 = Turtle("Kacper", 20)
zolw1.say_name()
zolw2.say_name()
print(zolw1.get_position())
zolw1.move(5)
print(zolw1.get_position())
