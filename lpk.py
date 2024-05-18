import streamlit as st

# Mengatur warna latar belakang dan gaya font
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFFFE0;  /* Warna latar belakang baru */
        color: black;               /* Warna teks baru */
        font-size: 25px;            /* Ukuran font tetap */
    }
      [data-testid="stSidebar"] {
        background-color: #FFB347;  /* Warna latar belakang coklat tua */
        color: white;               /* Warna teks baru, disesuaikan agar kontras dengan latar belakang */
        font-size: 23px;            /* Ukuran font tetap */
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Navigasi sidebar menggunakan st.selectbox
st.sidebar.title('Menu Pilihan')
selected = st.sidebar.selectbox('Silahkan Pilih Menu dibawah 👇🏻👇🏻👇🏻',
        ('Perkenalan Aplikasi',
         'Hitung Satuan Konsentrasi',
         'Konversi Satuan Konsentrasi'),
        index=0)

def home():
    
#Halaman Perkenalan Aplikasi
    if selected == 'Perkenalan Aplikasi':
        st.header('✨Selamat datang di Web Aplikasi Menghitung Konsentrasi dalam berbagai Satuan✨', divider='rainbow')
        st.write('Scroll kebawah untuk mendapatkan informasi lengkap ya!😊')
        st.image('kelompok5.jpg',output_format="auto")
        st.header('Tentang Aplikasi', divider='orange')
        st.write('Konsentrasi larutan adalah jumlah zat yang terlarut dalam setiap satuan larutan atau pelarut. '
                'Secara sederhana, konsentrasi larutan dapat memberikan gambaran atau sebuah informasi '
                'tentang perbandingan jumlah zat terlarut dan jumlah pelarutnya.')
        st.write('Web Aplikasi kami akan membantu untuk Menghitung Konsentrasi larutan dalam berbagai Satuan. Selain itu, Web kami juga dapat membantu untuk Mengkonversi Satuan konsentrasi yang sudah diketahui menjadi Satuan Konsentrasi yang lain.')
        st.write('Selanjutnya, klik tanda ">" yang terletak dibagian kiri atas web kami untuk memilih menu tampilan yang telah disediakan.')
        st.subheader('Semoga Membantu✨✨✨')
    
#Halaman Hitung Konsentrasi dalam berbagai Satuan
    elif selected == 'Hitung Satuan Konsentrasi':
        tabs = st.tabs(['1. % b/b','2. % v/v','3. % b/v','4. Molaritas','5. Normalitas','6. PPM'])
        
#Halaman Hitung % b/b
        with tabs[0] :
            st.header('Hitung Konsentrasi % b/b', divider='orange')
            st.write("Persen berat per berat (% b/b) digunakan untuk mengukur konsentrasi suatu zat berdasarkan berat zat terlarut dibandingkan dengan berat total larutan(zat terlarut + zat pelarut).")
            st.write("Jadi, (% b/b) digunakan saat keduanya (zat terlarut dan pelarut) diukur berdasarkan berat.")
            st.latex(r''' \% \text{b/b} = \frac{\text{zat terlarut(g)}}{\text{zat terlarut(g)} + \text{zat pelarut(g)}} \times 100\% ''')
            zat_terlarut = st.number_input("Masukkan Nilai Zat Terlarut (g)", key="zat_terlarut_bb")
            zat_pelarut = st.number_input("Masukkan Nilai Zat Pelarut (g)", key="zat_pelarut_bb")
            hitung = st.button("Hitung Konsentrasi % b/b", key="hitung_bb")
        
            if hitung:
                konsentrasi = zat_terlarut / (zat_terlarut + zat_pelarut) * 100
                konsentrasi_formatted = round(konsentrasi, 2)
                st.success(f"Konsentrasinya adalah = {konsentrasi_formatted}% b/b")

#Halaman Hitung % v/v
        with tabs[1] :
            st.header('Hitung Konsentrasi % v/v', divider='orange')
            st.write("Persen volume per volume (% v/v) digunakan unuk mengukur konsentrasi suatu zat berdasarkan volume zat terlarut dibandingkan dengan volume total larutan(zat terlarut + zat pelarut).")
            st.write("Jadi, (% v/v) digunakan saat keduanya (zat terlarut dan pelarut) diukur berdasarkan volume.")
            st.latex(r''' \% \text{v/v} = \frac{\text{zat terlarut(mL)}}{\text{zat terlarut(mL)} + \text{zat pelarut(mL)}} \times 100\% ''')
            zat_terlarut = st.number_input("Masukkan Nilai Zat Terlarut (mL)", key="zat_terlarut_vv")
            zat_pelarut = st.number_input("Masukkan Nilai Zat Pelarut (mL)", key="zat_pelarut_vv")
            hitung = st.button("Hitung Konsentrasi % v/v", key="hitung_vv")
            
            if hitung:
                konsentrasi = zat_terlarut / (zat_terlarut + zat_pelarut) * 100
                konsentrasi_formatted = round(konsentrasi, 2)
                st.success(f"Konsentrasinya adalah = {konsentrasi_formatted}% v/v")

#Halaman Hitung % b/v
        with tabs[2] :  
            st.header('Hitung Konsentrasi % b/v', divider='orange')
            st.write("Persen berat per volume (% b/v) digunakan untuk mengukur konsentrasi suatu zat berdasarkan berat zat terlarut dibandingkan dengan volume total larutan(zat terlarut + zat pelarut).")
            st.write("Jadi, (% b/v) digunakan saat zat terlarut diukur berdasarkan berat dan pelarut diukur berdasarkan volume.")
            st.latex(r''' \% \text{b/v} = \frac{\text{zat terlarut(g)}}{\text{zat terlarut(g)} + \text{zat pelarut(mL)}} \times 100\% ''')
            zat_terlarut = st.number_input("Masukkan Nilai Zat Terlarut (g)", key="zat_terlarut_bv")
            zat_pelarut = st.number_input("Masukkan Nilai Zat Pelarut (mL)", key="zat_pelarut_bv")
            hitung = st.button("Hitung Konsentrasi % b/v", key="hitung_bv")
                
            if hitung:
                konsentrasi = zat_terlarut / (zat_terlarut + zat_pelarut) * 100
                konsentrasi_formatted = round(konsentrasi, 2)
                st.success(f"Konsentrasinya adalah = {konsentrasi_formatted}% b/v")          

#Halaman Hitung Molaritas
        with tabs[3] :  
            st.header('Hitung Konsentrasi Molaritas', divider='orange')
            st.write("Molaritas didefinisikan sebagai jumlah mol zat terlarut dalam larutan.")
            st.write("Molaritas dapat digunakan untuk Menentukan konsentrasi larutan, Menyesuaikan volume larutan untuk mencapai konsentrasi yang diinginkan, dan Menghitung jumlah zat yang diperlukan untuk suatu reaksi kimia.")
            st.latex(r''' \text{Molaritas} = \frac{\text{massa(g)}}{\text{Berat Molekul(g/mol)} \times \text{Volume(L)}} ''')
            massa = st.number_input("Masukkan Jumlah Massa (g)",format="%.4f", key="massa_molaritas")
            bm = st.number_input("Masukkan Nilai Berat Molekul (g/mol)", key="bm_molaritas")
            volume = st.number_input("Masukkan Jumlah Volume (L)",format="%.4f", key="volume_molaritas")
            hitung = st.button("Hitung Konsentrasi Molaritas", key="hitung_molaritas")
        
            if hitung:            
                konsentrasi = massa / (bm * volume)
                konsentrasi_formatted = round(konsentrasi, 4)
                st.success(f"Konsentrasinya adalah = {konsentrasi_formatted} mol/L")    

 #Halaman Hitung Normalitas
        with tabs[4] :
            st.header('Hitung Konsentrasi Normalitas', divider='orange')
            st.write("Normalitas didefinisikan sebbagai jumlah ekivalen zat terlarut dalam larutan.")
            st.write("Normalitas dapat digunakan untuk Menentukan konsentrasi larutan dalam reaksi asam-basa, Mengukur kekuatan larutan oksidator atau reduktor, dan Menyesuaikan volume larutan untuk mencapai kekuatan yang diinginkan dalam reaksi redoks.")
            st.latex(r''' \text{Normalitas} = \frac{\text{massa(g)}}{\text{Berat Ekuivalen(g/grek)} \times \text{Volume(L)}} ''')
            massa = st.number_input("Masukkan Jumlah Massa (g)",format="%.4f", key="massa_normalitas")    
            be = st.number_input("Masukkan Nilai Berat Ekuivalen (g/grek)", key="be_normalitas")
            volume = st.number_input("Masukkan Jumlah Volume (L)",format="%.4f", key="volume_normalitas")
            hitung = st.button("Hitung Konsentrasi Normalitas", key="hitung_normalitas")
        
            if hitung:
                konsentrasi = massa / (be * volume)
                konsentrasi_formatted = round(konsentrasi, 4)
                st.success(f"Konsentrasinya adalah = {konsentrasi_formatted} grek/L")

#Halaman Hitung ppm
        with tabs[5] :
            st.header('Hitung Konsentrasi ppm', divider='orange')
            st.write("PPM adalah singkatan dari 'Parts Per Million' (Bagian Per Juta) Ini adalah satuan yang digunakan untuk mengukur konsentrasi atau jumlah keberadaan suatu zat dalam campuran, di mana satu bagian per juta mewakili 1 bagian dari 1 juta bagian total campuran.")
            st.write("ppm dapat digunakan untuk Mengukur konsentrasi logam berat dalam air minum, Mengontrol konsentrasi gas polutan dalam udara, dan Memantau tingkat zat kimia beracun dalam tanah di sekitar fasilitas industri.")
            st.latex(r''' \text{ppm} = \frac{\text{massa(mg)}}{\text{Volume(L)}} ''')
            massa = st.number_input("Masukkan Jumlah Massa (mg)", key="massa_ppm")
            volume = st.number_input("Masukkan Jumlah Volume (L)", key="volume_ppm")
            hitung = st.button("Hitung Konsentrasi ppm", key="hitung_ppm")
        
            if hitung:
                konsentrasi = massa / volume
                konsentrasi_formatted = round(konsentrasi, 2)
                st.success(f"Konsentrasinya adalah = {konsentrasi_formatted} ppm")
    
#Halaman Konvesi Satuan dalam Konsentrasi
    elif selected == 'Konversi Satuan Konsentrasi':
        tabs = st.tabs(['1. mol ➡ grek','2. Molaritas ➡ Normalitas','3. % b/b ➡ % b/v','4. % b/v ➡ ppm'])

#Halaman Konversi Satuan Konsentrasi mol ➡ grek
        with tabs[0] :
            st.header('Konversi mol ➡ grek', divider='orange')
            st.write('Konversi dari mol ke grek (berat ekuivalen) adalah konsep yang digunakan untuk menggambarkan jumlah mol suatu zat dalam hal ekuivalen (grek) berdasarkan reaksi kimia tertentu.')
            st.latex(r''' \text{grek} = {\text{mol}}\times{\text{Faktor Ekuivalen}} ''')
            mol = st.number_input("Masukkan Nilai mol (mol)", key="mol_grek")
            faktor_ekuivalen = st.number_input("Masukkan Faktor Ekuivalen ", min_value= 1, key="konstanta_grek")
            hitung = st.button("Konversi menjadi grek", key="hitung_grek")

            if hitung:
                konsentrasi = mol * faktor_ekuivalen
                konsentrasi_formatted = round(konsentrasi, 2)
                st.success(f"Jadi, {mol} mol = {konsentrasi_formatted} grek")

#Halaman Konversi Satuan Konsentrasi Molaritas ➡ Normalitas
        with tabs[1] :
            st.header('Konversi Molaritas ➡ Normalitas', divider='orange')
            st.write('Konversi dari molaritas ke normalitas dilakukan dengan mengalikan molaritas dengan faktor ekuivalen . Ini memungkinkan perubahan satuan dari jumlah zat terlarut per volume larutan dalam liter (mol/L) menjadi jumlah ekivalen zat terlarut per volume larutan dalam liter (grek/L).')
            st.latex(r''' \text{Normalitas} = {\text{Molaritas}}\times{\text{Faktor Ekuivalen}} ''')
            molaritas = st.number_input("Masukkan Nilai Molaritas (mol/L)", format="%.4f", key="molaritas_normalitas")
            faktor_ekuivalen = st.number_input("Masukkan Faktor Ekuivalen ", min_value= 1, key="fe_normalitas")
            hitung = st.button("Konversi menjadi Normalitas", key="hitung_normalitas")

            if hitung:
                konsentrasi = molaritas * faktor_ekuivalen
                konsentrasi_formatted = round(konsentrasi, 4)
                st.success(f"Jadi, {molaritas} M = {konsentrasi_formatted} N")


 #Halaman Konversi Satuan Konsentrasi % b/b ➡ % b/v
        with tabs[2] :
            st.header('Konversi % b/b ➡ % b/v', divider='orange')
            st.write('Konversi dari persentase berat per berat (% b/b) menjadi persentase berat per volume (% b/v), dapat digunakan dengan cara mengalikan berat jenis(g/mL). Ini  akan memberikan cara yang jelas dan akurat untuk mengubah basis perhitungan konsentrasi larutan dari berat ke volume.')  
            st.latex(r''' \% \text{b/v} = {\% \text{b/b}}\times{\text{Berat Jenis}} ''')
            persenbb = st.number_input("Masukkan Nilai % b/b (g/g)", key="persenbb_bv")
            bj = st.number_input("Masukkan Nilai Berat Jenis(g/mL) ", key="bj_bv")
            hitung = st.button("Konversi menjadi % b/v", key="hitung_bv")

            if hitung:
                konsentrasi = persenbb * bj
                konsentrasi_formatted = round(konsentrasi, 2)
                st.success(f"Jadi, {persenbb} % b/b = {konsentrasi_formatted} % b/v")

#Halaman Konversi Satuan Konsentrasi % b/v ➡ ppm
        with tabs[3] :
            st.header('Konversi % b/v ➡ ppm', divider='orange')
            st.write('Konversi dari % b/v ke ppm, dapat digunakan cara dengan mengalikan nilai % b/v dengan 10⁴. Ini memberikan hasil dalam bagian per juta (ppm), yang merupakan satuan yang sangat umum digunakan untuk konsentrasi zat dalam larutan.')
            st.latex(r''' \text{ppm} = {\% \text{b/v}}\times{\text{10⁴}} ''')
            persenbv = st.number_input("Masukkan Nilai % b/v (g/mL)", key="persenbv_ppm") 
            hitung = st.button("Konversi menjadi ppm", key="hitung_ppm")

            if hitung:
                konsentrasi = persenbv 
                st.success(f"Jadi, {persenbv} % b/v = {konsentrasi} x 10⁴ ppm")                   

home()
