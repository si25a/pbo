"""Scaffold latihan mandiri - Polymorphism pada pembayaran."""

class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError # diimplementasikan oleh setiap subclass

class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Memproses pembayaran tunai sebesar Rp{self.jumlah}")

class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi
        
    def proses(self):
        print(f"Anda menyelesaikan transfer sebesar Rp{self.jumlah} (Ref: {self.nomor_referensi})")


def proses_semua(daftar_pembayaran):
    for pembayaran in daftar_pembayaran:
        pembayaran.proses()

# Pengujian
if __name__ == "__main__":
    tunai = PembayaranTunai(4000000)
    transfer = PembayaranTransfer(400000, "BCA - 0331033")

    daftar = [tunai, transfer]
    
    print("Memproses semua pembayaran:")
    proses_semua(daftar)
