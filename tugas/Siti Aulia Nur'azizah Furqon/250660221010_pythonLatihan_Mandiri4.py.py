class Akun:
    """Superclass yang menyimpan data umum pengguna."""

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError(
            "Method tampilkan_peran() harus diimplementasikan oleh subclass"
        )

    def ringkasan(self):
        raise NotImplementedError(
            "Method ringkasan() harus diimplementasikan oleh subclass"
        )


class AkunMahasiswa(Akun):
    """Subclass untuk akun mahasiswa."""

    def __init__(self, nama, email, nim, program_studi):
        super().__init__(nama, email)
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return (
            f"Nama: {self.nama}\n"
            f"Email: {self.email}\n"
            f"NIM: {self.nim}\n"
            f"Program Studi: {self.program_studi}\n"
            f"Peran: {self.tampilkan_peran()}"
        )


class AkunDosen(Akun):
    """Subclass untuk akun dosen."""

    def __init__(self, nama, email, nip, mata_kuliah):
        super().__init__(nama, email)
        self.nip = nip
        self.mata_kuliah = mata_kuliah

    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return (
            f"Nama: {self.nama}\n"
            f"Email: {self.email}\n"
            f"NIP: {self.nip}\n"
            f"Mata Kuliah: {self.mata_kuliah}\n"
            f"Peran: {self.tampilkan_peran()}"
        )


if __name__ == "__main__":
    mahasiswa = AkunMahasiswa(
        "Siti Aulia N.F",
        "sitiaulianr3.zzh@gmail.com",
        "250660221010",
        "Sistem Informasi"
    )

    dosen = AkunDosen(
        "Yanyan Sofyan M.Kom",
        "yysofiyan@unsap.ac.id",
        "1234567890",
        "Pemrograman Berorientasi Objek"
    )

    print("=== Data Mahasiswa ===")
    print(mahasiswa.ringkasan())

    print("\n=== Data Dosen ===")
    print(dosen.ringkasan())
