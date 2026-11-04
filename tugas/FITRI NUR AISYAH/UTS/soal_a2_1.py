class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo             

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah

    def get_saldo(self):                  # 
        return self.__saldo

r = Rekening(100000)
r.setor(50000)
print(r.get_saldo())    
