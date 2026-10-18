class ProfilMahasiswa:
    def __init__(self, nama, email, semester):
        self.nama = nama
        self.email = email
        self.semester = semester

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nilai):
        if "@" not in nilai:
            raise ValueError("Email tidak valid! Harus mengandung karakter '@'.")
        self._email = nilai

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, nilai):
        if not isinstance(nilai, int) or nilai <= 0:
            raise ValueError("Semester harus berupa bilangan bulat (integer) positif.")
        self._semester = nilai

    def tampilkan_info(self):
        print(f"Nama     : {self.nama}")
        print(f"Email    : {self.email}")
        print(f"Semester : {self.semester}")


if __name__ == "__main__":
    profil = ProfilMahasiswa("Fitri Nur Aisyah", "250660221049@sisteminformasi.com", 3)
    profil.tampilkan_info()