data_mahasiswa = []

def tambah_data():
    nama = input("Nama : ")
    nim = input("NIM : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS : "))
    uas = float(input("Nilai UAS : "))
    nilai_akhir = (0.3 * tugas) + (0.35 * uts) + (0.35 * uas)
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })

def tampilkan_data():
    print("=" * 60)
    print("| No |   Nama   |   NIM   | Tugas |  UTS  |  UAS  |  Akhir |")
    print("=" * 60)
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(f"| {i:2} | {mhs['nama']:<8} | {mhs['nim']:<6} | {mhs['tugas']:5.0f} | {mhs['uts']:5.0f} | {mhs['uas']:5.0f} | {mhs['nilai_akhir']:6.2f} |")
    print("=" * 60)

while True:
    tambah_data()
    lanjut = input("Tambah data(y/t)? ")
    if lanjut.lower() != 'y':
        break

tampilkan_data()