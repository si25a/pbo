# UTS PBO BAGIAN B— Coding dan Problem Solving
# Soal B1 — Class dan Encapsulation

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


# Program utama
buku1 = Buku("Harry Potter", "J.K.Rowling")
buku2 = Buku("Sherlock Holmes", "Sir Arthur Conan Doyle")

# Meminjam buku pertama
buku1.pinjam()

# Menampilkan informasi kedua buku
print("Daftar Buku:")
print(buku1)
print(buku2)
