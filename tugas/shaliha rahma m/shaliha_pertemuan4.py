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
    """Subclass untuk akun mahasiswa dengan tambahan atribut NIM."""

    def __init__(self, nama, email, nim, prodi):
        super().__init__(nama, email)
        self.nim = nim
        self.prodi = prodi

    def tampilkan_peran(self):
        return "Peran: Mahasiswa"

    def ringkasan(self):
        return (
            f"Mahasiswa: {self.nama} ({self.nim}) - Prodi: {self.prodi} "
            f"[Email: {self.email}]"
        )


class AkunDosen(Akun):
    """Subclass untuk akun dosen dengan tambahan atribut NIDN dan keahlian."""

    def __init__(self, nama, email, nidn, departemen):
        super().__init__(nama, email)
        self.nidn = nidn
        self.departemen = departemen

    def tampilkan_peran(self):
        return "Peran: Dosen"

    def ringkasan(self):
        return (
            f"Dosen: {self.nama} (NIDN: {self.nidn}) - Departemen: {self.departemen} "
            f"[Email: {self.email}]"
        )


# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Membuat objek mahasiswa
    mhs = AkunMahasiswa(
        nama="shaliha",
        email="shaliha@student.unsap.ac.id",
        nim="250660221048",
        prodi="sistem informasi",
    )

    # Membuat objek dosen
    dosen = AkunDosen(
        nama="Dr. shaliha , M.T.",
        email="shaliha@unsap.ac.id",
        nidn="01122334455",
        departemen="sistem informasi",
    )

    # Menjalankan method dari masing-masing objek
    for akun in [mhs, dosen]:
        print(akun.tampilkan_peran())
        print(akun.ringkasan())
        print("-" * 40)
