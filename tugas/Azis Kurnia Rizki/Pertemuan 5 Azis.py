
"""Scaffold latihan mandiri — Polymorphism pada pembayaran."""


class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError


class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Pembayaran tunai sebesar Rp{self.jumlah:,}")


class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(f"Pembayaran transfer sebesar Rp{self.jumlah:,}")
        print(f"Nomor referensi: {self.nomor_referensi}")


def proses_semua(daftar):
    for pembayaran in daftar:
        pembayaran.proses()


# Pengujian program
tunai = PembayaranTunai(50000)
transfer = PembayaranTransfer(150000, "TRX12345")

daftar_pembayaran = [tunai, transfer]

proses_semua(daftar_pembayaran)

