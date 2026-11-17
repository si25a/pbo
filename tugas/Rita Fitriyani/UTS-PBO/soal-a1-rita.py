class Produk:
    def __init__(self, nama: str, harga: int):
        self.nama = nama
        self.harga = harga

    def info(self) -> str:
        return f"{self.nama} - Rp{self.harga:,}"

if __name__ == "__main__":
    laptop = Produk("Laptop Asus", 8500000)
    print(laptop.info())