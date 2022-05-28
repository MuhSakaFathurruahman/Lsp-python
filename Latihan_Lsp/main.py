from pbr import Pbr
from penghitung_bangun_datar import PenghitungBangunDatar
from kubus import Kubus
from persegi import Persegi
from view import View
from view_persegi import ViewPersegi 

print("Kubus")
shape = Pbr(5)
hitung = Kubus()
show = View()

show.show_keliling(shape, hitung)
show.show_luas(shape, hitung)
show.show_volume(shape, hitung)

print("\nPersegi")
shape = PenghitungBangunDatar(2)
hitung = Persegi()
show = ViewPersegi()

show.show_keliling_persegi(shape, hitung)
show.show_luas_persegi(shape, hitung)