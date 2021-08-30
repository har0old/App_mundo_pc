from Teclado import Teclado
from Monitor import Monitor
from Raton import Raton

class Computadora: 
    contador_computadores = 0

    def __init__(self, nombre, monitor, teclado, raton ) -> None:
        Computadora.contador_computadores += 1
        self._id_computador = Computadora.contador_computadores
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def monitor ( self):
        return self._monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor
    
    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado
    
    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self, raton):
        self._raton = raton 
    
    def __str__(self) -> str:
        return f'''
           {self._nombre}: {self._id_computador}
           Monitor: {self._monitor}
           Teclado: {self._teclado}
           Raton: {self._raton}

        '''
if __name__=='__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('BLUE', 'HP')
    monitor1 = Monitor('HP', '17"')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado('ASUS', 'USB')
    raton2 = Raton('BLUE', 'ASUS')
    monitor2 = Monitor('ASUS', '21"')
    computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)
    print(computadora2)
