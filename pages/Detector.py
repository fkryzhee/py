import streamlit as st
import cv2
import numpy as np

st.set_page_config(
    page_title="Detector DEKETA",
    page_icon="👋",
)



# Judul dan deskripsi aplikasi
st.title("DEKETA Detector")
st.write("Aplikasi ini akan mencoba mendeteksi tanda tangan dalam gambar yang Anda unggah.")

# User input file dokumen
uploaded_file = st.file_uploader("Pilih gambar dokumen", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

if uploaded_file is not None:
    # Baca gambar
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is not None:
        # Tampilkan gambar yang diunggah
        st.image(image, caption='Gambar yang Diunggah', use_column_width=True)

        # Proses membandingkan apakah tanda tangan asli atau palsu
        # Di sini Anda harus menambahkan logika atau model deteksi tanda tangan sesuai kebutuhan Anda.

        # Misalnya, untuk contoh sederhana, kita akan melakukan deteksi kontur
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            st.success("Tanda tangan terdeteksi. Ini bisa jadi tanda tangan asli atau palsu.")
        else:
            st.warning("Tanda tangan tidak terdeteksi. Mungkin tidak ada tanda tangan dalam gambar ini.")

        # Output asli atau palsu
        # Di sini Anda harus menambahkan logika atau model deteksi tanda tangan sesuai kebutuhan Anda.
    else:
        st.error("Gambar tidak dapat dibaca. Pastikan file yang diunggah adalah gambar.")
