import streamlit as st


st.set_page_config(
    page_title="DEKETA",
    page_icon="house",
)

# Judul dan deskripsi aplikasi
st.title("Thank You!")
st.write("Next, please fill in the questionnaire to help us develop a better system")

import streamlit as st

# Judul formulir
st.title("Kuesioner UI/UX Desain Web")

# Pertanyaan 1
pertanyaan_1 = st.text_area("1. Apa pendapat Anda tentang tata letak (layout) dari desain web ini?")

# Pertanyaan 2
pertanyaan_2 = st.text_area("2. Bagaimana pendapat Anda tentang penggunaan warna pada desain web ini?")

# Pertanyaan 3
pertanyaan_3 = st.text_area("3. Apakah navigasi pada desain web ini mudah dipahami dan digunakan?")

# Pertanyaan 4
pertanyaan_4 = st.text_area("4. Apakah ada elemen desain atau fitur khusus yang menarik perhatian Anda?")

# Pertanyaan 5
pertanyaan_5 = st.text_area("5. Saran atau saran perbaikan apa yang ingin Anda berikan untuk meningkatkan UI/UX desain web ini?")

# Tombol submit
if st.button("Kirim Jawaban"):
    # Simpan jawaban atau lakukan apa pun yang diinginkan dengan data formulir
    st.success("Jawaban Anda telah terkirim!")