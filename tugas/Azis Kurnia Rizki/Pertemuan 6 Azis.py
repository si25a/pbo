
"""Latihan Individu Pertemuan 6 - Abstraction dan Interface."""

from abc import ABC, abstractmethod


class Transaksi(ABC):
    def __init__(self, jumlah):
        self.jumlah = jumlah

    @abstractmethod
    def proses(self):
        pass


class TransaksiTunai(Transaksi):
    def proses(self):
        print(f"Transaksi tunai sebesar Rp{self.jumlah} berhasil diproses.")


class TransaksiTransfer(Transaksi):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Transfer sebesar Rp{self.jumlah} berhasil diproses. "
            f"Nomor referensi: {self.nomor_referensi}"
        )


def proses_daftar_transaksi(daftar_transaksi):
    for transaksi in daftar_transaksi:
        transaksi.proses()


if __name__ == "__main__":
    # Bantuan: ChatGPT - penjelasan abstract class dan abstract method.

    transaksi1 = TransaksiTunai(100000)
    transaksi2 = TransaksiTransfer(250000, "TRX001")

    daftar_transaksi = [transaksi1, transaksi2]

    proses_daftar_transaksi(daftar_transaksi)
