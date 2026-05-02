import streamlit as st

# Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯")

# 1. ADMIN TOMONIDAN BELGILANGAN FOYDALANUVCHILAR
users_db = {
    "Murat": "12062006"
}

# Login holati
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

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

# --- ASOSIY SAHIFA (FANLARNI TANLASH) ---
else:
    st.sidebar.write(f"👤 Foydalanuvchi: **{st.session_state.current_user}**")
    if st.sidebar.button("Chiqish"):
        st.session_state.logged_in = False
        st.session_state.test_started = False
        st.rerun()

    st.title("🎯 Testlar Markazi")
    
    option = st.selectbox("Fanni tanlang:", ["PYTHON", "Differensial tenglamalar", "Moliyaviy savodxonlik"])
    
    if st.button("Testni boshlash"):
        st.session_state.test_started = True

    if st.session_state.get('test_started'):
        st.divider()
        st.subheader(f"Fan: {option}")

        # SAVOLLAR BAZASI
        quiz_data = {
            "PYTHON": [
                {"q": "Python qaysi yili yaratilgan?", "o": ["1991", "1985", "2000", "2010"], "a": "1991"},
                {"q": "O'zgaruvchi turini aniqlash funksiyasi?", "o": ["type()", "id()", "print()", "input()"], "a": "type()"},
                {"q": "Ro'yxatga oxiridan element qo'shish usuli?", "o": ["append()", "add()", "push()", "insert()"], "a": "append()"},
                {"q": "Qaysi operator darajaga ko'taradi?", "o": ["**", "^", "//", "%"], "a": "**"},
                {"q": "Lug'at (dictionary) qaysi qavslar bilan yoziladi?", "o": ["{}", "[]", "()", "<>"], "a": "{}"},
                {"q": "O'zgarmas ro'yxat turi nima deyiladi?", "o": ["tuple", "list", "set", "dictionary"], "a": "tuple"},
                {"q": "Qatorni ekranga chiqarish funksiyasi?", "o": ["print()", "echo()", "write()", "output()"], "a": "print()"},
                {"q": "Butun son turi qanday belgilanadi?", "o": ["int", "float", "str", "bool"], "a": "int"},
                {"q": "Shartli operatorni ko'rsating?", "o": ["if", "for", "while", "def"], "a": "if"},
                {"q": "Funksiya yaratish kalit so'zi?", "o": ["def", "func", "function", "create"], "a": "def"}
            ],
            "Differensial tenglamalar": [
                {"q": "y' = f(x,y) qanday tenglama?", "o": ["1-tartibli", "2-tartibli", "Bernoulli", "Chiziqli"], "a": "1-tartibli"},
                {"q": "Puasson formulasi nima uchun ishlatiladi?", "o": ["Ehtimollik", "Integral", "Hajm", "Tezlik"], "a": "Ehtimollik"},
                {"q": "Bernoulli tenglamasi qaysi ko'rinishda?", "o": ["y' + Py = Qy^n", "y' = f(x)", "y'' + p = 0", "y = kx+b"], "a": "y' + Py = Qy^n"},
                {"q": "Chiziqli differensial tenglamaning tartibi nimaga bog'liq?", "o": ["Yuqori hosilaga", "Erkli o'zgaruvchiga", "Yechim soniga", "Integralga"], "a": "Yuqori hosilaga"},
                {"q": "Garmonik tebranish tenglamasi qanday tartibli?", "o": ["2-tartibli", "1-tartibli", "3-tartibli", "4-tartibli"], "a": "2-tartibli"},
                {"q": "Differensial tenglamaning umumiy yechimi nimani o'z ichiga oladi?", "o": ["O'zgarmas C ni", "Faqat sonlarni", "Faqat x ni", "Integralni"], "a": "O'zgarmas C ni"},
                {"q": "y'' + w^2y = 0 tenglamaning yechimi?", "o": ["Sinus/Kosinus", "Eksponenta", "Logarifm", "Polinom"], "a": "Sinus/Kosinus"},
                {"q": "Koshi masalasi nimani topishni talab qiladi?", "o": ["Xususiy yechimni", "Umumiy yechimni", "Integralni", "Limitni"], "a": "Xususiy yechimni"},
                {"q": "Eyler usuli nima uchun qo'llaniladi?", "o": ["Sonli yechish", "Aniq integrallash", "Hosila olish", "Soddalashtirish"], "a": "Sonli yechish"},
                {"q": "Bir jinsli tenglamada f(tx, ty) nimaga teng?", "o": ["f(x,y)", "t*f(x,y)", "f(x)/t", "0"], "a": "f(x,y)"}
            ],
            "Moliyaviy savodxonlik": [
                {"q": "Inflyatsiya nima?", "o": ["Narx oshishi", "Narx tushishi", "Soliq", "Qarz"], "a": "Narx oshishi"},
                {"q": "Aktiv nima?", "o": ["Daromad keltiruvchi", "Xarajat keltiruvchi", "Qarz", "Soliq"], "a": "Daromad keltiruvchi"},
                {"q": "Passiv nima?", "o": ["Xarajat keltiruvchi", "Daromad keltiruvchi", "Mulk", "Sarmoya"], "a": "Xarajat keltiruvchi"},
                {"q": "Diversifikatsiya nima?", "o": ["Xavfni bo'lish", "Pul yig'ish", "Kredit olish", "Soliq to'lash"], "a": "Xavfni bo'lish"},
                {"q": "Murakkab foiz nima?", "o": ["Foizdan foiz", "Oddiy foiz", "Kredit foizi", "Soliq turi"], "a": "Foizdan foiz"},
                {"q": "Likvidlik nima?", "o": ["Tez pulga aylanish", "Qarz miqdori", "Soliq stavkasi", "Foyda foizi"], "a": "Tez pulga aylanish"},
                {"q": "Budjet nima?", "o": ["Kirim va chiqim rejasi", "Faqat daromad", "Soliq yig'indisi", "Bank hisobi"], "a": "Kirim va chiqim rejasi"},
                {"q": "Keshbek (Cashback) nima?", "o": ["Pulning bir qismini qaytishi", "Qarz olish", "Soliq to'lash", "Xizmat haqi"], "a": "Pulning bir qismini qaytishi"},
                {"q": "Depozit nima?", "o": ["Bankdagi omonat", "Kredit", "Soliq", "Sug'urta"], "a": "Bankdagi omonat"},
                {"q": "Aktsiya nima?", "o": ["Ulishli qimmatli qog'oz", "Qarz qog'ozi", "Soliq kvitansiyasi", "Shartnoma"], "a": "Ulishli qimmatli qog'oz"}
            ]
        }

        current_questions = quiz_data[option]
        score = 0
        user_answers = {}

        for i, q in enumerate(current_questions):
            st.write(f"**{i+1}. {q['q']}**")
            # MUHIM: index=None varianti belgilanmagan holda chiqaradi
            ans = st.radio(f"Javobni tanlang:", q['o'], key=f"ans_{option}_{i}", index=None)
            user_answers[i] = ans

        if st.button("Natijani ko'r"):
            unanswered = [i for i, a in user_answers.items() if a is None]
            if unanswered:
                st.warning(f"Iltimos, barcha savollarga javob bering! (Belgilanmagan: {len(unanswered)} ta)")
            else:
                for i, q in enumerate(current_questions):
                    if user_answers[i] == q['a']:
                        score += 1
                
                st.divider()
                st.success(f"Natijangiz: {score} / {len(current_questions)}")
                if score == len(current_questions):
                    st.balloons()
