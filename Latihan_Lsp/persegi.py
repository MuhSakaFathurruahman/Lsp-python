from penghitung_bangun_datar import PenghitungBangunDatar

class Persegi:
    
    def hitung_keliling_persegi(self, penghitung_bangun_datar: PenghitungBangunDatar)-> float:
        return (4*penghitung_bangun_datar.get_sisi())
    
    def hitung_luas_persegi(self, penghitung_bangun_datar: PenghitungBangunDatar)-> float:
        return (penghitung_bangun_datar.get_sisi()*penghitung_bangun_datar.get_sisi())