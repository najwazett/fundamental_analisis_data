# Proyek Analisis Data: Bike Sharing Dataset

- **Nama:** Najwa Zhafir Hanysa
- **NIM:** 2405551069
- **Dataset:** Bike Sharing Dataset (`day.csv` & `hour.csv`)

## Deskripsi Proyek

Proyek ini merupakan proyek akhir analisis data yang mengeksplorasi pola penyewaan sepeda pada sistem Capital Bikeshare (tahun 2011–2012) berdasarkan faktor musim, kondisi cuaca, serta perbedaan jam operasional antara hari kerja dan akhir pekan/hari libur. Hasil analisis disajikan secara interaktif menggunakan dashboard berbasis Streamlit.

## Link Dashboard

Dashboard yang telah di-deploy dapat diakses melalui tautan berikut:  
https://vznoqnj7vzlruzxjvsbrtm.streamlit.app/

## Pertanyaan Bisnis

1. Bagaimana pengaruh perbedaan musim (`season`) dan kondisi cuaca (`weathersit`) terhadap rata-rata penyewaan sepeda harian (`cnt`) selama periode tahun 2011–2012, sebagai dasar penentuan jadwal perawatan (_maintenance_) armada dan strategi promosi musiman?
2. Pada jam berapa saja (`hr`) lonjakan rata-rata penyewaan sepeda terjadi pada hari kerja (`workingday = 1`) dibandingkan akhir pekan atau hari libur (`workingday = 0`) selama tahun 2011–2012, guna mengoptimalkan alokasi dan redistribusi (_rebalancing_) stok unit sepeda di titik stasiun transit?

## Struktur Direktori

- `day.csv` : Dataset penyewaan sepeda agregasi harian
- `hour.csv` : Dataset penyewaan sepeda agregasi per jam
- `notebook.ipynb` : Jupyter Notebook proses analisis data lengkap
- `dashboard.py` : Berkas utama aplikasi dashboard interaktif Streamlit
- `requirements.txt` : Daftar library Python yang digunakan
- `README.md` : Panduan setup environment dan cara menjalankan dashboard

## Setup Environment - Shell / Terminal

1. Pastikan Python sudah terinstal di komputer lokal Anda.
2. Buka terminal atau Command Prompt (CMD), lalu arahkan ke direktori utama folder proyek:
   ```bash
   cd path/ke/folder/proyek
   ```
3. Buat _virtual environment_ baru agar dependensi terisolasi:
   ```bash
   python -m venv venv
   ```
4. Aktifkan _virtual environment_ yang telah dibuat:
   - **Untuk Windows (CMD / PowerShell):**
     ```bash
     venv\Scripts\activate
     ```
   - **Untuk MacOS / Linux:**
     ```bash
     source venv/bin/activate
     ```
5. Instal seluruh _library_ yang dibutuhkan menggunakan berkas `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Dashboard

Pastikan _virtual environment_ dalam keadaan aktif, lalu jalankan perintah berikut di terminal pada direktori utama proyek:

```bash
streamlit run dashboard.py
```

Setelah perintah dijalankan, aplikasi dashboard akan otomatis terbuka melalui browser pada alamat `http://localhost:8501`.
