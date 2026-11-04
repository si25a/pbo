# Soal B3 — Analisis dan Perbaikan Kode
class RekeningBank:
    def __init__(self, pemilik: str, saldo: float):
        self.pemilik = pemilik
        self.__saldo = max(0.0, float(saldo))

    @property
    def saldo(self) -> float:
        return self.__saldo

    def setor(self, jumlah: float) -> bool:
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor berhasil: Rp{jumlah:,.2f}")
            return True
        print("Setor gagal: Jumlah setoran harus lebih besar dari 0.")
        return False

    def tarik(self, jumlah: float) -> bool:
        if jumlah <= 0:
            print("Tarik gagal: Jumlah penarikan harus lebih besar dari 0.")
            return False
        if jumlah > self.__saldo:
            print(f"Tarik gagal: Saldo tidak mencukupi (Saldo: Rp{self.__saldo:,.2f}).")
            return False

        self.__saldo -= jumlah
        print(f"Tarik berhasil: Rp{jumlah:,.2f}")
        return True

    def tampilkan_saldo(self) -> None:
        print(f"Saldo {self.pemilik}: Rp{self.__saldo:,.2f}")

if __name__ == "__main__":
    rek = RekeningBank("EDEULIO", 500000)
    rek.tampilkan_saldo()
    print("=" * 40)
    rek.setor(200000)
    rek.tarik(150000)
    rek.tarik(1000000)
    rek.tarik(-50000)
