class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    def tampilkan_info(self):
        print(f"{self.kode} - {self.nama} ({self.sks} SKS)")
        
pbo = MataKuliah("SI204", "Pemrograman Berorientasi Objek", 2)
basis_data = MataKuliah("SI205", "Basis Data", 3)

pbo.tampilkan_info()
basis_data.tampilkan_info()