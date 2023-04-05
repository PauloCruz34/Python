#exercício 1
nota=  float(input('Nota: '))
n = 0
while nota <0 or nota > 10:
    print("Notas entre 0 e 10: ")
    nota = float(input("Nota: "))
#exercício 2

nome = str(input("digite o nome de usário: "))
senha = str(input("digite a senha: "))
while nome == senha:
    print("digite uma senha válida!")
    senha = str(input("digite a senha: "))

#exercício 3
p1 = 80000
p2 = 200000
anos = 0
while p1 <= p2:
   p1= p1 +p1 * 0.03
   p2 = p2 + p2 * 0.015
   anos = anos+1
print(anos)

#exercício 4
n = int(input('Digite o valor de n: '))
a,b = 1,1
k = 1
while k <= n-2:
    a,b = b,a+b
    k=k+1
print(b)

#exercício 5
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
while n1 % n2 !=0: # enquanto resto da divisão for diferente de 0 vai pegar o b avançar pra frente e o resto vai pro lugar do b
   n1,n2 = n2,n1%n2
print(f'mdc = {n2}')
   

   


