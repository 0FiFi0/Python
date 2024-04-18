class Fridge:
    __products = list()
    __volume = 0
    def __init__(self, model, temperature, maxvolume):
        self.model = model
        self.temperature = temperature
        self.maxvolume = maxvolume
        self.temp_max = 18
        self.temp_min = 0

    def addProduct(self, product):
        if(self.__volume + product.volume <= self.maxvolume):
            self.__products.append(product)
            self.__volume += product.volume
        else:
            print('W lodowce jest za duzo itemow!!!')

    def showFridgeProducts(self):
        print(f'Produkty: ')
        for product in self.__products:
            print(f'{product.name}')

    def takeProduct(self, product):
        self.__products.remove(product.name)
        self.__volume -= product.volume

    def changeTemperature(self, temperature):
        if temperature<self.temp_max or temperature>self.temp_min:
            self.temperature = temperature

class Product:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

fridge = Fridge('Samsung cooler - fr123', 4, 10)
p1 = Product('carrot',2)
p2 = Product('beer',2)
p3 = Product('apple',3)
p4 = Product('orange',3)
p5 = Product('mango',3)

fridge.addProduct(p1)
fridge.addProduct(p2)
fridge.addProduct(p3)
fridge.addProduct(p4)
fridge.addProduct(p5)

fridge.showFridgeProducts()


