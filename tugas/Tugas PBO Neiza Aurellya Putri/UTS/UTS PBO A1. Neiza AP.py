class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_data(self):
        print(self.nama, self.nim)

# Membuat object
mhs1 = Mahasiswa("Budi", "12345")

# Memanggil method
mhs1.tampilkan_data()