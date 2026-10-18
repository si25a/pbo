"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        self.nama = nama
        # Menggunakan setter agar validasi langsung berjalan saat inisialisasi
        self.email = email
        self.semester = semester

    @property
    def email(self):
        # Kembalikan atribut private _email
        return self._email

    @email.setter
    def email(self, nilai):
        # Validasi email memuat karakter @
        if "@" not in nilai:
            raise ValueError("Email harus memuat karakter '@'.")
        self._email = nilai

    @property
    def semester(self):
        # Kembalikan atribut private _semester
        return self._semester

    @semester.setter
    def semester(self, nilai):
        # Validasi semester berupa integer positif
        if not isinstance(nilai, int) or nilai <= 0:
            raise ValueError("Semester harus berupa integer positif (lebih dari 0).")
        self._semester = nilai

    def tampilkan_info(self):
        # Tampilkan data profil mahasiswa
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"Semester : {self.semester}")


if __name__ == "__main__":
    # Inisialisasi dengan nama Alfi dan semester 3
    profil = ProfilMahasiswa("Alfi", "alfi@example.com", 3)
    profil.tampilkan_info()

    # Contoh memperbarui email tanpa mengubah semester
    profil.email = "alfi.new@example.com"
    print("\n--- Setelah Email Diperbarui ---")
    profil.tampilkan_info()

    # Contoh kasus yang memicu ValueError (uncomment untuk mencoba)
    # profil.email = "email_tidak_valid.com"
    # profil.semester = -1