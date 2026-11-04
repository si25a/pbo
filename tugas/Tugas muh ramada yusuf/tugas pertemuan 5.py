class Hewan:
    """Superclass yang merepresentasikan hewan secara umum."""

    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."  # method dasar yang akan dioverride oleh subclass


class Kucing(Hewan):
    # 1. Override method suara() untuk Kucing
    def suara(self):
        return "Meong"


class Anjing(Hewan):
    # 2. Override method suara() untuk Anjing
    def suara(self):
        return "Guk"


# 3. Buat fungsi tampilkan_suara(daftar)
def tampilkan_suara(daftar_hewan):
    for hewan in daftar_hewan:
        # Memanggil suara() secara polymorphic dan menampilkan hasilnya
        print(f"{hewan.nama} bersuara: {hewan.suara()}")


# 4. Pengujian dengan object Kucing dan Anjing
if __name__ == "__main__":
    kucing1 = Kucing("Mimi")
    anjing1 = Anjing("Milo")

    daftar_hewan = [kucing1, anjing1]

    print("--- Daftar Suara Hewan ---")
    tampilkan_suara(daftar_hewan)