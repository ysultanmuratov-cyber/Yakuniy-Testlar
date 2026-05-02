import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Quiz Bot Style", layout="centered")

# 2. Telegram Quiz dizayni (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #e6ebf0; }
    
    .quiz-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        max-width: 500px;
        margin: auto;
    }
    
    .question-header {
        font-weight: bold;
        font-size: 19px;
        color: #000;
        margin-bottom: 20px;
    }

    /* Radio tugmalarni chiroyli qilish */
    div[role="radiogroup"] {
        padding: 5px;
    }
    
    div[role="radiogroup"] label {
        font-size: 17px !important;
        color: #333 !important;
        margin-bottom: 10px !important;
    }

    /* Natija foizlari (Progress Bar) */
    .stat-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 15px;
    }
    .label-row {
        display: flex;
        justify-content: space-between;
        margin-bottom: 5px;
        font-size: 16px;
    }
    .bar-bg {
        height: 10px;
        background-color: #f0f0f0;
        border-radius: 5px;
        width: 100%;
        overflow: hidden;
    }
    .bar-fill { height: 100%; border-radius: 5px; }

    /* Tugma */
    .stButton button {
        width: 100%;
        background-color: #0088cc !important;
        color: white !important;
        border-radius: 10px !important;
        height: 45px;
        font-weight: bold;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatni saqlash
if 'answered' not in st.session_state: st.session_state.answered = False

# --- QUIZ EKRANI ---
st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
st.markdown('<div class="question-header">[1/1] Kredit stavkasi nima?</div>', unsafe_allow_html=True)

options = ["Daromad solig'i", "Kredit berish narxi", "Kredit miqdori", "Bank balansidagi mablag'"]
correct_ans = "Kredit berish narxi"

# JAVOB BERILMAGAN HOLAT
if not st.session_state.answered:
    # Radio tugma faqat javob berilmaganda ko'rinadi
    choice = st.radio("Tanlang:", options, index=None, key="quiz_opt", label_visibility="collapsed")
    
    if choice:
        st.session_state.answered = True
        st.session_state.user_choice = choice
        st.rerun()

# JAVOB BERILGAN HOLAT (Natija videodagidek chiqadi)
else:
    for opt in options:
        # To'g'ri yoki noto'g'ri ekanligini aniqlash
        is_correct = (opt == correct_ans)
        is_user_choice = (opt == st.session_state.user_choice)
        
        # Foiz va ranglar
        percent = 100 if is_correct else 0
        fill_color = "#4CAF50" if is_correct else "#e0e0e0"
        text_suffix = "✔️" if is_correct else ("❌" if is_user_choice else "")
        
        st.markdown(f"""
            <div class="stat-row">
                <div class="label-row">
                    <span>{opt} {text_suffix}</span>
                    <span>{percent}%</span>
                </div>
                <div class="bar-bg">
                    <div class="bar-fill" style="width: {percent}%; background-color: {fill_color};"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("Keyingi savol ➔"):
        st.session_state.answered = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
