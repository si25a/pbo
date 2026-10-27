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
    def __init__(self, nama, email, nim, program_studi):
        # Memanggil constructor superclass
        super().__init__(nama, email)

        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        print("Peran: Mahasiswa")

    def ringkasan(self):
        print("=== Data Mahasiswa ===")
        print("Nama          :", self.nama)
        print("Email         :", self.email)
        print("NIM           :", self.nim)
        print("Program Studi :", self.program_studi)


class AkunDosen(Akun):
    def __init__(self, nama, email, nuptk, bidang_keahlian):
        # Memanggil constructor superclass
        super().__init__(nama, email)

        self.nuptk = nuptk
        self.bidang_keahlian = bidang_keahlian

    def tampilkan_peran(self):
        print("Peran: Dosen")

    def ringkasan(self):
        print("=== Data Dosen ===")
        print("Nama             :", self.nama)
        print("Email            :", self.email)
        print("NUPTK            :", self.nuptk)
        print("Bidang Keahlian  :", self.bidang_keahlian)


# Pengujian object mahasiswa
mahasiswa = AkunMahasiswa(
    "Jhon Doe",
    "jhon.doe@example.com",
    "20260001",
    "Sistem Informasi"
)

mahasiswa.tampilkan_peran()
mahasiswa.ringkasan()

print()

# Pengujian object dosen
dosen = AkunDosen(
    "Budi Santoso",
    "budi.santoso@example.com",
    "1234567890",
    "Pemrograman"
)

dosen.tampilkan_peran()
dosen.ringkasan()