class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True        # privat

    def pinjam(self):                  # method
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False

    def kembalikan(self):           # method 
        self.__tersedia = True

    @property
    def tersedia(self):               # property
        return self.__tersedia

    def __str__(self):
        status = "Tersedia" if self.__tersedia else "Dipinjam"  #method
        return f"{self.judul} — {self.penulis} [{status}]"


# Program utama
buku1 = Buku("Negeri 5 Menara", "Ahmad Fuadi")
buku2 = Buku("Filosofi Teras", "Henry Manampiring")

buku1.pinjam()

print(buku1)  # Negeri 5 Menara — Ahmad Fuadi [Dipinjam]
print(buku2)  # Filosofi Teras — Henry Manampiring [Tersedia]