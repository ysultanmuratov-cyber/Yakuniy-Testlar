import streamlit as st

# Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯")

# 1. ADMIN TOMONIDAN BELGILANGAN FOYDALANUVCHILAR (Login va Parollar)
# Haqiqiy loyihada bularni Streamlit Secrets-ga qo'yish yaxshi,
# lekin hozircha kod ichida ro'yxat qilib turamiz:
users_db = {
    "Murat": "12062006",
    "Bekchon": "Beko1212x",
}

# Session state orqali login holatini tekshirish
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- KIRISH OYNASI ---
if not st.session_state.logged_in:
    st.title("🎯 Testlar Markaziga Kirish")
    st.info("Testni boshlash uchun administrator tomonidan berilgan ma'lumotlarni kiriting.")

    # Uchta qator (talabingiz bo'yicha)
    full_name = st.text_input("1. Ism va Familiyangizni kiriting:", placeholder="Masalan: Ali Valiyev")
    user_login = st.text_input("2. Login:", placeholder="Loginni kiriting")
    user_password = st.text_input("3. Parol:", type="password", placeholder="Parolni kiriting")

    if st.button("Tizimga kirish"):
        if full_name and user_login in users_db and users_db[user_login] == user_password:
            st.session_state.logged_in = True
            st.session_state.user_full_name = full_name
            st.rerun()
        elif not full_name:
            st.error("Iltimos, ism va familiyangizni kiriting!")
        else:
            st.error("Login yoki parol xato! Iltimos, adminga murojaat qiling.")

# --- TEST OYNASI (Faqat login qilgandan keyin ko'rinadi) ---
else:
    st.sidebar.write(f"👤 Foydalanuvchi: **{st.session_state.user_full_name}**")
    if st.sidebar.button("Chiqish"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("🎯 Python Bo'yicha Testlar")
    st.write(f"Xush kelibsiz, **{st.session_state.user_full_name}**! Bilimingizni sinab ko'ring.")

    # Test savollari (Namuna sifatida)
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
        ans = st.radio(f"Variantni tanlang ({i}):", q['variantlar'], key=f"q{i}")
        user_answers.append(ans)

    if st.button("Natijani tekshirish"):
        for i, q in enumerate(questions):
            if user_answers[i] == q['javob']:
                score += 1

        st.divider()
        if score == len(questions):
            st.balloons()
            st.success(
                f"Ajoyib natija, {st.session_state.user_full_name}! Siz hamma savolga to'g'ri javob berdingiz: {score}/{len(questions)}")
        else:
            st.info(f"Yaxshi, {st.session_state.user_full_name}. Sizning natijangiz: {score}/{len(questions)}")
