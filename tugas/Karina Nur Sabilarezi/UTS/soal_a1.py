
# SOAL A1 - KONSEP DASAR OOP

# 1. CLASS
# Class adalah cetakan atau rancangan untuk membuat object.
class Mahasiswa:
    pass


# 2. OBJECT
# Object adalah hasil dari pembuatan sebuah class.
mahasiswa1 = Mahasiswa()


# 3. ATTRIBUTE
# Attribute adalah variabel yang menyimpan data
# atau karakteristik object.
class DataMahasiswa:
    def __init__(self):
        self.nama = "Andi"


# 4. METHOD
# Method adalah fungsi yang berada di dalam class
# dan digunakan untuk menjalankan suatu tindakan.
class MahasiswaBelajar:
    def belajar(self):
        print("Mahasiswa sedang belajar")


# 5. CONSTRUCTOR
# Constructor adalah method khusus __init__()
# yang otomatis dijalankan ketika object dibuat.
class MahasiswaBaru:
    def __init__(self, nama):
        self.nama = nama


# PROGRAM UTAMA
data1 = DataMahasiswa()
mhs1 = MahasiswaBelajar()
mhs2 = MahasiswaBaru("Budi")

print("Contoh Attribute:", data1.nama)
print("Contoh Method:")
mhs1.belajar()
print("Contoh Constructor:", mhs2.nama)
