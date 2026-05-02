import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Quiz Bot Style", layout="centered")

# 2. Telegram uslubidagi TOZA dizayn (CSS)
st.markdown("""
    <style>
    /* Umumiy fon */
    .stApp { background-color: #e6ebf0; }
    
    /* Streamlit'ning hamma ortiqcha elementlarini yashirish */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 2rem;}

    /* Quiz kartasi */
    .quiz-container {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        max-width: 450px;
        margin: auto;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    .q-header {
        font-weight: 700;
        font-size: 17px;
        color: #000;
        margin-bottom: 20px;
    }

    /* Variantlar dizayni */
    .option-row {
        display: flex;
        align-items: center;
        padding: 12px 0;
        border-bottom: 1px solid #f2f2f2;
        cursor: pointer;
    }
    .option-row:last-child { border-bottom: none; }
    
    .radio-circle {
        width: 20px;
        height: 20px;
        border: 2px solid #b1b1b1;
        border-radius: 50%;
        margin-right: 15px;
        flex-shrink: 0;
    }

    /* Natija foizlari va progress bar */
    .res-row { margin-bottom: 15px; }
    .res-label { display: flex; justify-content: space-between; margin-bottom: 6px; font-size: 15px; }
    .res-bar-bg { height: 6px; background-color: #f0f2f5; border-radius: 3px; width: 100%; }
    .res-bar-fill { height: 100%; border-radius: 3px; }

    /* "Keyingi" tugmasi */
    div.stButton > button {
        width: 100%;
        background-color: #0088cc !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        height: 44px;
        font-weight: 600;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatni boshqarish
if 'ans' not in st.session_state: st.session_state.ans = False

# --- ASOSIY EKRAN ---
# Barcha savollarni bitta HTML blok ichida chiqaramiz
st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
st.markdown('<div class="q-header">[1/1] Kredit stavkasi nima?</div>', unsafe_allow_html=True)

opts = ["Daromad solig'i", "Kredit berish narxi", "Kredit miqdori", "Bank balansidagi mablag'"]
corr = "Kredit berish narxi"

if not st.session_state.ans:
    # JAVOB BERILMAGAN: Variantlarni radio doirachalari bilan chizish
    # Streamlit radio'sini yashirin holda ishlatamiz
    sel = st.radio("", opts, index=None, key="q_real", label_visibility="collapsed")
    
    if sel:
        st.session_state.ans = True
        st.session_state.sel_val = sel
        st.rerun()
else:
    # JAVOB BERILGAN: Natijalarni foizli progress bar bilan chizish
    for o in opts:
        is_c = (o == corr)
        is_u = (o == st.session_state.sel_val)
        p = 100 if is_c else 0
        clr = "#4CAF50" if is_c else "#e0e0e0"
        icon = "✔️" if is_c else ("❌" if is_u else "")
        
        st.markdown(f"""
            <div class="res-row">
                <div class="res-label">
                    <span>{o} {icon}</span>
                    <span style="font-weight:600;">{p}%</span>
                </div>
                <div class="res-bar-bg">
                    <div class="res-bar-fill" style="width: {p}%; background-color: {clr};"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    if st.button("Keyingi savol ➔"):
        st.session_state.ans = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
