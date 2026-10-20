# Deteksi Dini Mahasiswa Berisiko Gagal Sebelum Ujian (SIS + Moodle + eDify)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23095211.svg)](https://doi.org/10.5281/zenodo.23095211)

Kode dan hasil analisis untuk artikel:

> Rumintarsih, A. (2026). *Before the exam: A deployment-realistic evaluation of early-warning models for at-risk students in information systems courses* [Naskah dalam proses].

Kode dan hasil diarsipkan di Zenodo: https://doi.org/10.5281/zenodo.23095211 (versi v-1.1H). DOI untuk semua versi: https://doi.org/10.5281/zenodo.23095210

Penelitian ini mengevaluasi ulang dataset publik SIS–Moodle–eDify (326 mahasiswa, 5 mata kuliah Sistem Informasi, 2017–2021). Analisis membandingkan cara evaluasi studi sebelumnya (semua fitur termasuk UAS, split acak) dengan deteksi dini yang realistis: hanya informasi sebelum UTS, diuji pada kelas dan semester yang belum pernah dilihat model.

## Isi repositori

| File/folder | Isi |
|---|---|
| `Deteksi_Dini_Mahasiswa_Berisiko.ipynb` | Notebook lengkap: penggabungan data, model, validasi per kelas (20 ulangan), validasi waktu (2017–2019 → 2020–2021), kalibrasi, *decision curve*, beban dosen, analisis sensitivitas |
| `download_data.py` | Mengunduh dataset asli dari Zenodo ke folder ini |
| `hasil/Hasil_Deteksi_Dini.xlsx` | Semua tabel hasil (15 sheet) |
| `gambar/` | Gambar artikel (Figure 1–3, bahasa Inggris) dan gambar notebook (bahasa Indonesia) |
| `requirements.txt` | Paket Python |

## Data

Dataset **tidak disertakan** di repositori ini. Sumbernya:

> Hasan, R., Palaniappan, S., Mahmood, S., Abbas, A., & Sarker, K. U. (2021). Dataset of students' performance using student information system, Moodle and the mobile application "eDify". *Data, 6*(11), 110. https://doi.org/10.3390/data6110110

Data tersedia di Zenodo: https://zenodo.org/records/5591907 (lisensi CC BY 4.0).

Analisis tidak memakai kolom alamat IP pada log Moodle mentah, dan tidak berusaha mengidentifikasi ulang mahasiswa.

## Cara menjalankan

1. Pasang Python 3.10 atau lebih baru (misalnya lewat Anaconda).
2. Pasang paket: `pip install -r requirements.txt`
3. Unduh data: `python download_data.py`. Alternatifnya, unduh manual 77 file dari Zenodo dan letakkan di folder yang sama dengan notebook.
4. Buka notebook di Jupyter, lalu jalankan **Kernel → Restart & Run All** (sekitar 4 menit).

*Seed* acak ditetapkan (2026). Hasil telah diuji di dua komputer dengan versi pustaka berbeda; selisih AUC tidak lebih dari 0,001.

## Ringkasan hasil

| Desain evaluasi | AUC |
|---|---|
| *Oversampling* sebelum split acak, semua fitur (meniru studi sebelumnya) | 0,978 |
| Split acak, semua fitur | 0,885 |
| Deteksi dini sebelum UTS, validasi per kelas (rata-rata 20 ulangan) | 0,676 (0,596–0,719) |
| Deteksi dini sebelum UTS, uji semester pandemi 2020–2021 | 0,713 (95% CI 0,570–0,847) |

## Lisensi

- **Kode** (notebook dan skrip): MIT License (lihat `LICENSE`).
- **Hasil dan gambar**: CC BY 4.0.
- **Data**: tetap mengikuti lisensi dataset asli (CC BY 4.0). Harap sitasi Hasan dkk. (2021).

## Sitasi

Rumintarsih, A. (2026). *Kode dan hasil: Deteksi dini mahasiswa berisiko gagal sebelum ujian (SIS + Moodle + eDify)* (Version v-1.1H) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23095211

Lihat juga `CITATION.cff`.

## Ucapan terima kasih

Terima kasih kepada Raza Hasan dan rekan di Middle East College, Oman, yang telah membuka dataset SIS–Moodle–eDify untuk publik.
