import streamlit as st
import time

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Quiz Bot Style", layout="centered")

# 2. Telegram Quiz dizayni (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #e6ebf0; } /* Telegram foni rangi */
    
    /* Quiz konteyneri */
    .quiz-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    
    /* Savol matni */
    .question-header {
        font-weight: bold;
        font-size: 18px;
        color: #000;
        margin-bottom: 15px;
    }

    /* Radio tugmalarni Telegram uslubiga keltirish */
    div[role="radiogroup"] label {
        padding: 10px 0;
        font-size: 16px !important;
        border-bottom: 1px solid #f0f0f0;
    }
    
    /* Natija foizlari ko'rinishi */
    .stat-row {
        display: flex;
        align-items: center;
        padding: 8px 0;
        font-size: 15px;
    }
    .progress-bar {
        height: 8px;
        border-radius: 4px;
        background-color: #f0f0f0;
        flex-grow: 1;
        margin: 0 10px;
        overflow: hidden;
    }
    .progress-fill { height: 100%; border-radius: 4px; }
    
    /* Tugmalar */
    .stButton button {
        background-color: #0088cc !important; /* Telegram ko'k rangi */
        color: white !important;
        border-radius: 8px !important;
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatlarni boshqarish
if 'step' not in st.session_state: st.session_state.step = "start"
if 'answered' not in st.session_state: st.session_state.answered = False

# --- BOSHLANG'ICH EKRAN ---
if st.session_state.step == "start":
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.write("📋 **Moliyaviy savodxonlik 1-70**")
    st.write("1 ta savol · Har bir savol uchun 10 soniya")
    if st.button("Testni boshlash"):
        st.session_state.step = "quiz"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- TEST EKRANI ---
elif st.session_state.step == "quiz":
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.markdown('<div class="question-header">[1/1] Kredit stavkasi nima?</div>', unsafe_allow_html=True)
    
    options = ["Daromad solig'i", "Kredit berish narxi", "Kredit miqdori", "Bank balansidagi mablag'"]
    correct_ans = "Kredit berish narxi"
    
    # Videodagi kabi radio tugmalar
    choice = st.radio("", options, index=None, key="quiz_radio", disabled=st.session_state.answered, label_visibility="collapsed")
    
    if choice and not st.session_state.answered:
        st.session_state.answered = True
        st.rerun()

    # Agar javob berilgan bo'lsa, natijani foizlarda ko'rsatish (Telegram uslubida)
    if st.session_state.answered:
        st.write("---")
        for opt in options:
            percent = 100 if opt == correct_ans else 0
            color = "#4CAF50" if opt == correct_ans else "#e0e0e0"
            icon = "✔️" if opt == correct_ans else ""
            
            st.markdown(f"""
                <div class="stat-row">
                    <div style="width: 30px;">{percent}%</div>
                    <div class="progress-bar"><div class="progress-fill" style="width: {percent}%; background-color: {color};"></div></div>
                    <div>{opt} {icon}</div>
                </div>
            """, unsafe_allow_html=True)
        
        time.sleep(1)
        if st.button("Yakunlash"):
            st.session_state.step = "result"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- NATIJA EKRANI ---
elif st.session_state.step == "result":
    st.balloons()
    st.markdown('<div class="quiz-card" style="text-align: center;">', unsafe_allow_html=True)
    st.write("🏁 **Test yakunlandi!**")
    st.write("Siz 1 ta savolga javob berdingiz:")
    st.markdown("✅ To'g'ri: **1** | ❌ Xato: **0**")
    if st.button("Qaytadan urinish"):
        st.session_state.step = "start"
        st.session_state.answered = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
