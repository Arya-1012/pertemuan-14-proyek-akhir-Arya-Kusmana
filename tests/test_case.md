# Test Case Awal — Rekap Nilai Matematika

| ID | Kategori | Input/kondisi | Hasil yang diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Baris ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ditemukan | Program menampilkan pesan, tidak crash |
| TC06 | Normal | Semua nilai >= KKM | Jumlah tuntas sama dengan jumlah data |
| TC07 | Invalid | Teks nilai bukan angka | Baris dilewati dengan pesan |
| TC08 | Kosong | File tanpa data valid | Program menampilkan pesan tidak ada data |

## Catatan
KKM pada program contoh adalah 75. Nilai sama dengan KKM dihitung tuntas.
