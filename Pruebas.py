# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 08/17/2023

# Pruebas de la Librería de Números Complejos

from Libreria_Numeros_Complejos import *
import unittest as ut

class Test_Complex_Operations(ut.TestCase):
    
    def test_complex_sum(self):
        """Prueba del cálculo de la suma de dos números complejos
        None -> OK or FAILED (failures=#)"""
        sum = complex_sum((1,2),(3,4))    
        self.assertAlmostEqual(sum[0],4)
        self.assertAlmostEqual(sum[1],6)
        sum = complex_sum((-0.5,7),(3.6,-2))
        self.assertAlmostEqual(sum[0],3.1)
        self.assertAlmostEqual(sum[1],5)
    
    
    def test_complex_dif(self):
        """Prueba del cálculo de la resta de dos números complejos
        None -> OK or FAILED (failures=#)"""
        dif = complex_dif((0,0),(7.7,-4))    
        self.assertAlmostEqual(dif[0],-7.7)
        self.assertAlmostEqual(dif[1],4)
        dif = complex_dif((-1.6,9),(7.1,-2.2))
        self.assertAlmostEqual(dif[0],-8.7)
        self.assertAlmostEqual(dif[1],11.2)


    def test_complex_prod(self):
        """Prueba del cálculo del producto de dos números complejos
        None -> OK or FAILED (failures=#)"""
        prod = complex_prod((3,-4.2),(5.6,-1))    
        self.assertAlmostEqual(prod[0],12.6)
        self.assertAlmostEqual(prod[1],-26.52)
        prod = complex_prod((-6,1),(7,-8))
        self.assertAlmostEqual(prod[0],-34)
        self.assertAlmostEqual(prod[1],55)


    def test_complex_div(self):
        """Prueba del cálculo del cociente de la división de dos números complejos
        None -> OK or FAILED (failures=#)"""
        div = complex_div((3,-4.2),(5.6,-1))    
        self.assertAlmostEqual(div[0],0.6489493201)
        self.assertAlmostEqual(div[1],-0.6341161928)
        div = complex_div((-6,1),(7,-8))
        self.assertAlmostEqual(div[0],-0.4424778761)
        self.assertAlmostEqual(div[1],-0.3628318584)

        
    def test_complex_mod(self):
        """Prueba del cálculo del módulo de un número complejo
        None -> OK or FAILED (failures=#)"""
        mod = complex_mod((1,2))    
        self.assertAlmostEqual(mod,2.236067977)
        mod = complex_mod((3.6,-2.5))
        self.assertAlmostEqual(mod,4.3829214)

        
    def test_complex_conj(self):
        """Prueba del cálculo del conjugado de un número complejo
        None -> OK or FAILED (failures=#)"""
        conj = complex_conj((3,-7))   
        self.assertAlmostEqual(conj[0],3)
        self.assertAlmostEqual(conj[1],7)
        conj = complex_conj((7.4,-2.6))
        self.assertAlmostEqual(conj[0],7.4)
        self.assertAlmostEqual(conj[1],2.6)


    def test_complex_fase(self):
        """Prueba del cálculo de la fase de un número complejo
        None -> OK or FAILED (failures=#)"""
        fase = complex_fase((3,-7)) 
        self.assertAlmostEqual(fase,-1.165904540)
        fase = complex_fase((7.4,-2.6))
        self.assertAlmostEqual(fase,-0.337878188)
        
        
    def test_cart_to_polar(self):
        """Prueba de la conversión de coordenadas cartesianas a polares de un número complejo
        None -> OK or FAILED (failures=#)"""
        ctp = cart_to_polar((-3,4)) 
        self.assertAlmostEqual(ctp[0],5)
        self.assertAlmostEqual(ctp[1],2.214297435)
        ctp = cart_to_polar((-5.5,-7))
        self.assertAlmostEqual(ctp[0],8.902246907)
        self.assertAlmostEqual(ctp[1],-2.23676556)
    
    
    def test_polar_to_cart(self):
        """Prueba de la conversión de coordenadas polares a cartesianas de un número complejo
        None -> OK or FAILED (failures=#)"""
        ptc = polar_to_cart((4,0.7854)) 
        self.assertAlmostEqual(ptc[0],2.828421930)
        self.assertAlmostEqual(ptc[1],2.828432319)
        ptc = polar_to_cart((9,5.2359))
        self.assertAlmostEqual(ptc[0],4.499315992)
        self.assertAlmostEqual(ptc[1],-7.794623505)


if __name__ == '__main__':
    ut.main()