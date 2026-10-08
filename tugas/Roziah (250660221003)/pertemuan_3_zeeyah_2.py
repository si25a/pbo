class RekeningMahasiswa:
    """Latihan private attribute dan property saldo."""

    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = 0
        # Memanggil setter saldo untuk memvalidasi saldo_awal
        self.saldo = saldo_awal

    @property
    def saldo(self):
        # Getter untuk mengakses saldo private
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        # Validasi agar saldo berupa angka (int/float), bukan boolean, dan tidak negatif
        if not isinstance(nilai, (int, float)) or isinstance(nilai, bool) or nilai < 0:
            raise ValueError("Saldo harus berupa angka tidak negatif")
        self.__saldo = nilai

    def setor(self, jumlah):
        # Validasi jumlah setoran harus angka positif
        if not isinstance(jumlah, (int, float)) or isinstance(jumlah, bool) or jumlah <= 0:
            raise ValueError("Jumlah setoran harus berupa angka positif")
        self.saldo += jumlah

    def tarik(self, jumlah):
        # Opsional: Validasi penarikan uang (tidak boleh melebihi saldo)
        if not isinstance(jumlah, (int, float)) or isinstance(jumlah, bool) or jumlah <= 0:
            raise ValueError("Jumlah penarikan harus berupa angka positif")
        if jumlah > self.__saldo:
            raise ValueError("Saldo tidak mencukupi untuk penarikan ini")
        self.saldo -= jumlah


if __name__ == "__main__":
    rekening = RekeningMahasiswa("Roziah", 50000)
    rekening.setor(25000)
    print(f"Pemilik : {rekening.pemilik}")
    print(f"Saldo akhir: {rekening.saldo}")  # Output: 75000
    
    # Contoh pengujian tarik tunai
    rekening.tarik(15000)
    print(f"Saldo setelah tarik 15.000: {rekening.saldo}") # Output: 60000
