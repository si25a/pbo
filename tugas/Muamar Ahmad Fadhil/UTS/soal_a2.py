# Soal A2 — Pilar OOP
# File: soal_a2.py

from abc import ABC, abstractmethod

# 1. Encapsulation (Enkapsulasi)
class AkunBank:
    def __init__(self, saldo: float):
        self.__saldo = saldo  # Attribute privat (__saldo)

    def get_saldo(self) -> float:
        return self.__saldo


# 2. Inheritance (Pewarisan)
class Perangkat:
    def nyalakan(self) -> str:
        return "Perangkat dinyalakan."

class Smartphone(Perangkat):  # Smartphone mewarisi Perangkat
    pass


# 3. Polymorphism (Polimorfisme)
class SensorSuhu:
    def baca_data(self) -> str:
        return "Membaca suhu ruangan..."

class SensorHujan:
    def baca_data(self) -> str:
        return "Membaca curah hujan..."

def proses_sensor(sensor):
    print(sensor.baca_data())


# 4. Abstraction (Abstraksi)
class Microcontroller(ABC):
    @abstractmethod
    def setup(self):
        pass

class ESP32(Microcontroller):
    def setup(self) -> str:
        return "Inisialisasi Wi-Fi dan pin GPIO pada ESP32..."


if __name__ == "__main__":
    print("--- 1. Encapsulation ---")
    akun = AkunBank(500000)
    print(f"Saldo: Rp{akun.get_saldo()}")

    print("2. Inheritance ---")
    hp = Smartphone()
    print(hp.nyalakan())

    print("3. Polymorphism ---")
    proses_sensor(SensorSuhu())
    proses_sensor(SensorHujan())

    print("4. Abstraction ---")
    esp = ESP32()
    print(esp.setup())
