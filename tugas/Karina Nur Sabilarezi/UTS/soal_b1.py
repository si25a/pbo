
# SOAL B1 - CLASS DAN ENCAPSULATION

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True

    @property
    def tersedia(self):
        return self.__tersedia

    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            return True
        else:
            return False

    def kembalikan(self):
        self.__tersedia = True

    def __str__(self):
        status = "Tersedia" if self.__tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"


# PROGRAM UTAMA

# Membuat dua object Buku
buku_1 = Buku("Laskar Pelangi", "Andrea Hirata")
buku_2 = Buku("Bumi", "Tere Liye")

# Meminjam buku pertama
if buku_1.pinjam():
    print("Buku berhasil dipinjam.")
else:
    print("Buku tidak tersedia.")

# Menampilkan status kedua buku
print("\nStatus Buku:")
print(buku_1)
print(buku_2)
