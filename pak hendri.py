for i in range(1000):
    print('hello word')
x = [1,2,3,4,5,7,8,9]
y = {'nama': 'tono', 'umur':30}
print(x[3])
print(y['umur'])

print('-------------')
for i in range(len(x)):
    print(x[i])
print('-------------')
for i in range(len(x)):
    if x[i] % 2 == 0:
        print(str(x[i]) + ' adalah genap')
    else:
        print(str(x[i])+ ' adalah ganjil')
print('-------------')
import fungsibilangan
for i in range(len(x)):
    if fungsibilangan.fungsigenap(x[i]):
        print(str(x[i]) + ' ini adalah bilangan genap')
    else:
        print(str(x[i]) + ' ini adalah bilangan ganjil')

hasil = fungsibilangan.fungsigenap(100002)
print(hasil)
hasil2 = fungsibilangan.fungsigenap(5000)
print(hasil2)