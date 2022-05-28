from penghitung_bangun_datar import PenghitungBangunDatar
from persegi import Persegi

class ViewPersegi:
    
    def show_keliling_persegi(self, penghitung_bangun_datar: PenghitungBangunDatar, persegi:Persegi):
        print (persegi.hitung_keliling_persegi(penghitung_bangun_datar))
        
    def show_luas_persegi(self, penghitung_bangun_datar: PenghitungBangunDatar, persegi:Persegi):
        print (persegi.hitung_luas_persegi(penghitung_bangun_datar))