'''
Módulo que me permite hacer las operaciones basicas para despues utilizarlas en el archivo principal
'''

def suma(n1,n2,n3 = 0):
  return n1+n2+n3
def restar(n1,n2):
  return n1 - n2
def multiplicar(n1,n2):
  return n1 * n2

def dividir (n1,n2):
  if n2 == 0:
    return None
  return n1/n2
