"""
Soal A3 - Analisis Desain

Perhatikan rancangan class berikut:
"""

class Pengguna:
    def __init__(self, nama, email):
        self.__nama = nama
        self.__email = email

    @property
    def nama(self):
        return self.__nama

class Mahasiswa(Pengguna):
    def __init__(self, nama, email, nim):
        super().__init__(nama, email)
        self.nim = nim

    def tampilkan_peran(self):
        return f"{self.nama} adalah mahasiswa dengan NIM {self.nim}"

"""
1. Konsep OOP mana yang diterapkan pada self.__nama dan @property? Jelaskan alasan teknisnya.
Jawaban:  Konsep Encapsulation.
    Awalan dua garis bawah (`self.__nama`) mengubah atribut nama menjadi privat (name mangling) sehingga tidak dapat diakses atau diubah secara langsung dari luar class. Sedangkan `@property` digunakan untuk membuat 'getter' aman yang memberikan akses baca ke atribut privat tersebut.

2. Konsep OOP mana yang diterapkan pada class Mahasiswa(Pengguna)? Jelaskan apa yang dilakukan super().
Jawaban: Konsep Inheritance (Pewarisan).
    Class Mahasiswa mewarisi semua sifat/atribut dari superclass Pengguna. Fungsi `super().__init__(nama, email)` memanggil constructor milik parent class (Pengguna) untuk menginisialisasi atribut `nama` dan `email` tanpa perlu menulis ulang logikanya.

3. Mengapa self.nama dapat dipanggil pada method tampilkan_peran() di subclass meskipun attribute tersebut privat di superclass?
Jawaban: Karena `self.nama` pada subclass mendatangi `@property` milik superclass (bukan langsung mengakses atribut privat `self.__nama`). Property `nama` bertindak sebagai method getter publik yang mengembalikan nilai `self.__nama`, sehingga subclass dapat mengakses nilainya dengan aman.
"""