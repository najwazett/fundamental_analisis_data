import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Konfigurasi
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")


#Fungsi Visualisasi
def plot_season_rentals(df):
    season_labels = {1: "Spring (1)", 2: "Summer (2)", 3: "Fall (3)", 4: "Winter (4)"}
    
    # Agregasi dengan Pandas terlebih dahulu agar aman dari bug Seaborn
    season_avg = df.groupby("season")["cnt"].mean().reset_index()
    season_avg["season_label"] = season_avg["season"].map(season_labels)
    
    fig = plt.figure(figsize=(8, 6))
    sns.barplot(
        data=season_avg,
        x="season_label",
        y="cnt",
        hue="season_label",
        palette="Blues_d",
        legend=False
    )
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Musim", fontsize=13, fontweight="bold")
    plt.xlabel("Musim", fontsize=11)
    plt.ylabel("Rata-rata Penyewaan Harian", fontsize=11)
    st.pyplot(fig)

def plot_weather_rentals(df):
    weather_labels = {
        1: "Cerah / Berawan (1)", 
        2: "Berkabut / Mendung (2)", 
        3: "Hujan Ringan / Salju (3)",
        4: "Hujan Lebat / Ekstrem (4)"
    }
    
    weather_avg = df.groupby("weathersit")["cnt"].mean().reset_index()
    weather_avg["weather_label"] = weather_avg["weathersit"].map(weather_labels)
    
    fig = plt.figure(figsize=(8, 6))
    sns.barplot(
        data=weather_avg,
        x="weather_label",
        y="cnt",
        hue="weather_label",
        palette="Oranges_d",
        legend=False
    )
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca", fontsize=13, fontweight="bold")
    plt.xlabel("Kondisi Cuaca", fontsize=11)
    plt.ylabel("Rata-rata Penyewaan Harian", fontsize=11)
    st.pyplot(fig)

def plot_hourly_comparison(df):
    hourly_comparison = df.pivot_table(
        index="hr",
        columns="workingday",
        values="cnt",
        aggfunc="mean"
    )
    
    fig = plt.figure(figsize=(14, 6))
    if 0 in hourly_comparison.columns:
        plt.plot(
            hourly_comparison.index,
            hourly_comparison[0],
            label="Akhir Pekan / Libur (0)",
            color="red",
            linewidth=2,
            marker="o"
        )
    if 1 in hourly_comparison.columns:
        plt.plot(
            hourly_comparison.index,
            hourly_comparison[1],
            label="Hari Kerja (1)",
            color="blue",
            linewidth=2,
            marker="o"
        )
    plt.title("Perbandingan Waktu Penyewaan Sepeda antara Hari Kerja dan Hari Libur", fontsize=15, fontweight="bold")
    plt.xlabel("Jam", fontsize=12)
    plt.ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
    plt.xticks(range(0, 24))
    plt.legend(title="Status Hari")
    plt.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)


#Load Data
@st.cache_data
def load_data():
    day_df = pd.read_csv('day.csv')
    hour_df = pd.read_csv('hour.csv')

    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    return day_df, hour_df

day_df, hour_df = load_data()


#Initialize Session State
if 'page' not in st.session_state:
    st.session_state.page = "Visualisasi Data"


