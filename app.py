import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Penilaian Inovasi Sampah", layout="wide")

# Data Kriteria (Diekstrak dari file Excel)
kriteria_list = [
    {
        "Kriteria": "Dampak nyata pengurangan sampah",
        "Bobot": 0.25,
        "Rubrik": {
            0: "Tidak ada bukti penurunan sampah ke TPA/TPST; tidak ada peningkatan 3R/daur ulang.",
            1: "Penurunan sampah ke TPA <5% atau <1 ton/hari; peningkatan 3R <5%.",
            2: "Penurunan sampah ke TPA 5-10% atau 1-3 ton/hari; peningkatan 3R 5-10%.",
            3: "Penurunan sampah ke TPA 10-20% atau 3-5 ton/hari; peningkatan 3R 10-20%.",
            4: "Penurunan sampah ke TPA 20-30% atau 5-10 ton/hari; peningkatan 3R 20-30%.",
            5: "Penurunan sampah ke TPA >30% atau >10 ton/hari; peningkatan 3R >30%."
        }
    },
    {
        "Kriteria": "Cakupan & partisipasi masyarakat",
        "Bobot": 0.20,
        "Rubrik": {
            0: "Inovasi hanya di 1 lokasi pilot; tidak ada partisipasi masyarakat/komunitas.",
            1: "Cakupan <25% wilayah target; partisipasi masyarakat sangat terbatas (<10 KK/kelompok).",
            2: "Cakupan 25-50% wilayah target; partisipasi masyarakat terbatas (10-50 KK/kelompok).",
            3: "Cakupan 50-75% wilayah target; partisipasi masyarakat cukup baik (50-200 KK/kelompok).",
            4: "Cakupan >75% wilayah target; partisipasi masyarakat baik (>200 KK/kelompok, bank sampah aktif).",
            5: "Cakupan hampir seluruh wilayah (>90%); partisipasi masyarakat sangat baik (ribuan KK, banyak bank sampah/komunitas)."
        }
    },
    {
        "Kriteria": "Kelembagaan & keberlanjutan",
        "Bobot": 0.20,
        "Rubrik": {
            0: "Tidak ada SK/tim pengelola; tidak ada SOP; tidak ada anggaran operasional.",
            1: "SK/tim ada tetapi tidak aktif; SOP tidak jelas; anggaran tidak pasti.",
            2: "SK/tim cukup aktif; SOP ada tetapi belum lengkap; anggaran operasional terbatas.",
            3: "SK/tim aktif; SOP jelas; anggaran operasional cukup untuk 1-2 tahun.",
            4: "SK/tim sangat aktif; SOP lengkap dan terdokumentasi; anggaran operasional terjamin >2 tahun.",
            5: "SK/tim sangat kuat; SOP terintegrasi dengan sistem daerah; anggaran operasional terjamin >3 tahun dengan diversifikasi sumber."
        }
    },
    {
        "Kriteria": "Kepatuhan dasar pengelolaan sampah",
        "Bobot": 0.25,
        "Rubrik": {
            0: "Terdapat TPS liar di wilayah cakupan; pengangkutan tidak terjadwal; TPA open dumping tanpa pengendalian lindi/gas.",
            1: "Masih ada 1-2 TPS liar; pengangkutan kadang terlambat; TPA open dumping dengan pengendalian minimal.",
            2: "TPS liar berkurang signifikan; pengangkutan terjadwal namun belum konsisten; TPA mendekati controlled landfill namun belum memenuhi semua syarat.",
            3: "Tidak ada TPS liar di wilayah cakupan; pengangkutan terjadwal konsisten; TPA minimal controlled landfill (penutupan tanah berkala, pengendalian lindi dasar).",
            4: "Tidak ada TPS liar; pengangkutan terjadwal dan terpantau; TPA controlled landfill dengan pengendalian lindi & gas memadai.",
            5: "Tidak ada TPS liar; pengangkutan terjadwal, terpantau digital; TPA controlled landfill mendekati sanitary landfill dengan pengendalian lingkungan baik."
        }
    },
    {
        "Kriteria": "Kebaruan dan potensi replikasi",
        "Bobot": 0.10,
        "Rubrik": {
            0: "Tidak ada unsur kebaruan; tidak dapat direplikasi ke wilayah lain.",
            1: "Kebaruan sangat rendah; replikasi sulit tanpa modifikasi",
            2: "Ada sedikit kebaruan; replikasi mungkin dengan pendampingan intensif.",
            3: "Ada kebaruan yang jelas; replikasi layak dengan modifikasi ",
            4: "Kebaruan tinggi (teknologi/model layanan/skema pendanaan baru); replikasi mudah dengan panduan SOP.",
            5: "Kebaruan sangat tinggi (inovasi percontohan tingkat provinsi/nasional); replikasi sangat mudah dengan dokumentasi lengkap."
        }
    }
]

def main():
    st.title("Aplikasi Penilaian Inovasi Pengelolaan Sampah")
    st.markdown("**(Kabupaten/Kota Sehat) 2026**")
    st.divider()

    # Sidebar untuk Informasi Penilai
    st.sidebar.header("Data Penilaian")
    nama_daerah = st.sidebar.text_input("Nama Kabupaten/Kota:")
    nama_inovasi = st.sidebar.text_input("Nama Inovasi:")
    nama_penilai = st.sidebar.text_input("Nama Penilai:")

    st.header("Form Penilaian")
    
    total_skor_akhir = 0
    hasil_penilaian = []

    # Looping untuk setiap kriteria membuat form input
    for i, item in enumerate(kriteria_list):
        st.subheader(f"{i+1}. {item['Kriteria']} (Bobot: {item['Bobot'] * 100:.0f}%)")
        
        # Accordion untuk melihat rubrik indikator
        with st.expander("Lihat Indikator Penilaian (Klik untuk membuka)"):
            for skor, deskripsi in item['Rubrik'].items():
                st.markdown(f"**Skor {skor}:** {deskripsi}")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            skor_input = st.number_input(f"Input Skor (0-5)", min_value=0, max_value=5, value=0, key=f"skor_{i}")
            nilai_akhir = skor_input * item['Bobot']
            total_skor_akhir += nilai_akhir
            st.info(f"Nilai Akhir Kriteria: **{nilai_akhir:.2f}**")
            
        with col2:
            catatan = st.text_area(f"Catatan Penilai", key=f"catatan_{i}", height=100)
            
        hasil_penilaian.append({
            "Kriteria": item['Kriteria'],
            "Bobot (%)": item['Bobot'] * 100,
            "Skor (0-5)": skor_input,
            "Nilai Akhir": nilai_akhir,
            "Catatan": catatan
        })
        st.divider()
        
    # Kalkulasi Hasil Akhir
    st.header("Hasil Akhir Penilaian")
    st.metric(label="Total Nilai Keseluruhan", value=f"{total_skor_akhir:.2f}")
    
    # Tombol Simpan/Export
    if st.button("Tampilkan & Unduh Ringkasan"):
        if not nama_daerah or not nama_inovasi:
            st.warning("Peringatan: Mohon lengkapi Nama Kabupaten/Kota dan Nama Inovasi di menu samping (sidebar).")
        
        st.success("Tabel Ringkasan Penilaian:")
        df_hasil = pd.DataFrame(hasil_penilaian)
        st.dataframe(df_hasil, use_container_width=True)
        
        # Fitur export ke CSV
        csv = df_hasil.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Unduh Data (CSV)",
            data=csv,
            file_name=f"Penilaian_{nama_daerah}_{nama_inovasi}.csv",
            mime='text/csv',
        )

if __name__ == '__main__':
    main()
