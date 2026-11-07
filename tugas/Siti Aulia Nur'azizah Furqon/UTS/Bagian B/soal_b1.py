"""
Soal B1 - Class dan Encapsulation

Buat class Buku dengan ketentuan berikut:
1. Constructor menerima judul (str) dan penulis (str).
2. Attribute tersedia diinisialisasi dengan True dan bersifat privat.
3. Method pinjam() mengubah tersedia menjadi False dan mengembalikan True jika buku tersedia. Jika tidak tersedia, kembalikan False.
4. Method kembalikan() mengubah tersedia menjadi True.
5. Property tersedia mengembalikan status ketersediaan tanpa bisa diubah langsung dari luar class.
6. Method __str__() mengembalikan string berformat: "judul — penulis [Tersedia]" atau "judul — penulis [Dipinjam]".
Tulis program utama yang membuat dua object Buku, meminjam satu buku, dan menampilkan status kedua buku.
"""

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

    def kembalikan(self):
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
    buku2 = Buku("Struktur Data", "Budi Raharjo")

    print("--- Status Awal ---")
    print(buku1)
    print(buku2)

    print("\n--- Meminjam Buku 1 ---")
    buku1.pinjam()

    print("\n--- Status Akhir ---")
    print(buku1)
    print(buku2)