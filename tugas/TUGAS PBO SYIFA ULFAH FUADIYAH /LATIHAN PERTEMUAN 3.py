"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        self.nama = nama
        self.email = email
        self.semester = semester

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nilai):
        if "@" not in nilai:
            raise ValueError("Email harus memuat karakter @")
        self.__email = nilai

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, nilai):
        if not isinstance(nilai, int) or isinstance(nilai, bool) or nilai <= 0:
            raise ValueError("Semester harus berupa integer positif")
        self.__semester = nilai

    def tampilkan_info(self):
        print("Nama     :", self.nama)
        print("Email    :", self.email)
        print("Semester :", self.semester)


if __name__ == "__main__":
    profil = ProfilMahasiswa("syifa", "syifa@example.com", 3)
    profil.tampilkan_info()
