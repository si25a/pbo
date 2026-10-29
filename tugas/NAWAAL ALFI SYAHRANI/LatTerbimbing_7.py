"""Scaffold latihan terbimbing — Perbandingan pengelolaan nilai mahasiswa."""


def hitung_rata_rata(daftar_nilai):
    # LATIHAN 1: hitung rata-rata dari daftar_nilai dan kembalikan hasilnya.
    if not daftar_nilai:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)


class Mahasiswa:
    """Class yang menggabungkan data nilai dan perilaku perhitungan."""

    def __init__(self, nama, daftar_nilai):
        # LATIHAN 2: simpan nama dan daftar_nilai sebagai attribute.
        self.nama = nama
        self.daftar_nilai = daftar_nilai

    def rata_rata(self):
        # LATIHAN 3: hitung rata-rata dari attribute daftar_nilai.
        if not self.daftar_nilai:
            return 0
        return sum(self.daftar_nilai) / len(self.daftar_nilai)


# Tugas:
# 1. Lengkapi fungsi hitung_rata_rata() pada pendekatan prosedural. (Selesai)
# 2. Lengkapi class Mahasiswa pada pendekatan OOP. (Selesai)
# 3. Uji kedua pendekatan dengan data yang sama.
# 4. Bandingkan cara data dikelola pada kedua pendekatan.

if __name__ == "__main__":
    # Data Uji
    nama_mhs = "Budi"
    nilai_mhs = [80, 85, 90, 75]

    print("=== 1. UJI PENDEKATAN PROSEDURAL ===")
    rata_prosedural = hitung_rata_rata(nilai_mhs)
    print(f"Mahasiswa : {nama_mhs}")
    print(f"Rata-rata : {rata_prosedural:.2f}\n")

    print("=== 2. UJI PENDEKATAN OOP ===")
    mhs = Mahasiswa(nama_mhs, nilai_mhs)
    print(f"Mahasiswa : {mhs.nama}")
    print(f"Rata-rata : {mhs.rata_rata():.2f}\n")

    print("=== 3. PERBANDINGAN PENGELOLAAN DATA ===")
    print(
        """
1. Pendekatan Prosedural:
   - Data (nama & daftar_nilai) terpisah dari fungsi (hitung_rata_rata).
   - Fungsi tidak menyimpan status data, sehingga data harus selalu dikirimkan
     sebagai argumen setiap kali fungsi dipanggil.

2. Pendekatan Object-Oriented (OOP):
   - Data (attribute `nama` dan `daftar_nilai`) membungkus satu kesatuan
     dengan perilaku/fungsi (`rata_rata()`) di dalam satu objek/class (Enkapsulasi).
   - Method `rata_rata()` secara otomatis dapat mengakses attribute milik objek
     itu sendiri (`self.daftar_nilai`) tanpa perlu menerima data eksternal lagi.
"""
    )