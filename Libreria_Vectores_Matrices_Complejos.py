# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 2023/09/06

# Librería de Operaciones con Vectores y Matrices Complejos

from math import *
from numpy import *

def cplx_vect_sum(v1,v2):
    """Calcula y devuelve la suma de dos vectores complejos
    (1D array, 1D array) -> 1D array"""
    try:
        v1,v2 = array(v1),array(v2)
        vr = v1 + v2
        return vr
    except:
        return "Los vectores NO son compatibles"


def cplx_vect_add_inver(v):
    """Calcula y devuelve el inverso aditivo de un vector complejo
    (1D array) -> 1D array"""
    v = array(v)
    vr = -1*v
    return vr


def cplx_vect_scal_mult(c,v):
    """Calcula y devuelve la multiplicación de un escalar por un vector complejo
    (int or float or complex, 1D array) -> 1D array"""
    v = array(v)
    vr = c*v
    return vr


def cplx_mtx_sum(m1,m2):
    """Calcula y devuelve la suma de matrices complejas
    (2D array, 2D array) -> 2D array"""
    try:
        m1,m2 = array(m1),array(m2)
        mr = m1 + m2
        return mr
    except:
        return "Las matrices NO son compatibles"


def cplx_mtx_add_inver(m):
    """Calcula y devuelve la inversa aditiva de una matriz compleja
    (2D array) -> 2D array"""
    m = array(m)
    mr = -1*m
    return mr


def cplx_mtx_scal_mult(c,m):
    """Calcula y devuelve la multiplicación de un escalar por una matriz compleja
    (int ot float or complex, 1D array) -> 1D array"""
    m = array(m)
    mr = c*m
    return mr


def cplx_vct_mtx_trans(vm):
    """Calcula y devuelve la transpuesta de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vmt = transpose(vm)
    return vmt


def cplx_vct_mtx_conj(vm):
    """Calcula y devuelve el conjugado de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vm = array(vm)
    vmc = conjugate(vm)
    return vmc


def cplx_vct_mtx_adj(vm):
    """Calcula y devuelve la adjunta (daga) de un vector o matriz complejos
    (1D array or 2D array) -> 1D array or 2D array"""
    vm = array(vm)
    vma = transpose(conjugate(vm))
    return vma


def cplx_mtx_prod(m1,m2):
    """Calcula y devuelve el producto de dos matrices complejas
    (2D array, 2D array) -> 2D array"""
    try: 
        m1,m2 = array(m1),array(m2)
        mr = dot(m1,m2)
        return mr
    except:
        return "Las matrices NO son compatibles"
        
        
def cplx_vct_mtx_act(m,v):
    """Calcula y devuelve la acción de una matriz compleja sobre un vector complejo
    (2D array, 1D array) -> 1D array"""
    try:
        m,v = array(m),array(v)
        vma = dot(m,v)
        return vma
    except:
        return "La matriz y el vector NO son compatibles"


def cplx_vct_mtx_inter_prod(vm1,vm2):
    """Calcula y devuelve el producto interno de dos vectores o matrices complejos
    (1D array, 1D array or 2D array, 2D array) -> 1D array or 2D array or int or float"""
    try:
        vm1,vm2 = array(vm1),array(vm2)
        d1 = vm1.ndim
        d2 = vm2.ndim
        if d1 == 1 == d2:
            vip = dot(cplx_vct_mtx_adj(vm1),vm2)
            return vip
        elif vm1.shape[0] == vm2.shape[0]:
            mip = trace(dot(cplx_vct_mtx_adj(vm1),vm2))
            return mip
        else:
            return "Los vectores o matrices NO son compatibles"
    except:
        return "Los vectores o matrices NO son compatibles"
        
        
def cplx_vct_mtx_norm(vm):
    """Calcula y devuelve la norma de un vector o matriz complejos
    (1D array or 2D array) -> int or float"""
    vm = array(vm)
    vmn = linalg.norm(vm)
    return(vmn)
    

def cplx_vct_mtx_dist(vm1,vm2):
    """Calcula y devuelve la distancia entre dos vectores o matrices complejos
    (1D array, 1D array or 2D array, 2D array) -> int or float"""
    vm1,vm2 = array(vm1),array(vm2)
    dist = linalg.norm(vm1-vm2)
    return dist

 
def cplx_mtx_val_vect(m):
    """Calcula y devuelve los valores y vectores propios de una matriz compleja
    (2D array) -> 1D array, 2D array"""
    m = array(m)
    val,vect = linalg.eig(m)
    return val,vect


def cplx_unt_mtx(m):
    """Indica si una matriz compleja es unitaria
    (2D array) -> True or False"""
    m = array(m)
    a,b = m.shape
    if a == b:
        unit = [list(x) for x in dot(m,cplx_vct_mtx_adj(m))]
        ident = [list(x) for x in identity(a)]
        if  unit == ident :
            return True
        else:
            return False
    else:
        return "La matriz No es cuadrada"


def cplx_herm_mtx(m):
    """Indica si una matriz compleja es hermitiana
    (2D array) -> True or False"""
    m = array(m)
    a,b = m.shape
    if a == b:
        hm = [list(x) for x in m]
        hmt = [list(x) for x in cplx_vct_mtx_adj(m)]
        if  hm == hmt:
            return True
        else:
            return False
    else:
        return "La matriz No es cuadrada"
    

def cplx_vct_mtx_tens_prod(vm1,vm2):
    """Calcula y devuelve el producto tensorial entre dos vectores y/o matrices complejos
    (1D array or 2D array, 1D array or 2D array) -> 1D array or 2D array"""
    vm1,vm2 = array(vm1),array(vm2)
    d1,d2 = vm1.ndim,vm2.ndim
    
    if d1 == 1 and d2 == 1:
        a,b = vm1.shape[0],1
        c,d = vm2.shape[0],1
    elif d1 == 1 and d2 == 2:
        a,b = vm1.shape[0],1
        c,d = vm2.shape
    elif d1 == 2 and d2 == 1:
        a,b = vm1.shape
        c,d = vm2.shape[0],1
    else:
        a,b = vm1.shape
        c,d = vm2.shape
    
    m,n = a*c,b*d
    vmtp = full((m,n),0+0j)
    
    if d1 == 1 and d2 == 1:
        for j in range(m):
            for k in range(n):
                vmtp[j,k] = vm1[j//c]*vm2[j%c]
    elif d1 == 1 and d2 == 2:
        for j in range(m):
            for k in range(n):
                vmtp[j,k] = vm1[j//c]*vm2[j%c,k%d]
    elif d1 == 2 and d2 == 1:
        for j in range(m):
            for k in range(n):
                vmtp[j,k] = vm1[j//c,k//d]*vm2[j%c]
    else:
        for j in range(m):
            for k in range(n):
                vmtp[j,k] = vm1[j//c,k//d]*vm2[j%c,k%d]
    
    return vmtp