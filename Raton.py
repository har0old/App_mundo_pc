from dispositivo_entrada import DispositivoEntrada
class Raton(DispositivoEntrada): 
    contador_ratones = 0
    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(tipo_entrada, marca)
        
    
    def __str__(self) -> str:
        return f' Id: {self._id_raton}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'
    

if __name__=='__main__':
    raton1 = Raton('USB', 'HP')
    print(raton1)

    raton2 = Raton('blue', 'ACER')
    print(raton2)
   