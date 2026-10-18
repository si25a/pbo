class Akun:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError 

    def ringkasan(self):
        raise NotImplementedError


class AkunMahasiswa(Akun):
    def __init__(self, nama, email, nim, jurusan):
        super().__init__(nama, email)
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan_peran(self):
        return "Mahasiswa"

    def ringkasan(self):
        return (
            f"[{self.tampilkan_peran()}] Nama: {self.nama}, "
            f"Email: {self.email}, NIM: {self.nim}, Jurusan: {self.jurusan}"
        )


class AkunDosen(Akun):
    def __init__(self, nama, email, nidn, departemen):
        super().__init__(nama, email)
        self.nidn = nidn
        self.departemen = departemen

    def tampilkan_peran(self):
        return "Dosen"

    def ringkasan(self):
        return (
            f"[{self.tampilkan_peran()}] Nama: {self.nama}, "
            f"Email: {self.email}, NIDN: {self.nidn}, Departemen: {self.departemen}"
        )


if __name__ == "__main__":
    mhs = AkunMahasiswa("Fitri Nur Aisyah", "250660221049@student.ac.id", "250660221049", "sistem informasi")
    dsn = AkunDosen("Pak Yanyan", "unsap@lecturer.ac.id", "0283740021", "PBo")

    print(mhs.ringkasan())
    print(dsn.ringkasan())