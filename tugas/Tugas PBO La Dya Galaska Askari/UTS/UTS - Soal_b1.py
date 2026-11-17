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

    def kembalikan(self):
        self.__tersedia = True

    @property
    def tersedia(self) -> bool:
        return self.__tersedia

    def __str__(self) -> str:
        status = "Tersedia" if self.__tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"

if __name__ == "__main__":
    buku1 = Buku("Malioboro at Midnight", "Skyphire")
    buku2 = Buku("Thesis & Tension", "Liara Audrina")

    buku1.pinjam()

    print(buku1)
    print(buku2)