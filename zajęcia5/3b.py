class Monster:
    def __init__(self, name, hp, spawn_location):
        self.name = name
        self.hp = hp
        self.spawn_location = spawn_location

    def bestiary(self):
        print("Name: "+str(self.name)+"\nHP="+str(self.hp)+"\nSpawn location: "+str(self.spawn_location))
    def change_spawn(self, new_spawn):
        self.spawn_location = new_spawn
    def change_hp(self, new_hp):
        self.hp = new_hp

monster1 = Monster("Utopiec", 70, "Forest")
monster1.bestiary()
monster1.change_spawn("River")
monster1.change_hp(55)
print("")
monster1.bestiary()
