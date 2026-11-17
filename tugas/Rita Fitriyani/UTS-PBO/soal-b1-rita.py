# Soal B1 — Class dan Encapsulation (Studi Kasus Rental Kamar Hotel)
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

if __name__ == "__main__":
    k1 = Kamar("101", "Deluxe")
    k2 = Kamar("102", "Suite")
    print("--- Status Awal ---")
    print(k1)
    print(k2)

    print("\n--- Memesan Kamar 101 ---")
    k1.pesan()
    print("--- Status Akhir ---")
    print(k1)
    print(k2)