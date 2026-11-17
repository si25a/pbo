# 1. CLASS: Cetak biru (blueprint) untuk membuat objek
class Kucing:
    
    # 5. CONSTRUCTOR: Method khusus (__init__) untuk inisialisasi awal
    def __init__(self, nama, warna):
        # 3. ATTRIBUTE: Variabel yang melekat pada objek untuk menyimpan data
        self.nama = nama
        self.warna = warna

    # 4. METHOD: Fungsi di dalam class yang mendefinisikan perilaku objek
    def bersuara(self):
        return f"{self.nama} mengeong: Meow!"

# 2. OBJECT: Wujud nyata (instance) dari class Kucing di dalam memori
kucing_saya = Kucing("Milo", "Oranye")

# Contoh penggunaan:
print(kucing_saya.nama)        # Mengakses attribute -> Output: Milo
print(kucing_saya.bersuara())  # Memanggil method -> Output: Milo mengeong: Meow!