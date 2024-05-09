import streamlit as st

#Navigasi sidebar menggunakan st.selectbox
selected = st.sidebar.selectbox('',
        ('Perkenalan Kelompok',
         'Tentang Aplikasi',
         'Hitung Konsentrasi % b/b',
         'Hitung Konsentrasi % v/v',
         'Hitung Konsentrasi % b/v',
         'Hitung Konsentrasi Molaritas',
         'Hitung Konsentrasi Normalitas',
         'Hitung Konsentrasi PPM'),
        index=0)

def home():
    #Halaman Perkenalan Kelompok
    if selected == 'Perkenalan Kelompok':
        st.image('kelompok5.jpg',output_format="auto")
        
    #Halaman Perkenalan Aplikasi
    elif selected == 'Tentang Aplikasi':
        st.header('Selamat datang di Aplikasi Hitung Konsentrasi', divider='rainbow')
        st.write('Aplikasi ini memungkinkan Anda untuk menghitung berbagai satuan konsentrasi larutan.')
        st.header('Tentang Aplikasi')
        st.write('Konsentrasi larutan adalah jumlah zat yang terlarut dalam setiap satuan larutan atau pelarut. '
                'Secara sederhana, konsentrasi larutan dapat memberikan gambaran atau sebuah informasi '
                'tentang perbandingan jumlah zat terlarut dan jumlah pelarutnya.')
        st.write('Satuan-satuan Konsentrasi yang disediakan : \n',
                 '1. % b/b \n',
                '2. % v/v \n',
                '3. % b/v \n',
                '4. Molaritas \n',
                '5. Normalitas \n',
                '6. PPM ')

    #Halaman Hitung % b/b
    elif selected == 'Hitung Konsentrasi % b/b':
        st.header('Hitung Konsentrasi % b/b', divider='blue')
        zat_terlarut = st.number_input("Masukkan Nilai Zat Terlarut (g)",format="%.4f")
        zat_pelarut = st.number_input("Masukkan Nilai Zat Pelarut (g)",format="%.4f")
        hitung = st.button("Hitung Konsentrasi % b/b")
        
        if hitung:
            konsentrasi = zat_terlarut / (zat_terlarut + zat_pelarut) * 100
            konsentrasi_formatted = round(konsentrasi, 2)
            st.success(f"Konsentrasinya adalah = {konsentrasi_formatted}% b/b")
    
    #Halaman Hitung % v/v
    elif selected == 'Hitung Konsentrasi % v/v':
        st.header('Hitung Konsentrasi % v/v', divider='blue')
        zat_terlarut = st.number_input("Masukkan Nilai Zat Terlarut (mL)",format="%.4f")
        zat_pelarut = st.number_input("Masukkan Nilai Zat Pelarut (mL)",format="%.4f")
        hitung = st.button("Hitung Konsentrasi % v/v")
        
        if hitung:
            konsentrasi = zat_terlarut / (zat_terlarut + zat_pelarut) * 100
            konsentrasi_formatted = round(konsentrasi, 2)
            st.success(f"Konsentrasinya adalah = {konsentrasi_formatted}% v/v")

    #Halaman Hitung % b/v        
    elif selected == 'Hitung Konsentrasi % b/v':
        st.header('Hitung Konsentrasi % b/v', divider='blue')
        zat_terlarut = st.number_input("Masukkan Nilai Zat Terlarut (g)",format="%.4f")
        zat_pelarut = st.number_input("Masukkan Nilai Zat Pelarut (mL)",format="%.4f")
        hitung = st.button("Hitung Konsentrasi % b/v")
        
        if hitung:
            konsentrasi = zat_terlarut / (zat_terlarut + zat_pelarut) * 100
            konsentrasi_formatted = round(konsentrasi, 2)
            st.success(f"Konsentrasinya adalah = {konsentrasi_formatted}% b/v")

    #Halaman Hitung Molaritas        
    elif selected == 'Hitung Konsentrasi Molaritas':
        st.header('Hitung Konsentrasi Molaritas', divider='blue')
        massa = st.number_input("Masukkan Jumlah Massa (g)",format="%.4f")
        bm = st.number_input("Masukkan Nilai BM (g/mol)",format="%.4f")
        volume = st.number_input("Masukkan Jumlah Volume (L)",format="%.4f")
        hitung = st.button("Hitung Konsentrasi Molaritas")
        
        if hitung:            
            konsentrasi = massa / (bm * volume)
            konsentrasi_formatted = round(konsentrasi, 4)
            st.success(f"Konsentrasinya adalah = {konsentrasi_formatted} mol/L")            

    #Halaman Hitung Normalitas        
    elif selected == 'Hitung Konsentrasi Normalitas':
        st.header('Hitung Konsentrasi Normalitas', divider='blue')
        massa = st.number_input("Masukkan Jumlah Massa (g)",format="%.4f")    
        be = st.number_input("Masukkan Nilai BE (g/grek)",format="%.4f")
        volume = st.number_input("Masukkan Jumlah Volume (L)",format="%.4f")
        hitung = st.button("Hitung Konsentrasi Normalitas")
        
        if hitung:
            konsentrasi = massa / (be * volume)
            konsentrasi_formatted = round(konsentrasi, 4)
            st.success(f"Konsentrasinya adalah = {konsentrasi_formatted} grek/L")
    
    #Halaman Hitung PPM
    elif selected == 'Hitung Konsentrasi PPM':
        st.header('Hitung Konsentrasi PPM', divider='blue')
        massa = st.number_input("Masukkan Jumlah Massa (mg)",format="%.4f")
        volume = st.number_input("Masukkan Jumlah Volume (L)",format="%.4f")
        hitung = st.button("Hitung Konsentrasi PPM")
        
        if hitung:
            konsentrasi = massa / volume
            konsentrasi_formatted = round(konsentrasi, 2)
            st.success(f"Konsentrasinya adalah = {konsentrasi_formatted} ppm")

home()
