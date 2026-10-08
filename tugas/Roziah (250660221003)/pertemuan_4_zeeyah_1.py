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
    """Subclass untuk akun dengan peran Mahasiswa."""

    def __init__(self, nama, email, nim, semester):
        # Memanggil constructor superclass (Akun)
        super().__init__(nama, email)
        self.nim = nim
        self.semester = semester

    def tampilkan_peran(self):
        print("Peran: Mahasiswa")

    def ringkasan(self):
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"NIM      : {self.nim}")
        print(f"Semester : {self.semester}")


class AkunDosen(Akun):
    """Subclass untuk akun dengan peran Dosen."""

    def __init__(self, nama, email, nidn, prodi):
        # Memanggil constructor superclass (Akun)
        super().__init__(nama, email)
        self.nidn = nidn
        self.prodi = prodi

    def tampilkan_peran(self):
        print("Peran: Dosen")

    def ringkasan(self):
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"NIDN     : {self.nidn}")
        print(f"Prodi    : {self.prodi}")


if __name__ == "__main__":
    # Pengujian objek AkunMahasiswa dan AkunDosen
    mhs = AkunMahasiswa("Roziah", "Roziah@student.ac.id", "12345678", 4)
    dosen = AkunDosen("Dr. Roziah", "Roziah@lecturer.ac.id", "0012345678", "Teknik Informatika")

    # Menggunakan polimorfisme untuk memanggil metode dari masing-masing subclass
    daftar_akun = [mhs, dosen]
    
    for akun in daftar_akun:
        akun.tampilkan_peran()
        akun.ringkasan()
        print("-" * 35)
