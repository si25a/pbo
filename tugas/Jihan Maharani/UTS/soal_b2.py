# UTS PBO BAGIAN B — Coding dan Problem Solving
# Soal B2 — Inheritance dan Polymorphism 

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


class BukuDigital(Buku):
    def __init__(self, judul, penulis, format_file):
        super().__init__(judul, penulis)
        self.format_file = format_file

    def __str__(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return (
            f"{self.judul} — {self.penulis} "
            f"[{status}] ({self.format_file})"
        )

    def unduh(self):
        if self.tersedia:
            return (
                f"Mengunduh {self.judul} "
                f"dalam format {self.format_file}."
            )
        return "Buku tidak tersedia."


def tampilkan_info(daftar_buku):
    for buku in daftar_buku:
        print(buku)


# Program utama
buku1 = Buku("Harry Potter", "J.K.Rowling")
buku2 = BukuDigital("Sherlock Holmes", "Sir Arthur Conan Doyle ", "PDF")

daftar_buku = [buku1, buku2]

# Meminjam buku digital
buku2.pinjam()

# Menampilkan informasi buku
tampilkan_info(daftar_buku)

# Mengunduh buku digital
print(buku2.unduh())