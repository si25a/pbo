"""Scaffold latihan mandiri Pertemuan 2.

Buat class KartuMahasiswa sesuai spesifikasi materi, lalu jalankan:
    python3 latihan_mandiri_2.py
"""


class KartuMahasiswa:
    """Latihan class object dengan method perubahan data."""

    def __init__(self, nama, nim, saldo):
        # LATIHAN: simpan nama, nim, dan saldo sebagai attribute.
        self._nama = nama
        self._nim = nim
        self._saldo = saldo

    def isi_saldo(self, jumlah):
        # LATIHAN: tambahkan jumlah ke saldo.
        self._saldo += jumlah

    def gunakan_saldo(self, jumlah):
        # LATIHAN: kurangi saldo jika saldo mencukupi dan kembalikan True.
        if self._saldo >= jumlah:
            self._saldo -= jumlah
            return True
        return False

    def tampilkan_info(self):
        # LATIHAN: cetak nama, nim, dan saldo.
        print(f"Nama: {self._nama}, NIM: {self._nim}, Saldo: {self._saldo}")


if __name__ == "__main__":
    kartu = KartuMahasiswa("Ani Lestari", "SI-102", 20000)
    kartu.tampilkan_info()
    kartu.isi_saldo(10000)
    kartu.gunakan_saldo(15000)
    kartu.tampilkan_info()