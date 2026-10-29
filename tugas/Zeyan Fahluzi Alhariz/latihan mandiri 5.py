"""Scaffold latihan mandiri – Polymorphism pada pembayaran."""

class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError  


class PembayaranTunai(Pembayaran):
   
    def proses(self):
        print(f"Pembayaran tunai berhasil diproses sebesar Rp{self.jumlah}")


class PembayaranTransfer(Pembayaran):
    
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    
    def proses(self):
        print(
            f"Pembayaran transfer berhasil diproses sebesar Rp{self.jumlah} "
            f"(No. Referensi: {self.nomor_referensi})"
        )



def proses_semua(daftar):
    for pembayaran in daftar:
        pembayaran.proses()



if __name__ == "__main__":
    tunai = PembayaranTunai(50000)
    transfer = PembayaranTransfer(150000, "REF123456")

    daftar_pembayaran = [tunai, transfer]
    proses_semua(daftar_pembayaran)