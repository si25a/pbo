class Buku:
    def __init__(self, judul):
        self.judul = judul

    def info(self):
        print(self.judul)


class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def pinjam_buku(self, buku):
        self.daftar_buku.append(buku)
        print(f"{self.nama} meminjam:")
        buku.info()


anggota = Anggota("Fitri Nur Aisyah")
buku = Buku("Pemrograman Berorientasi Objek")

anggota.pinjam_buku(buku)