import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Quiz Bot Style", layout="centered")

# 2. Telegram Quiz dizayni (CSS) - Faqat kerakli elementlar qoldirildi
st.markdown("""
    <style>
    /* Umumiy fon kulrang */
    .stApp { background-color: #e6ebf0; }
    
    /* Barcha elementlarni o'rab turuvchi yagona oq karta */
    .quiz-card {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        max-width: 500px;
        margin: 20px auto;
    }
    
    /* Savol sarlavhasi */
    .question-header {
        font-weight: bold;
        font-size: 18px;
        color: #000;
        margin-bottom: 20px;
    }

    /* Radio variantlar orasidagi masofa */
    div[role="radiogroup"] label {
        padding: 12px 0 !important;
        border-bottom: 1px solid #f8f8f8;
    }

    /* Natija foizlari dizayni */
    .stat-row {
        margin-bottom: 18px;
    }
    .label-row {
        display: flex;
        justify-content: space-between;
        margin-bottom: 6px;
        font-size: 16px;
        color: #333;
    }
    .bar-bg {
        height: 8px;
        background-color: #f0f2f5;
        border-radius: 4px;
        width: 100%;
    }
    .bar-fill { height: 100%; border-radius: 4px; transition: width 0.5s; }

    /* "Keyingi" tugmasi dizayni */
    .stButton button {
        background-color: #0088cc !important;
        color: white !important;
        border-radius: 8px !important;
        width: 100%;
        height: 45px;
        font-weight: bold;
        border: none;
        margin-top: 10px;
    }
    
    /* Ortiqcha oq tugma chiqishining oldini olish */
    div.stSelectbox, div.stTextInput, div.stMultiSelect { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatni saqlash
if 'answered' not in st.session_state: st.session_state.answered = False

# --- ASOSIY KARTA ---
st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

# Savol matni
st.markdown('<div class="question-header">[1/1] Kredit stavkasi nima?</div>', unsafe_allow_html=True)

options = ["Daromad solig'i", "Kredit berish narxi", "Kredit miqdori", "Bank balansidagi mablag'"]
correct_ans = "Kredit berish narxi"

# JAVOB BERILMAGAN HOLAT
if not st.session_state.answered:
    # Radio tugmalar yordamida tanlov (oq tugmalarsiz toza variantlar)
    choice = st.radio("", options, index=None, key="quiz_opt", label_visibility="collapsed")
    
    if choice:
        st.session_state.answered = True
        st.session_state.user_choice = choice
        st.rerun()

# JAVOB BERILGAN HOLAT
else:
    for opt in options:
        is_correct = (opt == correct_ans)
        is_user_choice = (opt == st.session_state.user_choice)
        
        # Telegram uslubidagi foizlar
        percent = 100 if is_correct else 0
        fill_color = "#4CAF50" if is_correct else "#e0e0e0"
        
        # Belgi qo'shish (To'g'ri bo'lsa qushcha, xato bo'lsa krestik)
        icon = ""
        if is_correct: icon = "✔️"
        elif is_user_choice: icon = "❌"
        
        st.markdown(f"""
            <div class="stat-row">
                <div class="label-row">
                    <span>{opt} {icon}</span>
                    <span>{percent}%</span>
                </div>
                <div class="bar-bg">
                    <div class="bar-fill" style="width: {percent}%; background-color: {fill_color};"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    if st.button("Keyingi savol ➔"):
        st.session_state.answered = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Karta yopilishi
