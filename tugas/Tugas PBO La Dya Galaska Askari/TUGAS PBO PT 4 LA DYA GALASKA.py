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
        # Memanggil constructor superclass menggunakan super()
        super().__init__(nama, email)
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        print("Peran: Mahasiswa")

    def ringkasan(self):
        print(f"Nama          : {self.nama}")
        print(f"Email         : {self.email}")
        print(f"NIM           : {self.nim}")
        print(f"Program Studi : {self.program_studi}")
        self.tampilkan_peran()


class AkunDosen(Akun):
    def __init__(self, nama, email, nuptk, bidang_keahlian):
        # Memanggil constructor superclass menggunakan super()
        super().__init__(nama, email)
        self.nuptk = nuptk
        self.bidang_keahlian = bidang_keahlian

    def tampilkan_peran(self):
        print("Peran: Dosen")

    def ringkasan(self):
        print(f"Nama           : {self.nama}")
        print(f"Email          : {self.email}")
        print(f"NUPTK          : {self.nuptk}")
        print(f"Bidang Keahlian: {self.bidang_keahlian}")
        self.tampilkan_peran()


# Pengujian program dengan minimal satu object dari setiap subclass
if __name__ == "__main__":
    print("=== INFORMASI AKUN MAHASISWA ===")
    mhs = AkunMahasiswa(
        "La Dya Galaska", "dyaglsk.mhs@campus.ac.id", "137654", "Sistem Informasi"
    )
    mhs.ringkasan()

    print("\n=== INFORMASI AKUN DOSEN ===")
    dosen = AkunDosen(
        "Pak Budi Santoso, M.Kom.",
        "budisantoso.dosen@campus.ac.id",
        "987654321",
        "Pemograman Berorientasi Objek",
    )
    dosen.ringkasan()