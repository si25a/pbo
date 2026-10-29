"""
Scaffold latihan mandiri — Abstraction pada transaksi.
"""

from abc import ABC, abstractmethod


class Transaksi(ABC):
    """Abstract class yang menetapkan kontrak perilaku transaksi."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    @abstractmethod
    def proses(self):
        # Abstract method: wajib diimplementasikan oleh setiap subclass.
        pass


class TransaksiTunai(Transaksi):
    """Subclass transaksi tunai."""

    def proses(self):
        print(f"Memproses pembayaran tunai sejumlah: Rp{self.jumlah:,}")


class TransaksiTransfer(Transaksi):
    """Subclass transaksi transfer bank."""

    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Memproses transfer sejumlah: Rp{self.jumlah:,} "
            f"(No. Ref: {self.nomor_referensi})"
        )


def proses_semua(daftar_transaksi):
    """Fungsi yang memanggil proses() untuk setiap item dalam daftar."""
    for transaksi in daftar_transaksi:
        transaksi.proses()


# Uji Coba Program
if __name__ == "__main__":
    t1 = TransaksiTunai(150000)
    t2 = TransaksiTransfer(500000, "REF-20261028-001")

    daftar = [t1, t2]

    print("--- Memproses Semua Transaksi ---")
    proses_semua(daftar)