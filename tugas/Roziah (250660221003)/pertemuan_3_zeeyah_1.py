class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        # Menyimpan nama (public/protected) dan menggunakan property untuk email serta semester
        self.nama = nama
        self.email = email      # Memanggil setter email
        self.semester = semester  # Memanggil setter semester

    @property
    def email(self):
        # Mengembalikan email private
        return self._email

    @email.setter
    def email(self, nilai):
        # Validasi bahwa email memuat karakter @
        if "@" not in nilai:
            raise ValueError("Email tidak valid: harus mengandung karakter '@'")
        self._email = nilai

    @property
    def semester(self):
        # Mengembalikan semester private
        return self._semester

    @semester.setter
    def semester(self, nilai):
        # Validasi semester berupa integer positif (lebih besar dari 0)
        if not isinstance(nilai, int) or nilai <= 0:
            raise ValueError("Semester harus berupa bilangan bulat (integer) positif")
        self._semester = nilai

    def tampilkan_info(self):
        # Menampilkan nama, email, dan semester
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"Semester : {self.semester}")


if __name__ == "__main__":
    # Pengujian normal
    profil = ProfilMahasiswa("Roziah", "Roziah@gmail.com", 3)
    profil.tampilkan_info()

