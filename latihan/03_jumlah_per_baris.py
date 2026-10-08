# Latihan 3: Jumlah per Baris
# Loop luar mengatur nilai i dari 1 sampai 4.
# Loop dalam menghitung nilai i * j untuk setiap j dari 1 sampai 3.
# Akumulator total_baris menjumlahkan hasil perkalian pada setiap baris.
# Output menampilkan jumlah setiap baris.

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}")
    