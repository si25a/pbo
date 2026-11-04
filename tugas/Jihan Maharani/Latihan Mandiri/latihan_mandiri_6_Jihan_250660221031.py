
"""Latihan Mandiri - Abstraction pada transaksi."""

from abc import ABC, abstractmethod


class Transaksi(ABC):
    """Abstract class yang menetapkan kontrak perilaku transaksi."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    @abstractmethod
    def proses(self):
        """Wajib diimplementasikan oleh setiap subclass."""
        pass


class TransaksiTunai(Transaksi):
    """Class untuk transaksi pembayaran tunai."""

    def proses(self):
        print(f"Transaksi tunai: Rp{self.jumlah:,.0f}")


class TransaksiTransfer(Transaksi):
    """Class untuk transaksi pembayaran melalui transfer."""

    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Transaksi Transfer: Rp{self.jumlah:,.0f}, "
            f"Nomor Referensi: {self.nomor_referensi}"
        )


def proses_semua(daftar):
    """Memproses semua transaksi dalam daftar."""

    for transaksi in daftar:
        transaksi.proses()


# Pengujian program
transaksi1 = TransaksiTunai(200000)
transaksi2 = TransaksiTransfer(350000, "TRX001")

daftar_transaksi = [transaksi1, transaksi2]

proses_semua(daftar_transaksi)
