"""Scaffold latihan mandiri — Polymorphism pada pembayaran."""


class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass


class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Memproses pembayaran tunai: Rp {self.jumlah}")


class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(f"Memproses pembayaran transfer: Rp {self.jumlah}, Nomor Referensi: {self.nomor_referensi}")


# Tugas:
# 1. Tambahkan attribute khusus pada PembayaranTransfer (nomor_referensi).
# 2. Implementasikan proses() pada PembayaranTunai yang menampilkan jumlah yang dibayarkan.
# 3. Implementasikan proses() pada PembayaranTransfer yang menampilkan jumlah dan nomor referensi.
# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() pada setiap object tanpa pemeriksaan tipe.
# 5. Uji fungsi dengan minimal satu object dari setiap subclass.

def proses_semua(daftar):
    for item in daftar:
        item.proses()

if __name__ == "__main__":
    # Contoh penggunaan
    pembayaran1 = PembayaranTunai(100000)
    pembayaran2 = PembayaranTransfer(250000, "REF123456")

    daftar_pembayaran = [pembayaran1, pembayaran2]
    proses_semua(daftar_pembayaran)