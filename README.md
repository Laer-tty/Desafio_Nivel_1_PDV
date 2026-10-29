# Desafio_Nivel_1_PDV
Primeiro Desafio do Programa Trilhas Inova 3 - Trilha Backend.

# O que faz?
O código recebe a idade e o valor da compra e valida se não são negativos.
- Se for negativo, é pedido novamente a idade ou o valor da compra.
- Se for positivo ou 0 continua normalmente.

Se a sua idade for maior ou igual a 65 é recebido um desconto de 20% da compra. Se o valor descontado for maior que R$ 100 é recebido um desconto de 10%.

O programa para quando o usuário digita 0 no valor da compra. Após parar as compras, é perguntado ao usuário se ele tem algum cupom e então é feita a validação desse cupom. Se o cupom for FIDELIDADE10, é aplicado um desconto de 10% ao total final.

Outro desconto ocorre se o total de produtos comprados for maior que 3, assim sendo aplicado um desconto de 5%.

Ao terminar o programa, é salvo suas compras e o resumo de suas compras em uma arquivo .txt chamado resume que contém:
- O preço de cada compra individual (apenas aplicando os descontos de idade e maior que R$ 100);
- Quantidade de compras realizadas;
- Total bruto;
- Total de desconto concedido;
- Total final;
