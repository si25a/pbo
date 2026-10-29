"""Scaffold latihan mandiri — Analisis pengelolaan data buku."""


# ==========================================
# PENDEKATAN PROSEDURAL
# ==========================================


def tambah_buku(daftar_buku, judul, penulis):
    # LATIHAN 1: tambahkan dictionary buku ke daftar_buku.
    daftar_buku.append({"judul": judul, "penulis": penulis})


def tampilkan_buku(daftar_buku):
    # LATIHAN 2: tampilkan seluruh buku dalam daftar_buku.
    if not daftar_buku:
        print("Daftar buku kosong.")
        return
    for idx, buku in enumerate(daftar_buku, start=1):
        print(f"{idx}. Judul: {buku['judul']}, Penulis: {buku['penulis']}")


def hapus_buku(daftar_buku, judul):
    # LATIHAN 3: hapus buku dengan judul tertentu dari daftar_buku.
    for buku in daftar_buku:
        if buku["judul"].lower() == judul.lower():
            daftar_buku.remove(buku)
            print(f"Buku '{judul}' berhasil dihapus.")
            return
    print(f"Buku '{judul}' tidak ditemukan.")


# ==========================================
# PENDEKATAN OBJECT-ORIENTED (OOP)
# ==========================================


class Buku:
    """Class yang menggabungkan data dan perilaku buku."""

    def __init__(self, judul, penulis):
        # LATIHAN 4: simpan judul dan penulis sebagai attribute.
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        # LATIHAN 5: tampilkan judul dan penulis buku.
        print(f"Judul: {self.judul}, Penulis: {self.penulis}")


class KoleksiBuku:
    """Class yang mengelola daftar object Buku."""

    def __init__(self):
        # LATIHAN 6: siapkan list kosong untuk menyimpan object Buku.
        self.daftar_buku = []

    def tambah(self, buku):
        # LATIHAN 7: tambahkan object Buku ke dalam koleksi.
        self.daftar_buku.append(buku)

    def hapus(self, judul):
        """Fitur tambahan untuk menghapus buku berdasarkan judul."""
        for buku in self.daftar_buku:
            if buku.judul.lower() == judul.lower():
                self.daftar_buku.remove(buku)
                print(f"Buku '{judul}' berhasil dihapus dari koleksi.")
                return
        print(f"Buku '{judul}' tidak ditemukan dalam koleksi.")

    def tampilkan_semua(self):
        # LATIHAN 8: tampilkan seluruh buku dalam koleksi.
        if not self.daftar_buku:
            print("Koleksi buku kosong.")
            return
        for idx, buku in enumerate(self.daftar_buku, start=1):
            print(f"{idx}. ", end="")
            buku.tampilkan()


# ==========================================
# PENGUJIAN & ANALISIS
# ==========================================

if __name__ == "__main__":
    print("=== 1. UJI PENDEKATAN PROSEDURAL ===")
    koleksi_prosedural = []
    tambah_buku(koleksi_prosedural, "Laskar Pelangi", "Andrea Hirata")
    tambah_buku(koleksi_prosedural, "Bumi Manusia", "Pramoedya Ananta Toer")

    print("Daftar Buku Awal:")
    tampilkan_buku(koleksi_prosedural)

    print("\nMenghapus 'Laskar Pelangi':")
    hapus_buku(koleksi_prosedural, "Laskar Pelangi")

    print("Daftar Buku Setelah Penghapusan:")
    tampilkan_buku(koleksi_prosedural)

    print("\n" + "=" * 40 + "\n")

    print("=== 2. UJI PENDEKATAN OOP ===")
    koleksi_oop = KoleksiBuku()
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
    buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")

    koleksi_oop.tambah(buku1)
    koleksi_oop.tambah(buku2)

    print("Daftar Koleksi Buku Awal:")
    koleksi_oop.tampilkan_semua()

    print("\nMenghapus 'Laskar Pelangi':")
    koleksi_oop.hapus("Laskar Pelangi")

    print("Daftar Koleksi Buku Setelah Penghapusan:")
    koleksi_oop.tampilkan_semua()

    print("\n" + "=" * 40 + "\n")

    print("=== 3. ANALISIS TEKNIS ===")
    print(
        """
Pendekatan yang Lebih Tepat untuk Sistem Perpustakaan Berkemang:
-> PENDEKATAN OBJECT-ORIENTED PROGRAMMING (OOP)

Alasan Teknis:
1. Enkapsulasi & Validasi Data:
   Pada OOP, data buku terikat dalam kelas `Buku`. Jika sistem berkembang (misalnya
   menambahkan status peminjaman, ISBN, atau denda), logika validasi dan pengubah status
   dapat disembunyikan di dalam class `Buku` tanpa mengganggu struktur koleksi.

2. Skalabilitas & Modul
   Class `KoleksiBuku` memisahkan tanggung jawab pengelolaan daftar dengan entitas `Buku` itu
   sendiri (Single Responsibility Principle). Menambahkan fitur pencarian, penyaringan,
   atau pengurutan cukup dilakukan di dalam class `KoleksiBuku`.

3. Reusabilitas & Pewarisan (Inheritance):
   Jika sistem perpustakaan menambah entitas baru seperti `BukuDigital` atau `Majalah`, 
   pendekatan OOP memungkinkan kita melakukan inheritance dari class `Buku` tanpa harus
   membuat ulang struktur data baru.

4. Integritas Data:
   Pada pendekatan prosedural, data buku berupa dictionary rentan berubah struktur 
   (misal key typo: 'judull' vs 'judul') karena tidak ada struktur acuan yang kaku.
"""
    )