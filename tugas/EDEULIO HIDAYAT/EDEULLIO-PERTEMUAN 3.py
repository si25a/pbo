class Mahasiswa:

  def __init__(self, nama: str, email: str, semester: int):
    self.nama = nama
    self.email = email
    self.semester = semester

  @property
  def nama(self) -> str:
    return self._nama

  @nama.setter
  def nama(self, value: str):
    if not isinstance(value, str) or not value.strip():
      raise ValueError("Nama tidak boleh kosong.")
    self._nama = value.strip()

  @property
  def email(self) -> str:
    return self._email

  @email.setter
  def email(self, value: str):
    if not isinstance(value, str) or "@" not in value:
      raise ValueError("Email harus memuat karakter '@'.")
    self._email = value

  @property
  def semester(self) -> int:
    return self._semester

  @semester.setter
  def semester(self, value: int):
    if type(value) is not int or value <= 0:
      raise ValueError("Semester harus berupa integer positif.")
    self._semester = value

  def tampilkan_info(self):
    print(f"Nama    : {self.nama}")
    print(f"Email   : {self.email}")
    print(f"Semester: {self.semester}")


# Penggunaan dengan data Edeullio Hidayat
mhs = Mahasiswa(
    nama="Edeullio Hidayat", email="edeullio.hidayat@gmail.com", semester=3
)

mhs.tampilkan_info()
