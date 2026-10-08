class ProfilMahasiswa:
    """Latihan encapsulation pada data email dan semester."""

    def __init__(self, nama, email, semester):
        # LATIHAN: simpan nama dan gunakan property untuk email serta semester
        self.nama = nama
        self.email = email
        self.semester = semester

    @property
    def email(self):
        # LATIHAN: kembalikan email private.
        return self.__email

    @email.setter
    def email(self, nilai):
        # LATIHAN: validasi bahwa email memuat karakter @.
        if "@" not in nilai:
            raise ValueError("Email harus mengandung karakter '@'")
        self.__email = nilai

    @property
    def semester(self):
        # LATIHAN: kembalikan semester private.
        return self.__semester

    @semester.setter
    def semester(self, nilai):
        # LATIHAN: validasi semester berupa integer positif.
        if not isinstance(nilai, int) or nilai <= 0:
            raise ValueError("Semester harus berupa integer positif")
        self.__semester = nilai

    def tampilkan_info(self):
        # LATIHAN: tampilkan nama, email, dan semester.
        print(f"Nama: {self.nama}")
        print(f"Email: {self.email}")
        print(f"Semester: {self.semester}")


if __name__ == "__main__":
    profil = ProfilMahasiswa("salwa", "salwa.dwi@example.com", 4)
    profil.tampilkan_info()