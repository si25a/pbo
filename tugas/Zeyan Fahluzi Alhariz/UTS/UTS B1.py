class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True          # attribute privat

    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False

    def kembalikan(self):
        self.__tersedia = True

    @property
    def tersedia(self):                 # read-only dari luar class
        return self.__tersedia

    def __str__(self):
        status = "Tersedia" if self.__tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"


# Program utama
if __name__ == "__main__":
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
    buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")

    buku1.pinjam()

    print(buku1)
    print(buku2)