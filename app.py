import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="SabaqAI.pk", page_icon="📚")
st.title("📚 SabaqAI.pk - Urdu me Samjho")

# API Key yahan se lega
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Free limit
if 'count' not in st.session_state:
    st.session_state.count = 0

st.sidebar.markdown("**Roz 5 Sawal FREE** ✅")
st.sidebar.markdown("Unlimited: 99 Rs/mahina")
st.sidebar.markdown("Nayapay: 03288508483")

# Pic upload
pic = st.file_uploader("Book ki pic upload karein 👇", type=["jpg","png","jpeg"])
sawal = st.text_input("Sawal likhein ya khali chhor dein")

if st.button("Samjhao"):
    if pic is None:
        st.error("Pehle pic upload karo")
    elif st.session_state.count >= 5:
        st.error("Aaj ke 5 free sawal khatam. 99 Rs me unlimited le lo. JazzCash: 0300-XXXXXXX")
    else:
        with st.spinner("Ustaad soch raha hai..."):
            img = Image.open(pic)
            prompt = f"""Is image ko dekho. Sawal: {sawal if sawal else 'Poora page samjhao'}. 
            Jawab bilkul aasan Urdu me do. 9th class ke bache ko samjhao. 
            3 points me samjhao aur 1 real life example do. 150 words me."""
            
            jawab = model.generate_content([prompt, img]).text
            st.session_state.count += 1
            st.success("Ustaad ka Jawab:")
            st.write(jawab)
            st.info(f"Aaj ke {5 - st.session_state.count} sawal baaki hain")
