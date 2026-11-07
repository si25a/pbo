class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.sks = 0

    def tambah_sks(self, jumlah):
        self.sks += jumlah

    def info(self):
        print(f"{self.nama} - Total SKS: {self.sks}")

mahasiswa = Mahasiswa("Fitri Nur Aisyah-3A")
mahasiswa.tambah_sks(3)
mahasiswa.info()