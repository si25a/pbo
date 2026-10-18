class Pembayaran:
    """Superclass yang menyimpan jumlah pembayaran."""

    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError  # diimplementasikan oleh setiap subclass


class PembayaranTunai(Pembayaran):
    # Menggunakan __init__ dari superclass (Pembayaran)

    def proses(self):
        # Implementasi proses() untuk pembayaran tunai
        print(f"Pembayaran tunai berhasil diproses sebesar Rp{self.jumlah:,}.")


class PembayaranTransfer(Pembayaran):
    # 1. Menambahkan atribut khusus (nomor_referensi)
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)  # Menginisialisasi atribut jumlah dari Pembayaran
        self.nomor_referensi = nomor_referensi

    # 3. Implementasi proses() untuk pembayaran transfer
    def proses(self):
        print(
            f"Pembayaran transfer sebesar Rp{self.jumlah:,} berhasil diproses. "
            f"(No. Referensi: {self.nomor_referensi})"
        )


# 4. Fungsi proses_semua yang memanfaatkan polymorphism
def proses_semua(daftar_pembayaran):
    for pembayaran in daftar_pembayaran:
        pembayaran.proses()  # Memanggil method proses() tanpa peduli tipe spesifiknya


# 5. Pengujian dengan object dari setiap subclass
if __name__ == "__main__":
    bayar_tunai = PembayaranTunai(50000)
    bayar_transfer = PembayaranTransfer(150000, "TRX-20261015-001")

    daftar_pembayaran = [bayar_tunai, bayar_transfer]

    print("--- Memproses Daftar Pembayaran ---")
    proses_semua(daftar_pembayaran)