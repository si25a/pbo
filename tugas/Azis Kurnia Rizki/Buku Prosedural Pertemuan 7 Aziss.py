
"""Pengelolaan buku menggunakan pendekatan prosedural."""

# Bantuan: ChatGPT - penjelasan perbedaan pendekatan prosedural dan OOP.

daftar_buku = []


def tambah_buku(judul):
    daftar_buku.append(judul)
    print(f"Buku '{judul}' berhasil ditambahkan.")


def tampilkan_buku():
    if not daftar_buku:
        print("Belum ada buku.")
    else:
        print("Daftar Buku:")
        for nomor, judul in enumerate(daftar_buku, start=1):
            print(f"{nomor}. {judul}")


def hapus_buku(judul):
    if judul in daftar_buku:
        daftar_buku.remove(judul)
        print(f"Buku '{judul}' berhasil dihapus.")
    else:
        print(f"Buku '{judul}' tidak ditemukan.")


if __name__ == "__main__":
    tambah_buku("Pemrograman Python")
    tambah_buku("Basis Data")
    tampilkan_buku()
    hapus_buku("Basis Data")
    tampilkan_buku()

