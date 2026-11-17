class Kendaraan:
    def __init__(self, merk: str, warna: str):
        self.merk = merk  # Attribute
        self.warna = warna  # Attribute

    def info(self) -> str:  # Method
        return f"Mobil {self.merk} berwarna {self.warna}"


if __name__ == "__main__":
    # Membuat Object
    mobil_saya = Kendaraan("Toyota", "Hitam")
    print(mobil_saya.info())
