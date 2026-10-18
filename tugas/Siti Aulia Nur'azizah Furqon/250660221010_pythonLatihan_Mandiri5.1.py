"""Latihan terbimbing: Polymorphism pada hewan."""


class Hewan:
    """Superclass yang merepresentasikan hewan secara umum."""

    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."  # method dasar yang akan dioverride oleh subclass


class Kucing(Hewan):
    # 1. Override method suara() pada Kucing mengembalikan "Meong".
    def suara(self):
        return "Meong"


class Anjing(Hewan):
    # 2. Override method suara() pada Anjing mengembalikan "Guk".
    def suara(self):
        return "Guk"


# 3. Buat fungsi tampilkan_suara(daftar) yang memanggil suara() pada setiap object.
def tampilkan_suara(daftar):
    for hewan in daftar:
        print(f"{hewan.nama} bersuara: {hewan.suara()}")


# 4. Uji fungsi dengan minimal satu object Kucing dan satu object Anjing.
if __name__ == "__main__":
    print("--- Uji Coba Latihan Hewan ---")
    daftar_hewan = [
        Kucing("Jerry"),
        Anjing("Boni")
    ]
    tampilkan_suara(daftar_hewan)
    print()
