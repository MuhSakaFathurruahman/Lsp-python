from pbr import Pbr

class Kubus:
    
    def hitung_keliling(self, pbr: Pbr)-> float:
        return (12*pbr.get_sisi())
    
    def hitung_luas(self, pbr: Pbr)-> float:
        return (6*pbr.get_sisi()*pbr.get_sisi())
    
    def hitung_volume(self, pbr: Pbr)-> float:
        return (pbr.get_sisi() * pbr.get_sisi() * pbr.get_sisi())