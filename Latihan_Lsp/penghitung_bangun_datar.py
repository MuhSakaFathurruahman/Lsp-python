from abc import ABC, abstractmethod

class PenghitungBangunDatar():
    
    def __init__(self, sisi: float,):
        self.__sisi = sisi

    def set_sisi(self, sisi:float) -> None:
        self.__sisi = sisi
        
    def get_sisi(self) -> float :
        return self.__sisi
    
    @abstractmethod
    def hitung_keliling_persegi():
        pass
    
    @abstractmethod
    def hitung_luas_persegi():
        pass
    