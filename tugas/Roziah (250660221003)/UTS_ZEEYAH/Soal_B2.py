# --- Bagian 1: Class Buku (dari Soal B1) ---
class Buku:

  def __init__(self, judul: str, penulis: str):
    self.judul = judul
    self.penulis = penulis
    self.__tersedia = True

  def pinjam(self) -> bool:
    if self.__tersedia:
      self.__tersedia = False
      return True
    return False

  def kembalikan(self):
    self.__tersedia = True

  @property
  def tersedia(self) -> bool:
    return self.__tersedia

  def __str__(self) -> str:
    status = "Tersedia" if self.__tersedia else "Dipinjam"
    return f"{self.judul} — {self.penulis} [{status}]"


# --- Bagian 2: Subclass BukuDigital (Soal B2) ---
class BukuDigital(Buku):

  def __init__(self, judul: str, penulis: str, format_file: str):
    super().__init__(judul, penulis)
    self.format_file = format_file

  def __str__(self) -> str:
    status = "Tersedia" if self.tersedia else "Dipinjam"
    return f"{self.judul} — {self.penulis} [{status}] ({self.format_file})"

  def unduh(self) -> str:
    if self.tersedia:
      return f"Mengunduh {self.judul} dalam format {self.format_file}."
    return "Buku tidak tersedia."


# Fungsi Polymorphism
def tampilkan_info(daftar_buku):
  for buku in daftar_buku:
    print(buku)


# --- Program Utama ---
if __name__ == "__main__":
  buku_fisik = Buku("Algoritma Pemrograman", "Zeyyah")
  buku_digital = BukuDigital("Clean Code", "Roziah. Zie", "crong")

  # Meminjam buku digital untuk menguji method unduh dan status
  buku_digital.pinjam()

  daftar_koleksi = [buku_fisik, buku_digital]

  print("=== Daftar Koleksi Perpustakaan ===")
  tampilkan_info(daftar_koleksi)

  print("\n=== Uji Coba Pengunduhan Buku Digital ===")
  print(buku_digital.unduh())

  # Mengembalikan buku digital
  buku_digital.kembalikan()
  print(buku_digital.unduh())
