from data_io import baca_data, simpan_laporan
from analisis import hitung_statistik, hitung_ketuntasan


def main():
    path_data = "data/nilai_contoh.txt"
    path_laporan = "output/laporan.txt"
    kkm = 75

    data = baca_data(path_data)
    if not data:
        print("Tidak ada data nilai valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data)
    ketuntasan = hitung_ketuntasan(data, kkm)

    print("=== REKAP NILAI MATEMATIKA ===")
    print(f"Jumlah siswa : {statistik['jumlah']}")
    print(f"Rata-rata    : {statistik['rata_rata']:.2f}")
    print(f"Nilai minimum: {statistik['minimum']}")
    print(f"Nilai maksimum: {statistik['maksimum']}")
    print(f"Tuntas       : {ketuntasan['tuntas']}")
    print(f"Belum tuntas : {ketuntasan['belum_tuntas']}")

    hasil = {
        "statistik": statistik,
        "ketuntasan": ketuntasan,
        "kkm": kkm,
    }
    if simpan_laporan(hasil, path_laporan):
        print(f"Laporan disimpan ke: {path_laporan}")


if __name__ == "__main__":
    main()
