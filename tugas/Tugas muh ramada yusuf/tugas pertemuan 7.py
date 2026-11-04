"""
Latihan Mandiri 7
Perbandingan pendekatan prosedural dan berorientasi objek
untuk pengelolaan data buku.
"""


# ============================================================
# A. PENDEKATAN PROSEDURAL
# ============================================================

def tambah_buku_prosedural(daftar_buku, judul, penulis, tahun):
    """Menambahkan data buku ke daftar berbentuk list of dictionary."""
    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
    }
    daftar_buku.append(buku)
    print(f'Buku "{judul}" berhasil ditambahkan.')


def tampilkan_buku_prosedural(daftar_buku):
    """Menampilkan semua buku dalam daftar."""
    if not daftar_buku:
        print("Belum ada data buku.")
        return

    print("\nDaftar Buku (Prosedural)")
    for nomor, buku in enumerate(daftar_buku, start=1):
        print(
            f'{nomor}. {buku["judul"]} | '
            f'Penulis: {buku["penulis"]} | '
            f'Tahun: {buku["tahun"]}'
        )


def hapus_buku_prosedural(daftar_buku, judul):
    """Menghapus buku berdasarkan judul."""
    for buku in daftar_buku:
        if buku["judul"].casefold() == judul.casefold():
            daftar_buku.remove(buku)
            print(f'Buku "{judul}" berhasil dihapus.')
            return

    print(f'Buku "{judul}" tidak ditemukan.')


# ============================================================
# B. PENDEKATAN BERORIENTASI OBJEK (OOP)
# ============================================================

class Buku:
    """Mewakili satu buku beserta atributnya."""

    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"{self.judul} | Penulis: {self.penulis} | Tahun: {self.tahun}"


class KoleksiBuku:
    """Mengelola kumpulan objek Buku."""

    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        if not isinstance(buku, Buku):
            raise TypeError("Data yang ditambahkan harus berupa objek Buku.")
        self.daftar_buku.append(buku)
        print(f'Buku "{buku.judul}" berhasil ditambahkan.')

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Belum ada data buku.")
            return

        print("\nDaftar Buku (OOP)")
        for nomor, buku in enumerate(self.daftar_buku, start=1):
            print(f"{nomor}. {buku}")

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul.casefold() == judul.casefold():
                self.daftar_buku.remove(buku)
                print(f'Buku "{judul}" berhasil dihapus.')
                return

        print(f'Buku "{judul}" tidak ditemukan.')


# ============================================================
# C. PENGUJIAN KEDUA PENDEKATAN
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("A. PENGUJIAN PENDEKATAN PROSEDURAL")
    print("=" * 55)

    data_buku = []
    tambah_buku_prosedural(
        data_buku, "Belajar Python", "fikri maulana", 2024
    )
    tambah_buku_prosedural(
        data_buku, "Dasar Pemrograman", "rahma", 2023
    )
    tampilkan_buku_prosedural(data_buku)
    hapus_buku_prosedural(data_buku, "Dasar Pemrograman")
    tampilkan_buku_prosedural(data_buku)

    print("\n" + "=" * 55)
    print("B. PENGUJIAN PENDEKATAN OOP")
    print("=" * 55)

    koleksi = KoleksiBuku()
    koleksi.tambah_buku(Buku("Belajar Python", "fikri maulana", 2024))
    koleksi.tambah_buku(Buku("Dasar Pemrograman", " Rahma", 2023))
    koleksi.tampilkan_buku()
    koleksi.hapus_buku("Dasar Pemrograman")
    koleksi.tampilkan_buku()

    print("\n" + "=" * 55)
    print("C. PERBANDINGAN DAN ANALISIS")
    print("=" * 55)
    print(
        "Prosedural: data disimpan sebagai dictionary dalam list, "
        "sedangkan perilaku diatur oleh fungsi terpisah."
    )
    print(
        "OOP: data tiap buku disimpan dalam objek Buku, sedangkan "
        "KoleksiBuku mengelola operasi tambah, tampil, dan hapus."
    )
    print(
        "Kesimpulan: OOP lebih tepat untuk sistem perpustakaan yang "
        "berkembang karena tanggung jawab lebih terstruktur, data dan "
        "perilaku dikelompokkan, serta lebih mudah diperluas dengan fitur "
        "pencarian, peminjaman, stok, dan kategori."
    )
