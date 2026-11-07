# Soal A1 — Konsep Dasar OOP
class Kendaraan:
    def __init__(self, nama: str, kecepatan_maks: int):
        self.nama = nama
        self.kecepatan_maks = kecepatan_maks

    def info(self) -> str:
        return f"{self.nama} (Maks: {self.kecepatan_maks} km/jam)"

if __name__ == "__main__":
    motor = Kendaraan("Yamaha NMAX", 120)
    print(motor.info())
