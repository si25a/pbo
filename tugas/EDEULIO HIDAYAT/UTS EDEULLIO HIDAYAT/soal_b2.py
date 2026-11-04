# Soal B2 — Inheritance dan Polymorphism
from soal_b1 import Buku

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

def tampilkan_info(daftar_buku: list):
    for buku in daftar_buku:
        print(buku)

if __name__ == "__main__":
    buku_cetak = Buku("Sistem Operasi", "Silberschatz")
    buku_pdf = BukuDigital("Kriptografi", "Stallings", "PDF")
    buku_pdf.pinjam()

    tampilkan_info([buku_cetak, buku_pdf])
