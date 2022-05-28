from pbr import Pbr
from kubus import Kubus
from view import View


shape = Pbr(5)
hitung = Kubus()
show = View()

show.show_keliling(shape, hitung)
show.show_luas(shape, hitung)
show.show_volume(shape, hitung)