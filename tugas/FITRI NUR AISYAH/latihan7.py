# ==========================================
# PENDEKATAN PROSEDURAL
# ==========================================


def tambah_buku(daftar_buku, judul, penulis):
    daftar_buku.append({"judul": judul, "penulis": penulis})


def tampilkan_buku(daftar_buku):
    if not daftar_buku:
        print("Daftar buku kosong.")
        return
    for i, buku in enumerate(daftar_buku, 1):
        print(f"{i}. Judul: {buku['judul']} | Penulis: {buku['penulis']}")


def hapus_buku(daftar_buku, judul):
    daftar_buku[:] = [
        b for b in daftar_buku if b["judul"].lower() != judul.lower()
    ]


# ==========================================
# PENDEKATAN BERORIENTASI OBJEK (OOP)
# ==========================================


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        print(f"Judul: {self.judul} | Penulis: {self.penulis}")


class KoleksiBuku:
    def __init__(self):
        self.daftar_buku = []

    def tambah(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_semua(self):
        if not self.daftar_buku:
            print("Koleksi buku kosong.")
            return
        for i, buku in enumerate(self.daftar_buku, 1):
            print(f"{i}.", end=" ")
            buku.tampilkan()

if __name__ == "__main__":
    print("=== 1. Pengujian Pendekatan Prosedural ===")
    perpustakaan_prosedural = []
    tambah_buku(perpustakaan_prosedural, "Phyton untuk Pemula", "Fitri Nur Aisyah")
    tambah_buku(perpustakaan_prosedural, "Algoritma", "Aisyah")
    tampilkan_buku(perpustakaan_prosedural)

    print("\nMenghapus 'Belajar Python'...")
    hapus_buku(perpustakaan_prosedural, "Phyton untuk Pemula")
    tampilkan_buku(perpustakaan_prosedural)

    print("\n=== 2. Pengujian Pendekatan OOP ===")
    perpus_oop = KoleksiBuku()
    buku1 = Buku("Phyton untuk Pemula", "Fitri Nur Aisyah")
    buku2 = Buku("Algoritma", "Aisyah")

    perpus_oop.tambah(buku1)
    perpus_oop.tambah(buku2)
    perpus_oop.tampilkan_semua()