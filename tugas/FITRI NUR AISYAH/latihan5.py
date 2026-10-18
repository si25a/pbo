class Pembayaran:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError 


class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Memproses pembayaran tunai sebesar: Rp {self.jumlah:,}")


class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Memproses pembayaran transfer sebesar: Rp {self.jumlah:,} | No. Referensi: {self.nomor_referensi}"
        )


def proses_semua(daftar):
    for pembayaran in daftar:
        pembayaran.proses()

if __name__ == "__main__":
    tunai = PembayaranTunai(20000)
    transfer = PembayaranTransfer(10000, "REF-2026-250660221049")
    daftar_pembayaran = [tunai, transfer]

    print("--- Hasil Proses Pembayaran Fitri Nur Aisyah ---")
    proses_semua(daftar_pembayaran)