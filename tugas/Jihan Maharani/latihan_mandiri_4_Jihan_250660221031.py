class Akun:
    """"Superclass yang menyimpan data umum pengguna."""
    def __init__(self, nama, email):
       self.nama = nama
       self.email = email

    def tampilkan_peran (self):
        raise NotImplementedError

    def ringkasan(self):
        raise NotImplementedError

class AkunMahasiswa(Akun):
    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return f"Nama: {self.nama}, Email: {self.email}, Peran: Mahasiswa"

class AkunDosen(Akun):
    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return f"Nama: {self.nama}, Email: {self.email}, Peran: Dosen"


mahasiswa = AkunMahasiswa("Jihan Maharani", "Jihan@gmail.com")
dosen = AkunDosen("Yanyan Sofiyan", "Yanyan@gmail.com")

print(mahasiswa.tampilkan_peran())
print(mahasiswa.ringkasan())

print(dosen.tampilkan_peran())
print(dosen.ringkasan())