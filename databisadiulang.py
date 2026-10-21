1
# Program Tabungan Mahasiswa

tabungan = []

while True:
    nominal = int(input("Masukkan nominal tabungan: Rp"))

    tabungan.append(nominal)

    lanjut = input("Tambah tabungan lagi? (ya/tidak): ")

    if lanjut == "tidak":
        break

print("\n=== DATA TABUNGAN MAHASISWA ===")

for i, nominal in enumerate(tabungan, start=1):
    print(f"Tabungan ke-{i}: Rp{nominal}")

print("Total tabungan: Rp", sum(tabungan))
