"""Scaffold latihan persiapan UTS — Gabungan konsep dasar OOP.

File ini berisi latihan bertahap yang menggabungkan:
1. Class, object, attribute, method, dan constructor.
2. Encapsulation dengan attribute privat dan property.
3. Inheritance menggunakan super() dan overriding.
4. Polymorphism melalui pemrosesan object beragam tipe.
"""


class Buku:
    """Class dasar untuk merepresentasikan buku dalam perpustakaan."""

    def __init__(self, judul, penulis):
        # LATIHAN 1: Simpan judul dan penulis sebagai attribute.
        # Buat attribute privat __tersedia dengan nilai awal True.
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True

    def pinjam(self):
        # LATIHAN 2: Jika buku tersedia, ubah __tersedia menjadi False dan kembalikan True.
        # Jika tidak tersedia, kembalikan False.
        if self.__tersedia:
            self.__tersedia = False
            return True
        return False

    def kembalikan(self):
        # LATIHAN 3: Ubah __tersedia menjadi True.
        self.__tersedia = True

    @property
    def tersedia(self):
        # LATIHAN 4: Kembalikan nilai attribute __tersedia.
        return self.__tersedia

    def __str__(self):
        # LATIHAN 5: Kembalikan string berformat: "judul — penulis [Tersedia/Dipinjam]".
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} — {self.penulis} [{status}]"


class BukuDigital(Buku):
    """Subclass yang merepresentasikan buku elektronik."""

    def __init__(self, judul, penulis, format_file):
        # LATIHAN 6: Panggil constructor superclass menggunakan super().
        # Simpan format_file sebagai attribute.
        super().__init__(judul, penulis)
        self.format_file = format_file

    def __str__(self):
        # LATIHAN 7: Override method __str__ untuk menambahkan format_file di akhir.
        # Format: "judul — penulis [Tersedia/Dipinjam] (format_file)".
        return f"{super().__str__()} ({self.format_file})"

    def unduh(self):
        # LATIHAN 8: Jika buku tersedia, kembalikan "Mengunduh <judul> dalam format <format_file>."
        # Jika tidak tersedia, kembalikan "Buku tidak tersedia."
        if self.tersedia:
            return f"Mengunduh {self.judul} dalam format {self.format_file}."
        return "Buku tidak tersedia."


def tampilkan_daftar_buku(daftar_buku):
    """Fungsi polimorfik untuk menampilkan status buku dari berbagai tipe."""
    # LATIHAN 9: Lakukan perulangan pada daftar_buku dan cetak setiap object.
    for buku in daftar_buku:
        print(buku)


# === Program utama ===
if __name__ == "__main__":
    print("Lengkapi bagian bertanda LATIHAN, lalu jalankan kembali program ini.")
    daftar_buku = []
    buku1 = Buku("Python untuk Pemula", "Andi")
    buku2 = BukuDigital("Belajar Data Science", "Budi", "PDF")
    daftar_buku.append(buku1)
    daftar_buku.append(buku2)
    tampilkan_daftar_buku(daftar_buku)