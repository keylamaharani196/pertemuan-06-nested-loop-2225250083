# Tugas 3: Tabel Perkalian dan Statistik
# Input: bilangan bulat positif n.
# Loop luar membuat setiap baris tabel.
# Loop dalam membuat setiap kolom dan menghitung hasil perkalian.
# total_baris menjumlahkan hasil pada setiap baris.
# total_semua menjumlahkan seluruh hasil perkalian.
# count_genap menghitung banyak hasil perkalian yang genap.
# Output: tabel perkalian, jumlah setiap baris,
# total keseluruhan, dan banyak hasil genap.

print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("n: "))

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end="\t")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f"| Jumlah baris {i} = {total_baris}")

print(f"\nTotal semua = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")
