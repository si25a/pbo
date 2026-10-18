# ==============================================================================
# SOAL 1 — KONSEP POLYMORPHISM
# ==============================================================================
# Pengertian:
# Polymorphism (banyak bentuk) adalah konsep OOP yang memungkinkan satu nama 
# method yang sama memiliki perilaku/implementasi berbeda tergantung pada objeknya.

class Kucing:
    def bersuara(self):
        return "Meow!"

class Anjing:
    def bersuara(self):
        return "Guk guk!"

def demo_soal_1():
    print("=== SOAL 1 ===")
    hewan_list = [Kucing(), Anjing()]
    for hewan in hewan_list:
        print(hewan.bersuara())
    print()


# SOAL 2 — OVERRIDING DAN POLYMORPHISM (DENGAN CONTOH RUNNING)
# ==============================================================================

class Bentuk:
    def hitung_luas(self):
        # Method dasar pada class induk
        return 0

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    # OVERRIDING: Mengganti method hitung_luas milik Bentuk
    def hitung_luas(self):
        return self.sisi * self.sisi

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    # OVERRIDING: Mengganti method hitung_luas dengan rumus lingkaran
    def hitung_luas(self):
        return 3.14 * self.jari_jari * self.jari_jari


def cetak_luas(bentuk_objek):
    # PERILAKU POLIMORFIK:
    # Fungsi ini hanya memanggil .hitung_luas()
    # Python secara otomatis memilih versi method milik class anak yang tepat saat runtime
    print(f"Luas: {bentuk_objek.hitung_luas()}")


def demo_soal_2():
    print("=== DEMO SOAL 2 ===")
    p = Persegi(sisi=4)
    l = Lingkaran(jari_jari=7)

    # Memanggil fungsi yang sama, tetapi perilakunya berbeda sesuai objeknya
    cetak_luas(p)  # Menjalankan hitung_luas() milik Persegi -> 16
    cetak_luas(l)  # Menjalankan hitung_luas() milik Lingkaran -> 153.86


if __name__ == "__main__":
    demo_soal_2()
# ==============================================================================
# SOAL 3 — PREDIKSI OUTPUT
# ==============================================================================
class Pengguna:
    def tampilkan_peran(self):
        return "Pengguna sistem"

class Mahasiswa(Pengguna):
    def tampilkan_peran(self):
        return "Mahasiswa"

class Dosen(Pengguna):
    def tampilkan_peran(self):
        return "Dosen"

def demo_soal_3():
    print("=== SOAL 3 ===")
    # Output:
    # Mahasiswa
    # Dosen
    #
    # Konsep OOP: Subtype Polymorphism / Inheritance-based Polymorphism.
    # Method tampilkan_peran() di-override oleh class Mahasiswa dan Dosen.
    for data in [Mahasiswa(), Dosen()]:
        print(data.tampilkan_peran())
    print()


# ==============================================================================
# SOAL 4 — DUCK TYPING
# ==============================================================================
class MhsDuck:
    def ringkasan(self):
        return "Mahasiswa — zia"

class DsnDuck:
    def ringkasan(self):
        return "Dosen — roziah"

def tampilkan(data):
    print(data.ringkasan())

def demo_soal_4():
    print("=== SOAL 4 ===")
    # Fungsi tampilkan() bisa menerima kedua objek tanpa inheritance karena Duck Typing:
    # Python hanya peduli "apakah objek memiliki method ringkasan()?", 
    # bukan "apa tipe data atau class induk dari objek tersebut?".
    tampilkan(MhsDuck())
    tampilkan(DsnDuck())
    print()


# ==============================================================================
# SOAL 5 — MERANCANG FUNGSI POLIMORFIK
# ==============================================================================
def tampilkan_semua(daftar):
    for item in daftar:
        print(item.ringkasan())

class Produk:
    def ringkasan(self):
        return "Produk — Laptop"

class ObjekTanpaRingkasan:
    pass

def demo_soal_5():
    print("=== SOAL 5 ===")
    daftar_objek = [MhsDuck(), DsnDuck(), Produk()]
    print("1. Memanggil objek yang valid:")
    tampilkan_semua(daftar_objek)
    
    print("\n2. Apa yang terjadi jika objek tidak punya method ringkasan():")
    print("Akan memicu AttributeError dan program terhenti/error saat runtime.")
    
    # Penanganan dengan try-except untuk demonstrasi aman:
    daftar_campuran = [MhsDuck(), ObjekTanpaRingkasan()]
    try:
        tampilkan_semua(daftar_campuran)
    except AttributeError as e:
        print(f"Error tertangkap: {e}")


# ==============================================================================
# RUNNER UTAMA
# ==============================================================================
if __name__ == "__main__":
    demo_soal_1()
    demo_soal_3()
    demo_soal_4()
    demo_soal_5()
