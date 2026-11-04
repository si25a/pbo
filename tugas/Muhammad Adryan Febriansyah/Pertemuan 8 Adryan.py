
class Buku:
    def __init__(self, judul, penulis, tersedia=True):
        self.judul = judul
        self.penulis = penulis
        self.tersedia = tersedia

    def pinjam(self):
        if self.tersedia:
            self.tersedia = False
            print(f"Buku '{self.judul}' berhasil dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

    def tampilkan_info(self):
        status = "Tersedia" if self.tersedia else "Dipinjam"
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Status: {status}")


class Anggota:
    def __init__(self, nama):
        self._nama = nama

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if not isinstance(nilai, str) or not nilai.strip():
            raise ValueError("Nama tidak boleh kosong.")
        self._nama = nilai.strip()


class BukuDigital(Buku):
    def __init__(self, judul, penulis, ukuran_file):
        super().__init__(judul, penulis)
        self.ukuran_file = ukuran_file

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Ukuran file: {self.ukuran_file}")


def tampilkan_info(objek):
    objek.tampilkan_info()


# Pengujian program
buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
buku2 = BukuDigital("Bumi", "Tere Liye", "5 MB")

anggota1 = Anggota("Badar")

print("=== Data Anggota ===")
print("Nama:", anggota1.nama)

print("\n=== Informasi Buku ===")
tampilkan_info(buku1)

print("\n=== Informasi Buku Digital ===")
tampilkan_info(buku2)

print("\n=== Peminjaman Buku ===")
buku1.pinjam()
buku1.pinjam()

# Contoh validasi nama
# anggota1.nama = ""
