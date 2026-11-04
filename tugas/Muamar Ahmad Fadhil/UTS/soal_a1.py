# Soal A1 — Konsep Dasar OOP
# File: soal_a1.py

# 1. class: Blueprint/templat untuk membuat objek
class Laptop:
    # 5. constructor: Method khusus untuk inisialisasi atribut saat objek dibuat
    def __init__(self, merk: str, ram: int):
        # 3. attribute: Variabel yang menyimpan data/state objek
        self.merk = merk
        self.ram = ram

    # 4. method: Fungsi yang menentukan perilaku/behavior objek
    def tampilkan_spesifikasi(self) -> str:
        return f"Laptop {self.merk} dengan RAM {self.ram}GB"

if __name__ == "__main__":
    # 2. object: Instansiasi nyata dari class
    laptop_fadhil = Laptop("Lenovo", 16)
    print(laptop_fadhil.tampilkan_spesifikasi())
