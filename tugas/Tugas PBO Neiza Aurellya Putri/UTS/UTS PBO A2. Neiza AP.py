#Encapsulation
class Mahasiswa:
    def __init__(self, nama):
        self.__nama = nama

    def tampilkan_nama(self):
        return self.__nama

mhs = Mahasiswa("Budi")
print(mhs.tampilkan_nama())

#Inheritance
class Hewan:
    def makan(self):
        print("Hewan sedang makan")

class Kucing(Hewan):
    pass

kucing = Kucing()
kucing.makan()

#Polymorphism
class Kucing:
    def suara(self):
        print("Meong")

class Anjing:
    def suara(self):
        print("Guk guk")

hewan1 = Kucing()
hewan2 = Anjing()

hewan1.suara()
hewan2.suara()

#Abstraction
from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def berjalan(self):
        pass

class Mobil(Kendaraan):
    def berjalan(self):
        print("Mobil berjalan")

mobil = Mobil()
mobil.berjalan()