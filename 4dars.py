import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Telegram Quiz dizayni (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #e6ebf0; }
    
    /* Quiz kartasi */
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

    /* Radio variantlar dizayni */
    div[role="radiogroup"] label {
        font-size: 17px !important;
        color: #333 !important;
        padding: 10px 0 !important;
        border-bottom: 1px solid #f8f8f8;
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
    .bar-fill { height: 100%; border-radius: 5px; transition: width 0.5s; }

    /* Keyingi tugmasi */
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
        st.title("🚀 Bo'limni tanlang")
        
        ms_all = [
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
            {"q": "Aktivlar deganda nimani tushuniladi?", "o": ["Qarzdorlik majburiyatlari", "Shaxsiy va korporativ mulk", "Faqat pul mablag‘lari", "Daromad manbalari"], "a": "Shaxsiy va korporativ mulk"},
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"}
        ]
        
        blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("🚀 BOSHLASH"):
            st.session_state.active_questions = ms_all # Jami 300 ta savolni shu yerga qo'shishingiz mumkin
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()

    # --- TEST ISHLASH ---
    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        
        if q_idx < len(questions):
            curr = questions[q_idx]
            
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="question-header">[{q_idx + 1}/{len(questions)}] {curr["q"]}</div>', unsafe_allow_html=True)

            if not st.session_state.answered:
                choice = st.radio("", curr['o'], index=None, key=f"q_{q_idx}", label_visibility="collapsed")
                if choice:
                    st.session_state.answered = True
                    st.session_state.selected_option = choice
                    if choice == curr['a']: st.session_state.user_score += 1
                    st.rerun()
            else:
                for opt in curr['o']:
                    is_correct = (opt == curr['a'])
                    is_user_choice = (opt == st.session_state.selected_option)
                    percent = 100 if is_correct else 0
                    fill_color = "#4CAF50" if is_correct else "#e0e0e0"
                    icon = "✔️" if is_correct else ("❌" if is_user_choice else "")
                    
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
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.session_state.selected_option = None
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.success(f"🏁 Test tugadi! Natija: {st.session_state.user_score}/{len(questions)}")
            if st.button("🏠 Menyuga qaytish"):
                for k in ['test_started','current_q_index','user_score','answered','selected_option']:
                    del st.session_state[k]
                st.rerun()
