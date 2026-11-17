class Buku:
    def __init__(self, judul: str, penulis: str):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True  # Atribut privat

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


if __name__ == "__main__":
    # Membuat dua objek Buku
    buku_1 = Buku("Pemrograman Python", "Budi Santoso")
    buku_2 = Buku("Struktur Data", "Ani Wijaya")

    print("--- Status Awal ---")
    print(buku_1)
    print(buku_2)

    # Meminjam satu buku
    buku_1.pinjam()

    print("\n--- Status Setelah Buku 1 Dipinjam ---")
    print(buku_1)
    print(buku_2)
