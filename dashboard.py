import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Konfigurasi
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")


#Fungsi Visualisasi
def plot_season_rentals(df):
    season_avg = df.groupby("season")["cnt"].mean()
    
    fig = plt.figure(figsize=(8, 6))
    plt.bar(
        x=["Spring (1)", "Summer (2)", "Fall (3)", "Winter (4)"],
        height=season_avg.values,
        color=["#6baed6", "#4292c6", "#2171b5", "#084594"]
    )
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Musim", fontsize=13, fontweight="bold")
    plt.xlabel("Musim", fontsize=11)
    plt.ylabel("Rata-rata Penyewaan Harian", fontsize=11)
    st.pyplot(fig)

def plot_weather_rentals(df):
    weather_avg = df.groupby("weathersit")["cnt"].mean()
    
    fig = plt.figure(figsize=(8, 6))
    plt.bar(
        x=["Cerah / Berawan (1)", "Berkabut / Mendung (2)", "Hujan Ringan / Salju (3)"],
        height=weather_avg.values,
        color=["#fd8d3c", "#e6550d", "#a63603"]
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
    plt.plot(
        hourly_comparison.index,
        hourly_comparison[0],
        marker="o",
        linewidth=2,
        color="red",
        label="Hari Libur"
    )
    plt.plot(
        hourly_comparison.index,
        hourly_comparison[1],
        marker="o",
        linewidth=2,
        color="blue",
        label="Hari Kerja"
    )

    plt.title("Perbandingan Waktu Penyewaan Sepeda antara Hari Kerja dan Hari Libur", fontsize=13, fontweight="bold")
    plt.xlabel("Jam", fontsize=11)
    plt.ylabel("Rata-rata Penyewaan Harian", fontsize=11)

    plt.xticks(range(0, 24), fontsize=11)
    plt.yticks(fontsize=11)

    plt.legend(title="Status Hari", fontsize=11)
    plt.grid(True, alpha=0.5)
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


#Render Halaman
if st.session_state.page == "Visualisasi Data":
    st.title("Bike Sharing Analysis Dashboard")
    st.markdown("Dashboard ini menampilkan tren dan pola penyewaan sepeda berdasarkan musim, cuaca, dan jam operasional.")

    #Metrik Ringkasan
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.metric("Total Penyewaan (2011-2012)", f"{day_df['cnt'].sum():,}")
    with col_m2:
        st.metric("Rata-rata Penyewaan / Hari", f"{int(day_df['cnt'].mean()):,}")
    with col_m3:
        st.metric("Total Hari Tercatat", f"{len(day_df)} Hari")
        
    st.markdown("---")

    #Pertanyaan Bisnis 1
    st.markdown("### 1. Bagaimana pengaruh musim dan kondisi cuaca terhadap penyewaan sepeda?")
    col1, col2 = st.columns(2)
    with col1:
        plot_season_rentals(day_df)
    with col2:
        plot_weather_rentals(day_df)

    st.markdown("---")

    # Pertanyaan Bisnis 2
    st.markdown("### 2. Pada jam berapa saja puncak penyewaan terjadi pada Hari Kerja vs Hari Libur?")
    plot_hourly_comparison(hour_df)

elif st.session_state.page == "Conclusion & Recommendation":
    st.title("Conclusion & Recommendation")
    
    st.subheader("Conclusion")
    st.markdown("""
    - **Pengaruh Musim & Cuaca:** Musim gugur (*Fall*) mencatat rata-rata penyewaan harian tertinggi (~5.644 sepeda/hari), sedangkan musim semi (*Spring*) terendah (~2.604 sepeda/hari). Kondisi cuaca cerah/berawan tipis mendominasi penyewaan, sementara hujan ringan/salju menurunkan penyewaan hingga lebih dari 50%.
    - **Pola Jam Sibuk:** Pada hari kerja, lonjakan penyewaan terjadi pada jam komuter (pukul **08.00 pagi** dan **17.00–18.00 sore**). Sebaliknya, pada akhir pekan atau hari libur, penyewaan memuncak secara landai di siang hari (pukul **12.00–16.00**).
    """)
    
    st.subheader("Rekomendasi Action Item")
    st.markdown("""
    - **Optimalisasi Armada di Jam Komuter:** Menambah ketersediaan unit sepeda di area stasiun transit dan pemukiman sebelum pukul 07.00 pagi serta di area perkantoran/kampus sebelum pukul 16.30 sore pada hari kerja.
    - **Strategi Promosi & Maintenance Musiman:** Memberikan promo khusus selama musim sepi (*Spring*) untuk menjaga tingkat okupansi, sekaligus menjadwalkan perawatan besar (*maintenance*) armada pada musim tersebut agar siap menghadapi puncak permintaan di musim panas (*Summer*) dan gugur (*Fall*).
    """)