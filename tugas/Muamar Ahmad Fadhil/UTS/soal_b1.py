# Soal B1 — Class dan Encapsulation
# File: soal_b1.py

class Buku:
    def __init__(self, judul: str, penulis: str):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True  # Attribute privat

    def pinjam(self) -> bool:
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False

    def kembalikan(self) -> None:
        self.__tersedia = True

    @property
    def tersedia(self) -> bool:
        return self.__tersedia

    def __str__(self) -> str:
        status = "Tersedia" if self.__tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"


# Program Utama
if __name__ == "__main__":
    buku1 = Buku("Pemrograman Python", "Guido van Rossum")
    buku2 = Buku("Sistem Informasi Modern", "John Doe")

    print("--- Status Awal ---")
    print(buku1)
    print(buku2)

    print("Meminjam Buku 1 ---")
    hasil_pinjam = buku1.pinjam()
    print(f"Status peminjaman: {hasil_pinjam}")

    print("Status Akhir ---")
    print(buku1)
    print(buku2)
