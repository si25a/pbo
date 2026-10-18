class Pembayaran:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError


class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Pembayaran tunai sebesar Rp{self.jumlah} telah dibayarkan.")


class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Pembayaran transfer sebesar Rp{self.jumlah} "
            f"dengan nomor referensi {self.nomor_referensi} telah diproses."
        )


def proses_semua(daftar):
    for pembayaran in daftar:
        pembayaran.proses()


# Pengujian
pembayaran1 = PembayaranTunai(50000)
pembayaran2 = PembayaranTransfer(100000, "TRX001")

daftar_pembayaran = [pembayaran1, pembayaran2]

proses_semua(daftar_pembayaran)