from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):                       
        return self.sisi ** 2

p = Persegi(4)
print(p.luas())        
