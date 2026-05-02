import streamlit as st
import random

# Sahifa sozlamalari va yangi dizayn (CSS)
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .question-container {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-top: 10px solid #4CAF50;
        margin-bottom: 25px;
    }
    .question-title {
        font-size: 20px !important;
        color: #666;
        margin-bottom: 10px;
    }
    .question-text {
        font-size: 26px !important;
        font-weight: 800 !important;
        color: #1a1a1a;
        line-height: 1.4;
    }
    .stRadio > label {
        font-size: 20px !important;
        font-weight: 500 !important;
        color: #444 !important;
        padding: 10px 0px;
    }
    /* Variantlar orasidagi masofa */
    div[role="radiogroup"] {
        gap: 15px;
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
    st.title("🎯 Testlar Markaziga Kirish")
    user_login = st.text_input("Login:")
    user_password = st.text_input("Parol:", type="password")

    if st.button("Tizimga kirish"):
        if user_login in users_db and users_db[user_login] == user_password:
            st.session_state.logged_in = True
            st.session_state.current_user = user_login
            st.rerun()
        else:
            st.error("Login yoki parol xato!")

# --- ASOSIY TEST OYNASI ---
else:
    st.sidebar.write(f"👤 Foydalanuvchi: **{st.session_state.current_user}**")
    if st.sidebar.button("Chiqish"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

    if not st.session_state.test_started:
        st.title("🚀 Fanlarni tanlang")
        option = st.selectbox("Fan:", ["PYTHON", "Differensial tenglamalar", "Moliyaviy savodxonlik"])
        
        if option == "Moliyaviy savodxonlik":
            blok_choice = st.radio("Blok:", ["1-70 gacha", "71-140 gacha", "141-210 gacha", "211-300 gacha"])
        
        if st.button("Testni boshlash"):
            # Barcha 300 ta savol shu yerda[cite: 1]
            ms_all = [
                {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
                {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
                {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"},
                {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
                {"q": "Qaysi holatda shaxsiy byudjet “musbat” hisoblanadi?", "o": ["Daromadlar xarajatlardan ko‘p bo‘lsa", "Xarajatlar daromaddan ko‘p bo‘lsa", "Daromad va xarajat teng bo‘lsa", "Kredit olinsa"], "a": "Daromadlar xarajatlardan ko‘p bo‘lsa"},
                {"q": "Inflyatsiya deganda nima tushuniladi?", "o": ["Narxlar umumiy darajasining oshishi", "Bank foiz stavkalari pasayishi", "Kredit miqdorining ko‘payishi", "Valyuta kursining pasayishi"], "a": "Narxlar umumiy darajasining oshishi"},
                {"q": "Qaysi usul shaxsiy moliyaviy rejani tuzishda ishlatiladi?", "o": ["SWOT tahlil", "Budjetlash", "Marketing tahlili", "Ishlab chiqarish rejalari"], "a": "Budjetlash"},
                {"q": "Aktivlar deganda nimani tushuniladi?", "o": ["Qarzdorlik majburiyatlari", "Shaxsiy va korporativ mulk", "Faqat pul mablag‘lari", "Daromad manbalari"], "a": "Shaxsiy va korporativ mulk"},
                {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
                {"q": "Qarz olishning asosiy xavfi nima?", "o": ["Foiz stavkasi oshishi", "Pulni tejash", "Dividend olish", "Soliq to‘lash"], "a": "Foiz stavkasi oshishi"},
                # ... (Qolgan barcha savollar fayldan to'liq joylanadi)[cite: 1]
            ]
            
            # Blokni ajratish
            if option == "PYTHON":
                selected_qs = ms_all[0:10] # Namuna
            elif option == "Differensial tenglamalar":
                selected_qs = ms_all[10:20] # Namuna
            else:
                if blok_choice == "1-70 gacha": selected_qs = ms_all[0:70]
                elif blok_choice == "71-140 gacha": selected_qs = ms_all[70:140]
                elif blok_choice == "141-210 gacha": selected_qs = ms_all[140:210]
                else: selected_qs = ms_all[210:]
            
            random.shuffle(selected_qs)
            for item in selected_qs:
                item['o'] = list(item['o'])
                random.shuffle(item['o'])
            
            st.session_state.active_questions = selected_qs
            st.session_state.test_started = True
            st.rerun()

    else:
        q_idx = st.session_state.current_q_index
        total_qs = len(st.session_state.active_questions)
        
        if q_idx < total_qs:
            current_q = st.session_state.active_questions[q_idx]
            
            # Yangi dizayndagi savol qolipi (box)
            st.markdown(f"""
                <div class="question-container">
                    <div class="question-title">Savol {q_idx + 1} / {total_qs}</div>
                    <div class="question-text">{current_q['q']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Funksiya: Javob tanlanishi bilan tekshirish[cite: 1]
            def auto_check():
                if st.session_state[f"q_radio_{q_idx}"] is not None:
                    st.session_state.answered = True
                    if st.session_state[f"q_radio_{q_idx}"] == current_q['a']:
                        st.session_state.user_score += 1

            # Radio variantlar
            ans = st.radio("Javobingizni belgilang:", current_q['o'], 
                           index=None, key=f"q_radio_{q_idx}", 
                           on_change=auto_check, 
                           disabled=st.session_state.answered,
                           label_visibility="collapsed")
            
            if st.session_state.answered:
                st.write("---")
                user_choice = st.session_state[f"q_radio_{q_idx}"]
                
                # Vizual natija[cite: 1]
                for variant in current_q['o']:
                    if variant == current_q['a']:
                        st.markdown(f'<div style="background-color:#d4edda; color:#155724; padding:18px; border-radius:12px; border:2px solid #c3e6cb; margin-bottom:12px; font-size:22px;"><b>✅ To‘g‘ri javob: {variant}</b></div>', unsafe_allow_html=True)
                    elif variant == user_choice and variant != current_q['a']:
                        st.markdown(f'<div style="background-color:#f8d7da; color:#721c24; padding:18px; border-radius:12px; border:2px solid #f5c6cb; margin-bottom:12px; font-size:22px;"><b>❌ Sizning javobingiz: {variant}</b></div>', unsafe_allow_html=True)

                if st.button("Keyingi savol ➔", use_container_width=True):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.balloons()
            st.success(f"🏁 Test yakunlandi! Siz {total_qs} tadan {st.session_state.user_score} ta topdingiz.")
            if st.button("Qaytadan boshlash"):
                for key in ['test_started', 'current_q_index', 'user_score', 'active_questions', 'answered']:
                    if key in st.session_state: del st.session_state[key]
                st.rerun()
