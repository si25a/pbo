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
        return f"Mahasiswa: {self.nama} | Email: {self.email}"


class AkunDosen(Akun):
    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return f"Dosen: {self.nama} | Email: {self.email}"


if __name__ == "__main__":
    mahasiswa = AkunMahasiswa(
        "Rita Fitriyani",
        "rita252@gmail.com"
    )

    dosen = AkunDosen(
        "Yanyan Sofiyan",
        "Yanyan@gmail.com"
    )

    print("=== AKUN MAHASISWA ===")
    print("Peran   :", mahasiswa.tampilkan_peran())
    print("Ringkasan:", mahasiswa.ringkasan())

    print("\n=== AKUN DOSEN ===")
    print("Peran   :", dosen.tampilkan_peran())
    print("Ringkasan:", dosen.ringkasan())
