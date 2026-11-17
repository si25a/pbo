# Soal B3 — Analisis dan Perbaikan Kode (Studi Kasus Paket Data Mobile)
class PaketData:
    def __init__(self, nama_pengguna: str, kuota_mb: float):
        self.nama_pengguna = nama_pengguna
        self.__kuota_mb = max(0.0, float(kuota_mb))

    @property
    def kuota_mb(self) -> float:
        return self.__kuota_mb

    def isi_ulang(self, jumlah: float) -> bool:
        if jumlah > 0:
            self.__kuota_mb += jumlah
            print(f"Isi ulang berhasil: +{jumlah:,.2f} MB")
            return True
        print("Isi ulang gagal: Jumlah kuota isi ulang harus lebih besar dari 0.")
        return False

    def pakai_kuota(self, jumlah: float) -> bool:
        if jumlah <= 0:
            print("Penggunaan gagal: Jumlah penggunaan harus lebih besar dari 0.")
            return False
        if jumlah > self.__kuota_mb:
            print(f"Penggunaan gagal: Kuota tidak mencukupi (Sisa Kuota: {self.__kuota_mb:,.2f} MB).")
            return False

        self.__kuota_mb -= jumlah
        print(f"Penggunaan berhasil: -{jumlah:,.2f} MB")
        return True

    def tampilkan_kuota(self) -> None:
        print(f"Sisa Kuota {self.nama_pengguna}: {self.__kuota_mb:,.2f} MB")


if __name__ == "__main__":
    paket = PaketData("Rita", 5000)
    paket.tampilkan_kuota()
    print("=" * 40)
    paket.isi_ulang(2000)
    paket.pakai_kuota(1500)
    paket.pakai_kuota(10000)
    paket.pakai_kuota(-500)