import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Mobil va Dark Mode uchun optimallashgan CSS
st.markdown("""
    <style>
    /* Umumiy fon rangi */
    .stApp { background-color: #e6ebf0 !important; }
    
    /* Sarlavhalar va matnlar rangini majburiy qora qilish */
    h1, h2, h3, p, span, div, label {
        color: #333333 !important;
    }
    
    /* Quiz kartasi */
    .quiz-card {
        background-color: white !important;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        max-width: 500px;
        margin: auto;
    }
    
    /* Radio variantlar matni */
    div[role="radiogroup"] label p {
        color: #333333 !important;
        font-size: 17px !important;
    }
    
    /* Ortig'cha oq joyni yo'qotish */
    div[data-testid="stWidgetLabel"] {
        display: none !important;
    }
    
    /* Keyingi/Boshlash tugmasi */
    .stButton button {
        width: 100%;
        background-color: #0088cc !important;
        color: white !important;
        border-radius: 10px !important;
        height: 48px;
        font-weight: bold;
        border: none;
        margin-top: 10px;
    }

    /* Progress bar va foizlar */
    .label-row span {
        color: #333333 !important;
        font-weight: 600;
    }
    .bar-bg {
        background-color: #eeeeee !important;
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
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.title("🎯 Kirish")
    u_login = st.text_input("Login:", value="Murat")
    u_pass = st.text_input("Parol:", type="password")
    if st.button("KIRISH"):
        if u_login == "Murat" and u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Xato!")
    st.markdown('</div>', unsafe_allow_html=True)

# --- MENYU ---
else:
    if not st.session_state.test_started:
        st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
        st.title("🚀 Bo'limni tanlang")
        
        ms_all = [
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
            {"q": "Aktivlar deganda nimani tushuniladi?", "o": ["Qarzdorlik majburiyatlari", "Shaxsiy va korporativ mulk", "Faqat pul mablag‘lari", "Daromad manbalari"], "a": "Shaxsiy va korporativ mulk"},
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"}
        ]
        
        blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("🚀 BOSHLA"):
            st.session_state.active_questions = ms_all 
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- TEST ISHLASH ---
    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        
        if q_idx < len(questions):
            curr = questions[q_idx]
            
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="question-header">[{q_idx + 1}/{len(questions)}] {curr["q"]}</div>', unsafe_allow_html=True)

            if not st.session_state.answered:
                choice = st.radio("Tanlang", curr['o'], index=None, key=f"q_{q_idx}", label_visibility="collapsed")
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
                    fill_color = "#4CAF50" if is_correct else "#cccccc"
                    icon = "✔️" if is_correct else ("❌" if is_user_choice else "")
                    
                    st.markdown(f"""
                        <div style="margin-bottom: 15px;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                                <span style="color: #333; font-weight: 500;">{opt} {icon}</span>
                                <span style="color: #333;">{percent}%</span>
                            </div>
                            <div style="height: 10px; background-color: #eee; border-radius: 5px; overflow: hidden;">
                                <div style="width: {percent}%; height: 100%; background-color: {fill_color};"></div>
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
            st.markdown('<div class="quiz-card" style="text-align: center;">', unsafe_allow_html=True)
            st.title("🏁 Test tugadi!")
            st.write(f"Natijangiz: **{st.session_state.user_score}/{len(questions)}**")
            if st.button("🏠 Menyuga qaytish"):
                for k in ['test_started','current_q_index','user_score','answered','selected_option']:
                    del st.session_state[k]
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
