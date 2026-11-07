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
        return f"{super().__str__()} ({self.format_file})"

    def unduh(self):
        if self.tersedia:
            return f"Mengunduh {self.judul} dalam format {self.format_file}."
        return "Buku tidak tersedia."


def tampilkan_info(daftar_buku):
    for buku in daftar_buku:
        print(buku)


# Program utama
b1 = Buku("Negeri 5 Menara", "Ahmad Fuadi")
b2 = BukuDigital("Filosofi Teras", "Henry Manampiring", "PDF")

b2.pinjam()

tampilkan_info([b1, b2])
# Negeri 5 Menara — Ahmad Fuadi [Tersedia]
# Filosofi Teras — Henry Manampiring [Dipinjam] (PDF)

print(b2.unduh())  # Buku tidak tersedia.