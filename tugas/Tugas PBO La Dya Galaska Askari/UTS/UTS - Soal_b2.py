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
    b1 = Buku("Malioboro at Midnight", "Skyphire")
    b2 = BukuDigital("Thesis & Tension", "Liara Audrina", "EPUB")
    
    b2.pinjam()
    
    pustaka = [b1, b2]
    tampilkan_info(pustaka)
    print(b2.unduh())