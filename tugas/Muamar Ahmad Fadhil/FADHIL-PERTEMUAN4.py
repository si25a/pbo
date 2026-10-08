"""Latihan mandiri Pertemuan 4 — hierarki Akun."""


class Akun:
    """Superclass yang menyimpan data umum pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError 

    def ringkasan(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass


class AkunMahasiswa(Akun):
    def __init__(self, nama, email, nim, prodi):
        super().__init__(nama, email)
        self.nim = nim
        self.prodi = prodi

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return f"{self.nama} {self.nim} - {self.prodi} - {self.email}"


class AkunDosen(Akun):
    def __init__(self, nama, email, nidn, bidang):
        super().__init__(nama, email)
        self.nidn = nidn
        self.bidang = bidang

    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return f"{self.nama} NIDN {self.nidn} - Bidang {self.bidang} - {self.email}"


if __name__ == "__main__":
    daftar_akun = [
        AkunMahasiswa("Fadhil", "fadhil@unsap.ac.id", "2506622234", "Sistem Informasi"),
        AkunDosen("Yanyan Sofiyan", "yanyansofiyan@unsap.ac.id", "01234567", "PBO"),
    ]


    for akun in daftar_akun:
        print(f"{akun.tampilkan_peran()} {akun.ringkasan()}")
