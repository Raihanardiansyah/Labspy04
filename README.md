# Praktikum 4

## Membuat program sederhana untuk menambahkan data ke dalam list

### Berikut prgram dan penjelesan dari masing masinh program

![Gambar1](https://github.com/Raihanardiansyah/Labspy04/blob/main/ss/py1.png?raw=true)

### Berikut penjelasan dari program di atas

Berikut adalah penjelasan dari masing-masing bagian kode:

### 1. Inisialisasi List:

data_mahasiswa = []

List data_mahasiswa digunakan untuk menyimpan data dari setiap mahasiswa yang akan dimasukkan. Setiap elemen list ini akan berisi dictionary yang merepresentasikan data dari seorang mahasiswa.

### 2. Fungsi tambah_data: Fungsi tambah_data() digunakan untuk menerima input data mahasiswa dan menghitung nilai akhir berdasarkan bobot tertentu.

### Input Data Mahasiswa:

nama = input("Nama : ")
nim = input("NIM : ")

Program meminta pengguna untuk memasukkan nama dan NIM mahasiswa.

### Input Nilai Mahasiswa:

tugas = float(input("Nilai Tugas : "))
uts = float(input("Nilai UTS : "))
uas = float(input("Nilai UAS : "))

Program meminta pengguna untuk memasukkan nilai tugas, nilai UTS, dan nilai UAS. Setiap nilai ini dikonversi ke dalam tipe float agar dapat digunakan dalam perhitungan.

### Perhitungan Nilai Akhir:

nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)

Nilai akhir dihitung berdasarkan bobot:

Tugas: 30%

UTS: 35%

UAS: 35%

### Menambahkan Data ke List:

data_mahasiswa.append({
    "nama": nama,
    "nim": nim,
    "tugas": tugas,
    "uts": uts,
    "uas": uas,
    "nilai_akhir": nilai_akhir
})

Data mahasiswa yang meliputi nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir disimpan dalam bentuk dictionary, lalu ditambahkan ke dalam list data_mahasiswa.

Dengan menjalankan fungsi tambah_data(), data seorang mahasiswa akan ditambahkan ke dalam list data_mahasiswa.

