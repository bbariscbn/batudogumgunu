import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="İyi ki Doğdun!", 
    page_icon="🎂",
    layout="centered"
)

# --- 1. MÜZİK ---
# Sayfa açılır açılmaz müziği en üstte gösteriyoruz
st.audio("kalem_cektim.mp3", format="audio/mp3")
st.write("🎵 *Fon müziğimiz hazırsa, anılara yolculuk başlasın...*")

# --- 2. GİRİŞ ---
st.balloons()
st.title("🎂 İyi ki Doğdun!")
st.markdown("### Dostluğumuzun en güzel 12 karesi...")
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
            st.warning(f"{i}.jpg dosyası bulunamadı, klasörü kontrol etmeyi unutma!")
    
    st.divider() # Her medyadan sonra bir çizgi çek

# --- 4. KAPANIŞ ---
st.success("Daha nice güzel anılar biriktirmek dileğiyle!")
st.snow() # Sayfanın sonuna bir sürpriz daha ekleyelim

if st.button("Buraya Tıkla! 📩"):

    st.info("Senin gibi bir dostun varlığı, en büyük başarı katsayısıdır. İyi ki varsın!")
