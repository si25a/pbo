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
        print(
            f"[Tunai] Membayar uang tunai sebesar Rp {self.jumlah:,.0f} secara langsung."
        )


class TransaksiTransfer(Transaksi):

    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"[Transfer] Mengirim dana sebesar Rp {self.jumlah:,.0f} | No. Referensi: {self.nomor_referensi}"
        )


# 4. Fungsi proses_semua(daftar) yang memanfaatkan polimorfisme (tanpa pemeriksaan tipe)
def proses_semua(daftar):
    for transaksi in daftar:
        transaksi.proses()


# 5. Uji fungsi dengan minimal satu object dari setiap subclass
if __name__ == "__main__":
    # Membuat object dari masing-masing subclass
    transaksi_1 = TransaksiTunai(80000)
    transaksi_2 = TransaksiTransfer(1200000, "REF-987654321")

    # Memasukkan ke dalam list / daftar transaksi
    daftar_transaksi = [transaksi_1, transaksi_2]

    # Menjalankan fungsi proses_semua
    print("--- Proses Transaksi Mandiri ---")
    proses_semua(daftar_transaksi)