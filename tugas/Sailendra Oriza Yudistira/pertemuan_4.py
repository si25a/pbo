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
    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return f"Nama: {self.nama}, Email: {self.email}, Peran: {self.tampilkan_peran()}"


class AkunDosen(Akun):
    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return f"Nama: {self.nama}, Email: {self.email}, Peran: {self.tampilkan_peran()}"


if __name__ == "__main__":
    # Contoh penggunaan
    mahasiswa = AkunMahasiswa("Budi", "budi@example.com")
    dosen = AkunDosen("Dr. Siti", "siti@example.com")

    print(mahasiswa.ringkasan())
    print(dosen.ringkasan())