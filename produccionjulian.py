#Importamos módulo calculadora

import calculadora

print(f"suma es : {calculadora.suma(5,3,10)}")

from calculadora import restar

print(f" La resta es : {restar(2,10)}")

from calculadora import suma,restar

print(f" La suma de 12 y 12 es : {suma(12,12)} y la resta es : {restar(12,12)}")

from calculadora import *

print(f" La suma de 12 y 12 es : {multiplicar(12,12)} y la resta es : {dividir(12,12)}")

from calculadora import dividir as jaja

print(f" La suma de 12 y 12 es : {multiplicar(12,12)} y la resta es : {jaja(12,12)}")

