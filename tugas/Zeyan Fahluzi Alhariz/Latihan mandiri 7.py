"""Scaffold latihan mandiri - Analisis pengelolaan data buku."""

# --- PENDEKATAN PROSEDURAL ---

def tambah_buku(daftar_buku, judul, penulis):
    # LATIHAN 1: tambahkan dictionary buku ke daftar_buku.
    buku_baru = {"judul": judul, "penulis": penulis}
    daftar_buku.append(buku_baru)


def tampilkan_buku(daftar_buku):
    # LATIHAN 2: tampilkan seluruh buku dalam daftar_buku.
    print("Daftar Buku (Prosedural):")
    for buku in daftar_buku:
        print(f"- {buku['judul']} oleh {buku['penulis']}")


def hapus_buku(daftar_buku, judul):
    # LATIHAN 3: hapus buku dengan judul tertentu dari daftar_buku.
    for buku in daftar_buku:
        if buku["judul"] == judul:
            daftar_buku.remove(buku)
            break


# --- PENDEKATAN BERORIENTASI OBJEK (OOP) ---

class Buku:
    """Class yang menggabungkan data dan perilaku buku."""

    def __init__(self, judul, penulis):
        # LATIHAN 4: simpan judul dan penulis sebagai attribute.
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        # LATIHAN 5: tampilkan judul dan penulis buku.
        print(f"- {self.judul} oleh {self.penulis}")


class KoleksiBuku:
    """Class yang mengelola daftar object Buku."""

    def __init__(self):
        # LATIHAN 6: siapkan list kosong untuk menyimpan object Buku.
        self.koleksi = []

    def tambah(self, buku):
        # LATIHAN 7: tambahkan object Buku ke dalam koleksi.
        self.koleksi.append(buku)

    def tampilkan_semua(self):
        # LATIHAN 8: tampilkan seluruh buku dalam koleksi.
        print("Daftar Buku (OOP):")
        for buku in self.koleksi:
            buku.tampilkan()


# --- UJI KEDUA PENDEKATAN ---
if __name__ == "__main__":
    # Uji Pendekatan Prosedural
    list_buku_prosedural = []
    tambah_buku(list_buku_prosedural, "Bumi Manusia", "Pramoedya Ananta Toer")
    tambah_buku(list_buku_prosedural, "Cantik Itu Luka", "Eka Kurniawan")
    
    tampilkan_buku(list_buku_prosedural)
    print("-" * 30)

    # Uji Pendekatan Berorientasi Objek (OOP)
    koleksi = KoleksiBuku()
    buku1 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")
    buku2 = Buku("Cantik Itu Luka", "Eka Kurniawan")
    
    koleksi.tambah(buku1)
    koleksi.tambah(buku2)
    
    koleksi.tampilkan_semua()
    print("-" * 30)