"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        self.nama = nama
        # Menggunakan setter (bukan langsung _email) agar validasi
        # juga berjalan saat objek pertama kali dibuat.
        self.email = email
        self.semester = semester

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nilai):
        if not isinstance(nilai, str) or "@" not in nilai:
            raise ValueError("Email na salah kudu pake '@'.")
        self.__email = nilai

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, nilai):
        # bool adalah subclass dari int, jadi True dianggap 1; tolak secara eksplisit.
        if not isinstance(nilai, int) or isinstance(nilai, bool) or nilai <= 0:
            raise ValueError("Semester teh kudu bilangan positif.")
        self.__semester = nilai

    def tampilkan_info(self):
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"Semester : {self.semester}")


if __name__ == "__main__":
    profil = ProfilMahasiswa("Fadhil", "fadhilceha@gmail.com", 3)
    profil.tampilkan_info()
