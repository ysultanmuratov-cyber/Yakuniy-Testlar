import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Variantlar uchun maxsus effektli dizayn (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    
    /* Savol qolipi */
    .question-container {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-top: 10px solid #4CAF50;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }
    
    /* Variant tugmalari uchun umumiy dizayn */
    div.stButton > button {
        width: 100%;
        text-align: left;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #eee;
        background-color: white;
        color: #333;
        font-size: 18px !important;
        margin-bottom: 10px;
        transition: 0.3s;
    }
    
    /* Tugma ustiga borganda */
    div.stButton > button:hover {
        border-color: #4CAF50;
        background-color: #f9fdf9;
    }

    /* To'g'ri javob yashil yonishi */
    .correct-btn button {
        background-color: #d4edda !important;
        border-color: #28a745 !important;
        color: #155724 !important;
        font-weight: bold;
    }

    /* Noto'g'ri javob qizil yonishi */
    .wrong-btn button {
        background-color: #f8d7da !important;
        border-color: #dc3545 !important;
        color: #721c24 !important;
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
    st.title("🎯 Tizimga kirish")
    u_login = st.text_input("Login:", value="Murat")
    u_pass = st.text_input("Parol:", type="password")
    if st.button("KIRISH"):
        if u_login == "Murat" and u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Login yoki parol xato!")

# --- MENYU ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Bo'limni tanlang")
        
        # Barcha 300 tacha savollar bazasi
        ms_all = [
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
            # Fayldagi qolgan savollarni shu yerga to'liq qo'shing
        ]
        
        blok = st.radio("Test bloki:", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("🚀 TESTNI BOSHLASH"):
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
        curr = questions[q_idx]
        
        # Natija paneli (Yuqorida)
        if st.session_state.answered:
            if st.session_state.selected_option == curr['a']:
                st.markdown(f'<div style="background-color:#d4edda; color:#155724; padding:15px; border-radius:10px; margin-bottom:15px; font-weight:bold; text-align:center;">✅ TO‘G‘RI JAVOB!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="background-color:#f8d7da; color:#721c24; padding:15px; border-radius:10px; margin-bottom:15px; font-weight:bold; text-align:center;">❌ NOTO‘G‘RI! To‘g‘ri javob: {curr["a"]}</div>', unsafe_allow_html=True)

        # Savol qutisi
        st.markdown(f"""
            <div class="question-container">
                <div style="color:#888; font-size:14px;">Savol {q_idx + 1} / {len(questions)}</div>
                <div style="font-size:24px; font-weight:700;">{curr['q']}</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Variant tugmalarini chiqarish
        for option in curr['o']:
            button_type = "normal"
            if st.session_state.answered:
                if option == curr['a']:
                    st.markdown('<div class="correct-btn">', unsafe_allow_html=True)
                elif option == st.session_state.selected_option:
                    st.markdown('<div class="wrong-btn">', unsafe_allow_html=True)
                else:
                    st.markdown('<div>', unsafe_allow_html=True)
            else:
                st.markdown('<div>', unsafe_allow_html=True)
            
            if st.button(option, key=f"opt_{option}_{q_idx}", disabled=st.session_state.answered):
                st.session_state.answered = True
                st.session_state.selected_option = option
                if option == curr['a']:
                    st.session_state.user_score += 1
                st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)

        # Pastki boshqaruv tugmalari
        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.session_state.answered:
                if st.button("Keyingi savol ➔"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.session_state.selected_option = None
                    st.rerun()
        with col2:
            if st.button("🏠 Menyuga qaytish"):
                for k in ['test_started','current_q_index','user_score','active_questions','answered','selected_option']:
                    if k in st.session_state: del st.session_state[k]
                st.rerun()
