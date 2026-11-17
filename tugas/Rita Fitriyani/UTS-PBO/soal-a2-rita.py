# Soal A2 — Pilar OOP (Studi Kasus Restoran & Pemesanan)
from abc import ABC, abstractmethod

# 1. Encapsulation (Enkapsulasi)
class RejekiKasir:
    def __init__(self, total_penjualan: float):
        self.__total_penjualan = total_penjualan  # Private attribute

    def cek_penjualan(self) -> float:
        return self.__total_penjualan

# 2. Inheritance (Pewarisan)
class Makanan:
    def siapkan(self) -> str:
        return "Makanan sedang disiapkan di dapur."

class NasiGoreng(Makanan):
    pass

# 3. Polymorphism (Polimorfisme)
class PesananDineIn:
    def cetak_resi(self) -> str:
        return "Resi: Makan di Tempat (Meja #4)."

class PesananTakeAway:
    def cetak_resi(self) -> str:
        return "Resi: Bawa Pulang (Kemasan Paper Bag)."

def cetak_nota(pesanan):
    print(pesanan.cetak_resi())

# 4. Abstraction (Abstraksi)
class SistemPembayaran(ABC):
    @abstractmethod
    def verifikasi_pembayaran(self) -> str:
        pass

class PembayaranTunai(SistemPembayaran):
    def verifikasi_pembayaran(self) -> str:
        return "Pembayaran tunai berhasil diterima oleh kasir."

if __name__ == "__main__":
    # 1. Encapsulation
    kasir = RejekiKasir(1500000.0)
    print(f"Total Kas: Rp{kasir.cek_penjualan():,.0f}")

    # 2. Inheritance
    nasgor = NasiGoreng()
    print(nasgor.siapkan())

    # 3. Polymorphism
    cetak_nota(PesananDineIn())
    cetak_nota(PesananTakeAway())

    # 4. Abstraction
    pembayaran = PembayaranTunai()
    print(pembayaran.verifikasi_pembayaran())