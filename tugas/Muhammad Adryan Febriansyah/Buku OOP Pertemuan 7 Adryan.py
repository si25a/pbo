
"""Pengelolaan buku menggunakan pendekatan OOP."""

# Bantuan: ChatGPT - penjelasan perbedaan pendekatan prosedural dan OOP.


class Buku:
    def __init__(self, judul):
        self.judul = judul

    def __str__(self):
        return self.judul


class KoleksiBuku:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, judul):
        buku = Buku(judul)
        self.daftar_buku.append(buku)
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def tampilkan_buku(self):
        if not self.daftar_buku:
            print("Belum ada buku.")
        else:
            print("Daftar Buku:")
            for nomor, buku in enumerate(self.daftar_buku, start=1):
                print(f"{nomor}. {buku}")

    def hapus_buku(self, judul):
        for buku in self.daftar_buku:
            if buku.judul == judul:
                self.daftar_buku.remove(buku)
                print(f"Buku '{judul}' berhasil dihapus.")
                return

        print(f"Buku '{judul}' tidak ditemukan.")


if __name__ == "__main__":
    koleksi = KoleksiBuku()

    koleksi.tambah_buku("Pemrograman Python")
    koleksi.tambah_buku("Basis Data")
    koleksi.tampilkan_buku()
    koleksi.hapus_buku("Basis Data")
    koleksi.tampilkan_buku()
