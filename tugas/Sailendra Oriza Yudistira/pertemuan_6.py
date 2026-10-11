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
    def proses(self):
        print(f"Memproses transaksi tunai: Rp {self.jumlah}")


class TransaksiTransfer(Transaksi):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(f"Memproses transaksi transfer: Rp {self.jumlah}, Nomor Referensi: {self.nomor_referensi}")


# Tugas:
# 1. Tambahkan attribute khusus pada TransaksiTransfer (nomor_referensi).
# 2. Implementasikan proses() pada TransaksiTunai yang menampilkan jumlah yang dibayarkan.
# 3. Implementasikan proses() pada TransaksiTransfer yang menampilkan jumlah dan nomor referensi.
# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() pada setiap object tanpa pemeriksaan tipe.
# 5. Uji fungsi dengan minimal satu object dari setiap subclass.

def proses_semua(daftar_transaksi):
    for transaksi in daftar_transaksi:
        transaksi.proses()

if __name__ == "__main__":
    transaksi1 = TransaksiTunai(100000)
    transaksi2 = TransaksiTransfer(250000, "REF123456")

    daftar_transaksi = [transaksi1, transaksi2]
    proses_semua(daftar_transaksi)