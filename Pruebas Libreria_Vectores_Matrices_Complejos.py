# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/06

# Pruebas de la Librería de Operaciones con Vectores y Números Complejos

from Libreria_Vectores_Matrices_Complejos import *
import unittest as ut

class Test_Libreria_Nombre(ut.TestCase):
    
    def test_cplx_vect_sum(self):
        """Prueba del cálculo de la suma de dos vectores complejos
        None -> OK or FAILED (failures=#)"""
        vr = list(cplx_vect_sum([1+2j, 5-2j], [4+4j, -1+7j]))
        self.assertEqual(vr, [5+6j, 4+5j])
        vr = list(cplx_vect_sum([1.5j, 3, -1-1.2j], [7, 4.7+9.2j, 3j]))
        self.assertEqual(vr, [7+1.5j, 7.7+9.2j, -1+1.8j])
    

    def test_cplx_vect_add_inver(self):
        """Prueba del cálculo del inverso aditivo de un vector complejo
        None -> OK or FAILED (failures=#)"""
        vr = list(cplx_vect_add_inver([2-5.7j, 7+4j]))
        self.assertEqual(vr, [-2+5.7j, -7-4j])
        vr = list(cplx_vect_add_inver([-1-5j, 1j, -1j]))
        self.assertEqual(vr, [1+5j, -1j, +1j])
        
        
    def test_cplx_vect_scal_mult(self):
        """Prueba del cálculo de la suma de dos vectores complejos
        None -> OK or FAILED (failures=#)"""
        vr = list(cplx_vect_scal_mult(9, [1+2j, 5-2j]))
        self.assertEqual(vr, [9+18j, 45-18j])
        vr = list(cplx_vect_scal_mult(2-3j, [7, 4+9j, 2.5-3j]))
        self.assertEqual(vr, [14-21j, 35+6j, -4-13.5j])
    
      
    def test_cplx_mtx_sum(self):
        """Prueba del cálculo de la suma de dos matrices complejas
        None -> OK or FAILED (failures=#)"""
        mr = [list(x) for x in cplx_mtx_sum([[1+3j, -5-7j], [4-1j, 8+4j]], [[1+1j, 2-6j], [9+9j, -10+20j]])]
        self.assertEqual(mr, [[2+4j, -3-13j], [13+8j, -2+24j]])
        mr = [list(x) for x in cplx_mtx_sum([[-33+2j, 6-74j], [14-8j, 18-4j]], [[-4+1j, 11-1j], [21+7j, -1+2j]])]
        self.assertEqual(mr, [[-37+3j, 17-75j], [35-1j, 17-2j]])
        
    
    def test_cplx_mtx_add_inver(self):
        """Prueba del cálculo de la inversa aditiva de una matriz compleja
        None -> OK or FAILED (failures=#)"""
        mr = [list(x) for x in cplx_mtx_add_inver([[1+3j, -5-7j], [4-1j, 8+4j]])]
        self.assertEqual(mr, [[-1-3j, 5+7j], [-4+1j, -8-4j]])
        mr = [list(x) for x in cplx_mtx_add_inver([[-4+1j, 11-1j], [21+7j, -1+2j]])]
        self.assertEqual(mr, [[4-1j, -11+1j], [-21-7j, 1-2j]])
        
    
    def test_cplx_mtx_scal_mult(self):
        """Prueba del cálculo de la multiplicación de un escalar por una matriz compleja
        None -> OK or FAILED (failures=#)"""
        vmt = [list(x) for x in cplx_mtx_scal_mult(2+3j,[[1+3j, -5-7j], [4-1j, 8+4j]])]
        self.assertEqual(vmt, [[-7+9j, 11-29j], [11+10j, 4+32j]])
        vmt = [list(x) for x in cplx_mtx_scal_mult(5,[[-4+1j, 11-1j], [21+7j, -1+2j]])]
        self.assertEqual(vmt, [[-20+5j, 55-5j], [105+35j, -5+10j]])
     
        
    def test_cplx_vct_mtx_trans(self):
        """Prueba del cálculo de la transpuesta de un vector o matriz complejos
        None -> OK or FAILED (failures=#)"""
        mr = list(cplx_vct_mtx_trans([1+3j, -5-7j, 4-1j, 8+4j]))
        self.assertEqual(mr, [1+3j, -5-7j, 4-1j, 8+4j])
        mr = [list(x) for x in cplx_vct_mtx_trans([[-4.6+3j, 1.1-1j, 2j], [21+7j, 4, -1+2j], [-15.2+9j, -1-4.4j, -100+2.2j]])]
        self.assertEqual(mr, [[-4.6+3j, 21+7j, -15.2+9j], [1.1-1j, 4+0j, -1-4.4j], [2j, -1+2j, -100+2.2j]])
    
    
    def test_cplx_vct_mtx_conj(self):
        """Prueba del cálculo del conjugado de un vector o matriz complejos
        None -> OK or FAILED (failures=#)"""
        vmc = list(cplx_vct_mtx_conj([1+3j, -5-7j, 4-1j, 8+4j]))
        self.assertEqual(vmc, [1-3j, -5+7j, 4+1j, 8-4j])
        vmc = [list(x) for x in cplx_vct_mtx_conj([[-4.6+3j, 1.1-1j, 2j], [21+7j, 4, -1+2j], [-15.2+9j, -1-4.4j, -100+2.2j]])]
        self.assertEqual(vmc, [[-4.6-3j, 1.1+1j, -2j], [21-7j, 4, -1-2j], [-15.2-9j, -1+4.4j, -100-2.2j]])


    def test_cplx_vct_mtx_adj(self):
        """Prueba del cálculo de la adjunta (daga) de un vector o matriz complejos
        None -> OK or FAILED (failures=#)"""
        vma = list(cplx_vct_mtx_adj([1+3j, -5-7j, 4-1j, 8+4j]))
        self.assertEqual(vma, [1-3j, -5+7j, 4+1j, 8-4j])
        vma = [list(x) for x in cplx_vct_mtx_adj([[-4.6+3j, 1.1-1j], [21+7j,-1+2j]])]
        self.assertEqual(vma, [[-4.6-3j, 21-7j], [1.1+1j, -1-2j]])
    
    
    def test_cplx_mtx_prod(self):
        """Prueba del cálculo del producto de dos matrices complejas
        None -> OK or FAILED (failures=#)"""
        mr = [list(x) for x in cplx_mtx_prod([[1+3j, -5+1j], [4-1j, 8+4j]], [[1-1j, 2-6j], [3+9j, -4+2j]])]
        self.assertEqual(mr, [[-20-40j, 38-14j], [-9+79j, -38-26j]])
        mr = [list(x) for x in cplx_mtx_prod([[-1+2j, 6-7j], [1-8j, 5]], [[1j, 1-1j], [1+7j, 0]])]
        self.assertEqual(mr, [[53+34j, 1+3j], [13+36j, -7-9j]])
        
    
    def test_cplx_vct_mtx_act(self):
        """Prueba del cálculo de la acción de una matriz compleja sobre un vector complejo
        None -> OK or FAILED (failures=#)"""
        vma = list(cplx_vct_mtx_act([1+3j, -5+1j], [[1-1j, 2-6j], [3+9j, -4+2j]]))
        self.assertEqual(vma, [-20-40j, 38-14j])
        vma = list(cplx_vct_mtx_act([-2, 1j], [[1j, 1-1j], [1+7j, 0]]))
        self.assertEqual(vma, [-7-1j, -2+2j])
        
    
    def test_cplx_vct_mtx_inter_prod(self):
        """Prueba del cálculo del producto interno de dos vectores o matrices complejos
        None -> OK or FAILED (failures=#)"""
        vip = cplx_vct_mtx_inter_prod([1+3j, -5+1j], [1-1j, 2-6j])
        self.assertEqual(vip, -18+24j)
        mip = cplx_vct_mtx_inter_prod([[-1+2j, 1], [1-3j, 5]], [[1j, 1-1j], [1+7j, 0]])
        self.assertEqual(mip, -17+8j)
        
    
    def test_cplx_vct_mtx_norm(self):
        """Prueba del cálculo de la norma de un vector o matriz complejos
        None -> OK or FAILED (failures=#)"""
        vmn = cplx_vct_mtx_norm([1+7j, 4-1j, 2-6j])
        self.assertAlmostEqual(vmn, 10.34408043)
        vmn = cplx_vct_mtx_norm([[-1+2j, -3j], [1-3j, 5]])
        self.assertAlmostEqual(vmn, 7)
        
    
    def test_cplx_vct_mtx_dist(self):
        """Prueba del cálculo de la distancia entre dos vectores o matrices complejos
        None -> OK or FAILED (failures=#)"""
        dist = cplx_vct_mtx_dist([-1+2j, 6-7j, 1-8j], [4+1j, -12, 1-1j])
        self.assertAlmostEqual(dist, 21.166010488)
        dist = cplx_vct_mtx_dist([[-1+2j, 1], [1-3j, 0]], [[1j, 1-1j], [1+7j, 0]])
        self.assertAlmostEqual(dist, 10.148891565)
    
    
    def test_cplx_mtx_val_vect(self):
        """Prueba del cálculo de los valores y vectores propios de una matriz compleja
        None -> OK or FAILED (failures=#)"""
        val,vect = cplx_mtx_val_vect([[-1j, 1], [0, 1j]])
        val,vect = list(val), [list(x) for x in vect]
        self.assertEqual(val, [-1j, 1j])
        self.assertAlmostEqual(vect[0][0], 1)
        self.assertAlmostEqual(vect[0][1], -0.447213595j)
        self.assertAlmostEqual(vect[1][0], 0)
        self.assertAlmostEqual(vect[1][1], 0.894427190)
        
        val,vect = cplx_mtx_val_vect([[2-3j, 0], [3, -5+2j]])
        val,vect = list(val), [list(x) for x in vect]
        self.assertEqual(val, [-5+2j, 2-3j])
        self.assertAlmostEqual(vect[0][0], 0)
        self.assertAlmostEqual(vect[0][1], 0.94422787)
        self.assertAlmostEqual(vect[1][0], 1)
        self.assertAlmostEqual(vect[1][1], 0.26795656+0.19139754j)
        
    
    def test_cplx_unt_mtx(self):
        """Prueba de la validación de una matriz compleja unitaria
        None -> OK or FAILED (failures=#)"""
        ans = cplx_unt_mtx([[1j, 0, 0], [0, 1j, 0], [0, 0, 1j]])
        self.assertEqual(ans, True)
        ans = cplx_unt_mtx([[-1+2j, 1], [1-3j, 0]])
        self.assertEqual(ans, False)
    
    
    def test_cplx_herm_mtx(self):
        """Prueba de la validación de una matriz compleja hermitiana
        None -> OK or FAILED (failures=#)"""
        ans = cplx_herm_mtx([[3, 3-8j, -1-1j], [3+8j, 1, -5-6j], [-1+1j, -5+6j, -2]])
        self.assertEqual(ans, True)
        ans = cplx_herm_mtx([[-1+2j, 1], [1-3j, 0]])
        self.assertEqual(ans, False)
        
        
    def test_cplx_vct_mtx_tens_prod(self):
        """Prueba del calculo del producto tensorial entre dos vectores y/o matrices complejos
        None -> OK or FAILED (failures=#)"""
        vmtp = [list(x) for x in cplx_vct_mtx_tens_prod([4+2j, -3j], [-1+2j, 1-3j, 5j])]
        self.assertEqual(vmtp, [[-8+6j], [10-10j], [-10+20j], [6+3j], [-9-3j], [15]])
        vmtp = [list(x) for x in cplx_vct_mtx_tens_prod([1+7j, 2-6j], [[-1+2j, 1], [1-3j, 0], [-1j, 7]])]
        self.assertEqual(vmtp, [[-15-5j, 1+7j], [22+4j, 0], [7-1j, 7+49j], [10+10j, 2-6j], [-16-12j, 0], [-6-2j, 14-42j]])
        vmtp = [list(x) for x in cplx_vct_mtx_tens_prod([[2j, 1+6j], [1j, 0]], [[-5j, 3+4j], [2, -1j]])]
        self.assertEqual(vmtp, [[10, -8+6j, 30-5j, -21+22j], [4j, 2, 2+12j, 6-1j], [5, -4+3j, 0, 0], [2j, 1, 0, 0]])

    
if __name__ == '__main__':
    ut.main()