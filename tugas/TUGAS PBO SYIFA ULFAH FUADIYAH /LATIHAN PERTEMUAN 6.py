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
    # 2. Implementasikan proses() pada TransaksiTunai
    def proses(self):
        print(f"Memproses transaksi tunai sebesar: Rp {self.jumlah:,}")


class TransaksiTransfer(Transaksi):
    # 1. Tambahkan attribute khusus pada TransaksiTransfer (nomor_referensi)
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)  # Memanggil constructor parent class
        self.nomor_referensi = nomor_referensi

    # 3. Implementasikan proses() pada TransaksiTransfer
    def proses(self):
        print(
            f"Memproses transaksi transfer sebesar: Rp {self.jumlah:,} | No. Referensi: {self.nomor_referensi}"
        )


# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() tanpa pemeriksaan tipe (Polimorfisme)
def proses_semua(daftar_transaksi):
    for transaksi in daftar_transaksi:
        transaksi.proses()  # Python otomatis tahu method mana yang harus dipanggil


# 5. Uji fungsi dengan minimal satu object dari setiap subclass
if __name__ == "__main__":
    # Membuat object dari masing-masing subclass
    tunai_1 = TransaksiTunai(150000)
    transfer_1 = TransaksiTransfer(750000, "REF-99887766")

    # Masukkan ke dalam satu list/daftar
    daftar = [tunai_1, transfer_1]

    # Jalankan fungsi utama
    print("--- Memulai Daftar Transaksi ---")
    proses_semua(daftar)