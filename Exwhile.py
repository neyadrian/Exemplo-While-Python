#Variable Declaration
x: int
sum: int

#Data Input
x = int(input('Digite um número: '))
sum = 0

#Data Processing
while x != 0:
    sum = sum + x
    x = int(input('Digite um número: '))

#Data Output
print(f'Soma vale: {sum} ')    