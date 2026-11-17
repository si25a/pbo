class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.__tersedia = True

    def pinjam(self):
        if self.__tersedia:
            self.__tersedia = False
            return True
        else:
            return False

    def kembalikan(self):
        self.__tersedia = True

    @property
    def tersedia(self):
        return self.__tersedia

    def __str__(self):
        if self.__tersedia:
            status = "Tersedia"
        else:
            status = "Dipinjam"

        return f"{self.judul} - {self.penulis} [{status}]"


class BukuDigital(Buku):
    """Subclass BukuDigital yang mewarisi Buku (Inheritance)."""

    def __init__(self, judul, penulis, format_file):
        # 1 & 2. Menggunakan super() untuk memanggil constructor parent dan menambahkan format_file[cite: 12]
        super().__init__(judul, penulis)
        self.format_file = format_file

    def __str__(self):
        # 3. Override method __str__() dengan menambahkan format_file di akhir[cite: 12]
        return f"{super().__str__()} ({self.format_file})"

    def unduh(self):
        # 4. Method unduh() berdasarkan ketersediaan buku[cite: 12]
        if self.tersedia:
            return f"Mengunduh {self.judul} dalam format {self.format_file}."
        else:
            return "Buku tidak tersedia."


def tampilkan_info(daftar_buku):
    """Fungsi polimorfik untuk mencetak informasi dari berbagai tipe object buku[cite: 12]."""
    for buku in daftar_buku:
        print(buku)


# === Program Utama ===
if __name__ == "__main__":
    # Membuat object Buku dan BukuDigital
    buku1 = Buku("Laut Bercerita", "Leila S. Chudori")
    buku_dig1 = BukuDigital("Tulisan Sastra", "Tenderlova", "EPUB")
    buku_dig2 = BukuDigital("Hujan", "Tere Liye", "PDF")

    # Meminjam salah satu buku digital
    buku_dig1.pinjam()

    # Kumpulan object dalam satu list untuk diuji secara polimorfik
    daftar_koleksi = [buku1, buku_dig1, buku_dig2]

    print("=== Menampilkan Info Semua Buku (Polimorfisme) ===")
    tampilkan_info(daftar_koleksi)

    print("\n=== Menguji Method Unduh Buku Digital ===")
    print(buku_dig1.unduh())  # Saat dipinjam
    print(buku_dig2.unduh())  # Saat tersedia
