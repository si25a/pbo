
"""Latihan Mandiri Pertemuan 1 — Class Produk."""

class Produk:
    # Bonus: menghitung jumlah object Produk yang dibuat
    total_produk = 0

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

        Produk.total_produk += 1

    def info(self):
        print(f"{self.nama} - Rp{self.harga} (stok: {self.stok})")

    def jual(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penjualan harus lebih dari 0!")
        elif self.stok < jumlah:
            print("Stok tidak cukup!")
        else:
            self.stok -= jumlah
            print(f"Berhasil menjual {jumlah} {self.nama}.")

    def restock(self, jumlah):
        if jumlah <= 0:
            print("Jumlah restock harus lebih dari 0!")
        else:
            self.stok += jumlah
            print(f"Stok {self.nama} berhasil ditambah {jumlah}.")


# Program utama untuk pengujian
if __name__ == "__main__":
    p = Produk("Laptop", 8000000, 5)

    p.info()
    p.jual(2)
    p.info()

    p.jual(10)
    p.restock(10)
    p.info()

    print(f"Total produk: {Produk.total_produk}")


