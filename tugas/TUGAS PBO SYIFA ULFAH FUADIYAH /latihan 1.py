class Produk:
    # Class attribute untuk menghitung jumlah objek Produk yang dibuat
    total_produk = 0

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
        
        # Setiap kali objek baru dibuat, tambahkan 1 ke total_produk
        Produk.total_produk += 1

    def info(self):
        """Mencetak informasi produk"""
        print(f"{self.nama} - Rp{self.harga} (stok: {self.stok})")

    def jual(self, jumlah):
        """Mengurangi stok, menolak jika stok tidak mencukupi"""
        if self.stok < jumlah:
            print(f"Transaksi ditolak! Stok {self.nama} tidak mencukupi (sisa: {self.stok}).")
        else:
            self.stok -= jumlah
            print(f"Berhasil menjual {jumlah} {self.nama}. Sisa stok: {self.stok}")

    def restock(self, jumlah):
        """Menambah stok produk"""
        self.stok += jumlah
        print(f"Berhasil menambah stok {self.nama} sebanyak {jumlah}. Total stok sekarang: {self.stok}")


# Contoh pengujian
if __name__ == "__main__":
    # Membuat beberapa objek produk
    p1 = Produk("Laptop ASUS", 7500000, 5)
    p2 = Produk("Mouse Wireless", 150000, 10)

    print("--- Info Awal ---")
    p1.info()
    p2.info()

    print("\n--- Aktivitas Jual & Restock ---")
    p1.jual(2)      # Berhasil
    p1.jual(4)      # Ditolak karena stok kurang
    p2.restock(5)   # Menambah stok

    print("\n--- Info Akhir ---")
    p1.info()
    p2.info()

    # Menampilkan total produk yang telah dibuat
    print(f"\nTotal objek Produk yang dibuat: {Produk.total_produk}")
    