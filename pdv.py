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
        valorDaCompra = float(input("Digite o valor da compra: "))

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

while True:
    temCupom = int(input("Possui cupom? 0 - Não  1 - Sim\n"))

    if temCupom == 1 or temCupom == 0:
        break
    else:
        print("Valor inválido. Tente novamente.")

if temCupom:
    cupom = input("Digite seu cupom: ").strip().upper()
    if cupom == "FIDELIDADE10":
        totalFinal = totalFinal * 0.90
        print("--------------------------------------------------------")
        print(f"Cupom aplicado (10% de desconto).")
    else:
        print("--------------------------------------------------------")
        print("Cupom inválido.")

if len(listaDeCompras) > 3:
    print("--------------------------------------------------------")
    print("Desconto de 5% para compras maiores de 3 itens.")
    totalFinal = totalFinal * 0.95
totalDesconto = totalBruto - totalFinal

# print("--------------------------------------------------------")
# for item in listaDeCompras:
#     print(f"Valor da compra: R${item: .2f}")    
# print("--------------------------------------------------------")
# print(f"Quantidade de compras realizadas: {len(listaDeCompras)}")
# print(f"Total bruto: R$ {totalBruto: .2f}")
# print(f"Total de desconto concedido: R$ {totalDesconto: .2f}")
# print(f"Total final: R$ {totalFinal: .2f}")
# print("--------------------------------------------------------")

with open("resume.txt", "w") as arquivo:
    arquivo.write("--------------------------------------------------------\n")
    for item in listaDeCompras:
        arquivo.write(f"Valor da compra: R${item: .2f}\n") 

    arquivo.write("--------------------------------------------------------\n")
    arquivo.write(f"Quantidade de compras realizadas: {len(listaDeCompras)}\n")
    arquivo.write(f"Total bruto: R${totalBruto: .2f}\n")
    arquivo.write(f"Total de desconto concedido: R${totalDesconto: .2f}\n")
    arquivo.write(f"Total final: R${totalFinal: .2f}\n")
    arquivo.write("--------------------------------------------------------")