![Gambar2](https://github.com/Raihanardiansyah/Labspy04/blob/main/ss/py2.png?raw=true)

### Berikut penjelasannya

### 1. Header Tabel:

print("-" * 60)

print("| No | Nama     | NIM    | Tugas | UTS  | UAS  | Akhir |")

print("-" * 60)

Baris-baris ini mencetak garis pemisah dan judul kolom tabel. Kolom-kolom yang ditampilkan meliputi:

No : Nomor urut data mahasiswa.

Nama : Nama mahasiswa.

NIM : Nomor Induk Mahasiswa.

Tugas : Nilai tugas.

UTS : Nilai Ujian Tengah Semester.

UAS : Nilai Ujian Akhir Semester.

Akhir : Nilai akhir.

### 2. Looping untuk Menampilkan Data Mahasiswa:

for i, mhs in enumerate(data_mahasiswa, start=1):

    print(f"| {i:2} | {mhs['nama']:8} | {mhs['nim']:<6} | {mhs['tugas']:5.0f} | {mhs['uts']:5.0f} | {mhs['uas']:5.0f} | {mhs['nilai_akhir']:6.2f} |")

enumerate(data_mahasiswa, start=1): Loop ini mengiterasi setiap elemen dalam list data_mahasiswa. 

enumerate digunakan untuk mendapatkan indeks i (nomor urut) dimulai dari 1.

print(f"| {i:2} | {mhs['nama']:8} | ... | {mhs['nilai_akhir']:6.2f} |"): Baris ini mencetak data setiap mahasiswa dalam format tabel. 

### Beberapa format khusus digunakan:

{i:2} : Menampilkan nomor urut dengan lebar 2 karakter.

{mhs['nama']:8} : Menampilkan nama dengan lebar 8 karakter.

{mhs['nim']:<6} : Menampilkan NIM rata kiri dengan lebar 6 karakter.

{mhs['tugas']:5.0f}, {mhs['uts']:5.0f}, {mhs['uas']:5.0f} : Menampilkan nilai tugas, UTS, dan UAS dengan lebar 5 karakter dan tanpa angka desimal.

{mhs['nilai_akhir']:6.2f} : Menampilkan nilai akhir dengan lebar 6 karakter dan 2 angka desimal.

### 3. Footer Tabel:

print("-" * 60)

Garis pemisah di akhir tabel untuk menutup tampilan tabel.

Fungsi tampilkan_data() ini akan menampilkan semua data mahasiswa yang ada di dalam list data_mahasiswa dalam format tabel dengan kolom yang rapi.

![Gambar3](https://github.com/Raihanardiansyah/Labspy04/blob/main/ss/py3.png?raw=true)

### Berikut penjelasannya

Potongan kode ini berfungsi untuk meminta pengguna memasukkan data mahasiswa secara berulang hingga pengguna memilih untuk berhenti. Berikut penjelasannya:

### 1. Loop Tak Terbatas dengan while True:

while True:

Bagian ini membuat loop tak terbatas yang akan terus berjalan hingga ditemukan perintah break untuk menghentikan loop.


### 2. Memanggil Fungsi tambah_data():

tambah_data()

Di dalam loop, fungsi tambah_data() dipanggil setiap kali. Fungsi ini berfungsi untuk meminta pengguna memasukkan data mahasiswa, yang kemudian ditambahkan ke dalam list data_mahasiswa.


### 3. Meminta Konfirmasi untuk Melanjutkan atau Berhenti:

lanjut = input("Tambah data(y/t)? ")
if lanjut.lower() != 'y':
    break

Setelah menambahkan data mahasiswa, program akan menanyakan kepada pengguna apakah ingin menambah data lagi. Jika pengguna memasukkan karakter selain 'y' (atau 'Y'), loop akan dihentikan menggunakan break. Fungsi lanjut.lower() digunakan untuk mengubah input menjadi huruf kecil, sehingga input 'Y' atau 'y' dianggap sama.


### 4. Menampilkan Data Mahasiswa:

tampilkan_data()

Setelah keluar dari loop, fungsi tampilkan_data() dipanggil untuk menampilkan seluruh data mahasiswa yang telah dimasukkan dalam format tabel.

### Berikut hasil dari program tersebut

![Gambar4](https://github.com/Raihanardiansyah/Labspy04/blob/main/ss/hasil.png?raw=true)

### Dan berikut adalah flowchart dari programnya

![Gambar5](https://github.com/Raihanardiansyah/Labspy04/blob/main/ss/Flowchart.png?raw=true)

Flowchart ini menjelaskan alur proses untuk membaca data mahasiswa, menghitung nilai akhir berdasarkan bobot nilai tugas, UTS, dan UAS, dan menampilkan hasilnya. Berikut adalah penjelasan dari masing-masing langkah pada flowchart:

1. Start: Flowchart dimulai dari simbol Start, menandakan awal dari proses.

2. Input Data Mahasiswa:

Proses ini ditandai dengan simbol paralelogram yang berlabel Read(Nama, NIM, Nilai Tugas, Nilai UTS, Nilai UAS).

Pada tahap ini, program meminta pengguna untuk memasukkan data mahasiswa, yaitu Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS.

3. Menanyakan Ingin Menambah Data atau Tidak:

Simbol decision berbentuk belah ketupat berisi pertanyaan If(Menambahkan Data Mahasiswa (Y/T)?).

Program menanyakan kepada pengguna apakah ingin menambah data mahasiswa lagi atau tidak.

Jika Jawaban YA (Y):

Program kembali ke proses awal untuk membaca data mahasiswa berikutnya.

Jika Jawaban TIDAK (T):

Program melanjutkan ke proses perhitungan nilai akhir.

4. Menghitung Nilai Akhir:

Simbol proses berbentuk persegi panjang berisi rumus untuk menghitung Nilai Akhir.

Nilai Akhir dihitung dengan rumus:

\text{Nilai Akhir} = (30\% \times \text{Nilai Tugas}) + (35\% \times \text{Nilai UTS}) + (35\% \times \text{Nilai UAS})

5. Menampilkan Nilai Akhir:

Simbol paralelogram ini berlabel Write(Nilai Akhir).

Setelah menghitung nilai akhir, program menampilkan hasil perhitungan tersebut.

6. End:

Simbol End menandakan akhir dari proses flowchart ini.
