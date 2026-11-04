# Soal B2 — Inheritance dan Polymorphism
# File: soal_b2.py

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
        # Polimorfisme: Memanggil __str__() tanpa pengecekan tipe eksplisit
        print(buku)


# Program Utama
if __name__ == "__main__":
    buku_cetak = Buku("Struktur Data", "Alice Smith")
    buku_digital = BukuDigital("Jaringan Komputer", "Bob Martin", "PDF")

    # Uji peminjaman buku digital
    buku_digital.pinjam()

    daftar = [buku_cetak, buku_digital]

    print("--- Daftar Buku (Polimorfisme) ---")
    tampilkan_info(daftar)
