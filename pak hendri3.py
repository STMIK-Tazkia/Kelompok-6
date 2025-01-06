# SOAL 1: Fungsi untuk mengurutkan himpunan A menggunakan Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # Tukar elemen
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# SOAL 2: Fungsi untuk mencari nilai x dalam himpunan A
def cari_nilai(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Kembalikan indeks jika ditemukan
    return -1  # Kembalikan -1 jika tidak ditemukan

# Himpunan A
A = [109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21,
     378, 400, 101, 201, 301, 1]

# Urutkan himpunan A menggunakan Bubble Sort
print("Himpunan A sebelum diurutkan:", A)
A_terurut = bubble_sort(A.copy())
print("Himpunan A setelah diurutkan:", A_terurut)

# Cari nilai x di dalam himpunan
x = 300
indeks = cari_nilai(A_terurut, x)
if indeks != -1:
    print(f"Nilai {x} ditemukan di indeks ke-{indeks}.")
else:
    print(f"Nilai {x} tidak ditemukan.")
