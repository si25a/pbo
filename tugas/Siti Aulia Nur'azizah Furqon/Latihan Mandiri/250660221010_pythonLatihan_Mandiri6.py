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
        print(f"Memproses pembayaran tunai sebesar Rp{self.jumlah}")


class TransaksiTransfer(Transaksi):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Memproses transfer sebesar Rp{self.jumlah} dengan nomor referensi: {self.nomor_referensi}"
        )


# 4. Fungsi proses_semua(daftar) memanggil proses() pada setiap object tanpa pemeriksaan tipe
def proses_semua(daftar):
    for transaksi in daftar:
        transaksi.proses()


# 5. Uji fungsi dengan minimal satu object dari setiap subclass
if __name__ == "__main__":
    # Membuat object dari masing-masing subclass
    tunai = TransaksiTunai(50000)
    transfer = TransaksiTransfer(250000, "REF123456789")

    # Memasukkan ke dalam sebuah daftar (list)
    daftar_transaksi = [tunai, transfer]

    # Menjalankan fungsi proses_semua
    proses_semua(daftar_transaksi)
