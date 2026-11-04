from abc import ABC, abstractmethod


# Abstract class
class Transaksi(ABC):

    @abstractmethod
    def proses(self):
        """Memproses transaksi."""
        pass


# Subclass untuk pembayaran tunai
class TransaksiTunai(Transaksi):

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        print(f"Pembayaran tunai sebesar Rp{self.jumlah:,} berhasil.")


# Subclass untuk pembayaran transfer
class TransaksiTransfer(Transaksi):

    def __init__(self, jumlah, nomor_referensi):
        self.jumlah = jumlah
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(f"Transfer sebesar Rp{self.jumlah:,} berhasil.")
        print(f"Nomor referensi: {self.nomor_referensi}")


# Fungsi untuk memproses daftar transaksi tanpa memeriksa tipe objek
def proses_semua_transaksi(daftar_transaksi):
    for transaksi in daftar_transaksi:
        transaksi.proses()
        print("-" * 40)


# Pengujian: minimal satu objek dari setiap subclass
if __name__ == "__main__":
    transaksi1 = TransaksiTunai(150000)
    transaksi2 = TransaksiTransfer(250000, "TRX20261029")

    daftar_transaksi = [transaksi1, transaksi2]
    proses_semua_transaksi(daftar_transaksi)
