class RekeningBank:
    """Class untuk merepresentasikan rekening bank dengan enkapsulasi dan validasi."""

    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        # 1. ENKAPSULASI: Membuat saldo menjadi privat (__saldo)
        self.__saldo = saldo_awal if saldo_awal >= 0 else 0

    def setor(self, jumlah):
        # 2. VALIDASI SETOR: Jumlah harus positif (> 0)
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor tunai Rp{jumlah:,} berhasil.")
        else:
            print("Gagal setor: Jumlah setoran harus bernilai positif.")

    def tarik(self, jumlah):
        # 2. VALIDASI TARIK: Harus positif dan tidak boleh melebihi saldo
        if jumlah <= 0:
            print("Gagal tarik: Jumlah penarikan harus bernilai positif.")
            return False
        elif jumlah > self.__saldo:
            print("Gagal tarik: Saldo tidak mencukupi!")
            return False
        else:
            self.__saldo -= jumlah
            print(f"Tarik tunai Rp{jumlah:,} berhasil.")
            return True

    @property
    def saldo(self):
        # 3. PROPERTY: Memungkinkan luar class membaca saldo secara aman
        return self.__saldo

    def tampilkan_saldo(self):
        print(f"Pemilik: {self.pemilik} | Saldo saat ini: Rp{self.__saldo:,}")


# === Program Utama untuk Pengujian ===
if __name__ == "__main__":
    # Membuat rekening dengan saldo awal Rp2.000.000
    rekening_salwa = RekeningBank("Salwa", 2000000)

    print("=== STATUS AWAL ===")
    rekening_salwa.tampilkan_saldo()
    print()

    print("=== 1. UJI SETOR UANG (VALID: +500rb) ===")
    rekening_salwa.setor(500000)
    rekening_salwa.tampilkan_saldo()
    print()

    print("=== 2. UJI TARIK UANG (VALID: -300rb) ===")
    rekening_salwa.tarik(300000)
    rekening_salwa.tampilkan_saldo()
    print()

    print("=== 3. UJI TARIK UANG MELEBIHI SALDO (GAGAL: -5jt) ===")
    rekening_salwa.tarik(5000000)  # Ini akan ditolak oleh program
    rekening_salwa.tampilkan_saldo()
    print()

    print("=== 4. UJI TARIK JUMLAH NEGATIF (GAGAL: -150rb) ===")
    rekening_salwa.tarik(-150000)  # Ini juga akan ditolak
    rekening_salwa.tampilkan_saldo()