nome = str(input())
salFixo = float(input())
totalVendas = float(input())
salTotal = salFixo + (totalVendas * 0.15)
print("TOTAL = R$ {:.2f}".format(salTotal))