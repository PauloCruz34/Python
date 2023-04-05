#exercício 1
from random import sample
vetor = sample(range(100), 10)
maior = menor = vetor[0]
for x in vetor[1:]:
  if x > maior: maior = x
  if x < menor: menor = x
print ('Vetor:', vetor)
print (f'Maior: {maior}')
print (f'Menor: {menor}')

#exercício 2

from random import sample
vetor = sample(range(100), 20)
pares = []
impares = []
for x in vetor:
    if x%2==0:
        pares.append(x)
    else:
        impares.append(x)
print('vetor',vetor)
print(f'Pares:{pares}')
print(f'Impares:{impares}')

#exercício 3
from random import randint
v1 = []
v2 = []
v3 = []

for x in range (10):
    x =  randint(1,100)
    v1.append(x)
    v3.append(x)
    x= randint(1,100)
    v2.append(x)
    v3.append(x)
print('v1',v1)
print('v2',v2)
print('v3',v3)

#exercício 4
texto = ('''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.''').lower()
import string
for c in string.punctuation:
    texto = texto.replace(c,'')
resp = []
for p in texto.split():
    if p[0] in "python" or p[-1] in "python":
        resp.append(p)
print(resp)

#exercício 5

texto = ('''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.''').lower()
import string
for p in string.punctuation:
    texto = texto.replace(c,'')
def txt (palavra):
    for letra in palavra:
       if letra in "python":
           return True
    return False

       
resp = [p for p in texto.split()
    if txt(p) and len(p)> 4]
print (resp)
print(len(resp))
