class RekeningBank:

  def __init__(self, pemilik: str, saldo: float):
    self.pemilik = pemilik
    self.__saldo = saldo  # Enkapsulasi: atribut saldo dibuat privat

  @property
  def saldo(self) -> float:
    return self.__saldo

  def setor(self, jumlah: float):
    if jumlah > 0:
      self.__saldo += jumlah
      print(
          f"Setor berhasil. Saldo {self.pemilik} sekarang: Rp{self.__saldo:,.2f}"
      )
    else:
      print("Gagal setor: Jumlah setoran harus bernilai positif.")

  def tarik(self, jumlah: float):
    if jumlah <= 0:
      print("Gagal tarik: Jumlah penarikan harus bernilai positif.")
    elif jumlah > self.__saldo:
      print(
          f"Gagal tarik: Saldo tidak mencukupi. Saldo saat ini:"
          f" Rp{self.__saldo:,.2f}"
      )
    else:
      self.__saldo -= jumlah
      print(
          f"Tarik berhasil. Saldo {self.pemilik} sekarang: Rp{self.__saldo:,.2f}"
      )

  def tampilkan_saldo(self):
    print(f"Saldo {self.pemilik}: Rp{self.__saldo:,.2f}")


# Program Utama / Demonstrasi
if __name__ == "__main__":
  rekening = RekeningBank("Roziah", 500000)
  rekening.tampilkan_saldo()

  print("\n1. Setor uang valid (Rp150.000):")
  rekening.setor(150000)

  print("\n2. Tarik uang valid (Rp200.000):")
  rekening.tarik(200000)

  print("\n3. Tarik uang melebihi saldo (Rp1.000.000):")
  rekening.tarik(1000000)

  print("\n4. Tarik jumlah negatif (-Rp50.000):")
  rekening.tarik(-50000)

  print("\n5. Akses saldo via property:")
  print(f"Saldo akhir {rekening.pemilik}: Rp{rekening.saldo:,.2f}")
