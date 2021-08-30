from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora
from Orden import Orden

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('BLUE', 'HP')
monitor1 = Monitor('HP', '17"')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('ASUS', 'USB')
raton2 = Raton('BLUE', 'ASUS')
monitor2 = Monitor('ASUS', '21"')
computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)

teclado3 = Teclado('DELL', 'USB')
raton3 = Raton('BLUE', 'DELL')
monitor3 = Monitor('DELL', '21"')
computadora3 = Computadora('DELL', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadoras(computadora3)
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)