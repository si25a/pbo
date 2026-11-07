"""
SOAL A1 - KONSEP DASAR OOP

Jelaskan pengertian dari kelima konsep berikut dan berikan satu contoh penerapannya pada kode Python:
1. class
2. object
3. attribute
4. method
5. constructor

Jawaban:
1. Class adalah cetakan (blueprint) yang merancang struktur dasar dari suatu entitas.
    Meskipun data aslinya belum diisi, class mendefinisikan data dan aksi apa saja yang akan disimpan dan dilakukan.

2. Object adalah hasil nyata atau output yang dibuat berdasarkan class.
    Object bisa diartikan sebagai produk jadinya dan memiliki data spesifik.

3. Attribute adalah variabel, nilai atau karakteristik yang melekat pada suatu object.
    Berfungsi menyimpan informasi atau status dari kondisi fisik object.

4. Method merupakan fungsi yang berada di dalam class.
    Mengatur prilaku, tindakan yang dapat dilakukan object.

5. Constructor adalah method khusus yang otomatis dijalankan saat membuat object baru pada sebuah class
Berikut Contoh Penerapan pada kode python
"""

class EventPaydaySale: # Class
    def __init__(self, nama_barang, harga, voucher, metode_bayar="COD"): # Constructor
        self.nama_barang = nama_barang      # Attribute 1
        self.harga = harga                  # Attribute 2
        self.voucher = voucher              # Attribute 3
        self.metode_bayar = metode_bayar    # Attribute 4

    def checkout_barang(self):
        return f"Anda Baru Saja memesan {self.nama_barang} seharga Rp{self.harga} dengan metode bayar {self.metode_bayar}. Pesanan anda sedang dikemas."

Keranjang_kuning = EventPaydaySale("Plushie Chiikawa", 199000, "Voucher25.11Sale", "COD") # Object

print(Keranjang_kuning.checkout_barang()) # memanggil method