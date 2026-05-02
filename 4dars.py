import streamlit as st
import random

# Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯")

# 1. ADMIN TOMONIDAN BELGILANGAN FOYDALANUVCHILAR
users_db = {
    "Murat": "12062006"
}

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

# --- TESTLAR OYNASI ---
else:
    st.sidebar.write(f"👤 Foydalanuvchi: **{st.session_state.current_user}**")
    if st.sidebar.button("Chiqish"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    if not st.session_state.test_started:
        st.title("🎯 Testlar Markazi")
        option = st.selectbox("Fanni tanlang:", ["PYTHON", "Differensial tenglamalar", "Moliyaviy savodxonlik"])
        
        if st.button("Testni boshlash"):
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
            selected_qs = list(quiz_data[option])
            random.shuffle(selected_qs)
            for item in selected_qs:
                item['o'] = list(item['o'])
                random.shuffle(item['o'])
            st.session_state.active_questions = selected_qs
            st.session_state.test_started = True
            st.rerun()

    else:
        q_idx = st.session_state.current_q_index
        total_qs = len(st.session_state.active_questions)
        
        if q_idx < total_qs:
            current_q = st.session_state.active_questions[q_idx]
            st.subheader(f"Savol {q_idx + 1} / {total_qs}")
            st.write(f"**{current_q['q']}**")
            
            # Javob berilgan bo'lsa radio bosib bo'lmaydigan qilinadi
            ans = st.radio("Javobni tanlang:", current_q['o'], 
                           index=None, key=f"q_{q_idx}", 
                           disabled=st.session_state.answered)
            
            if not st.session_state.answered:
                if st.button("Tekshirish ✅"):
                    if ans:
                        st.session_state.answered = True
                        if ans == current_q['a']:
                            st.session_state.user_score += 1
                        st.rerun()
                    else:
                        st.warning("Iltimos, variantlardan birini tanlang!")
            else:
                # Rangli xabar chiqarish
                if ans == current_q['a']:
                    st.success(f"To'g'ri! ✅ Javob: {current_q['a']}")
                else:
                    st.error(f"Xato! ❌ Siz tanladingiz: {ans}. To'g'ri javob: {current_q['a']}")
                
                if st.button("Keyingi savol ➡️"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.title("🏁 Test tugadi!")
            st.success(f"Siz {total_qs} tadan {st.session_state.user_score} ta to'g'ri javob berdingiz!")
            if st.session_state.user_score == total_qs:
                st.balloons()
            if st.button("Bosh sahifaga qaytish"):
                for key in ['test_started', 'current_q_index', 'user_score', 'active_questions', 'answered']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
