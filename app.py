import streamlit as st
import base64

# Sayfa Yapılandırması
st.set_page_config(
    page_title="İyi ki Doğdun!", 
    page_icon="🎂",
    layout="centered"
)

# --- MÜZİK OTOMATİK OYNATMA FONKSİYONU ---
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        # HTML kodunda 'autoplay' ekliyoruz, 'controls' eklemiyoruz (sayaç gözükmez)
        md = f"""
            <audio autoplay="true" style="display:none;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# Müziği arka planda başlat (Sayaç ve buton gözükmez)
try:
    autoplay_audio("kalem_cektim.mp3")
except:
    pass # Dosya yoksa hata vermesin

# --- 2. GİRİŞ ---
st.balloons()
st.title("🎂 İyi ki Doğdun!")
st.markdown("### Dostluğumuzun en güzel 12 karesi...")
st.write("🎵 *Anılarımıza yolculuk başlasın...*")
st.divider()

# --- 3. MEDYA GALERİSİ ---
medya_yolu = "medya/"

for i in range(1, 13):
    if i == 9:
        # 9. Dosya Video (MP4)
        video_dosyasi = f"{medya_yolu}9.mp4"
        try:
            st.video(video_dosyasi)
            st.caption("🎥 Özel Anı: Video #9")
        except:
            st.error(f"9.mp4 dosyası bulunamadı!")
    else:
        # Diğer dosyalar JPEG
        foto_dosyasi = f"{medya_yolu}{i}.jpeg"
        try:
            st.image(foto_dosyasi, use_container_width=True, caption=f"Anı #{i}")
        except:
            st.warning(f"{i}.jpeg dosyası bulunamadı!")
    
    st.divider()

# --- 4. KAPANIŞ ---
st.success("Daha nice güzel anılar biriktirmek dileğiyle!")
st.snow()

if st.button("Buraya Tıkla! 📩"):
    st.info("Senin gibi bir dostun varlığı, en büyük başarı katsayısıdır. İyi ki varsın!")
