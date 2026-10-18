"""Scaffold latihan mandiri Pertemuan 4 — hierarki Akun."""


class Akun:
    """Superclass yang menyimpan data umum pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError("Subclass harus mengimplementasikan tampilkan_peran()")

    def ringkasan(self):
        raise NotImplementedError("Subclass harus mengimplementasikan ringkasan()")


class AkunMahasiswa(Akun):
    """Subclass untuk entitas Mahasiswa."""

    def __init__(self, nama, email, nim, program_studi):
        super().__init__(nama, email)
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        print(f"[{self.tampilkan_peran()}]")
        print(f"Nama          : {self.nama}")
        print(f"NIM           : {self.nim}")
        print(f"Email         : {self.email}")
        print(f"Program Studi : {self.program_studi}")


class AkunDosen(Akun):
    """Subclass untuk entitas Dosen."""

    def __init__(self, nama, email, nidn, mata_kuliah):
        super().__init__(nama, email)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah

    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        print(f"[{self.tampilkan_peran()}]")
        print(f"Nama          : {self.nama}")
        print(f"NIDN          : {self.nidn}")
        print(f"Email         : {self.email}")
        print(f"Mata Kuliah   : {self.mata_kuliah}")


if __name__ == "__main__":
    # Penggunaan dengan data Nawaal Alfi Syahrani dan email UNSAP
    mahasiswa = AkunMahasiswa(
        nama="Nawaal Alfi Syahrani",
        email="250660221037@student.unsap.ac.id",
        nim="250660221037",
        program_studi="Sistem Informasi",
    )

    # Menampilkan ringkasan akun mahasiswa
    mahasiswa.ringkasan()

    print("\n" + "=" * 40 + "\n")

    # Objek Dosen disesuaikan ke Pak Yanyan, M.Kom.
    dosen = AkunDosen(
        nama="Yanyan Sofiyan, S.Kom., M.Kom.",
        email="yanyan@unsap.ac.id",
        nidn="0415058501",
        mata_kuliah="Pemrograman Berbasis Objek (PBO)",
    )

    # Menampilkan ringkasan akun dosen
    dosen.ringkasan()