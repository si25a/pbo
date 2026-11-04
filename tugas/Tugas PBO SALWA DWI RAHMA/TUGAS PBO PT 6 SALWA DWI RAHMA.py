"""Scaffold latihan mandiri — Abstraction pada transaksi."""

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
    """Subclass transaksi menggunakan metode tunai."""

    def proses(self):
        # 2. Implementasikan proses() pada TransaksiTunai
        print(f"Memproses transaksi tunai sejumlah: Rp{self.jumlah:,}")


class TransaksiTransfer(Transaksi):
    """Subclass transaksi menggunakan metode transfer bank."""

    def __init__(self, jumlah, nomor_referensi):
        # 1. Tambahkan attribute khusus pada TransaksiTransfer (nomor_referensi)
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        # 3. Implementasikan proses() pada TransaksiTransfer
        print(
            f"Memproses transaksi transfer sejumlah: Rp{self.jumlah:,} "
            f"dengan Nomor Referensi: {self.nomor_referensi}"
        )


# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() pada setiap object tanpa pemeriksaan tipe
def proses_semua(daftar_transaksi):
    """Memproses semua transaksi menggunakan prinsip Polimorfisme."""
    for transaksi in daftar_transaksi:
        transaksi.proses()


# 5. Uji fungsi dengan minimal satu object dari setiap subclass
if __name__ == "__main__":
    # Membuat instance dari subclass
    tunai_1 = TransaksiTunai(150000)
    transfer_1 = TransaksiTransfer(500000, "REF-20231024-001")
    transfer_2 = TransaksiTransfer(250000, "REF-20231024-002")

    # Daftar berisi berbagai objek transaksi
    daftar_transaksi = [tunai_1, transfer_1, transfer_2]

    print("=== PROSES SEMUA TRANSAKSI ===")
    proses_semua(daftar_transaksi)
    