#Sidebar Navigation
with st.sidebar:
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="https://www.dicoding.com/blog/wp-content/uploads/2014/12/dicoding-header-logo.png" width="200">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Menu")

    #Tombol Pertama
    if st.button("Visualisasi Data", use_container_width=True,
                 type="primary" if st.session_state.page == "Visualisasi Data" else "secondary"):
        st.session_state.page = "Visualisasi Data"
        st.rerun()

    #Tombol Kedua
    if st.button("Conclusion & Recommendation", use_container_width=True,
                 type="primary" if st.session_state.page == "Conclusion & Recommendation" else "secondary"):
        st.session_state.page = "Conclusion & Recommendation"
        st.rerun()

    st.markdown("---")
    st.info("**Info:** Dashboard ini menampilkan hasil analisis penyewaan sepeda (Bike Sharing) tahun 2011-2012")

    #Filter 1: Rentang Tanggal
    min_date = day_df["dteday"].min().date()
    max_date = day_df["dteday"].max().date()
    
    date_range = st.date_input(
        label="Pilih Rentang Tanggal:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    #Filter 2: Pilihan Musim
    season_options = {1: "Spring (1)", 2: "Summer (2)", 3: "Fall (3)", 4: "Winter (4)"}
    selected_seasons = st.multiselect(
        label="Pilih Musim:",
        options=list(season_options.keys()),
        default=list(season_options.keys()),
        format_func=lambda x: season_options[x]
    )

#Filtering Data
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

filtered_day_df = day_df[
    (day_df["dteday"].dt.date >= start_date) & 
    (day_df["dteday"].dt.date <= end_date) &
    (day_df["season"].isin(selected_seasons))
]

filtered_hour_df = hour_df[
    (hour_df["dteday"].dt.date >= start_date) & 
    (hour_df["dteday"].dt.date <= end_date) &
    (hour_df["season"].isin(selected_seasons))
]

#Render Halaman
if st.session_state.page == "Visualisasi Data":
    st.title("Bike Sharing Analysis Dashboard")
    st.markdown("Dashboard interaktif tren dan pola penyewaan sepeda berdasarkan musim, cuaca, dan jam operasional (2011–2012).")
    
    if filtered_day_df.empty:
        st.warning("Tidak ada data untuk kombinasi filter tanggal dan musim yang dipilih. Silakan ubah filter di sidebar.")
    else:
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.metric("Total Penyewaan", f"{filtered_day_df['cnt'].sum():,}")
        with col_m2:
            st.metric("Rata-rata Penyewaan / Hari", f"{int(filtered_day_df['cnt'].mean()):,}")
        with col_m3:
            st.metric("Total Hari Terpilih", f"{len(filtered_day_df)} Hari")
            
        st.markdown("---")

        #Pertanyaan 1
        st.markdown("### 1. Pengaruh Musim dan Kondisi Cuaca terhadap Rata-rata Penyewaan Sepeda")
        col1, col2 = st.columns(2)
        with col1:
            plot_season_rentals(filtered_day_df)
        with col2:
            plot_weather_rentals(filtered_day_df)

        st.markdown("---")

        #Pertanyaan 2
        st.markdown("### 2. Perbandingan Pola Jam Sibuk Penyewaan Sepeda (Hari Kerja vs Akhir Pekan/Libur)")
        plot_hourly_comparison(filtered_hour_df)

elif st.session_state.page == "Conclusion & Recommendation":
    st.title("Conclusion & Recommendation")
    
    st.subheader("Conclusion")
    st.markdown("""
    - **Conclusion Pertanyaan 1 (Pengaruh Musim & Cuaca):** Musim Gugur (*Fall*) mencatatkan rata-rata penyewaan tertinggi sebesar **5.644 sepeda/hari**, diikuti Musim Panas (**4.992 sepeda/hari**), Musim Dingin (**4.728 sepeda/hari**), dan terendah pada Musim Semi (*Spring*) sebesar **2.604 sepeda/hari**. Dari sisi cuaca, kondisi Cerah/Berawan Tipis mendominasi dengan rata-rata **4.877 sepeda/hari**, menurun saat Berkabut/Mendung (**4.036 sepeda/hari**), dan anjlok drastis saat Hujan Ringan/Salju (**1.803 sepeda/hari**).
    - **Conclusion Pertanyaan 2 (Pola Jam Sibuk Hari Kerja vs Akhir Pekan/Libur):** Pada hari kerja, penyewaan memuncak tajam pada jam berangkat kerja pukul **08.00** (**477 sepeda/jam**) dan pulang kerja pukul **17.00–18.00** (**525 dan 492 sepeda/jam**), jauh melampaui jam non-sibuk siang hari (**200–254 sepeda/jam**). Sebaliknya, pada akhir pekan/libur, puncak terjadi secara landai di siang hingga sore hari pukul **12.00–16.00** (**353–373 sepeda/jam**).
    """)
    
    st.subheader("Rekomendasi Action Item")
    st.markdown("""
    - **Optimalisasi Alokasi & Rebalancing Armada di Jam Komuter:** Menambah stok unit sepeda di stasiun transit dan pemukiman sebelum pukul 07.00 pagi serta di kawasan perkantoran/kampus sebelum pukul 16.30 sore pada hari kerja. Pada akhir pekan, armada difokuskan di area taman kota dan jalur rekreasi mulai pukul 11.00 siang.
    - **Strategi Promosi & Maintenance Musiman:** Memberikan promo diskon khusus selama musim sepi (*Spring*) dan hari mendung untuk menjaga tingkat okupansi, sekaligus menjadwalkan perawatan besar (*maintenance*) unit sepeda pada periode *Spring* agar seluruh unit siap beroperasi maksimal saat memasuki musim puncak (*Summer* dan *Fall*).
    """)