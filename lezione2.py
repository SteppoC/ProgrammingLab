#esercizio della somma lista fatto da sarusso
def sum_list(the_list):
    totale=0
    for item in the_list:
        totale += item
    return totale
#print(sum_list([1,2,3]))
mia_stringa='ciao, come va?'
lista_elementi=print(mia_stringa.split(', '))
print('-----')

print('--ESERCIZIO SHAMPOO--')
#carico il file
my_file=open('shampoo_sales.csv','r')
#leggo linea per linea e considero nel ciclo ogni volta la sola linea in considerazione
for linea in my_file:
    #divido ogni linea in base alla virgola
    elementiLinea=linea.split(' ')
    #elimino l'intestazione
    if elementiLinea[0]!='Date':
    #definisco gli elementi che fan parte della linea in data e quantità
        data = elementiLinea[0]
        quantita = elementiLinea[1]
        #aggiungo alla lista dei valori
        valori.append(quantita)
#sommo le quantità
    somma += sum(quantita)
    print(somma)
    