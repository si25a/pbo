class Kendaraan:  # Class

  def __init__(self, merk):  # Constructor
    self.merk = merk  # Attribute

  def klakson(self, suara):  # Method
    return f"{self.merk} berbunyi {suara}"


# Membuat Object
mobil = Kendaraan("Toyota")
print(mobil.klakson("Tin Tin"))
