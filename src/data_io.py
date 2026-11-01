from pathlib import Path


def validasi_nilai(nilai):
    """Nilai valid berada pada rentang 0 sampai 100."""
    return 0 <= nilai <= 100


def baca_data(path):
    """Membaca file berformat Nama,Nilai dan mengembalikan list dictionary."""
    data = []
    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris or baris.startswith("#"):
                    continue

                bagian = baris.split(",")
                if len(bagian) != 2:
                    print(f"Baris {nomor_baris} dilewati: format harus Nama,Nilai.")
                    continue

                nama = bagian[0].strip()
                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Baris {nomor_baris} dilewati: nilai bukan angka.")
                    continue

                if not nama:
                    print(f"Baris {nomor_baris} dilewati: nama kosong.")
                    continue
                if not validasi_nilai(nilai):
                    print(f"Baris {nomor_baris} dilewati: nilai harus 0-100.")
                    continue

                data.append({"nama": nama, "nilai": nilai})

    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")

    return data


def simpan_laporan(hasil, path):
    """Menyimpan ringkasan hasil analisis ke file teks."""
    file_path = Path(path)
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        statistik = hasil["statistik"]
        ketuntasan = hasil["ketuntasan"]

        with file_path.open("w", encoding="utf-8") as file:
            file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
            file.write("=" * 36 + "\n")
            file.write(f"Jumlah data: {statistik['jumlah']}\n")
            file.write(f"Rata-rata: {statistik['rata_rata']:.2f}\n")
            file.write(f"Nilai minimum: {statistik['minimum']}\n")
            file.write(f"Nilai maksimum: {statistik['maksimum']}\n")
            file.write(f"KKM: {hasil['kkm']}\n")
            file.write(f"Tuntas: {ketuntasan['tuntas']}\n")
            file.write(f"Belum tuntas: {ketuntasan['belum_tuntas']}\n")
        return True
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False
