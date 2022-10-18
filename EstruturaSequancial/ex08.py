"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês."""

b = True

while b:
    print("Horas trabalhadas")

    valorHora = float(input("Quanto você recebe por hora?: "))
    horaTrabalhada = float(input("Quantas horas?: "))

    salario = valorHora * horaTrabalhada
    salarioMes = salario * 21
    print(f"Se você trabalhar por {horaTrabalhada} horas receberá R${salarioMes:.6}")

