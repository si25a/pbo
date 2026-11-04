class Pembayaran:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def proses(self):
        raise NotImplementedError(
            "Method proses() harus diimplementasikan oleh subclass."
        )


class PembayaranTunai(Pembayaran):
    def proses(self):
        print(f"Memproses pembayaran tunai sebesar Rp{self.jumlah:,}.")


class PembayaranTransfer(Pembayaran):
    def __init__(self, jumlah, nomor_referensi):
        super().__init__(jumlah)
        self.nomor_referensi = nomor_referensi

    def proses(self):
        print(
            f"Memproses transfer sebesar Rp{self.jumlah:,} "
            f"dengan nomor referensi {self.nomor_referensi}."
        )


def proses_semua_pembayaran(daftar_pembayaran):
    for pembayaran in daftar_pembayaran:
        pembayaran.proses()


if __name__ == "__main__":
    pembayaran_tunai = PembayaranTunai(150000)
    pembayaran_transfer = PembayaranTransfer(275000, "TRX20261029")

    daftar_pembayaran = [
        pembayaran_tunai,
        pembayaran_transfer,
    ]

    proses_semua_pembayaran(daftar_pembayaran)
