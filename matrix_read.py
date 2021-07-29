'''
doc = "export_juni.csv"
file_cvs = open(doc)

lines = [line for line in open(doc)]

print(lines[0].strip().split('"'))'''

import csv
from datetime import datetime

path = "prueba.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)  #en este punto podemos searar por lineas los distintos datos, aún asi, los datos siguen siendo Strings
data = []
for row in reader:
#¿que datos tenemos?
#row = [  date,    payee, account number, transaction type, reference, category, amount, amount, currency,exchange rate]
#row = [datetime, String,     int       ,      String     , String   ,    String, float,  float,   String,    int]
    date = datetime.strptime(row[0], '%Y-%m-%d').date()
    payee = str(row[1])
    account_number = str(row[2])
    transac_type = str(row[3])
    reference = str(row[4])
    category = str(row[5])
    amount_eur = float(row[6])
    amount = float(row[7])
    currency = str(row[8])
    rate = float(row[9])

    data.append([date, payee, account_number, transac_type, reference, category, amount_eur, amount, currency, rate])

print(data[0])

def estadistica (lista, elementos, movimientos):
    for i in range(elementos):
        suma = 0
        for j in range(movimientos):
            suma = suma+ lista[i][j]
        print("movimientos", j+1, "es",suma)

def mostrar_matriz(data):
    for columnas in  data:
        print(columnas)

filas = len(data)
columnas = len(data[0])

print(filas, columnas)


print()
mostrar_matriz(data)



#print(f'''Durante el mes de {date.strftime("%B")} se hicieron {filas} movimientos''')









