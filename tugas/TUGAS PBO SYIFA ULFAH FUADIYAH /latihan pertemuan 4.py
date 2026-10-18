"""Scaffold latihan mandiri Pertemuan 4 — hierarki Akun."""


class Akun:
    """Superclass yang menyimpan data umum pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass

    def ringkasan(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass


class AkunMahasiswa(Akun):
    def __init__(self, nama, email, nim, program_studi):
        super().__init__(nama, email)
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        print("Peran: Mahasiswa")

    def ringkasan(self):
        print("=== Data Akun Mahasiswa ===")
        print("Nama          :", self.nama)
        print("Email         :", self.email)
        print("NIM           :", self.nim)
        print("Program Studi :", self.program_studi)


class AkunDosen(Akun):
    def __init__(self, nama, email, nuptk, bidang_keahlian):
        super().__init__(nama, email)
        self.nuptk = nuptk
        self.bidang_keahlian = bidang_keahlian

    def tampilkan_peran(self):
        print("Peran: Dosen")

    def ringkasan(self):
        print("=== Data Akun Dosen ===")
        print("Nama             :", self.nama)
        print("Email            :", self.email)
        print("NUPTK            :", self.nuptk)
        print("Bidang Keahlian  :", self.bidang_keahlian)


if __name__ == "__main__":
    mahasiswa = AkunMahasiswa(
        "syifa",
        "syifa@example.com",
        "23123456",
        "Teknik Informatika"
    )

    dosen = AkunDosen(
        "pak yanyan",
        "pak yanyan @example.com",
        "1234567890123456",
        "Pemrograman"
    )

    mahasiswa.tampilkan_peran()
    mahasiswa.ringkasan()

    print()

    dosen.tampilkan_peran()
    dosen.ringkasan()
