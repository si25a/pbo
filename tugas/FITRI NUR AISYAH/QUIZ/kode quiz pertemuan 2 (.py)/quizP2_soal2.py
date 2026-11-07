class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama      
        self.sks = 0          
    def tambah_sks(self, jumlah):   
        self.sks += jumlah

mahasiswa = Mahasiswa("FItri Nur Aisyah")
print(mahasiswa.sks)       
mahasiswa.tambah_sks(3)     
print(mahasiswa.sks)