"""Scaffold latihan mandiri — Analisis pengelolaan data buku."""


def tambah_buku(daftar_buku, judul, penulis):
    # LATIHAN 1: tambahkan dictionary buku ke daftar_buku.
    buku = {"judul": judul, "penulis": penulis}
    daftar_buku.append(buku)


def tampilkan_buku(daftar_buku):
    # LATIHAN 2: tampilkan seluruh buku dalam daftar_buku.
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. Judul: {buku['judul']}, Penulis: {buku['penulis']}")


def hapus_buku(daftar_buku, judul):
    # LATIHAN 3: hapus buku dengan judul tertentu dari daftar_buku.
    for buku in daftar_buku:
        if buku["judul"].lower() == judul.lower():
            daftar_buku.remove(buku)
            break


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

    def tampilkan_semua(self):
        # LATIHAN 8: tampilkan seluruh buku dalam koleksi.
        for i, buku in enumerate(self.daftar_buku, 1):
            print(f"{i}.", end=" ")
            buku.tampilkan()


if __name__ == "__main__":
    print("=== UJI PENDEKATAN PROSEDURAL ===")
    perpus_prosedural = []
    tambah_buku(perpus_prosedural, "Belajar Python", "Dya")
    tambah_buku(perpus_prosedural, "Struktur Data", "Fadlan")
    tampilkan_buku(perpus_prosedural)
    
    print("\nMenghapus buku 'Belajar Python'...")
    hapus_buku(perpus_prosedural, "Belajar Python")
    tampilkan_buku(perpus_prosedural)

    print("\n=== UJI PENDEKATAN OBJECT-ORIENTED PROGRAMMING (OOP) ===")
    koleksi = KoleksiBuku()
    buku_1 = Buku("Belajar Python", "Dya")
    buku_2 = Buku("Struktur Data", "Fadlan")
    koleksi.tambah(buku_1)
    koleksi.tambah(buku_2)
    koleksi.tampilkan_semua()