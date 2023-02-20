class Vehicle:
    
    def __init__(self, name:str, color:str, price:float, W:int):
        self.__name = name
        self.__color = color
        self.__price = price
        self.__W = W
    
    @property
    def _name(self):
      return self.__name
    
    @_name.setter
    def _name(self, new__name):
      self.__name = new__name
  
    @_name.deleter
    def _name(self):
      del self.__name

    @property
    def _color(self):
      return self.__color
    
    @_color.setter
    def _color(self, new__color):
      self.__color = new__color
  
    @_color.deleter
    def _color(self):
      del self.__color

    @property
    def _price(self):
      return self.__price
    
    @_price.setter
    def _price(self, new__price):
      self.__price = new__price
  
    @_price.deleter
    def _price(self):
      del self.__price

    @property
    def _W(self):
      return self.__W
    
    @_W.setter
    def _W(self, new__W):
      self.__W = new__W
  
    @_W.deleter
    def _W(self):
      del self.__W
    
    def printInformation(self):
        print(f"Name: {self.__name}")
        print(f"Color: {self.__color}")
        print(f"Price: {self.__price}")
        print(f"W: {self.__W}")


class Motobike(Vehicle):

    def __init__(self, name:str , color:str, price:float, W:int, mass:float, additionalPlace:bool):
       super().__init__(name, color, price, W)
       self.__mass = mass
       self.__additionalPlace = additionalPlace

    def printInformation(self):
      super().printInformation()
      print(f'Good value: {self.__mass}')
      if self.__additionalPlace:
        print(f'Have additional place: Yes')
      else:
        print(f'Have additional place: No')
        


class Car(Vehicle):

    def __init__(self, name:str, color:str, price:float, W:int, amOfDoors:int, type:str):
       super().__init__(name, color, price, W)
       self.__amOfDoors = amOfDoors
       self.__type = type

    @property
    def _amOfDoors(self):
      return self.__amOfDoors
    
    @_amOfDoors.setter
    def _amOfDoors(self, new__amOfDoors):
      self.__amOfDoors = new__amOfDoors
  
    @_amOfDoors.deleter
    def _amOfDoors(self):
      del self.__amOfDoors

    @property
    def _type(self):
      return self.__type
    
    @_type.setter
    def _type(self, new__type):
      self.__type = new__type
  
    @_type.deleter
    def _type(self):
      del self.__type
    
    def printInformation(self):
       super().printInformation()
       print(f"Amount of doors: {self.__amOfDoors}")
       print(f"Type: {self.__type}")


class Storage:
    
    def  __init__(self,lis_of_vehicle):
      self.__list_of_vehicle = lis_of_vehicle

    def __init__(self):
      self.__list_of_vehicle = list()
    
    def add(self, *vehicle):
      for v in vehicle:
        self.__list_of_vehicle.append(v)

    def remove(self,vehicle):
      self.__list_of_vehicle.remove(vehicle)
    
    def get_size(self):
      return len(self.__list_of_vehicle)

    def get_vehicle(self, index) -> Vehicle:
      return self.__list_of_vehicle[index-1]
    
    def printInfo(self) -> None:
      print('---------------------------------------')
      for n in self.__list_of_vehicle:
        print('---------------------------------------')
        n.printInformation()
        print('---------------------------------------')
      print('---------------------------------------')


def main():
    #создание гаража
    garazh = Storage()
  
    motobike = Motobike('Motobike','Red',1500,1200,450.5,0)
    lada = Car('Lada','Black',1000, 150,4,'Legkovaya')
    zhiguli = Car('Zhiguli','Purple',250, 150,4,'Legkovaya')
    bmw = Car('BMW','Red',1000,950,4,'Legkovaya')
    opel = Car('Opel','Black',650, 450,4,'Legkovaya')
    kamaz = Car('KAMAZ','Grey',850,1000,2,'Gruzovaya')
    
    garazh.add(lada,zhiguli,bmw,opel,kamaz,motobike)
    garazh.printInfo()

if __name__ == '__main__':
    main()