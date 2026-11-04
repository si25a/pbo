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


# Program Utama
if __name__ == "__main__":
  buku1 = Buku("Pemrograman Python Dasar", "zeeyah")
  buku2 = Buku("Struktur Data Lanjut", "Roziah zia")

  print("--- Status Awal Buku ---")
  print(buku1)
  print(buku2)

  print("\nMeminjam buku pertama...")
  buku1.pinjam()

  print("\n--- Status Setelah Peminjaman ---")
  print(buku1)
  print(buku2)
