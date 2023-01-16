lista=[1,4,67,59]

print('--- MODO 1 ---')
a=sum(lista)
print('La somma della lista è: {}' .format(a))

print('--- MODO 2 ---')
def somma(list):
    Sum=0;
    for i in range(len(list)):
        Sum=list[i]+Sum
    return Sum
risult=somma(lista)
print('La somma della lista è: {}' .format(risult))

print('--- MODO 3 ---')
def somma(list):
    Sum=0;
    for element in list:
        Sum+=element  #Sum=Sum+element
    return Sum
risult=somma(lista)
print('La somma della lista è: {}' .format(risult))

print('------')

print()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)