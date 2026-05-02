import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Telefon uchun maxsus kuchaytirilgan dizayn (CSS)
st.markdown("""
    <style>
    /* Asosiy fon */
    .stApp {
        background-color: #f4f7f6;
    }
    
    /* Savol qolipi (Container) */
    .question-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #4CAF50;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* Savol matni */
    .question-text {
        font-size: 24px !important;
        font-weight: 700 !important;
        color: #1a1a1a;
        line-height: 1.4;
    }

    /* Radio variantlarini katta qutilarga aylantirish */
    div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        border: 2px solid #e0e0e0 !important;
        padding: 18px !important;
        border-radius: 12px !important;
        margin-bottom: 12px !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        transition: all 0.3s ease !important;
        cursor: pointer !important;
    }
    
    /* Variant bosilganda (Tanlanganda) */
    div[role="radiogroup"] [data-checked="true"] {
        border-color: #4CAF50 !important;
        background-color: #f1f8f1 !important;
        box-shadow: 0 4px 10px rgba(74, 175, 80, 0.2) !important;
    }

    /* Variant ichidagi matnni kattalashtirish */
    .stRadio p {
        font-size: 20px !important;
        font-weight: 500 !important;
        color: #333 !important;
    }

    /* Natija xabarlari dizayni */
    .res-box {
        padding: 20px;
        border-radius: 12px;
        font-size: 20px;
        font-weight: bold;
        margin-top: 10px;
        border: 2px solid transparent;
    }
    .correct { background-color: #d4edda; color: #155724; border-color: #c3e6cb; }
    .wrong { background-color: #f8d7da; color: #721c24; border-color: #f5c6cb; }

    /* "Keyingi savol" tugmasi */
    .stButton > button {
        width: 100%;
        height: 55px;
        background-color: #4CAF50 !important;
        color: white !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        margin-top: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Holatlarni boshqarish (session_state)
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

# --- TEST OYNASI ---
else:
    if not st.session_state.test_started:
        st.title("🚀 Fan va blokni tanlang")
        
        # Barcha savollar bazasi (Fayldagi 300 taga yaqin savol)
        # Bu yerga fayldagi barcha savollarni birma-bir joylashtirib chiqish kerak
        ms_all = [
            {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
            {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
            {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"},
            {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
            {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
            {"q": "Inflyatsiya deganda nima tushuniladi?", "o": ["Narxlar umumiy darajasining oshishi", "Bank foiz stavkalari pasayishi", "Kredit miqdori ko'payishi", "Valyuta kursi tushishi"], "a": "Narxlar umumiy darajasining oshishi"},
            {"q": "Aktivlar deganda nimani tushuniladi?", "o": ["Qarzdorlik majburiyatlari", "Shaxsiy va korporativ mulk", "Faqat pul mablag'i", "Daromad manbalari"], "a": "Shaxsiy va korporativ mulk"},
            # ... (Fayldagi qolgan savollarni ham shu formatda qo'shing)
        ]
        
        option = st.selectbox("Fanni tanlang:", ["Moliyaviy savodxonlik", "PYTHON", "Differensial tenglamalar"])
        
        if option == "Moliyaviy savodxonlik":
            blok = st.radio("Blokni tanlang (70 tadan):", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("🚀 TESTNI BOSHLASH"):
            if option == "Moliyaviy savodxonlik":
                if blok == "1-70": st.session_state.active_questions = ms_all[0:70]
                elif blok == "71-140": st.session_state.active_questions = ms_all[70:140]
                elif blok == "141-210": st.session_state.active_questions = ms_all[140:210]
                else: st.session_state.active_questions = ms_all[210:]
            else:
                st.session_state.active_questions = ms_all[0:10] # Boshqa fanlar uchun namuna
            
            random.shuffle(st.session_state.active_questions)
            st.session_state.test_started = True
            st.rerun()

    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        
        if q_idx < len(questions):
            curr = questions[q_idx]
            
            # Savol dizayni[cite: 1]
            st.markdown(f"""
                <div class="question-box">
                    <div class="question-info">Savol {q_idx + 1} / {len(questions)}</div>
                    <div class="question-text">{curr['q']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Javobni tekshirish funksiyasi[cite: 1]
            def auto_check():
                if st.session_state[f"radio_{q_idx}"] is not None:
                    st.session_state.answered = True
                    if st.session_state[f"radio_{q_idx}"] == curr['a']:
                        st.session_state.user_score += 1

            # Variantlar - Radio label yashirilgan, quti ko'rinishida
            ans = st.radio("Javobingizni tanlang:", curr['o'], 
                           index=None, key=f"radio_{q_idx}", 
                           on_change=auto_check, 
                           disabled=st.session_state.answered,
                           label_visibility="collapsed")
            
            # Natija chiqishi[cite: 1]
            if st.session_state.answered:
                u_choice = st.session_state[f"radio_{q_idx}"]
                if u_choice == curr['a']:
                    st.markdown(f'<div class="res-box correct">✅ TO\'G\'RI: {curr["a"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="res-box wrong">❌ NOTO\'G\'RI!<br>To\'g\'ri javob: {curr["a"]}</div>', unsafe_allow_html=True)
                
                if st.button("Keyingi savol ➔"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.balloons()
            st.success(f"🏁 Test yakunlandi! Natijangiz: {st.session_state.user_score} / {len(questions)}")
            if st.button("Asosiy menyuga qaytish"):
                for k in ['test_started','current_q_index','user_score','active_questions','answered']:
                    if k in st.session_state: del st.session_state[k]
                st.rerun()
