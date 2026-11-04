"""Scaffold latihan mandiri - Analisis pengelolaan data buku."""


# ==============================================
# PENDEKATAN PROSEDURAL
# ==============================================

def tambah_buku(daftar_buku, judul, penulis):
    # Menambahkan dictionary buku ke daftar_buku
    buku = {
        "judul": judul,
        "penulis": penulis
    }

    daftar_buku.append(buku)



def tampilkan_buku(daftar_buku):
    # Menampilkan seluruh buku dalam daftar_buku
    if not daftar_buku:
        print("Daftar buku kosong.")
    else:
        for buku in daftar_buku:
            print(f"Judul: {buku['judul']}, Penulis: {buku['penulis']}")


def hapus_buku(daftar_buku, judul):
    # Menghapus buku dengan judul tertentu dari daftar_buku
    for buku in daftar_buku:
        if buku["judul"] == judul:
            daftar_buku.remove(buku)
            print(f"Buku '{judul}' berhasil dihapus.")
            return

        print(f"Buku '{judul}' tidak ditemukan.")


#==============================================
# PENDEKATAN OOP
#==============================================

class Buku:
    """Class yang menggabungkan data dan perilaku buku."""

    def __init__(self, judul, penulis):
        # Menyimpan judul dan penulis sebagai attribute
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        # Menampilkan judul dan penulis buku
        print(f"Judul: {self.judul}, Penulis: {self.penulis}")

class KoleksiBuku:
    """Class yang mengelola daftar object Buku."""

    def __init__(self):
        # Menyiapkan list kosong untuk menyimpan object Buku
        self.daftar_buku = []

    def tambah(self, buku):
        # Menambahkan object Buku ke dalam koleksi
        self.daftar_buku.append(buku)

    def tampilkan_semua(self):
        # Menampilkan seluruh buku dalam koleksi
        if not self.daftar_buku:
            print("Koleksi buku kosong.")
        else:
            for buku in self.daftar_buku:
                buku.tampilkan()

 #========================================
 #  PENGUJIAN PENDEKATAN PROSEDURAL
 #========================================
print("=== PENDEKATAN PROSEDURAL ===")

daftar_buku = []

tambah_buku(daftar_buku, "Bumi Manusia", "Pramoedya Ananta Toer")
tambah_buku(daftar_buku, "Harry Potter", "J.K. Rowling")
tambah_buku(daftar_buku, "Sherlock Holmes", "Arthur Conan Doyle")

print("\nDaftar buku:")
tampilkan_buku(daftar_buku)

print("\nDaftar buku:")
hapus_buku(daftar_buku, "Bumi Manusia")

print("\nDaftar buku setelah penghapusan:")
tampilkan_buku(daftar_buku)


#===========================================
# PENGUJIAN PENDEKATAN OOP
#===========================================

print("\n=== PENDEKATAN OOP===")

koleksi = KoleksiBuku()

buku1 = Buku("Bumi Manusia", "Pramoedya Ananta Toer")
buku2 = Buku("Harry Potter", "J.K. Rowling")
buku3 = Buku("Sherlock Holmes", "Arthur Conan Doyle")

koleksi.tambah(buku1)
koleksi.tambah(buku2)
koleksi.tambah(buku3)

print("\nDaftar buku:")
koleksi.tampilkan_semua()



# ==============================================
# ANALISIS PERBANDINGAN PENDEKATAN
# ==============================================

"""
Analisis:

Pendekatan prosedural menggunakan fungsi tambah_buku(), tampilkan_buku(),
dan hapus_buku() untuk mengelola data buku yang disimpan dalam list berisi
dictionary. Pendekatan ini memiliki struktur sederhana dan mudah dipahami,
sehingga cocok untuk program dengan kebutuhan yang masih terbatas.

Pendekatan OOP menggunakan class Buku untuk menggabungkan data dan perilaku
buku, serta class KoleksiBuku untuk mengelola kumpulan objek Buku. Dengan
pendekatan ini, program menjadi lebih terorganisasi karena data dan
perilakunya dikelompokkan ke dalam class.

Untuk sistem perpustakaan yang terus berkembang, pendekatan OOP lebih tepat
digunakan karena:

1. Modularitas: data dan perilaku buku dikelompokkan dalam class sehingga
   struktur program lebih teratur.
2. Mudah dikembangkan: fitur baru seperti pencarian buku, peminjaman,
   pengembalian, dan pengelolaan anggota dapat ditambahkan.
3. Reusabilitas: class Buku dapat digunakan kembali untuk membuat banyak
   objek buku.
4. Pemeliharaan kode: perubahan pada pengelolaan buku dapat dilakukan pada
   class yang berkaitan sehingga program lebih mudah dipelihara.

Kesimpulan:
Pendekatan prosedural lebih sesuai untuk program sederhana, sedangkan
pendekatan OOP lebih sesuai untuk sistem perpustakaan yang memiliki banyak
fitur dan kebutuhan pengembangan di masa depan.
"""
