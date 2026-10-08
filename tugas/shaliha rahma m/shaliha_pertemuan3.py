"""Scaffold latihan mandiri Pertemuan 3.

Buat class ProfilMahasiswa dengan private attribute dan property.
Jalankan:
    python3 latihan_mandiri_3.py
"""


class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        self.nama = nama
        self._email = ""  # Inisialisasi private attribute email
        self._semester = 0  # Inisialisasi private attribute semester
        
        # Menggunakan setter melalui pemanggilan property
        self.email = email
        self.semester = semester

    @property
    def email(self):
        """Getter untuk email."""
        return self._email

    @email.setter
    def email(self, nilai):
        """Setter untuk email dengan validasi karakter '@'."""
        if "@" not in nilai:
            raise ValueError("Email tidak valid: harus mengandung karakter '@'.")
        self._email = nilai

    @property
    def semester(self):
        """Getter untuk semester."""
        return self._semester

    @semester.setter
    def semester(self, nilai):
        """Setter untuk semester dengan validasi berupa integer positif."""
        if not isinstance(nilai, int) or nilai <= 0:
            raise ValueError("Semester harus berupa bilangan bulat (integer) positif.")
        self._semester = nilai

    def tampilkan_info(self):
        """Menampilkan informasi profil mahasiswa."""
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"Semester : {self.semester}")


if __name__ == "__main__":
    # Pengujian normal
    profil = ProfilMahasiswa("shaliha", "shasarm@gmail.com", 3)
    profil.tampilkan_info()
