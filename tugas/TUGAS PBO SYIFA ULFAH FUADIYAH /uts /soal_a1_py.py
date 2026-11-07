# Nama File: soal_a1.py

# 1. Class (Cetak biru utama dengan PascalCase)
class MahasiswaTeknik:

    # 5. Constructor (__init__) buat inisialisasi awal
    def __init__(self, nama_mhs, nim_mhs):
        # 3. Attribute (Variabel data dengan snake_case)
        self.nama_mhs = nama_mhs
        self.nim_mhs = nim_mhs

    # 4. Method (Fungsi perilaku dengan snake_case, indentasi pas di dalam class)
    def pamer_status(self):
        print(
            f"Halo, kenalin gue {self.nama_mhs} dengan NIM {self.nim_mhs} lagi"
            " berjuang ngerjain uts."
        )


# 2. Object (Wujud nyata dari class MahasiswaTeknik)
mahasiswa_satu = MahasiswaTeknik("SYIFA ULFAH F", "250660221013")

# Menjalankan method dari object
mahasiswa_satu.pamer_status()




