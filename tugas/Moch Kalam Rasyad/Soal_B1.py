
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True

    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            return True
        else:
            return False

    def kembalikan(self):
        self.__tersedia = True

    @property
    def tersedia(self):
        return self.__tersedia

    def __str__(self):
        if self.__tersedia:
            status = "Tersedia"
        else:
            status = "Dipinjam"

        return f"{self.judul} - {self.penulis} [{status}]"


# Program utama
buku1 = Buku("Laut Bercerita", "Lea S. Chudori")
buku2 = Buku("Hujan", "Tere Liye")

# Meminjam satu buku
buku1.pinjam()

# Menampilkan status kedua buku
print(buku1)
print(buku2)
