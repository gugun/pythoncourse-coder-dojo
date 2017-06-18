# function (modularisasi)

#menghitung luas 3 segitiga
#tanpa modularisasi

alas1 = 4
tinggi1 = 5
luas1 = alas1 * tinggi1 / 2
print(luas1)

alas2 = 4
tinggi2 = 5
luas2 = alas2 * tinggi2 / 2
print(luas2)

alas3 = 4
tinggi3 = 5
luas3 = alas3 * tinggi3 / 2
print(luas3)

print("----")

def hitung_segitiga(a, t):
	l = a, t / 2
	return l

luas1 = hitung_segitiga(4,5)
luas2 = hitung_segitiga(40, 5)
luas3 = hitung_segitiga(3,5)

print luas1
print luas2
print luas3