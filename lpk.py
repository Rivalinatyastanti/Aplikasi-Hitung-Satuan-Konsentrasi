import streamlit as st

# Navigasi sidebar menggunakan st.selectbox
selected = st.sidebar.selectbox('',
    ('Hitung Satuan Konsentrasi',
     'Hitung Konsentrasi % b/b',
     'Hitung Konsentrasi % v/v',
     'Hitung Konsentrasi % b/v',
     'Hitung Konsentrasi Molaritas',
     'Hitung Konsentrasi Normalitas',
     'Hitung Konsentrasi PPM'),
    index=0)

# Halaman Perkenalan
if selected == 'Hitung Satuan Konsentrasi':
    st.header('Aplikasi Hitung Satuan Konsentrasi',divider='rainbow')
    st.header('Anggota Kelompok 5')
    st.write('1. Amirah Alifah Adilah(2360069) \n',
             '2. Irda Ananthi Rahmatika(2360148) \n',
             '3. Muhammad Atilla Devito(2360182)\n',
             '4. Putri Ayu Salsabila(2360225) \n',
             '5. Rivalina Tyastanti(2360244)')
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

# Halaman hitung konsentrasi % b/b
if selected == 'Hitung Konsentrasi % b/b':
    st.header('Hitung Konsentrasi % b/b',divider='blue')

    zatterlarut = st.number_input("Masukkan Nilai Zat Terlarut (g)")
    zatpelarut = st.number_input("Masukkan Nilai Zat Pelarut (g)")
    hitung = st.button("Hitung Konsentrasi % b/b")

    if hitung:
        konsentrasi = zatterlarut / (zatterlarut + zatpelarut) * 100
        konsentrasi_formated = round(konsentrasi, 2)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}% b/b")

# Halaman hitung konsentrasi % v/v
if selected == 'Hitung Konsentrasi % v/v':
    st.header('Hitung Konsentrasi % v/v',divider='blue')

    zatterlarut = st.number_input("Masukkan Nilai Zat Terlarut (mL)")
    zatpelarut = st.number_input("Masukkan Nilai Zat Pelarut (mL)")
    hitung = st.button("Hitung Konsentrasi % v/v")

    if hitung:
        konsentrasi = zatterlarut / (zatterlarut + zatpelarut) * 100
        konsentrasi_formated = round(konsentrasi, 2)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}% v/v")

# Halaman hitung konsentrasi % b/v
if selected == 'Hitung Konsentrasi % b/v':
    st.header('Hitung Konsentrasi % b/v',divider='blue')

    zatterlarut = st.number_input("Masukkan Nilai Zat Terlarut (g)")
    zatpelarut = st.number_input("Masukkan Nilai Zat Pelarut (mL)")
    hitung = st.button("Hitung Konsentrasi % b/v")

    if hitung:
        konsentrasi = zatterlarut / (zatterlarut + zatpelarut) * 100
        konsentrasi_formated = round(konsentrasi, 2)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated}% b/v")

# Halaman hitung konsentrasi molaritas
if selected == 'Hitung Konsentrasi Molaritas':
    st.header('Hitung Konsentrasi Molaritas',divider='blue')

    massa = st.number_input("Masukkan Jumlah Massa (g)")
    bm = st.number_input("Masukkan Nilai BM (g/mol)")
    volume = st.number_input("Masukkan Jumlah Volume (L)")
    hitung = st.button("Hitung Konsentrasi Molaritas")

    if hitung:
        konsentrasi = massa / (bm * volume)
        konsentrasi_formated = round(konsentrasi, 4)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated} mol/L")

# Halaman hitung konsentrasi normalitas
if selected == 'Hitung Konsentrasi Normalitas':
    st.header('Hitung Konsentrasi Normalitas',divider='blue')

    massa = st.number_input("Masukkan Jumlah Massa (g)")
    be = st.number_input("Masukkan Nilai BE (g/grek)")
    volume = st.number_input("Masukkan Jumlah Volume (L)")
    hitung = st.button("Hitung Konsentrasi Normalitas")

    if hitung:
        konsentrasi = massa / (be * volume)
        konsentrasi_formated = round(konsentrasi, 4)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated} grek/L")

# Halaman hitung konsentrasi PPM
if selected == 'Hitung Konsentrasi PPM':
    st.header('Hitung Konsentrasi PPM',divider='blue')

    massa = st.number_input("Masukkan Jumlah Massa (mg)")
    volume = st.number_input("Masukkan Jumlah Volume (L)")
    hitung = st.button("Hitung Konsentrasi PPM")

    if hitung:
        konsentrasi = massa / volume
        konsentrasi_formated = round(konsentrasi, 2)
        st.success(f"Konsentrasinya adalah = {konsentrasi_formated} ppm")