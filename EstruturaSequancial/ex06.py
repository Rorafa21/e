"""Faça um Programa que peça o raio de um círculo, calcule e mostre sua área."""
import math

b = True
while b:
    print("Calculando Área!")

    r = float(input("Insira o valor do Raio: "))
    a = r**2 * math.pi

    print(f"A área do círculo é igual á {a:.5}")