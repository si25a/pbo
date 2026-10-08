class Akun:

    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def tampilkan_peran(self):
        raise NotImplementedError

    def ringkasan(self):
        raise NotImplementedError


class AkunMahasiswa(Akun):

    def tampilkan_peran(self):
        print("Peran: Mahasiswa")

    def ringkasan(self):
        print(f"Nama : {self.nama}")
        print(f"Email: {self.email}")
        print("Peran: Mahasiswa")


class AkunDosen(Akun):

    def tampilkan_peran(self):
        print("Peran: Dosen")

    def ringkasan(self):
        print(f"Nama : {self.nama}")
        print(f"Email: {self.email}")
        print("Peran: Dosen")


if __name__ == "__main__":
    mhs = AkunMahasiswa("Muhamad Luthfiansyah Nugraha", "luthfingrha24@gmail.com")
    dosen = AkunDosen("Yanyan Sofiyan", "yysofiyan@gmail.com")

    mhs.ringkasan()
    print()
    dosen.ringkasan()
