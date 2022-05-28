from pbr import Pbr
from kubus import Kubus

class View:
    
    def show_keliling(self, pbr: Pbr, kubus: Kubus):
        print (kubus.hitung_keliling(pbr))
        
    def show_luas(self, pbr: Pbr, kubus: Kubus):
        print (kubus.hitung_luas(pbr))
        
    def show_volume(self, pbr: Pbr, kubus: Kubus):
        print (kubus.hitung_volume(pbr))
        
# class ViewPersegi:
    
#     def show_keliling(self, penghitung_bangun_datar: PenghitungBangunDatar, persegi:Persegi):
#         print (persegi.hitung_keliling(penghitung_bangun_datar))
        
#     def show_luas(self, penghitung_bangun_datar: PenghitungBangunDatar, persegi:Persegi):
#         print (persegi.hitung_luas(penghitung_bangun_datar))