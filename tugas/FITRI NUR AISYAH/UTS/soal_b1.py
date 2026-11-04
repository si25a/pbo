class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True                

    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False

    def kembalikan(self):
        self.__tersedia = True

    @property
    def tersedia(self):                       
        return self.__tersedia

    def __str__(self):
        status = "Tersedia" if self.__tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"



if __name__ == "__main__":
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
    buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")

    print("Meminjam buku 1:", buku1.pinjam())  

    print(buku1)   
    print(buku2)   
