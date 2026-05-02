import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. DIZAYNNI TUZATISH (CSS)
st.markdown("""
    <style>
    /* Umumiy fon */
    .stApp { background-color: #f8f9fa; }
    
    /* Savol qolipi */
    .question-container {
        background-color: white;
        padding: 25px;
        border-radius: 15px 15px 0 0;
        border-top: 10px solid #4CAF50;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 0px !important;
    }
    
    /* Variant tugmalari - Yopishgan va to'liq kenglikda */
    div.stButton > button {
        width: 100% !important;
        text-align: left !important;
        padding: 18px 25px !important;
        border-radius: 0px !important; /* Burchaklarni yo'qotish */
        border: 0.5px solid #ddd !important;
        background-color: white !important;
        color: #333 !important;
        font-size: 19px !important;
        margin: 0 !important;
        display: block !important;
    }
    
    /* Birinchi va oxirgi tugma burchaklarini yumshatish */
    div.stButton:first-child > button { border-radius: 0px !important; }
    div.stButton:last-child > button { border-radius: 0 0 15px 15px !important; }

    /* To'g'ri javob yashil yonishi */
    .correct-btn button {
        background-color: #28a745 !important;
        color: white !important;
        border-color: #1e7e34 !important;
    }

    /* Noto'g'ri javob qizil yonishi */
    .wrong-btn button {
        background-color: #dc3545 !important;
        color: white !important;
        border-color: #bd2130 !important;
    }

    /* Elementlar orasidagi bo'shliqni yo'qotish */
    .element-container { margin-bottom: -1px !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_active' not in st.session_state: st.session_state.test_active = False
if 'q_idx' not in st.session_state: st.session_state.q_idx = 0
if 'score' not in st.session_state: st.session_state.score = 0
if 'answered' not in st.session_state: st.session_state.answered = False
if 'sel_opt' not in st.session_state: st.session_state.sel_opt = None

# --- KIRISH ---
if not st.session_state.logged_in:
    st.title("🎯 Kirish")
    u_pass = st.text_input("Parol:", type="password")
    if st.button("KIRISH"):
        if u_pass == "12062006":
            st.session_state.logged_in = True
            st.rerun()
        else: st.error("Xato!")

# --- TEST ---
else:
    if not st.session_state.test_active:
        st.title("🚀 Bo'limni tanlang")
        ms_all = [
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
            {"q": "Aktivlar nima?", "o": ["Qarzlar", "Shaxsiy mulk", "Soliqlar", "Xarajatlar"], "a": "Shaxsiy mulk"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi", "Bank balansi", "Soliq turi"], "a": "Kredit berish narxi"}
        ]
        if st.button("BOSHLASH"):
            st.session_state.questions = ms_all # Fayldagi 300 ta savolni shu yerga qo'shing
            random.shuffle(st.session_state.questions)
            st.session_state.test_active = True
            st.rerun()
    else:
        curr_idx = st.session_state.q_idx
        q_list = st.session_state.questions
        
        if curr_idx < len(q_list):
            curr_q = q_list[curr_idx]
            
            # Natija (Yuqorida)
            if st.session_state.answered:
                if st.session_state.sel_opt == curr_q['a']:
                    st.success("✅ TO'G'RI JAVOB!")
                else:
                    st.error(f"❌ NOTO'G'RI! To'g'ri: {curr_q['a']}")

            # Savol qutisi
            st.markdown(f"""
                <div class="question-container">
                    <div style="color:#888; font-size:13px;">Savol {curr_idx + 1} / {len(q_list)}</div>
                    <div style="font-size:22px; font-weight:700;">{curr_q['q']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Variantlar - To'g'ridan-to'g'ri yopishgan tugmalar
            for opt in curr_q['o']:
                btn_style = "<div>"
                if st.session_state.answered:
                    if opt == curr_q['a']: btn_style = '<div class="correct-btn">'
                    elif opt == st.session_state.sel_opt: btn_style = '<div class="wrong-btn">'
                
                st.markdown(btn_style, unsafe_allow_html=True)
                if st.button(opt, key=f"opt_{opt}_{curr_idx}", disabled=st.session_state.answered):
                    st.session_state.answered = True
                    st.session_state.sel_opt = opt
                    if opt == curr_q['a']: st.session_state.score += 1
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

            # Boshqaruv
            st.write("---")
            c1, c2 = st.columns(2)
            with c1:
                if st.session_state.answered:
                    if st.button("Keyingi ➔"):
                        st.session_state.q_idx += 1
                        st.session_state.answered = False
                        st.session_state.sel_opt = None
                        st.rerun()
            with c2:
                if st.button("🏠 Menyuga"):
                    for k in ['test_active','q_idx','score','questions','answered','sel_opt']:
                        if k in st.session_state: del st.session_state[k]
                    st.rerun()
