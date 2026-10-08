# Pertemuan 06 Nested Loop Python

Algoritma dan Pemrograman | Pertemuan 06

Nama: Keyla Maharani  
NIM: 2225250083  
Kelas: 3E  

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam pemrograman Python.

Pada tugas ini, nested loop digunakan untuk membuat tabel perkalian dari 1 sampai n. Program juga digunakan untuk menghitung jumlah setiap baris, total seluruh hasil perkalian, dan banyak hasil perkalian yang genap.

## Cara Menjalankan

Program dapat dijalankan melalui terminal VS Code dengan perintah:

~~~bash
python3 tugas/tabel_perkalian_dan_statistik.py
~~~

Pada Windows dapat menggunakan:

~~~bash
python tugas/tabel_perkalian_dan_statistik.py
~~~

## Algoritma Tugas 3

1. Baca nilai `n` sebagai bilangan bulat.
2. Validasi nilai `n`. Jika `n <= 0`, program meminta input kembali sampai nilai positif.
3. Set `total_semua = 0`.
4. Set `count_genap = 0`.
5. Ulangi `i` dari 1 sampai `n` menggunakan loop luar.
6. Set `total_baris = 0` pada setiap awal baris.
7. Ulangi `j` dari 1 sampai `n` menggunakan loop dalam.
8. Hitung `hasil = i * j`.
9. Tampilkan nilai `hasil`.
10. Tambahkan `hasil` ke `total_baris`.
11. Tambahkan `hasil` ke `total_semua`.
12. Periksa apakah `hasil` merupakan bilangan genap menggunakan kondisi `hasil % 2 == 0`.
13. Jika hasil genap, tambahkan `count_genap` sebanyak 1.
14. Setelah loop dalam selesai, tampilkan jumlah setiap baris.
15. Setelah kedua loop selesai, tampilkan total keseluruhan dan banyak hasil genap.

### Peran Loop, Akumulator, Counter, dan Output

- **Loop luar:** mengatur setiap baris tabel perkalian dari 1 sampai `n`.
- **Loop dalam:** mengatur setiap kolom pada setiap baris dari 1 sampai `n`.
- **Kondisi:** memeriksa apakah hasil perkalian merupakan bilangan genap.
- **`total_baris`:** sebagai akumulator untuk menjumlahkan hasil perkalian pada setiap baris.
- **`total_semua`:** sebagai akumulator untuk menjumlahkan seluruh hasil perkalian.
- **`count_genap`:** sebagai counter untuk menghitung banyak hasil perkalian yang genap.
- **Output:** menampilkan tabel perkalian, jumlah setiap baris, total keseluruhan, dan banyak hasil genap.

## Hasil Pengujian

| Input n | Jumlah Pasangan | Total Semua | Banyak Hasil Genap | Status |
|---|---:|---:|---:|---|
| 1 | 1 | 1 | 0 | Berhasil |
| 2 | 4 | 9 | 3 | Berhasil |
| 3 | 9 | 36 | 5 | Berhasil |

### Test Case 1

**Input:**

~~~text
1
~~~

**Hasil yang diharapkan:**

~~~text
Jumlah pasangan = 1
Total semua = 1
Banyak hasil genap = 0
~~~

**Keluaran aktual:**

~~~text
1    | Jumlah baris 1 = 1

Total semua = 1
Banyak hasil genap = 0
~~~

**Status:** Berhasil.

### Test Case 2

**Input:**

~~~text
2
~~~

**Hasil yang diharapkan:**

~~~text
Jumlah pasangan = 4
Total semua = 9
Banyak hasil genap = 3
~~~

**Keluaran aktual:**

~~~text
1    2    | Jumlah baris 1 = 3
2    4    | Jumlah baris 2 = 6

Total semua = 9
Banyak hasil genap = 3
~~~

**Status:** Berhasil.

### Test Case 3

**Input:**

~~~text
3
~~~

**Hasil yang diharapkan:**

~~~text
Jumlah pasangan = 9
Total semua = 36
Banyak hasil genap = 5
~~~

**Keluaran aktual:**

~~~text
1    2    3    | Jumlah baris 1 = 6
2    4    6    | Jumlah baris 2 = 12
3    6    9    | Jumlah baris 3 = 18

