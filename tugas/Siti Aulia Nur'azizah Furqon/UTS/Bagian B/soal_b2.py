"""
Soal B2 — Inheritance dan Polymorphism

Diberikan class Buku dari Soal B1. Buat subclass BukuDigital dengan ketentuan berikut:
1. Subclass mewarisi Buku dan menambahkan attribute format_file (str, misalnya "PDF" atau "EPUB").
2. Constructor menggunakan super() untuk memanggil constructor parent.
3. Override method __str__() sehingga formatnya menjadi: "judul — penulis [Dipinjam] (format_file)".
4. Method unduh() mengembalikan string "Mengunduh judul dalam format format_file." jika buku tersedia, dan "Buku tidak tersedia." jika sedang dipinjam.
Selanjutnya, tulis fungsi tampilkan_info(daftar_buku) yang menerima list berisi object Buku dan BukuDigital, lalu mencetak __str__() dari setiap object. Fungsi ini harus bekerja untuk kedua tipe object tanpa pengecekan tipe eksplisit.
"""
# Jawaban:
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


def tampilkan_info(daftar_buku):
    for buku in daftar_buku:
        print(buku)  # Memanggil __str__() secara eksplisit via polymorphism


# Program Utama
if __name__ == "__main__":
    b1 = Buku("Laskar Pelangi", "Andrea Hirata")
    b2 = BukuDigital("Clean Code", "Robert C. Martin", "PDF")
    b3 = BukuDigital("The Pragmatic Programmer", "Andrew Hunt", "EPUB")

    b2.pinjam()  # Meminjam buku digital 1

    daftar = [b1, b2, b3]
    print("--- Daftar Buku (Polymorphism) ---")
    tampilkan_info(daftar)

    print("\n--- Uji Method Unduh ---")
    print(b2.unduh())
    print(b3.unduh())