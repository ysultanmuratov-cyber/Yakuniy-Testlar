import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Telefon uchun maxsus dizayn (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    
    /* Savol qolipi */
    .question-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-top: 10px solid #4CAF50;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    .question-text {
        font-size: 22px !important;
        font-weight: 700 !important;
        color: #1a1a1a;
    }

    /* Natija xabari savol ustida */
    .res-header {
        padding: 15px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
        text-align: center;
    }
    .correct-header { background-color: #d4edda; color: #155724; border: 2px solid #c3e6cb; }
    .wrong-header { background-color: #f8d7da; color: #721c24; border: 2px solid #f5c6cb; }

    /* Variantlar (Katta qutilar) */
    div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        border: 2px solid #eee !important;
        padding: 15px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        width: 100% !important;
    }
    
    div[role="radiogroup"] [data-checked="true"] {
        border-color: #4CAF50 !important;
        background-color: #f1f8f1 !important;
    }

    .stRadio p { font-size: 18px !important; }

    /* Tugmalar */
    .stButton > button {
        width: 100%;
        height: 50px;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 10px !important;
    }
    .home-btn > button {
        background-color: #6c757d !important;
        color: white !important;
        margin-top: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'current_q_index' not in st.session_state: st.session_state.current_q_index = 0
if 'user_score' not in st.session_state: st.session_state.user_score = 0
if 'answered' not in st.session_state: st.session_state.answered = False

# --- KIRISH OYNASI ---
if not st.session_state.logged_in:
    st.title("🎯 Testlar Markazi")
    u_login = st.text_input("Login:", value="Murat")
    u_pass = st.text_input("Parol:", type="password")
    if st.button("KIRISH"):
        if u_login == "Murat" and u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Login yoki parol xato!")

# --- ASOSIY MENYU ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Bo'limni tanlang")
        
        # Barcha 300 tacha savollar bazasi
        ms_all = [
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"}, #[cite: 1]
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"}, #[cite: 1]
            {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"}, #[cite: 1]
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"}, #[cite: 1]
            {"q": "Qaysi holatda shaxsiy byudjet “musbat” hisoblanadi?", "o": ["Daromadlar xarajatlardan ko‘p bo‘lsa", "Xarajatlar daromaddan ko‘p bo‘lsa", "Daromad va xarajat teng bo‘lsa", "Kredit olinsa"], "a": "Daromadlar xarajatlardan ko‘p bo‘lsa"}, #[cite: 1]
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"}, #[cite: 1]
            {"q": "Likvidlik past bo‘lgan aktivlar nima?", "o": ["Naqd pul va depozitlar", "Davlat obligatsiyalari", "Bank foizi", "Ko‘chmas mulk, startap aksiyalari"], "a": "Ko‘chmas mulk, startap aksiyalari"}, #[cite: 1]
            # ... qolgan 300 ta savolni shu yerga fayldan to'liq ko'chirib o'tkazing[cite: 1]
        ]
        
        option = st.selectbox("Fan:", ["Moliyaviy savodxonlik", "PYTHON", "Differensial tenglamalar"])
        blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("🚀 BOSHLASH"):
            if blok == "1-70": st.session_state.active_questions = ms_all[0:70]
            elif blok == "71-140": st.session_state.active_questions = ms_all[70:140]
            elif blok == "141-210": st.session_state.active_questions = ms_all[140:210]
            else: st.session_state.active_questions = ms_all[210:]
            
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()

    # --- TEST JARAYONI ---
    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        
        if q_idx < len(questions):
            curr = questions[q_idx]
            
            # 1. Natija (Savolning ustida chiqadi)
            if st.session_state.answered:
                u_choice = st.session_state[f"r_{q_idx}"]
                if u_choice == curr['a']:
                    st.markdown(f'<div class="res-header correct-header">✅ TO\'G\'RI: {curr["a"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="res-header wrong-header">❌ NOTO\'G\'RI! To\'g\'ri javob: {curr["a"]}</div>', unsafe_allow_html=True)
            
            # 2. Savol qutisi
            st.markdown(f"""
                <div class="question-box">
                    <div style="color:#888; margin-bottom:5px;">Savol {q_idx + 1} / {len(questions)}</div>
                    <div class="question-text">{curr['q']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # 3. Javob tanlash
            def check():
                if st.session_state[f"r_{q_idx}"] is not None:
                    st.session_state.answered = True
                    if st.session_state[f"r_{q_idx}"] == curr['a']:
                        st.session_state.user_score += 1

            st.radio("Javobingiz:", curr['o'], index=None, key=f"r_{q_idx}", 
                     on_change=check, disabled=st.session_state.answered, label_visibility="collapsed")
            
            # 4. Tugmalar
            col1, col2 = st.columns(2)
            with col1:
                if st.session_state.answered:
                    if st.button("Keyingi ➔"):
                        st.session_state.current_q_index += 1
                        st.session_state.answered = False
                        st.rerun()
            with col2:
                st.markdown('<div class="home-btn">', unsafe_allow_html=True)
                if st.button("🏠 Menyuga qaytish"):
                    for k in ['test_started','current_q_index','user_score','active_questions','answered']:
                        if k in st.session_state: del st.session_state[k]
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
                
        else:
            st.balloons()
            st.success(f"Tugadi! Natija: {st.session_state.user_score} / {len(questions)}")
            if st.button("🏠 BOSH SAHIFA"):
                for k in ['test_started','current_q_index','user_score','active_questions','answered']:
                    if k in st.session_state: del st.session_state[k]
                st.rerun()
