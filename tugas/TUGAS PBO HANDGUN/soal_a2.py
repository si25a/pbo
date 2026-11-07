# Soal A2 — Pilar OOP
from abc import ABC, abstractmethod

# 1. Encapsulation
class DompetElektronik:
    def __init__(self, saldo: float):
        self.__saldo = saldo

    def cek_saldo(self) -> float:
        return self.__saldo

# 2. Inheritance
class Komputer:
    def boot(self) -> str:
        return "Sistem dinyalakan."

class PCDesktop(Komputer):
    pass

# 3. Polymorphism
class KartuKredit:
    def bayar(self) -> str:
        return "Bayar via Kartu Kredit."

class Qris:
    def bayar(self) -> str:
        return "Bayar via QRIS."

def proses_bayar(metode):
    print(metode.bayar())

# 4. Abstraction
class ModulIntronet(ABC):
    @abstractmethod
    def kirim_data(self):
        pass

class LoRaNode(ModulIntronet):
    def kirim_data(self) -> str:
        return "Kirim paket data via LoRa."

if __name__ == "__main__":
    print(f"Saldo: Rp{DompetElektronik(250000).cek_saldo()}")
    print(PCDesktop().boot())
    proses_bayar(KartuKredit())
    proses_bayar(Qris())
    print(LoRaNode().kirim_data())
