# ESCUELA COLOMBIANA DE INGENIERÍA JULIO GARAVITO 
# Carrera / Semestre: Ingeniería de Sistemas / 4to Semestre
# Asignatura: Ciencias Naturales y Tecnología (CNYT) 
# Nombre: Jesús Alfonso Pinzón Vega
# Fecha: 08/17/2023

# Librería de Números Complejos

from math import *

def complex_sum(c1,c2):
    """Calcula y devuelve la suma de dos números complejos
    (tuple,tuple) -> tuple"""
    a3 = c1[0] + c2[0] 
    b3 = c1[1] + c2[1]
    return (a3,b3)


def complex_dif(c1,c2):
    """Calcula y devuelve la resta de dos números complejos
    (tuple,tuple) -> tuple"""
    a3 = c1[0] - c2[0] 
    b3 = c1[1] - c2[1]
    return (a3,b3) 


def complex_prod(c1,c2):
    """Calcula y devuelve el producto de dos números complejos
    (tuple,tuple) -> tuple"""
    a3 = c1[0]*c2[0] - c1[1]*c2[1]
    b3 = c1[0]*c2[1] + c2[0]*c1[1]
    return (a3,b3)   


def complex_div(c1,c2):
    """Calcula y devuelve el cociente de la división de dos números complejos
    (tuple,tuple) -> tuple"""
    a3 = (c1[0]*c2[0] + c1[1]*c2[1]) / (c2[0]**2 + c2[1]**2)
    b3 = (c2[0]*c1[1] - c1[0]*c2[1]) / (c2[0]**2 + c2[1]**2)
    return (a3,b3)

    
def complex_mod(c1):
    """Calcula y devuelve el módulo de un número complejo
    (tuple) -> tuple"""
    mod = sqrt(c1[0]**2 + c1[1]**2)
    return mod

    
def complex_conj(c1):
    """Calcula y devuelve el conjugado de un número complejo
    (tuple) -> tuple"""
    a2 = c1[0]
    b2 = -c1[1]
    return (a2,b2)  


def complex_fase(c1):
    """Calcula y devuelve la fase de un número complejo
    (tuple) -> int or float"""
    θ = atan(c1[1]/c1[0])
    return θ
    
    
def cart_to_polar(c1):
    """Convierte las coordenadas cartesianas a polares de un número complejo
    (tuple) -> tuple"""
    p = complex_mod(c1)
    θ = complex_fase(c1)
    a1 = p*cos(θ)
    b1 = p*sin(θ)
    return (a1,b1)