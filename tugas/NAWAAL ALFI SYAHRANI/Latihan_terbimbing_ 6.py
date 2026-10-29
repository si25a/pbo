"""
Scaffold latihan terbimbing — Abstraction pada alat elektronik.
"""

from abc import ABC, abstractmethod


class AlatElektronik(ABC):
    """Abstract class yang menetapkan kontrak perilaku alat elektronik."""

    def __init__(self, merek):
        self.merek = merek

    @abstractmethod
    def nyalakan(self):
        # Abstract method: wajib diimplementasikan oleh setiap subclass.
        pass


class Televisi(AlatElektronik):
    # 1. Implementasikan nyalakan() pada Televisi
    def nyalakan(self):
        return f"Televisi {self.merek} menyala"


class Kulkas(AlatElektronik):
    # 2. Implementasikan nyalakan() pada Kulkas
    def nyalakan(self):
        return f"Kulkas {self.merek} menyala"


# 3. Buat satu object Televisi dan satu object Kulkas, lalu panggil nyalakan()
if __name__ == "__main__":
    tv = Televisi("Samsung")
    kulkas = Kulkas("LG")

    print(tv.nyalakan())
    print(kulkas.nyalakan())