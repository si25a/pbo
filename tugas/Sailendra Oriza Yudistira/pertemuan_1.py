# Latihan Mandiri Pertemuan 1
#
# Buat class Produk sesuai spesifikasi bagian Latihan Mandiri:
#   1. Attribute: nama, harga, stok
#   2. Constructor: mengisi ketiga attribute dari parameter
#   3. Method info(): cetak "{nama} - Rp{harga} (stok: {stok})"
#   4. Method jual(jumlah): kurangi stok; tolak jika stok < jumlah
#   5. Method restock(jumlah): tambah stok
#   6. Bonus: class attribute total_produk
#
# Kerjakan di file ini, lalu jalankan: python latihan_mandiri_1.py


class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def _kurangi_stock(self, jumlah):
        if self.stok < jumlah:
            print("Stok tidak cukup!")
        else:
            self.stok -= jumlah

    def _tambah_stock(self, jumlah):
        self.stok += jumlah

    def info(self):
        print(f"{self.nama} - Rp{self.harga} (stok: {self.stok})")
    
    def jual(self, jumlah):
        self._kurangi_stock(jumlah)
        
    def restock(self, jumlah):
        self._tambah_stock(jumlah)



# === Program utama (jangan diubah) ===
if __name__ == "__main__":
    p = Produk("Laptop", 8000000, 5)
    p.info()
    p.jual(2)
    p.info()
    p.jual(10)
    p.restock(10)
    p.info()

# Expected output:
# Laptop - Rp8000000 (stok: 5)
# Laptop - Rp8000000 (stok: 3)
# Stok tidak cukup!
# Laptop - Rp8000000 (stok: 13)