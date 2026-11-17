# Soal B2 — Inheritance dan Polymorphism (Standalone)
class Kamar:
    def __init__(self, nomor: str, tipe: str):
        self.nomor = nomor
        self.tipe = tipe
        self.__terisi = False  # Private attribute

    def pesan(self) -> bool:
        if not self.__terisi:
            self.__terisi = True
            return True
        return False

    def kosongkan(self) -> None:
        self.__terisi = False

    @property
    def terisi(self) -> bool:
        return self.__terisi

    def __str__(self) -> str:
        status = "Terisi" if self.__terisi else "Tersedia"
        return f"Kamar {self.nomor} ({self.tipe}) — [{status}]"


# Inheritance: KamarVip mewarisi sifat dari kelas Kamar
class KamarVip(Kamar):
    def __init__(self, nomor: str, tipe: str, fasilitas_tambahan: str):
        super().__init__(nomor, tipe)
        self.fasilitas_tambahan = fasilitas_tambahan

    # Polymorphism: Meng-override method __str__ milik class parent
    def __str__(self) -> str:
        status = "Terisi" if self.terisi else "Tersedia"
        return f"Kamar {self.nomor} ({self.tipe}) — [{status}] + Exclusives: {self.fasilitas_tambahan}"

    def layanan_butler(self) -> str:
        if self.terisi:
            return f"Memanggil layanan butler pribadi untuk Kamar {self.nomor}."
        return "Layanan butler hanya tersedia untuk kamar yang sedang terisi."


# Polymorphism: Fungsi ini memanggil __str__() sesuai tipe objek masing-masing
def tampilkan_info(daftar_kamar: list):
    for kamar in daftar_kamar:
        print(kamar)


if __name__ == "__main__":
    kamar_standar = Kamar("101", "Standard")
    kamar_vip = KamarVip("501", "Penthouse VIP", "Kolam Renang Privat & Jacuzzi")

    # Mengubah status kamar VIP menjadi terisi
    kamar_vip.pesan()

    print("--- Daftar Informasi Kamar ---")
    tampilkan_info([kamar_standar, kamar_vip])

    print("\n--- Layanan Khusus ---")
    print(kamar_vip.layanan_butler())