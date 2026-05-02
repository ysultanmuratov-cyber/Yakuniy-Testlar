import streamlit as st
import random

# Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# Maxsus dizayn (CSS) - Telefon uchun moslashtirilgan
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    /* Savol qolipi */
    .question-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        border-top: 12px solid #4CAF50;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    .question-info {
        color: #888;
        font-size: 18px;
        margin-bottom: 10px;
        font-weight: 500;
    }
    .question-text {
        font-size: 26px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        line-height: 1.4;
    }
    /* Variantlarni kattalashtirish va bosishga qulay qilish */
    .stRadio > label {
        display: none; /* Radio labelni yashirish */
    }
    div[role="radiogroup"] {
        gap: 15px;
    }
    /* Natija qoliplari */
    .result-correct {
        background-color: #d4edda;
        color: #155724;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #c3e6cb;
        margin-top: 15px;
        font-size: 22px;
        font-weight: bold;
    }
    .result-wrong {
        background-color: #f8d7da;
        color: #721c24;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #f5c6cb;
        margin-top: 15px;
        font-size: 22px;
        font-weight: bold;
    }
    /* Keyingi savol tugmasi */
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        border-radius: 15px;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 1. FOYDALANUVCHILAR BAZASI
users_db = {"Murat": "12062006"}

# Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'current_q_index' not in st.session_state: st.session_state.current_q_index = 0
if 'user_score' not in st.session_state: st.session_state.user_score = 0
if 'answered' not in st.session_state: st.session_state.answered = False

# --- KIRISH OYNASI ---
if not st.session_state.logged_in:
    st.title("🎯 Tizimga Kirish")
    user_login = st.text_input("Login:", placeholder="Ismingizni yozing...")
    user_password = st.text_input("Parol:", type="password", placeholder="Parolingizni yozing...")

    if st.button("KIRISH"):
        if user_login in users_db and users_db[user_login] == user_password:
            st.session_state.logged_in = True
            st.session_state.current_user = user_login
            st.rerun()
        else:
            st.error("Login yoki parol xato!")

# --- ASOSIY OYNA ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Testni tanlang")
        option = st.selectbox("Fan:", ["PYTHON", "Differensial tenglamalar", "Moliyaviy savodxonlik"])
        
        if option == "Moliyaviy savodxonlik":
            blok_choice = st.radio("Test bloki (300 tacha savol):", 
                                  ["1-70 gacha", "71-140 gacha", "141-210 gacha", "211-dan oxirigacha"])
        
        if st.button("TESTNI BOSHLASH"):
            # TO'LIQ SAVOLLAR BAZASI (Fayldagi barcha savollar asosida)
            ms_questions = [
                {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
                {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
                {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"},
                {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
                {"q": "Qaysi holatda shaxsiy byudjet “musbat” hisoblanadi?", "o": ["Daromadlar xarajatlardan ko‘p bo‘lsa", "Xarajatlar daromaddan ko‘p bo‘lsa", "Daromad va xarajat teng bo‘lsa", "Kredit olinsa"], "a": "Daromadlar xarajatlardan ko‘p bo‘lsa"},
                {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
                {"q": "Likvidlik past bo‘lgan aktivlar nima?", "o": ["Naqd pul va depozitlar", "Davlat obligatsiyalari", "Bank foizi", "Ko‘chmas mulk, startap aksiyalari"], "a": "Ko‘chmas mulk, startap aksiyalari"},
                # ... BU YERGA BARCHA 300 TA SAVOLNI JOYLASHTIRASIZ ...[cite: 1]
            ]
            
            if option == "PYTHON": selected_qs = ms_questions[0:10] # PYTHON namunasi
            elif option == "Differensial tenglamalar": selected_qs = ms_questions[0:10] # DIFF namunasi
            else:
                if blok_choice == "1-70 gacha": selected_qs = ms_questions[0:70]
                elif blok_choice == "71-140 gacha": selected_qs = ms_questions[70:140]
                elif blok_choice == "141-210 gacha": selected_qs = ms_questions[140:210]
                else: selected_qs = ms_questions[210:]
            
            random.shuffle(selected_qs)
            st.session_state.active_questions = selected_qs
            st.session_state.test_started = True
            st.rerun()

    else:
        q_idx = st.session_state.current_q_index
        total_qs = len(st.session_state.active_questions)
        
        if q_idx < total_qs:
            current_q = st.session_state.active_questions[q_idx]
            
            # Savol dizayni
            st.markdown(f"""
                <div class="question-box">
                    <div class="question-info">Savol {q_idx + 1} / {total_qs}</div>
                    <div class="question-text">{current_q['q']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Avtomatik tekshirish funksiyasi[cite: 1]
            def auto_check():
                if st.session_state[f"q_{q_idx}"] is not None:
                    st.session_state.answered = True
                    if st.session_state[f"q_{q_idx}"] == current_q['a']:
                        st.session_state.user_score += 1

            # Variantlar - Kattaroq va telefon uchun qulay
            st.write("### Javobni tanlang:")
            ans = st.radio("Javoblar", current_q['o'], 
                           index=None, key=f"q_{q_idx}", 
                           on_change=auto_check, 
                           disabled=st.session_state.answered,
                           label_visibility="collapsed")
            
            # Natijani ko'rsatish
            if st.session_state.answered:
                user_choice = st.session_state[f"q_{q_idx}"]
                if user_choice == current_q['a']:
                    st.markdown(f'<div class="result-correct">✅ TO\'G\'RI: {current_q["a"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="result-wrong">❌ NOTO\'G\'RI! <br> To\'g\'ri javob: {current_q["a"]}</div>', unsafe_allow_html=True)
                
                st.write("")
                if st.button("KEYINGI SAVOL ➔"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.balloons()
            st.title("🏁 Test tugadi!")
            st.metric("Natija", f"{st.session_state.user_score} / {total_qs}")
            if st.button("BOSH MENYUGA QAYTISH"):
                for key in ['test_started', 'current_q_index', 'user_score', 'active_questions', 'answered']:
                    if key in st.session_state: del st.session_state[key]
                st.rerun()
