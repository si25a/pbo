class Buku:
	def __init__(self, judul: str, penulis: str):
		self.judul = judul
		self.penulis = penulis
		self.__tersedia = True

	@property
	def tersedia(self) -> bool:
		return self.__tersedia

	def pinjam(self) -> bool:
		if self.__tersedia:
			self.__tersedia = False
			return True
		return False

	def kembalikan(self) -> None:
		self.__tersedia = True

	def __str__(self) -> str:
		status = "Tersedia" if self.tersedia else "Dipinjam"
		return f"{self.judul} — {self.penulis} [{status}]"


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


def tampilkan_info(daftar_buku: list[Buku]) -> None:
	for buku in daftar_buku:
		print(buku)


if __name__ == "__main__":
	buku1 = Buku("Laskar Pelangi", "Andrea Hirata")
	buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")
	buku1.pinjam()
	tampilkan_info([buku1, buku2])

