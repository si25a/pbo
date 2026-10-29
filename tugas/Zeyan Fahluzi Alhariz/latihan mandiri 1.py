class Produk:
    # Bonus: Class attribute untuk menghitung total object Produk yang dibuat
    total_produk = 0

    def __init__(self, nama, harga, stok):
        
        self.nama = nama
        self.harga = harga
        self.stok = stok
        
        
        Produk.total_produk += 1

    def info(self):
        
        print(f"{self.nama} - Rp{self.harga} (stok: {self.stok})")

    def jual(self, jumlah):
       
        if self.stok >= jumlah:
            self.stok -= jumlah
        else:
            print("Stok tidak cukup!")

    def restock(self, jumlah):
        
        self.stok += jumlah


# --- Contoh Pemakaian ---
p = Produk("Laptop", 8000000, 5)
p.info()        # Laptop - Rp8000000 (stok: 5)
p.jual(2)
p.info()        # Laptop - Rp8000000 (stok: 3)
p.jual(10)      # Stok tidak cukup!
p.restock(10)
p.info()        # Laptop - Rp8000000 (stok: 13)