class Buku:
    def __init__(self, judul):
        self.judul = judul
    def info(self):
        print(self.judul)
buku1 = Buku("Python Dasar")
buku2 = Buku("OOP dengan Python")
buku1.info()
buku2.info()