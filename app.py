import streamlit as st
import base64

# Sayfa Yapılandırması
st.set_page_config(page_title="İyi ki Doğdun!", page_icon="🎂")

# Müziği arka plana gömme fonksiyonu
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # 'autoplay' ve 'loop' aktif, controls kapalı (sayaç yok)
        md = f"""
            <audio autoplay="true" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# --- SÜRPRİZ BAŞLATICI ---
if 'started' not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:
    st.title("🎂 Senin İçin Bir Sürprizim Var!")
    st.write("Hazırsan aşağıdaki butona tıkla ve sesi açmayı unutma!")
    if st.button("Sürprizi Başlat ✨"):
        st.session_state.started = True
        st.rerun() # Sayfayı yenileyip içeriği ve müziği başlatır
else:
    # Müzik burada başlıyor (Kullanıcı tıkladığı için tarayıcı artık izin veriyor)
    try:
        play_audio("kalem_cektim.mp3")
    except:
        st.error("Müzik dosyası yüklenemedi.")

    # --- İÇERİK BÖLÜMÜ ---
    st.balloons()
    st.title("🎂 İyi ki Doğdun!")
    st.markdown("### Dostluğumuzun en güzel 12 karesi...")
    
    medya_yolu = "medya/"
    for i in range(1, 13):
        if i == 9:
            video_dosyasi = f"{medya_yolu}9.mp4"
            try:
                st.video(video_dosyasi)
            except:
                st.error("9.mp4 bulunamadı.")
        else:
            foto_dosyasi = f"{medya_yolu}{i}.jpeg"
            try:
                st.image(foto_dosyasi, use_container_width=True, caption=f"Anı #{i}")
            except:
                st.warning(f"{i}.jpeg bulunamadı.")
        st.divider()

    st.success("Nice mutlu yıllara!")
    st.snow()
