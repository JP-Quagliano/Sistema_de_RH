# Função para calcular o valor ganho com horas extras
def calcular_horas_extras(salario_base, horas):
    valor_horas_extras = salario_base * 0.015 * horas

    return valor_horas_extras

# Função para calcular o desconto das faltas
def calcular_descontos_faltas(salario_base, faltas):
    valor_desconto = salario_base * 0.02 * faltas

    return valor_desconto

# Função para calcular o bônus
def calcular_bonus(cargo, recebeu_bonus):
    bonus = 0

    if recebeu_bonus == "s":
        if cargo == 1:
            bonus = 1000
        elif cargo == 2:
            bonus = 500
        elif cargo == 3:
            bonus = 300
        else:
            bonus = 100

    return bonus

# Função pra mostrar o nome do car
def mostrar_nome_cargo(cargo):
    if cargo == 1:
        return "Gerente"
    elif cargo == 2:
        return "Analista"
    elif cargo == 3:
        return "Assistente"
    else:
        return "Estagiário"

# Início do programa
print("=" * 40) 
print("SISTEMA DE RH - CÁLCULO DO SALÁRIO FINAL")
print("=" * 40)

# Entrada do nome
nome_funcionario = input("Insira o nome do funcionário: ").strip()

while nome_funcionario == "":
    print("Por favor insira um nome válido, o espaco nao pode ficar vazio!")
    nome_funcionario = input("Digite o nome do funcionário: ").strip()

# Mostra os cargos
print("\nEscolha o cargo do funcionário:")
print("1 - Gerente")
print("2 - Analista")
print("3 - Assistente")
print("4 - Estagiário")

# Entrada do cargo
cargo = int(input("Insira o número do cargo: "))

while cargo < 1 or cargo > 4:
    print("Cargo inválido. Insira um número de 1 a 4.")
    cargo = int(input("Insira o número do cargo: "))

# Entrada do salário base
salario_base = float(input("Insira o salário base: R$ "))

while salario_base < 0:
    print("O salário base não pode ser negativo.")
    salario_base = float(input("Insira o salário base: R$ "))

# Entrada das horas extras
horas_extras = float(input("Insira a quantidade de horas extras: "))

while horas_extras < 0:
    print("A quantidade de horas extras não pode ser negativa.")
    horas_extras = float(input("Insira a quantidade de horas extras: "))

# Entrada das faltas
faltas = int(input("Insira a quantidade de faltas no mês: "))

while faltas < 0:
    print("A quantidade de faltas não pode ser negativa.")
    faltas = int(input("Insira a quantidade de faltas no mês: "))

# Entrada do bônus
recebeu_bonus = input("Recebeu bônus por desempenho? (s/n): ").lower().strip()

while recebeu_bonus != "s" and recebeu_bonus != "n":
    print("Resposta inválida. Insira apenas s ou n.")
    recebeu_bonus = input("Recebeu bônus por desempenho? (s/n): ").lower().strip()

# Cálculos
valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_faltas = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

total_acrescimos = valor_horas_extras + valor_bonus
salario_bruto = salario_base + total_acrescimos
salario_final = salario_bruto - valor_faltas

# Saída final
print("\n" + "=" * 40)
print("RESUMO DO FUNCIONÁRIO")
print("=" * 40)
print("Nome:", nome_funcionario)
print("Cargo:", mostrar_nome_cargo(cargo))
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Total de acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de descontos: R$ {valor_faltas:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")
print("=" * 40)