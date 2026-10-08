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

    def __init__(self, nama, email, nim, prodi):
        super().__init__(nama, email)
        self.nim = nim
        self.prodi = prodi

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return f"[{self.tampilkan_peran()}] {self.nama} ({self.email}) - NIM: {self.nim}, Prodi: {self.prodi}"


class AkunDosen(Akun):

    def __init__(self, nama, email, nidn, matakuliah):
        super().__init__(nama, email)
        self.nidn = nidn
        self.matakuliah = matakuliah

    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return f"[{self.tampilkan_peran()}] {self.nama} ({self.email}) - NIDN: {self.nidn}, Matkul: {self.matakuliah}"


# Contoh penggunaan dengan data terbaru
mhs = AkunMahasiswa(
    "EDEULIO HIDAYAT",
    "EDEULIO@STUDENT.AC.ID",
    "250660221043",
    "SISTEM INFORMASI",
)

dosen = AkunDosen(
    "YANYAN SOPIAN", "yanyansopian@lecturer.ac.id", "0012038501", "PBO"
)

# Output
print(mhs.ringkasan())
print(dosen.ringkasan())
