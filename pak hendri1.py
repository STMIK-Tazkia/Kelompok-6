# Matriks C
C = [
    [41, 16, 54, 10],
    [33, 86, 31, 13],
    [21, 27, 32, 11],
    [33, 54, 32, 15]
]

# Matriks D
D = [
    [1, 4, 1, 1],
    [2, 1, 0, 2],
    [2, 0, 1, 2],
    [1, 1, 4, 1]
]

# Inisialisasi matriks hasil
result = [[0 for _ in range(4)] for _ in range(4)]

# Perkalian matriks secara manual
for i in range(4):  # Baris matriks C
    for j in range(4):  # Kolom matriks D
        for k in range(4):  # Elemen untuk dikalikan
            result[i][j] += C[i][k] * D[k][j]

# Output hasil
print("Hasil perkalian matriks C x D:")
for row in result:
    print(row)
