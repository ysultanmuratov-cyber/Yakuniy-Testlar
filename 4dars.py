import streamlit as st

# Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯")

# 1. ADMIN TOMONIDAN BELGILANGAN FOYDALANUVCHILAR
# Bu yerga o'zingiz xohlagan login va parollarni qo'shing
users_db = {
    "Murat": "12062006"
}

# Session state orqali login holatini tekshirish
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- KIRISH OYNASI ---
if not st.session_state.logged_in:
    st.title("🎯 Testlar Markaziga Kirish")

    # Faqat ikkita qator (Login va Parol)
    user_login = st.text_input("Loginni kiriting:")
    user_password = st.text_input("Parolni kiriting:", type="password")

    if st.button("Tizimga kirish"):
        if user_login in users_db and users_db[user_login] == user_password:
            st.session_state.logged_in = True
            st.session_state.current_user = user_login
            st.rerun()
        else:
            st.error("Login yoki parol xato!")

# --- TEST OYNASI (Login qilgandan keyin ko'rinadi) ---
else:
    st.sidebar.write(f"👤 Foydalanuvchi: **{st.session_state.current_user}**")
    if st.sidebar.button("Chiqish"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🎯 Python Bo'yicha Testlar")
    st.write(f"Xush kelibsiz, **{st.session_state.current_user}**!")

    # Test savollari
    questions = [
        {
            "savol": "Python-da ro'yxatga element qo'shish uchun qaysi metod ishlatiladi?",
            "variantlar": ["add()", "append()", "insert_all()", "push()"],
            "javob": "append()"
        },
        {
            "savol": "NumPy kutubxonasi nima uchun ishlatiladi?",
            "variantlar": ["Veb-sayt yaratish", "Matematik hisoblashlar va massivlar", "O'yin yaratish",
                           "Rasm tahrirlash"],
            "javob": "Matematik hisoblashlar va massivlar"
        }
    ]

    score = 0
    user_answers = []

    for i, q in enumerate(questions):
        st.subheader(f"{i + 1}-savol: {q['savol']}")
        ans = st.radio(f"Variantni tanlang:", q['variantlar'], key=f"q{i}")
        user_answers.append(ans)

    if st.button("Natijani ko'rish"):
        for i, q in enumerate(questions):
            if user_answers[i] == q['javob']:
                score += 1

        st.divider()
        st.success(f"Sizning natijangiz: {score} ball")
        if score == len(questions):
            st.balloons()
