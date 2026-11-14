# Proyek Analisis Data: Bike Sharing Dataset

- **Nama:** Najwa Zhafir Hanysa
- **NIM:** 2405551069
- **Dataset:** Bike Sharing Dataset (`day.csv` & `hour.csv`)

## Deskripsi Proyek

Proyek ini merupakan proyek akhir analisis data yang bertujuan untuk mengeksplorasi pola penyewaan sepeda pada sistem Capital Bikeshare (tahun 2011–2012) berdasarkan faktor musim, kondisi cuaca, serta perbedaan jam operasional antara hari kerja dan akhir pekan/hari libur. Hasil analisis disajikan secara interaktif melalui dashboard berbasis Streamlit.

## Link Dashboard

Dashboard yang telah di-deploy dapat diakses secara langsung melalui tautan berikut:  
https://vznoqnj7vzlruzxjvsbrtm.streamlit.app/

## Pertanyaan Bisnis

1. Bagaimana pengaruh musim (`season`) dan kondisi cuaca (`weathersit`) terhadap rata-rata penyewaan sepeda harian (`cnt`) selama tahun 2011–2012?
2. Pada jam berapa saja (`hr`) puncak penyewaan sepeda terjadi pada hari kerja (`workingday = 1`) dibandingkan akhir pekan atau hari libur (`workingday = 0`)?

## Struktur Direktori

- `day.csv` : Dataset penyewaan sepeda agregasi harian
- `hour.csv` : Dataset penyewaan sepeda agregasi per jam
- `notebook.ipynb` : Jupyter Notebook proses analisis data lengkap
- `dashboard.py` : Berkas utama aplikasi dashboard Streamlit
- `requirements.txt` : Daftar library Python yang digunakan
- `README.md` : Panduan proyek dan cara menjalankan dashboard

## Setup Environment

1. Pastikan Python sudah terinstal di komputer lokal.
2. Buka terminal atau Command Prompt (CMD), lalu arahkan ke direktori utama folder proyek:
   ```bash
   cd path/ke/folder/proyek
   ```
3. Instal seluruh library yang dibutuhkan menggunakan berkas `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Dashboard

Jalankan perintah berikut di terminal pada direktori utama proyek:

```bash
streamlit run dashboard.py
```

Setelah perintah dijalankan, aplikasi dashboard akan otomatis terbuka melalui browser pada alamat `http://localhost:8501`.
