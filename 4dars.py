import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Optimal dizayn (CSS) - Variantlar jipslashgan va rangli effektli
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    
    /* Savol qolipi */
    .question-container {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 8px solid #4CAF50;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    
    /* Variant tugmalari - Yopishgan va to'liq kenglikda */
    div.stButton > button {
        width: 100% !important;
        text-align: left !important;
        padding: 12px 20px !important;
        border-radius: 0px !important;
        border: 0.5px solid #eee !important;
        background-color: white !important;
        color: #333 !important;
        font-size: 17px !important;
        margin-bottom: -10px !important;
        display: block !important;
    }
    
    /* Elementlar orasidagi masofani yo'qotish */
    .stElementContainer { margin-bottom: -10px !important; }

    /* To'g'ri javob foni yashil */
    .correct-btn button {
        background-color: #d4edda !important;
        border-color: #28a745 !important;
        color: #155724 !important;
        font-weight: bold !important;
    }

    /* Noto'g'ri javob foni qizil */
    .wrong-btn button {
        background-color: #f8d7da !important;
        border-color: #dc3545 !important;
        color: #721c24 !important;
    }
    
    /* Navigatsiya tugmalari */
    .nav-btn button { 
        height: 50px !important; 
        margin-top: 25px !important; 
        border-radius: 10px !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'current_q_index' not in st.session_state: st.session_state.current_q_index = 0
if 'user_score' not in st.session_state: st.session_state.user_score = 0
if 'answered' not in st.session_state: st.session_state.answered = False
if 'selected_option' not in st.session_state: st.session_state.selected_option = None

# --- KIRISH ---
if not st.session_state.logged_in:
    st.title("🎯 Kirish")
    u_pass = st.text_input("Parol:", type="password", placeholder="12062006")
    if st.button("KIRISH"):
        if u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Parol xato!")

# --- TEST MENYUSI ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Test blokini tanlang")
        
        # --- BARCHA SAVOLLAR BAZASI ---
        # Bu yerda 300 ta savol bo'lishi kerak. Men namunani ko'paytirib berdim
        ms_all = [
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
            {"q": "Aktivlar nima?", "o": ["Qarzlar", "Shaxsiy mulk", "Soliqlar", "Xarajatlar"], "a": "Shaxsiy mulk"},
            {"q": "Inflyatsiya nima?", "o": ["Narxlar oshishi", "Foiz tushishi", "Kredit kamayishi", "Eksport ortishi"], "a": "Narxlar oshishi"},
            {"q": "Likvidlik nima?", "o": ["Pulning qadri", "Aktivning tez naqd pulga aylanishi", "Bank qarzi", "Soliq imtiyozi"], "a": "Aktivning tez naqd pulga aylanishi"},
            {"q": "Dividend nima?", "o": ["Ish haqi", "Aksiya bo‘yicha olinadigan foyda", "Bank foizi", "Kredit turi"], "a": "Aksiya bo‘yicha olinadigan foyda"},
            # --- SHU YERDAN BOSHLAB QOLGAN SAVOLLARNI NUSXALAB QO'SHASIZ ---
        ]
        
        # Agar savollaringiz soni 300 taga yetmasa, bloklar bo'sh qolmasligi uchun 
        # testni blok tanlamasdan hamma savollarni chiqaradigan qilib sozlash mumkin.
        blok = st.radio("Blokni tanlang:", ["1-70", "71-140", "141-210", "211-300", "Hamma savollar"])
        
        if st.button("🚀 BOSHLASH"):
            if blok == "1-70": st.session_state.active_questions = ms_all[0:70]
            elif blok == "71-140": st.session_state.active_questions = ms_all[70:140]
            elif blok == "141-210": st.session_state.active_questions = ms_all[140:210]
            elif blok == "211-300": st.session_state.active_questions = ms_all[210:300]
            else: st.session_state.active_questions = ms_all # Bor hamma savollar
            
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()

    # --- TEST JARAYONI ---
    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        
        if q_idx < len(questions):
            curr = questions[q_idx]
            
            if st.session_state.answered:
                if st.session_state.selected_option == curr['a']:
                    st.success("✅ TO'G'RI JAVOB!")
                else:
                    st.error(f"❌ NOTO'G'RI! To'g'ri: {curr['a']}")

            st.markdown(f"""
                <div class="question-container">
                    <div style="color:#888; font-size:13px; margin-bottom:5px;">Savol {q_idx + 1} / {len(questions)}</div>
                    <div style="font-size:20px; font-weight:700;">{curr['q']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            for option in curr['o']:
                btn_class = "<div>"
                if st.session_state.answered:
                    if option == curr['a']: btn_class = '<div class="correct-btn">'
                    elif option == st.session_state.selected_option: btn_class = '<div class="wrong-btn">'
                
                st.markdown(btn_class, unsafe_allow_html=True)
                if st.button(option, key=f"btn_{option}_{q_idx}", disabled=st.session_state.answered):
                    st.session_state.answered = True
                    st.session_state.selected_option = option
                    if option == curr['a']: st.session_state.user_score += 1
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                if st.session_state.answered:
                    if st.button("Keyingi ➔"):
                        st.session_state.current_q_index += 1
                        st.session_state.answered = False
                        st.session_state.selected_option = None
                        st.rerun()
            with col2:
                if st.button("🏠 Menyuga"):
                    for k in ['test_started','current_q_index','user_score','active_questions','answered','selected_option']:
                        if k in st.session_state: del st.session_state[k]
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.balloons()
            st.success(f"🏁 Tugadi! Natija: {st.session_state.user_score} / {len(questions)}")
            if st.button("🏠 Bosh sahifaga qaytish"):
                for k in ['test_started','current_q_index','user_score','active_questions','answered','selected_option']:
                    if k in st.session_state: del st.session_state[k]
                st.rerun()
