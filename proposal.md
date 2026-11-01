# Proposal Proyek: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Latar Belakang
Guru matematika perlu merekap nilai siswa dan menghitung statistik kelas secara konsisten. Program console Python ini membantu membaca data dari file, memvalidasi nilai, menghitung statistik, menentukan ketuntasan, dan menyimpan laporan.

## 2. Pengguna dan Tujuan
**Pengguna utama:** guru matematika.  
**Tujuan:** mempercepat rekap nilai dan mengurangi kesalahan perhitungan manual.

## 3. Ruang Lingkup
### Fitur wajib
1. Membaca data nama dan nilai dari file teks.
2. Memvalidasi nilai pada rentang 0–100.
3. Menghitung jumlah data, rata-rata, minimum, dan maksimum.
4. Menghitung jumlah siswa tuntas/belum tuntas berdasarkan KKM.
5. Menyimpan ringkasan ke file laporan.

### Batasan
- Program berjalan di terminal/console.
- Data disimpan dalam file teks sederhana.
- KKM contoh ditetapkan 75 dan dapat diubah di `src/main.py`.
- Tidak menggunakan database, antarmuka web, atau layanan eksternal.

## 4. Kebutuhan
### Fungsional
- F01: program membaca file nilai.
- F02: program menolak nilai di luar rentang 0–100.
- F03: program menghitung statistik nilai.
- F04: program menentukan status ketuntasan.
- F05: program menyimpan laporan.

### Nonfungsional
- Mudah dijalankan dari terminal VS Code.
- Pesan kesalahan mudah dipahami.
- Fungsi dan variabel menggunakan nama yang jelas.
- Dapat diuji ulang menggunakan data yang sama.

## 5. Input, Proses, Output (IPO)
| Input | Proses | Output |
|---|---|---|
| `data/nilai_contoh.txt` berisi `Nama,Nilai` | Membaca file, validasi, menghitung statistik dan ketuntasan | Ringkasan di terminal dan `output/laporan.txt` |

## 6. Pseudocode
```text
MULAI
  baca data dari file
  jika tidak ada data valid:
      tampilkan pesan
      SELESAI
  hitung jumlah, rata-rata, minimum, maksimum
  hitung jumlah tuntas berdasarkan KKM
  tampilkan ringkasan
  simpan laporan ke file
SELESAI
```

## 7. Struktur Program
- `src/main.py`: mengatur alur program.
- `src/data_io.py`: membaca, memvalidasi, dan menyimpan data/laporan.
- `src/analisis.py`: menghitung statistik dan ketuntasan.
- `src/utilitas.py`: fungsi format nilai.
- `data/nilai_contoh.txt`: data contoh.
- `tests/test_case.md`: rancangan test case.

## 8. Struktur Data
- List of dictionary digunakan untuk menyimpan data siswa.
- Dictionary digunakan untuk mengelompokkan statistik dan hasil ketuntasan.
- String dan file teks digunakan untuk laporan.

## 9. Test Case
Lihat `tests/test_case.md`. Terdapat test case normal, batas, invalid, dan kondisi kosong.

## 10. Pembagian Tugas
| Peran | Tanggung jawab | PIC |
|---|---|---|
| Koordinator | Mengatur ruang lingkup dan integrasi | Isi nama |
| Programmer Data I/O | Membaca/validasi data dan menulis laporan | Isi nama |
| Programmer Logika | Statistik dan ketuntasan | Isi nama |
| Tester/QA | Memeriksa test case dan hasil | Isi nama |
| Dokumentasi | README dan proposal | Isi nama |

Sesuaikan PIC dengan anggota kelompok sebenarnya.

## 11. Jadwal/Milestone
- Pertemuan 14: proposal, struktur folder, pseudocode, test case, pembagian tugas.
- Antara P14–P15: implementasi fitur wajib.
- Pertemuan 15: integrasi, testing, debugging, dan dokumentasi.
- Pertemuan 16: presentasi dan evaluasi.

## 12. Repository
URL GitHub: isi URL repository kelompok.
