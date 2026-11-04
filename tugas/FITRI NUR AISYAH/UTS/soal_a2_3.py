class Hewan:
    def suara(self):
        return "..."

class Kucing(Hewan):
    def suara(self):                      
        return "Meong"

class Anjing(Hewan):
    def suara(self):                      # override
        return "Guk guk"

for h in [Kucing(), Anjing()]:
    print(h.suara())    
