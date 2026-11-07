"""
Soal B3 — Analisis dan Perbaikan Kode

Perhatikan kode berikut yang memiliki beberapa kesalahan:

class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo = self.saldo + jumlah

    def tarik(self, jumlah):
        self.saldo = self.saldo - jumlah

    def tampilkan_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.saldo}")

Tugas:
1. Identifikasi tiga kesalahan atau kelemahan pada kode tersebut dari perspektif OOP.
2. Perbaiki kode dengan menerapkan encapsulation (attribute privat), validasi pada method setor() dan tarik() (jumlah harus positif dan penarikan tidak boleh melebihi saldo), serta property untuk mengakses saldo.
3. Tulis program utama yang mendemonstrasikan: setor uang, tarik uang yang valid, tarik uang yang melebihi saldo (harus menolak), dan tarik jumlah negatif (harus menolak).

Jawaban:
1. Identifikasi 3 Kesalahan/Kelemahan dari Perspektif OOP pada Kode Asli:
   a. Tidak ada Encapsulation: Atribut `pemilik` dan `saldo` bersifat publik sehingga bisa diubah langsung dari luar tanpa validasi (misal: `rekening.saldo = -500000`).
   b. Kurangnya Validasi Input: Method `setor()` dan `tarik()` tidak mengecek apakah jumlah bernilai negatif.
   c. Kurangnya Validasi Saldo: Method `tarik()` membiarkan penarikan melebihi saldo yang tersedia sehingga saldo bisa bernilai negatif (minus).

   2. Berikut Perbaikan Kode dengan menerapkan encapsulation
"""
class RekeningBank:
    def __init__(self, pemilik: str, saldo: float):
        self.__pemilik = pemilik
        self.__saldo = 0
        if saldo >= 0:
            self.__saldo = saldo

    @property
    def pemilik(self):
        return self.__pemilik

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah: float):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Setor Rp{jumlah} berhasil.")
        else:
            print("Setor gagal: Jumlah harus positif.")

    def tarik(self, jumlah: float) -> bool:
        if jumlah <= 0:
            print("Penarikan gagal: Jumlah penarikan harus positif.")
            return False
        if jumlah > self.__saldo:
            print("Penarikan gagal: Saldo tidak mencukupi.")
            return False
        
        self.__saldo -= jumlah
        print(f"Tarik Rp{jumlah} berhasil.")
        return True

    def tampilkan_saldo(self):
        print(f"Saldo {self.__pemilik}: Rp{self.__saldo}")

"""
3. Berikut program utama yang mendemonstrasikan: setor uang, tarik uang yang valid, tarik uang yang melebihi saldo (harus menolak), dan tarik jumlah negatif (harus menolak).
"""
if __name__ == "__main__":
    rekening = RekeningBank("Siti Aulia Nur'azizah Furqon", 500000)
    rekening.tampilkan_saldo()

    print("\n1. Setor Uang Valid:")
    rekening.setor(200000)
    rekening.tampilkan_saldo()

    print("\n2. Tarik Uang Valid:")
    rekening.tarik(100000)
    rekening.tampilkan_saldo()

    print("\n3. Tarik Melebihi Saldo:")
    rekening.tarik(1000000)

    print("\n4. Tarik Jumlah Negatif:")
    rekening.tarik(-50000)

    print("\nSaldo Akhir:")
    rekening.tampilkan_saldo()