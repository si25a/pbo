"""Scaffold latihan mandiri — Analisis pengelolaan data buku."""


# ==========================================
# PENDEKATAN PROSEDURAL
# ==========================================


def tambah_buku(daftar_buku, judul, penulis):
    """Latihan 1: tambahkan dictionary buku ke daftar_buku."""
    daftar_buku.append({"judul": judul, "penulis": penulis})


def tampilkan_buku(daftar_buku):
    """Latihan 2: tampilkan seluruh buku dalam daftar_buku."""
    if not daftar_buku:
        print("Daftar buku kosong.")
        return
    for buku in daftar_buku:
        print(f"- Judul: {buku['judul']} | Penulis: {buku['penulis']}")


def hapus_buku(daftar_buku, judul):
    """Latihan 3: hapus buku dengan judul tertentu dari daftar_buku."""
    for buku in daftar_buku:
        if buku["judul"].lower() == judul.lower():
            daftar_buku.remove(buku)
            print(f"Buku '{judul}' berhasil dihapus.")
            return
    print(f"Buku '{judul}' tidak ditemukan.")


# ==========================================
# PENDEKATAN OBJECT-ORIENTED PROGRAMMING (OOP)
# ==========================================


class Buku:
    """Class yang menggabungkan data dan perilaku buku."""

    def __init__(self, judul, penulis):
        # Latihan 4: simpan judul dan penulis sebagai attribute.
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        # Latihan 5: tampilkan judul dan penulis buku.
        print(f"- Judul: {self.judul} | Penulis: {self.penulis}")


class KoleksiBuku:
    """Class yang mengelola daftar object Buku."""

    def __init__(self):
        # Latihan 6: siapkan list kosong untuk menyimpan object Buku.
        self.daftar_buku = []

    def tambah(self, buku):
        # Latihan 7: tambah object Buku ke dalam koleksi.
        self.daftar_buku.append(buku)

    def tampilkan_semua(self):
        # Latihan 8: tampilkan seluruh buku dalam koleksi.
        if not self.daftar_buku:
            print("Koleksi buku kosong.")
            return
        for buku in self.daftar_buku:
            buku.tampilkan()


# ==========================================
# UJI COBA KEDUA PENDEKATAN
# ==========================================
if __name__ == "__main__":
    print("=== 1. PENGUJIAN PENDEKATAN PROSEDURAL ===")
    library_procedural = []
    tambah_buku(library_procedural, "Analisis dan Perancangan Sistem", "Jogiyanto H.")
    tambah_buku(library_procedural, "Sistem Manajemen Basis Data", "Rosa A.S.")
    tampilkan_buku(library_procedural)

    print("\nMenghapus buku...")
    hapus_buku(library_procedural, "Analisis dan Perancangan Sistem")
    print("Daftar buku setelah penghapusan:")
    tampilkan_buku(library_procedural)

    print("\n=== 2. PENGUJIAN PENDEKATAN OOP ===")
    koleksi = KoleksiBuku()
    buku1 = Buku("Analisis dan Perancangan Sistem", "Jogiyanto H.")
    buku2 = Buku("Sistem Manajemen Basis Data", "Rosa A.S.")

    koleksi.tambah(buku1)
    koleksi.tambah(buku2)
    koleksi.tampilkan_semua()

#jawaban Analisis
#(Pendekatan mana yang lebih tepat untuk sistem perpustakaan yang berkembang, beserta alasan teknisnya?)
#Pendekatan Berorientasi Objek (OOP) jauh lebih tepat dan ideal untuk sistem perpustakaan yang berkembang (misalnya sistem yang mengelola buku seperti #"Analisis dan Perancangan Sistem" atau #"Sistem Manajemen Basis Data").
#Alasan Teknis:
#1. Modularitas dan Enkapsulasi: Dalam OOP, atribut buku (`judul`, `penulis`) dan perilakunya (`tampilkan()`) dibungkus menjadi satu kesatuan di dalam class `Buku`. Ketika sistem perpustakaan diperluas untuk mengelola atribut baru (seperti status peminjaman, ISBN, atau denda keterlambatan), kita cukup memodifikasi class terkait tanpa merusak alur fungsi global.
#2. Skalabilitas Data: Class 'KoleksiBuku' bertindak sebagai pengelola (manager) yang bersih. Jika nantinya sistem perpustakaan butuh fitur tambahan seperti pencarian buku berdasarkan penulis atau pengurutan berdasarkan tahun, kita bisa menambahkan method baru ke dalam class tanpa membuat kode menjadi rumit atau sulit dibaca, berbeda dengan pendekatan prosedural yang memisahkan data (menggunakan 'dictionary' mentah) dari logikanya.
