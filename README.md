# Program Rekap dan Analisis Nilai Matematika Kelas

**Nama kelompok:** isi nama kelompok  
**Anggota:** isi nama anggota  
**Mata kuliah:** Algoritma dan Pemrograman — Pertemuan 14

## Deskripsi
Proyek Python berbasis terminal untuk membaca nilai dari file, memvalidasi nilai 0–100, menghitung statistik kelas, menghitung ketuntasan berdasarkan KKM, dan menyimpan laporan.

## Struktur Folder
```text
pertemuan-14-proyek/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Persyaratan
- Python 3
- Visual Studio Code (disarankan)
- Git jika ingin mengunggah proyek ke GitHub

## Cara Menjalankan di VS Code
1. Ekstrak folder proyek.
2. Buka folder `pertemuan-14-proyek` melalui **File > Open Folder**.
3. Pilih interpreter Python 3.
4. Buka **Terminal > New Terminal**.
5. Jalankan:

```bash
python src/main.py
```

Jika perintah `python` tidak dikenali, coba `py src/main.py` di Windows atau `python3 src/main.py`.

## Format Data
Data berada di `data/nilai_contoh.txt`, satu siswa per baris dengan format:

```text
Nama,Nilai
Ayu,85
Budi,78
```

Nilai yang diterima adalah 0 sampai 100. Baris dengan format salah atau nilai di luar rentang dilewati dan menampilkan pesan.

## Output
Program menampilkan jumlah data, rata-rata, nilai minimum, maksimum, jumlah tuntas, dan jumlah belum tuntas. Laporan disimpan di `output/laporan.txt`.

KKM contoh adalah 75. Nilai yang sama dengan KKM termasuk tuntas.

## Test Case
Rancangan test case tersedia di `tests/test_case.md`, termasuk kondisi normal, batas, invalid, file tidak ditemukan, dan data kosong.

## Proposal
Lihat `proposal.md` untuk latar belakang, tujuan, ruang lingkup, kebutuhan, IPO, pseudocode, struktur data, pembagian tugas, dan milestone.

## GitHub
Ganti URL di bawah dengan URL repository kelompok.

```bash
git init
git add .
git commit -m "docs: menambahkan proposal dan test case proyek"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPOSITORY.git
git push -u origin main
```

Ganti `USERNAME` dan `NAMA-REPOSITORY` sesuai repository milik kelompok.
