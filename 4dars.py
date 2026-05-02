import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Variantlar uchun maxsus effektli dizayn (CSS)
st.markdown("""
    <style>
    /* Savol qolipi */
    .question-container {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 10px solid #4CAF50;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Variantlar uchun umumiy qoliplar */
    .option-box {
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
        border: 2px solid #eee;
        font-size: 18px;
        font-weight: 500;
        display: block;
    }

    /* To'g'ri javob effekti (Yashil yonishi) */
    .correct-option {
        background-color: #d4edda !important;
        border-color: #28a745 !important;
        color: #155724 !important;
        box-shadow: 0 0 10px rgba(40, 167, 69, 0.3);
    }

    /* Noto'g'ri javob effekti (Qizil yonishi) */
    .wrong-option {
        background-color: #f8d7da !important;
        border-color: #dc3545 !important;
        color: #721c24 !important;
        box-shadow: 0 0 10px rgba(220, 53, 69, 0.3);
    }

    /* Radio tugmalarini yashirish (faqat qoliplar qolishi uchun) */
    div[role="radiogroup"] { gap: 10px; }
    div[role="radiogroup"] > label { display: none !important; }

    /* Tugma dizayni */
    .stButton > button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'current_q_index' not in st.session_state: st.session_state.current_q_index = 0
if 'user_score' not in st.session_state: st.session_state.user_score = 0
if 'answered' not in st.session_state: st.session_state.answered = False

# --- KIRISH ---
if not st.session_state.logged_in:
    st.title("🎯 Kirish")
    u_login = st.text_input("Login:", value="Murat")
    u_pass = st.text_input("Parol:", type="password")
    if st.button("KIRISH"):
        if u_login == "Murat" and u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Xato!")

# --- MENYU ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Testni tanlang")
        
        # Barcha savollar bazasi
        ms_all = [
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
            {"q": "Inflyatsiya deganda nima tushuniladi?", "o": ["Narxlar umumiy darajasining oshishi", "Bank foiz stavkalari pasayishi", "Kredit miqdorining ko‘payishi", "Valyuta kursining pasayishi"], "a": "Narxlar umumiy darajasining oshishi"},
            {"q": "Likvidlik past bo‘lgan aktivlar nima?", "o": ["Naqd pul va depozitlar", "Davlat obligatsiyalari", "Bank foizi", "Ko‘chmas mulk, startap aksiyalari"], "a": "Ko‘chmas mulk, startap aksiyalari"},
            # ... qolgan 300 tacha savolni shu yerga fayldan to'liq joylang
        ]
        
        option = st.selectbox("Fan:", ["Moliyaviy savodxonlik", "PYTHON", "Differensial tenglamalar"])
        blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("TESTNI BOSHLASH"):
            if blok == "1-70": st.session_state.active_questions = ms_all[0:70]
            elif blok == "71-140": st.session_state.active_questions = ms_all[70:140]
            elif blok == "141-210": st.session_state.active_questions = ms_all[140:210]
            else: st.session_state.active_questions = ms_all[210:]
            
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()

    # --- TEST ISHLASH ---
    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        curr = questions[q_idx]
        
        # Natija paneli (Yuqorida)
        if st.session_state.answered:
            u_choice = st.session_state[f"r_{q_idx}"]
            if u_choice == curr['a']:
                st.markdown(f'<div style="background-color:#d4edda; color:#155724; padding:15px; border-radius:10px; margin-bottom:15px; font-weight:bold; text-align:center;">✅ TO‘G‘RI JAVOB!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="background-color:#f8d7da; color:#721c24; padding:15px; border-radius:10px; margin-bottom:15px; font-weight:bold; text-align:center;">❌ NOTO‘G‘RI! To‘g‘ri javob: {curr["a"]}</div>', unsafe_allow_html=True)

        # Savol qutisi
        st.markdown(f"""
            <div class="question-container">
                <div style="color:#888; font-size:14px;">Savol {q_idx + 1} / {len(questions)}</div>
                <div style="font-size:22px; font-weight:700;">{curr['q']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        def on_click_check():
            if st.session_state[f"r_{q_idx}"] is not None:
                st.session_state.answered = True
                if st.session_state[f"r_{q_idx}"] == curr['a']:
                    st.session_state.user_score += 1

        # Variantlarni chiqarish
        for option in curr['o']:
            # Effektlarni hisoblash
            css_class = "option-box"
            if st.session_state.answered:
                if option == curr['a']:
                    css_class += " correct-option"
                elif option == st.session_state.get(f"r_{q_idx}") and option != curr['a']:
                    css_class += " wrong-option"
            
            st.markdown(f'<div class="{css_class}">{option}</div>', unsafe_allow_html=True)

        # Radio (yashirin) orqali tanlovni qabul qilish
        ans = st.radio("Tanlang:", curr['o'], index=None, key=f"r_{q_idx}", 
                       on_change=on_click_check, disabled=st.session_state.answered, label_visibility="collapsed")
        
        # Boshqaruv tugmalari
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.answered:
                if st.button("Keyingi ➔"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        with col2:
            if st.button("🏠 Bosh sahifa"):
                for k in ['test_started','current_q_index','user_score','active_questions','answered']:
                    if k in st.session_state: del st.session_state[k]
                st.rerun()
