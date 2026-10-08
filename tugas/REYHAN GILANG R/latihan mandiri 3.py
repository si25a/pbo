"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        # Menyimpan nama
        self.nama = nama

        # Menggunakan property untuk memvalidasi email dan semester
        self.email = email
        self.semester = semester

    @property
    def email(self):
        # Mengembalikan email private
        return self.__email

    @email.setter
    def email(self, nilai):
        # Validasi bahwa email memuat karakter @
        if "@" not in nilai:
            raise ValueError("Email harus memuat karakter @")

        self.__email = nilai

    @property
    def semester(self):
        # Mengembalikan semester private
        return self.__semester

    @semester.setter
    def semester(self, nilai):
        # Validasi semester berupa integer positif
        if not isinstance(nilai, int) or isinstance(nilai, bool) or nilai <= 0:
            raise ValueError("Semester harus berupa integer positif")

        self.__semester = nilai

    def tampilkan_info(self):
        # Menampilkan nama, email, dan semester
        print("Nama:", self.nama)
        print("Email:", self.email)
        print("Semester:", self.semester)


if __name__ == "__main__":
    profil = ProfilMahasiswa(
        "reyhan",
        "reyhan@gmail.com",
        3
    )

    profil.tampilkan_info()