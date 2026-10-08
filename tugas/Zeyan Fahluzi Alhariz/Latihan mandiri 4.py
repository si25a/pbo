"""Scaffold latihan mandiri Pertemuan 4 — hierarki Akun."""


class Akun:
    """Superclass yang menyimpan data umum pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError

    def ringkasan(self):
        raise NotImplementedError


class AkunMahasiswa(Akun):
    """Subclass untuk akun mahasiswa."""

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return f"Nama: {self.nama}, Email: {self.email}, Peran: Mahasiswa"


class AkunDosen(Akun):
    """Subclass untuk akun dosen."""

    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return f"Nama: {self.nama}, Email: {self.email}, Peran: Dosen"


if __name__ == "__main__":
    mahasiswa = AkunMahasiswa(
        "Zeyan.Fahluzi",
        "ZeyanFahluzi@gmail.com")

    dosen = AkunDosen(
        "Dr. Budi",
        "budi@example.com"
    )

    print("=== AKUN MAHASISWA ===")
    print("Peran:", mahasiswa.tampilkan_peran())
    print(mahasiswa.ringkasan())

    print()

    print("=== AKUN DOSEN ===")
    print("Peran:", dosen.tampilkan_peran())
    print(dosen.ringkasan())