Total semua = 36
Banyak hasil genap = 5
~~~

**Status:** Berhasil.

## Analisis Efisiensi

Untuk input `n`, loop luar berjalan sebanyak `n` kali. Pada setiap iterasi loop luar, loop dalam juga berjalan sebanyak `n` kali.

Dengan demikian, jumlah iterasi badan loop dalam adalah:

~~~text
n × n = n²
~~~

Contoh:

- Jika `n = 1`, badan loop dalam berjalan `1² = 1` kali.
- Jika `n = 2`, badan loop dalam berjalan `2² = 4` kali.
- Jika `n = 3`, badan loop dalam berjalan `3² = 9` kali.
- Jika `n = 5`, badan loop dalam berjalan `5² = 25` kali.

Jadi, semakin besar nilai `n`, semakin banyak operasi yang dilakukan oleh program.

## Refleksi

Kesalahan yang perlu diperhatikan dalam penggunaan nested loop adalah kesalahan indentasi. Loop dalam harus berada di dalam loop luar. Jika indentasi salah, perintah dapat berjalan pada bagian yang tidak sesuai sehingga hasil program menjadi salah.

Cara memperbaikinya adalah dengan memastikan setiap perintah memiliki indentasi yang sesuai dengan struktur loop. Selain itu, `total_baris` harus berada di dalam loop luar agar setiap baris dapat dihitung secara terpisah.

## Refleksi Teknis

### 1. Mengapa `total_baris` direset di setiap iterasi loop luar?

`total_baris` direset menjadi 0 pada setiap iterasi loop luar karena setiap baris harus memiliki perhitungan jumlah sendiri. Jika tidak direset, jumlah dari baris sebelumnya akan ikut masuk ke baris berikutnya.

### 2. Mengapa `total_semua` tidak direset di setiap baris?

`total_semua` tidak direset di setiap baris karena variabel tersebut digunakan untuk menghitung jumlah seluruh hasil perkalian dari semua baris. Jika direset pada setiap baris, hasil akhirnya hanya akan menjadi jumlah dari baris terakhir.

### 3. Untuk n, berapa kali pernyataan `hasil = i * j` dieksekusi?

Pernyataan `hasil = i * j` dieksekusi sebanyak:

~~~text
n² kali
~~~

Hal ini terjadi karena loop luar berjalan `n` kali dan loop dalam berjalan `n` kali untuk setiap iterasi loop luar.

### 4. Bagaimana Anda membuktikan `count_genap` benar?

`count_genap` dibuktikan benar dengan memeriksa setiap hasil perkalian menggunakan kondisi:

~~~python
if hasil % 2 == 0:
    count_genap += 1
~~~

Counter hanya bertambah ketika hasil perkalian habis dibagi 2.

Untuk `n = 3`, hasil perkaliannya adalah:

~~~text
1  2  3
2  4  6
3  6  9
~~~

Hasil yang genap adalah:

~~~text
2, 2, 4, 6, 6
~~~

Jumlahnya adalah 5, sehingga `count_genap = 5`.

### 5. Apa bagian program yang akan paling banyak melakukan operasi ketika n membesar?

Bagian yang paling banyak melakukan operasi adalah nested loop karena badan loop dalam dijalankan sebanyak `n²` kali.

Di dalam nested loop terdapat proses menghitung `hasil = i * j`, menambahkan hasil ke akumulator, dan memeriksa kondisi bilangan genap. Oleh karena itu, ketika nilai `n` semakin besar, jumlah operasi juga semakin banyak.

## Kesimpulan

Program Tugas 3 berhasil menerapkan nested loop untuk membuat tabel perkalian dari 1 sampai `n`. Program juga berhasil menghitung jumlah setiap baris, total seluruh hasil perkalian, dan banyak hasil perkalian yang genap.

Berdasarkan pengujian `n = 1`, `n = 2`, dan `n = 3`, hasil program sesuai dengan hasil yang diharapkan. Nested loop menghasilkan tepat `n²` pasangan dan proses pencacahan hasil genap berjalan dengan benar.
## Catatan Pengembangan

Program telah diuji menggunakan beberapa nilai n untuk memastikan hasil tabel,
total keseluruhan, dan pencacahan hasil genap berjalan sesuai algoritma.
Pengumpulan dilakukan melalui GitHub.
