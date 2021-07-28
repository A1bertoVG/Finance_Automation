import csv

path = 'nummer_matriz.csv'
file = open(path, newline='')
reader = csv.reader(file)

def mostrar(data,cant_prod,venta_sem):
    for i in range(cant_prod):
        suma = 0

        for j in range(venta_sem):
            suma = suma + data[i][j]
        print(f'La cantidad de producto {j+1} es {suma}')

    for i in  range(venta_sem):
        suma = 0

        for j in range(cant_prod):
            suma=suma+data[j][i]
        print(f'La venta en semestre {i+1} es {suma}')




def main():

    header = next(reader)
    data = []

    for row in reader:
        data1 = int(row[0])
        data2 = int(row[1])
        data3 = int(row[2])
        data4 = int(row[3])

        data.append([data1,data2, data3, data4])
        mostrar(data,len(data),len(data[0]))



    print(data)
    print(f'matriz de {len(data)} x {len(data[0])}')

main()