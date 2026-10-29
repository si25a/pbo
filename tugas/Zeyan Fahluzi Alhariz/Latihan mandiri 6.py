"""Latihan mandiri — Abstraction pada transaksi."""

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
    def proses(self):
        print(f"Transaksi tunai: jumlah yang dibayarkan Rp{self.jumlah:,}")


class TransaksiTransfer(Transaksi):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Transaksi transfer: jumlah Rp{self.jumlah:,}, "
            f"nomor referensi {self.nomor_referensi}"
        )


def proses_semua(daftar):
    """Memanggil proses() pada setiap object tanpa pemeriksaan tipe."""
    for transaksi in daftar:
        transaksi.proses()


# Pengujian: minimal satu object dari setiap subclass
if __name__ == "__main__":
    daftar_transaksi = [
        TransaksiTunai(150000),
        TransaksiTransfer(500000, "TRF-2026-0001"),
    ]
    proses_semua(daftar_transaksi)

    # Bukti bahwa abstract class tidak bisa diinstansiasi
    try:
        Transaksi(1000)
    except TypeError as e:
        print("Error yang diharapkan:", e)