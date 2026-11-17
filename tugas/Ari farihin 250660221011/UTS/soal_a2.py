from abc import ABC, abstractmethod


# 4. Abstraction
class Bentuk(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass


# 2. Inheritance & 3. Polymorphism
class Persegi(Bentuk):
    def __init__(self, sisi: float):
        self.__sisi = sisi  # 1. Encapsulation

    def hitung_luas(self) -> float:
        return self.__sisi ** 2


if __name__ == "__main__":
    p = Persegi(5)
    print(f"Luas Persegi: {p.hitung_luas()}")
