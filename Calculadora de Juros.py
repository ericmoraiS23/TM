# Valores do investimento e juros de rendimento
Valor_inicial = float(input("Qual o valor inicial ?: "))
Aporte_mes = float(input("Quantos R$ mensais será o aporte ?: "))
Juros_ano = float(input("Qual o juros Anual ?: "))
Meses_investindo = int(input("quantos meses de investimento ?: "))
Juros_Mes = float((Juros_ano)/12)/100
##

mes = 1
ano = Valor_inicial*Juros_Mes+Valor_inicial

while mes < Meses_investindo:
    ano= ano*Juros_Mes+ano+Aporte_mes
    mes += 1

ValorInvestido = Meses_investindo*Aporte_mes+Valor_inicial
Juros_total = ano-ValorInvestido
    
    
print ("Em",Meses_investindo,"mes(es) de investimento voce terá",ano,"R$")  
print ("o valor investido em 24 meses é de",ValorInvestido,"e o juros é de",Juros_total)


