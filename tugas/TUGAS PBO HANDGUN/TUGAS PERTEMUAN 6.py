
from abc import ABC, abstractmethod


class Transaksi(ABC):
    """Abstract class untuk transaksi."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    @abstractmethod
    def proses(self):
        pass


# Transaksi Tunai
class TransaksiTunai(Transaksi):

    def proses(self):
        print(f"Transaksi tunai sebesar Rp{self.jumlah} berhasil dibayarkan.")


# Transaksi Transfer
class TransaksiTransfer(Transaksi):

    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(f"Transaksi transfer sebesar Rp{self.jumlah} berhasil.")
        print(f"Nomor Referensi: {self.nomor_referensi}")


# Fungsi Polymorphism
def proses_semua(daftar):
    for transaksi in daftar:
        transaksi.proses()


# Pengujian program
tunai = TransaksiTunai(25000000)
transfer = TransaksiTransfer(7000000, "TRX001")

daftar_transaksi = [tunai, transfer]

print("=== DAFTAR TRANSAKSI ===")
proses_semua(daftar_transaksi)



#1. MENAMBAHKAN NOMOR REFERENSI self.nomor_referensi
#2.Menampilkan jumalah pembayaran
#3.Menampilkan jumlah dan nomor refrensi
#4.menggunakan perulang for 
#5.membuat objek tunai dan transfer
