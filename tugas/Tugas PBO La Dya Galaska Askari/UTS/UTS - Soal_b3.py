class RekeningBank:
    def __init__(self, pemilik: str, saldo_awal: float = 0.0):
        self.__pemilik = pemilik
        if saldo_awal < 0:
            raise ValueError("Saldo awal tidak boleh negatif.")
        self.__saldo = saldo_awal

    @property
    def pemilik(self) -> str:
        return self.__pemilik

    @property
    def saldo(self) -> float:
        return self.__saldo

    def setor(self, jumlah: float):
        if jumlah <= 0:
            print(f"Gagal setor: Jumlah Rp{jumlah:,.2f} tidak valid (harus > 0).")
            return
        self.__saldo += jumlah
        print(f"Berhasil setor Rp{jumlah:,.2f}. Saldo terkini: Rp{self.__saldo:,.2f}")

    def tarik(self, jumlah: float):
        if jumlah <= 0:
            print(f"Gagal tarik: Jumlah Rp{jumlah:,.2f} tidak valid (harus > 0).")
            return
        if jumlah > self.__saldo:
            print(f"Gagal tarik: Saldo tidak mencukupi (Saldo: Rp{self.__saldo:,.2f}, Diminta: Rp{jumlah:,.2f})")
            return
        self.__saldo -= jumlah
        print(f"Berhasil tarik Rp{jumlah:,.2f}. Saldo terkini: Rp{self.__saldo:,.2f}")

    def tampilkan_saldo(self):
        print(f"Pemilik Rekening: {self.__pemilik} | Saldo: Rp{self.__saldo:,.2f}")

if __name__ == "__main__":
    rekening = RekeningBank("Rizki", 1000000.0)
    rekening.tampilkan_saldo()

    print("\n--- Demonstrasi Transaksi ---")
    rekening.setor(500000.0)      # Valid
    rekening.tarik(300000.0)      # Valid
    rekening.tarik(3000000.0)     # Melebihi saldo (Ditolak)
    rekening.setor(-50000.0)      # Negatif (Ditolak)
    rekening.tarik(-100000.0)     # Negatif (Ditolak)