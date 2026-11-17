class RekeningBank:
    def __init__(self, pemilik: str, saldo_awal: float = 0.0):
        self.pemilik = pemilik
        self.__saldo = float(saldo_awal) if saldo_awal >= 0 else 0.0

    @property
    def saldo(self) -> float:
        return self.__saldo

    def setor(self, jumlah: float):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"[SUKSES] Setor Rp{jumlah:,.2f} berhasil.")
        else:
            print("[GAGAL] Jumlah setoran harus bernilai positif (> 0).")

    def tarik(self, jumlah: float) -> bool:
        if jumlah <= 0:
            print("[GAGAL] Jumlah penarikan harus bernilai positif (> 0).")
            return False
        if jumlah > self.__saldo:
            print(f"[GAGAL] Saldo tidak mencukupi. Saldo saat ini: Rp{self.__saldo:,.2f}")
            return False

        self.__saldo -= jumlah
        print(f"[SUKSES] Tarik Rp{jumlah:,.2f} berhasil.")
        return True

    def tampilkan_saldo(self):
        print(f"Pemilik: {self.pemilik} | Saldo Terkini: Rp{self.__saldo:,.2f}")


if __name__ == "__main__":
    # Inisialisasi rekening dengan saldo awal Rp500.000
    rek_budi = RekeningBank("Budi", 500000)
    rek_budi.tampilkan_saldo()

    print("\n--- 1. Setor Uang Valid (Rp200.000) ---")
    rek_budi.setor(200000)
    rek_budi.tampilkan_saldo()

    print("\n--- 2. Tarik Uang Valid (Rp300.000) ---")
    rek_budi.tarik(300000)
    rek_budi.tampilkan_saldo()

    print("\n--- 3. Tarik Uang Melebihi Saldo (Rp1.000.000) ---")
    rek_budi.tarik(1000000)
    rek_budi.tampilkan_saldo()

    print("\n--- 4. Tarik Jumlah Negatif (-Rp50.000) ---")
    rek_budi.tarik(-50000)
    rek_budi.tampilkan_saldo()
