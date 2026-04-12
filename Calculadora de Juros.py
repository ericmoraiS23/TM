#variáveis
aporte_inicial = float(input("informe o valor do depósito: "))
aporte_mensal = float(input("informe o valor do aporte mensal: "))
taxa = float(input("informe a taxa de juros mensal: "))
tempo = int(input("informe o tempo em meses da aplicação: "))
taxa = taxa / 100
x = 0

#calculo dos juros compostos + aporte mensal
print("o aporte inicial foi",aporte_inicial)
while x < tempo:
    aporte_inicial = aporte_inicial + aporte_mensal
    total = aporte_inicial + aporte_inicial * taxa * (x + 1)
    print("Mês", x + 1, ": R$", total)
    x = x + 1
juros = total - aporte_inicial



print("aporte inicial",aporte_inicial)
print (juros)


print("Os juros acumulados em", tempo,"meses serão de R$",juros)
print("O valor total da aplicação será de R$", total)
