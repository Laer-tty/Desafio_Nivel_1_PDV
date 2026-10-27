idadeDoCliente = 0
valorDaCompra = 0
listaDeCompras = []
totalBruto = 0
totalFinal = 0

while True:
    idadeDoCliente = int(input("Digite a sua idade: "))

    if idadeDoCliente >= 0:
        break
    else:
        print("Idade inválida. Tente novamente.")

while True:
    
    while True:
        valorDaCompra = int(input("Digite o valor da compra: "))

        if valorDaCompra >= 0:
            break
        else:
            print("Valor da compra inválido. Tente novamente.")

    totalBruto = totalBruto + valorDaCompra
    if (valorDaCompra == 0):
        break

    if (idadeDoCliente >= 65):
        valorDaCompra = valorDaCompra * 0.8

    if (valorDaCompra > 100):
        valorDaCompra = valorDaCompra * 0.9

    totalFinal = totalFinal + valorDaCompra
    listaDeCompras.append(valorDaCompra)

print("--------------------------------------------------------")

for item in listaDeCompras:
    print(f"Valor da compra: R${item: .2f}")    

totalDesconto = totalBruto - totalFinal

print("--------------------------------------------------------")
print(f"Quantidade de compras realizadas: {len(listaDeCompras)}")
print(f"Total bruto: R$ {totalBruto: .2f}")
print(f"Total de desconto concedido: R$ {totalDesconto: .2f}")
print(f"Total final: R$ {totalFinal: .2f}")