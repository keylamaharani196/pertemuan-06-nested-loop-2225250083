# Latihan 2: Pola Segitiga
# Loop luar mengatur nomor baris dari 1 sampai n.
# Loop dalam mencetak bintang sesuai jumlah pada setiap baris.
# Output menampilkan pola segitiga bintang.

n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    