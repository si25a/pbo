"""Latihan mandiri: Polymorphism pada pembayaran."""


class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass


class PembayaranTunai(Pembayaran):
    # 2. Implementasikan proses() pada PembayaranTunai yang menampilkan jumlah yang dibayarkan.
    def proses(self):
        print(f"Pembayaran tunai sebesar Rp{self.jumlah:,} berhasil diproses.")


class PembayaranTransfer(Pembayaran):
    # 1. Tambahkan attribute khusus pada PembayaranTransfer (nomor_referensi).
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    # 3. Implementasikan proses() pada PembayaranTransfer yang menampilkan jumlah dan nomor referensi.
    def proses(self):
        print(f"Pembayaran transfer sebesar Rp{self.jumlah:,} dengan No. Referensi {self.nomor_referensi} berhasil diproses.")


# 4. Buat fungsi proses_semua(daftar) yang memanggil proses() pada setiap object tanpa pemeriksaan tipe.
def proses_semua(daftar):
    for transaksi in daftar:
        transaksi.proses()


# 5. Uji fungsi dengan minimal satu object dari setiap subclass.
if __name__ == "__main__":
    print("--- Uji Coba Latihan Pembayaran ---")
    daftar_pembayaran = [
        PembayaranTunai(100000),
        PembayaranTransfer(250000, "250660221010")
    ]
    proses_semua(daftar_pembayaran)
