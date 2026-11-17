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


class BukuDigital(Buku):
    def __init__(self, judul: str, penulis: str, format_file: str):
        super().__init__(judul, penulis)
        self.format_file = format_file

    def __str__(self) -> str:
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}] ({self.format_file})"

    def unduh(self) -> str:
        if self.tersedia:
            return f"Mengunduh {self.judul} dalam format {self.format_file}."
        return "Buku tidak tersedia."


def tampilkan_info(daftar_buku):
    for buku in daftar_buku:
        print(buku)


if __name__ == "__main__":
    buku_fisik = Buku("Algoritma Pemrograman", "Joko")
    buku_dig = BukuDigital("Machine Learning Dasar", "Siti", "PDF")

    buku_dig.pinjam()  # Simulasi buku digital sedang dipinjam

    daftar_koleksi = [buku_fisik, buku_dig]

    print("--- Informasi Daftar Buku (Polimorfisme) ---")
    tampilkan_info(daftar_koleksi)

    print("\n--- Uji Method Unduh ---")
    buku_dig.kembalikan()  # Dikembalikan agar tersedia kembali
    print(buku_dig.unduh())
