import streamlit as st
import random

# Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯")

# 1. FOYDALANUVCHILAR BAZASI
users_db = {"Murat": "12062006"}

# Holatlarni boshqarish
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'current_q_index' not in st.session_state:
    st.session_state.current_q_index = 0
if 'user_score' not in st.session_state:
    st.session_state.user_score = 0
if 'answered' not in st.session_state:
    st.session_state.answered = False

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
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    if not st.session_state.test_started:
        st.title("🎯 Testlar Markazi")
        option = st.selectbox("Fanni tanlang:", ["PYTHON", "Differensial tenglamalar", "Moliyaviy savodxonlik"])
        
        if option == "Moliyaviy savodxonlik":
            blok_choice = st.radio("Test blokini tanlang (70 tadan):", 
                                  ["1-70 gacha", "71-140 gacha", "141-210 gacha", "211-300 gacha"])
        
        if st.button("Testni boshlash"):
            # BARCHA SAVOLLAR BAZASI (Fayldagi 300 ga yaqin savol)
            ms_questions = [
                {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
                {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
                {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"},
                # ...[cite: 1]
                # Fayldagi barcha 300 ta savolni shu tartibda ms_questions ichiga joylashtiring.
                # Savol matni (q), Variantlar (o), To'g'ri javob (a).
            ]
            
            if option == "PYTHON":
                selected_qs = [
                    {"q": "Python qaysi yili yaratilgan?", "o": ["1991", "1985", "2000", "2010"], "a": "1991"},
                    # PYTHON SAVOLLARI
                ]
            elif option == "Differensial tenglamalar":
                selected_qs = [
                    {"q": "y' = f(x,y) qanday tenglama?", "o": ["1-tartibli", "2-tartibli", "Bernoulli", "Chiziqli"], "a": "1-tartibli"},
                    # DIFF SAVOLLARI
                ]
            else: # Moliyaviy savodxonlik bloklari
                if blok_choice == "1-70 gacha":
                    selected_qs = ms_questions[0:70]
                elif blok_choice == "71-140 gacha":
                    selected_qs = ms_questions[70:140]
                elif blok_choice == "141-210 gacha":
                    selected_qs = ms_questions[140:210]
                else:
                    selected_qs = ms_questions[210:]
            
            random.shuffle(selected_qs)
            for item in selected_qs:
                item['o'] = list(item['o'])
                random.shuffle(item['o'])
            
            st.session_state.active_questions = selected_qs
            st.session_state.test_started = True
            st.rerun()

    else:
        # TEST ISHLASH (BITTA SAVOL + VIZUAL RANG)
        q_idx = st.session_state.current_q_index
        total_qs = len(st.session_state.active_questions)
        
        if q_idx < total_qs:
            current_q = st.session_state.active_questions[q_idx]
            st.subheader(f"Savol {q_idx + 1} / {total_qs}")
            st.write(f"**{current_q['q']}**")
            
            for variant in current_q['o']:
                if st.session_state.answered:
                    if variant == current_q['a']:
                        st.markdown(f'<p style="background-color:#d4edda; color:#155724; padding:10px; border-radius:5px; border:1px solid #c3e6cb;"><b>✅ {variant}</b></p>', unsafe_allow_html=True)
                    elif variant == st.session_state.get('last_user_choice') and variant != current_q['a']:
                        st.markdown(f'<p style="background-color:#f8d7da; color:#721c24; padding:10px; border-radius:5px; border:1px solid #f5c6cb;"><b>❌ {variant}</b></p>', unsafe_allow_html=True)
                    else:
                        st.text(f"⚪ {variant}")

            if not st.session_state.answered:
                ans = st.radio("Javobni tanlang:", current_q['o'], index=None, key=f"q_{q_idx}")
                if st.button("Tekshirish ✅"):
                    if ans:
                        st.session_state.answered = True
                        st.session_state.last_user_choice = ans
                        if ans == current_q['a']:
                            st.session_state.user_score += 1
                        st.rerun()
                    else:
                        st.warning("Iltimos, javobni tanlang!")
            else:
                if st.button("Keyingi savol ➡️"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.title("🏁 Test tugadi!")
            st.success(f"Natijangiz: {st.session_state.user_score} / {total_qs}")
            if st.button("Bosh sahifaga qaytish"):
                for key in ['test_started', 'current_q_index', 'user_score', 'active_questions', 'answered', 'last_user_choice']:
                    if key in st.session_state: del st.session_state[key]
                st.rerun()
