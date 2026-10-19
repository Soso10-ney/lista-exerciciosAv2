# Questão 1: Divisão com tratamento de erros 
 try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)

except ValueError:
    print("Entrada inválida! Digite apenas números.")

except ZeroDivisionError:
    print("Não é possível dividir por zero!") 
    
# Questão 2: Média de notas

def calcular_media(notas):
    return sum(notas) / len(notas)

notas_lista = []
quantidade = int(input("Quantas notas você deseja digitar? "))

for i in range(quantidade):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas_lista.append(nota)

if len(notas_lista) > 0:
    media = calcular_media(notas_lista)
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")

# Questão 3: Verificar carga horária
def verificar_carga_horaria(horas):
    if horas >= 40:
        return "Carga completa"
    else:
        return "Carga incompleta"

horas_trabalhadas = float(input("Digite o número de horas trabalhadas na semana: "))
resultado = verificar_carga_horaria(horas_trabalhadas)
print("Situação do funcionário:", resultado)

# Questão 4: Saldo bancário
def calcular_saldo(saldo_atual, valor, operacao):
    if operacao == "deposito":
        return saldo_atual + valor
    elif operacao == "saque":
        return saldo_atual - valor
    else:
        return saldo_atual

saldo_atual = float(input("Digite o saldo atual da conta: "))
valor = float(input("Digite o valor da operação: "))
operacao = input("Digite o tipo da operação ('deposito' ou 'saque'): ").lower().strip()

novo_saldo = calcular_saldo(saldo_atual, valor, operacao)
print(f"O novo saldo é: R$ {novo_saldo:.2f}")

# Questão 5: Filtrar alunos aprovados
def filtrar_aprovados(notas):
    aprovados = []
    for nota in notas:
        if nota >= 7:
            aprovados.append(nota)
    return aprovados

# Parte interativa para executar
lista_notas = []
print("- Digitação de Notas (Digite -1 para encerrar) -")

while True:
    nota = float(input("Digite uma nota: "))
    if nota == -1:
        break
    lista_notas.append(nota)

aprovados = filtrar_aprovados(lista_notas)
print("Notas dos alunos aprovados:", aprovados)