import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Variantlar foni rangli yonishi uchun maxsus dizayn (CSS)
st.markdown("""
    <style>
    /* Asosiy fon */
    .stApp { background-color: #f8f9fa; }
    
    /* Savol qolipi */
    .question-container {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-top: 10px solid #4CAF50;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 5px;
    }
    
    /* VARIANTLARNI YOPISHTIRISH VA FONNI RANGLASH */
    div.stButton > button {
        width: 100% !important;
        text-align: left !important;
        padding: 18px 25px !important;
        border-radius: 0px !important; /* Tugmalar yopishib turishi uchun */
        border: 0.5px solid #ddd !important;
        background-color: white !important;
        color: #333 !important;
        font-size: 19px !important;
        margin: 0 !important; /* Masofani butunlay yo'qotish */
        display: block !important;
    }

    /* To'g'ri javob foni yashil yonishi */
    .correct-btn button {
        background-color: #28a745 !important; /* To'qroq yashil */
        color: white !important;
        border: 1px solid #1e7e34 !important;
        font-weight: bold !important;
    }

    /* Noto'g'ri javob foni qizil yonishi */
    .wrong-btn button {
        background-color: #dc3545 !important; /* To'qroq qizil */
        color: white !important;
        border: 1px solid #bd2130 !important;
    }

    /* Streamlit elementlari orasidagi standart bo'shliqni yo'qotish */
    .element-container { margin-bottom: 0px !important; }
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
    u_pass = st.text_input("Parol:", type="password")
    if st.button("KIRISH"):
        if u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Xato!")

# --- TEST JARAYONI ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Bo'limni tanlang")
        
        # Jami 300 tacha savollar bazasi (Fayldagi ma'lumotlar asosida)
        ms_all = [
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"}
        ]
        
        if st.button("🚀 BOSHLASH"):
            st.session_state.active_questions = ms_all # Hamma savollarni shu yerga qo'shing
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()

    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        curr = questions[q_idx]
        
        # Natija paneli (Savol ustida)
        if st.session_state.answered:
            if st.session_state.selected_option == curr['a']:
                st.success("✅ BARAKALLA! TO‘G‘RI JAVOB.")
            else:
                st.error(f"❌ NOTO‘G‘RI! To‘g‘ri javob: {curr['a']}")

        # Savol qutisi
        st.markdown(f"""
            <div class="question-container">
                <div style="color:#888; font-size:13px; margin-bottom:5px;">Savol {q_idx + 1} / {len(questions)}</div>
                <div style="font-size:22px; font-weight:700;">{curr['q']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # VARIANTLAR - Har biri rangli yonadigan tugma
        for option in curr['o']:
            # Konteyner klassini aniqlash
            btn_class = "<div>"
            if st.session_state.answered:
                if option == curr['a']:
                    btn_class = '<div class="correct-btn">' # To'g'ri bo'lsa yashil fon
                elif option == st.session_state.selected_option:
                    btn_class = '<div class="wrong-btn">' # Noto'g'ri bo'lsa qizil fon
            
            st.markdown(btn_class, unsafe_allow_html=True)
            if st.button(option, key=f"btn_{option}_{q_idx}", disabled=st.session_state.answered):
                st.session_state.answered = True
                st.session_state.selected_option = option
                if option == curr['a']:
                    st.session_state.user_score += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # Boshqaruv tugmalari
        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            if st.session_state.answered:
                if st.button("Keyingi savol ➔"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.session_state.selected_option = None
                    st.rerun()
        with c2:
            if st.button("🏠 Menyuga qaytish"):
                for k in ['test_started','current_q_index','user_score','active_questions','answered','selected_option']:
                    if k in st.session_state: del st.session_state[k]
                st.rerun()
