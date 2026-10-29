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
        print(f"Memproses transaksi tunai sejumlah: Rp {self.jumlah:,.2f}")


class TransaksiTransfer(Transaksi):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Memproses transaksi transfer sejumlah: Rp {self.jumlah:,.2f} | No. Referensi: {self.nomor_referensi}"
        )
def proses_semua(daftar_transaksi):
    for transaksi in daftar_transaksi:
        transaksi.proses()


# --- Pengujian Kode ---
if __name__ == "__main__":
    tunai1 = TransaksiTunai(38340000)
    transfer1 = TransaksiTransfer(1230000, "DNA-123693745")
    daftar = [tunai1, transfer1]

    print("=== Menjalankan Daftar Transaksi Fitri Nur Aisyah ===")
    proses_semua(daftar)