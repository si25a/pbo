
# SOAL B2 - INHERITANCE DAN POLYMORPHISM

# CLASS BUKU DARI SOAL B1

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


# SUBCLASS BUKU DIGITAL
# Inheritance: BukuDigital mewarisi class Buku.

class BukuDigital(Buku):
    def __init__(self, judul, penulis, format_file):
        super().__init__(judul, penulis)
        self.format_file = format_file

    # Polymorphism: override method __str__()
    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}] ({self.format_file})"

    def unduh(self):
        if self.tersedia:
            return f"Mengunduh {self.judul} dalam format {self.format_file}."
        else:
            return "Buku tidak tersedia."


# FUNCTION UNTUK MENAMPILKAN INFORMASI BUKU

def tampilkan_info(daftar_buku):
    for buku in daftar_buku:
        print(buku)


# PROGRAM UTAMA

# Membuat object Buku dan BukuDigital
buku_1 = Buku("Laskar Pelangi", "Andrea Hirata")
buku_2 = BukuDigital("Bumi", "Tere Liye", "PDF")

# Menampilkan informasi buku
print("Informasi Buku:")
daftar_buku = [buku_1, buku_2]
tampilkan_info(daftar_buku)

# Menguji method unduh saat buku tersedia
print("\nPercobaan Unduh:")
print(buku_2.unduh())

# Meminjam buku digital
buku_2.pinjam()

# Menguji method unduh saat buku dipinjam
print("\nSetelah Buku Dipinjam:")
print(buku_2.unduh())

# Menampilkan informasi buku setelah dipinjam
print("\nInformasi Buku Terbaru:")
tampilkan_info(daftar_buku)
