# Soal B3 — Analisis dan Perbaikan Kode
# File: soal_b3.py

class RekeningBank:
    def __init__(self, pemilik: str, saldo: float):
        self.pemilik = pemilik
        self.__saldo = max(0.0, float(saldo))  # Enkapsulasi privat

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


# Program Utama
if __name__ == "__main__":
    rek = RekeningBank("Fadhil", 500000)
    rek.tampilkan_saldo()
    print("=" * 45)

    # Demo 1: Setor uang
    print("[1] Uji Coba Setor Uang (Rp200.000):")
    rek.setor(200000)
    rek.tampilkan_saldo()
    print("-" * 45)

    # Demo 2: Tarik uang yang valid
    print("[2] Uji Coba Penarikan Valid (Rp150.000):")
    rek.tarik(150000)
    rek.tampilkan_saldo()
    print("-" * 45)

    # Demo 3: Tarik uang melebihi saldo (Harus menolak)
    print("[3] Uji Coba Tarik Melebihi Saldo (Rp1.000.000):")
    rek.tarik(1000000)
    rek.tampilkan_saldo()
    print("-" * 45)

    # Demo 4: Tarik jumlah negatif (Harus menolak)
    print("[4] Uji Coba Tarik Jumlah Negatif (-Rp50.000):")
    rek.tarik(-50000)
    rek.tampilkan_saldo()
