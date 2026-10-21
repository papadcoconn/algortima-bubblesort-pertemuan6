
angka = [10, 5, 20, 15, 30]

n = len(angka)
i = 0

while i < n - 1:
    j = 0

    while j < n - 1 - i:
        if angka[j] > angka[j + 1]:
            sementara = angka[j]
            angka[j] = angka[j + 1]
            angka[j + 1] = sementara

        j += 1

    i += 1

print("Hasil Bubble Sort:", angka)
