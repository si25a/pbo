# Soal B1 — Class dan Encapsulation
class Buku:
    def __init__(self, judul: str, penulis: str):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True

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

if __name__ == "__main__":
    b1 = Buku("Algoritma Pemrograman", "Rinaldi Munir")
    b2 = Buku("Jaringan Komputer", "Andrew S. Tanenbaum")
    print("--- Status Awal ---")
    print(b1)
    print(b2)

    print("\n--- Meminjam Buku 1 ---")
    b1.pinjam()
    print("--- Status Akhir ---")
    print(b1)
    print(b2)
