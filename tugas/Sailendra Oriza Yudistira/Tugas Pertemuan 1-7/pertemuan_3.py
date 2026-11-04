"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        # LATIHAN: simpan nama dan gunakan property untuk email serta semester.
        self._nama = nama
        self._email = email
        self._semester = semester

    @property
    def email(self):
        # LATIHAN: kembalikan email private.
        return self._email

    @email.setter
    def email(self, nilai):
        # LATIHAN: validasi bahwa email memuat karakter @.
        if "@" not in nilai:
            raise ValueError("Email harus memuat karakter @")
        self._email = nilai

    @property
    def semester(self):
        # LATIHAN: kembalikan semester private.
        return self._semester

    @semester.setter
    def semester(self, nilai):
        # LATIHAN: validasi semester berupa integer positif.
        if not isinstance(nilai, int):
            raise ValueError("Semester harus berupa integer")
        if nilai <= 0:
            raise ValueError("Semester harus berupa integer positif")
        self._semester = nilai

    def tampilkan_info(self):
        # LATIHAN: tampilkan nama, email, dan semester.
        print(f"Nama: {self._nama}")
        print(f"Email: {self._email}")
        print(f"Semester: {self._semester}")


if __name__ == "__main__":
    profil = ProfilMahasiswa("Jhon Doe", "jhon.doe@example.com", 3)
    profil.tampilkan_info()