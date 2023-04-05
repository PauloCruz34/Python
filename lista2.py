# execicio 1
x=int(input("Digite um Número inteiro: "))
y=int(input("Digite Outro Número Inteiro: "))
print(x+y)

# exercício 2
metro = float(input("digite a medida em metros: "))
print(f"a medida é :{metro * 1000} milimetros")

# exercício 3
dias = int(input("Dias: "))
horas = int(input("horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total = dias * 24*60*60 + horas*60*60 + minutos*60 + segundos
print(f"{total} segundos")

# exercício 4
salario = float(input("Valor do Salário Atual: "))
aumento = float(input("Aumento: "))
total_aumento = salario * aumento/100
total =  total_aumento + salario
print(f"O aumento foi de R${total_aumento} e o novo salário é de R${total}.")

# exercício 5
pm = float(input("Preço da mercadoria: "))
dc = float(input("Percentual de desconto: "))
vdc = pm * dc/100
vtm = pm - vdc
print(f"O desconto foi de R${vdc} e o valor a pagar é R${vtm}.")

# exercício 6
d = float(input("Digite a distância a ser percorrida: "))
vm = float(input("Digite a velocidade média: "))
tempo = (d / vm)
print(f"O tempo de viagem do carro com uma velocidade média de {vm} para uma distancia de {d} e de {tempo} horas.")

# exercício 7
temperatura_c = float(input("digite a temperatura a ser convertida:"))
temperatura_f = 9* temperatura_c/5+32
print(f'{temperatura_f}fahrenheit')

# exercício 8
temperatura_f = float(input("digite a temperatura a ser convertida:"))
temperatura_c = (temperatura_f - 32)*5/9
print(f'{temperatura_c}celcius')

# exercício 9
km = float(input('quantidade de kms percorridos: '))
dias = int(input("quantidade de dias de locação:"))
preco = (km*0.15)+(dias*60)
print(f" O valor a pagar é de R${preco}.")

# exercício 10
qtd =int(input("quantidade de cigarros fumados por dia? "))
tempo = int(input("tempo de fumente?"))
qtd_total= (tempo*365)*qtd
tempo_perdido= (qtd_total*10/60)/24
print(f'o tempo perdido é de {tempo_perdido} dias.')

# exercício 11
print (len(str(2**1000000)))


           
                 

