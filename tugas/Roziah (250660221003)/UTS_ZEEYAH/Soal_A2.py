from abc import ABC, abstractmethod


# 4. Abstraction (Abstraksi)
class Bentuk(ABC):

  @abstractmethod
  def hitung_luas(self):
    pass


# 2. Inheritance (Pewarisan) & 1. Encapsulation (Enkapsulasi)
class Persegi(Bentuk):

  def __init__(self, sisi):
    self.__sisi = sisi  # Atribut privat (Encapsulation)

  # Getter untuk mengakses atribut privat
  @property
  def sisi(self):
    return self.__sisi

  def hitung_luas(self):  # 3. Polymorphism (Polimorfisme)
    return self.__sisi ** 2


# Class lain untuk demonstrasi Polymorphism
class Lingkaran(Bentuk):

  def __init__(self, jari_jari):
    self.__jari_jari = jari_jari

  def hitung_luas(self):  # Method yang sama, implementasi berbeda
    return 3.14159 * (self.__jari_jari ** 2)


# Program Utama / Demonstrasi
if __name__ == "__main__":
  # Membuat objek dari class turunan
  kotak = Persegi(4)
  bulat = Lingkaran(7)

  print("=== Demonstrasi Pilar OOP ===")
  print(f"Luas Persegi (sisi = {kotak.sisi}): {kotak.hitung_luas()}")
  print(f"Luas Lingkaran: {bulat.hitung_luas():.2f}")
