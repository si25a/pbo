
"""Latihan mandiri - Polymorphism pada pembayaran."""


class Pembayaran:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError(
            "Method proses() harus diimplementasikan oleh subclass."
        )


class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Pembayaran tunai sebesar Rp{self.jumlah:,.0f}")


class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Pembayaran transfer sebesar Rp{self.jumlah:,.0f}, "
            f"nomor referensi: {self.nomor_referensi}"
        )


def proses_semua(daftar):
    for pembayaran in daftar:
        pembayaran.proses()


if __name__ == "__main__":
    tunai = PembayaranTunai(350000)
    transfer = PembayaranTransfer(500000, "TRX001")

    daftar_pembayaran = [tunai, transfer]
    proses_semua(daftar_pembayaran)
