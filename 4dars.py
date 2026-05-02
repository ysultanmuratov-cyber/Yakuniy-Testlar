import streamlit as st
import random
import time

# --- SAHIFA SOZLAMALARI ---
st.set_page_config(page_title="Testlar Markazi", layout="centered")

# --- SAVOLLAR BAZASI ---
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = {
        "PYTHON": [
            {"q": "Python qaysi yili yaratilgan?", "o": ["1991", "1985", "2000", "2010"], "a": "1991"},
            {"q": "O'zgaruvchi turini aniqlash funksiyasi?", "o": ["type()", "id()", "print()", "input()"],
             "a": "type()"},
            {"q": "Ro'yxatga oxiridan element qo'shish usuli?", "o": ["append()", "add()", "push()", "insert()"],
             "a": "append()"},
            {"q": "Qaysi operator darajaga ko'taradi?", "o": ["**", "^", "//", "%"], "a": "**"},
            {"q": "Lug'at (dictionary) qaysi qavslar bilan yoziladi?", "o": ["{}", "[]", "()", "<>"], "a": "{}"},
            {"q": "O'zgarmas ro'yxat turi nima deyiladi?", "o": ["tuple", "list", "set", "dictionary"], "a": "tuple"},
            {"q": "Qatorni ekranga chiqarish funksiyasi?", "o": ["print()", "echo()", "write()", "output()"],
             "a": "print()"},
            {"q": "Butun son turi qanday belgilanadi?", "o": ["int", "float", "str", "bool"], "a": "int"},
            {"q": "Shartli operatorni ko'rsating?", "o": ["if", "for", "while", "def"], "a": "if"},
            {"q": "Funksiya yaratish kalit so'zi?", "o": ["def", "func", "function", "create"], "a": "def"}
        ],
        "Differensial tenglamalar": [
            {"q": "y' = f(x,y) qanday tenglama?", "o": ["1-tartibli", "2-tartibli", "Bernoulli", "Chiziqli"],
             "a": "1-tartibli"},
            {"q": "Puasson formulasi nima uchun ishlatiladi?", "o": ["Ehtimollik", "Integral", "Hajm", "Tezlik"],
             "a": "Ehtimollik"},
            {"q": "Bernoulli tenglamasi qaysi ko'rinishda?",
             "o": ["y' + Py = Qy^n", "y' = f(x)", "y'' + p = 0", "y = kx+b"], "a": "y' + Py = Qy^n"},
            {"q": "Chiziqli differensial tenglamaning tartibi nimaga bog'liq?",
             "o": ["Yuqori hosilaga", "Erkli o'zgaruvchiga", "Yechim soniga", "Integralga"], "a": "Yuqori hosilaga"},
            {"q": "Garmonik tebranish tenglamasi qanday tartibli?",
             "o": ["2-tartibli", "1-tartibli", "3-tartibli", "4-tartibli"], "a": "2-tartibli"},
            {"q": "Differensial tenglamaning umumiy yechimi nimani o'z ichiga oladi?",
             "o": ["O'zgarmas C ni", "Faqat sonlarni", "Faqat x ni", "Integralni"], "a": "O'zgarmas C ni"},
            {"q": "y'' + w^2y = 0 tenglamaning yechimi?", "o": ["Sinus/Kosinus", "Eksponenta", "Logarifm", "Polinom"],
             "a": "Sinus/Kosinus"},
            {"q": "Koshi masalasi nimani topishni talab qiladi?",
             "o": ["Xususiy yechimni", "Umumiy yechimni", "Integralni", "Limitni"], "a": "Xususiy yechimni"},
            {"q": "Eyler usuli nima uchun qo'llaniladi?",
             "o": ["Sonli yechish", "Aniq integrallash", "Hosila olish", "Soddalashtirish"], "a": "Sonli yechish"},
            {"q": "Bir jinsli tenglamada f(tx, ty) nimaga teng?", "o": ["f(x,y)", "t*f(x,y)", "f(x)/t", "0"],
             "a": "f(x,y)"}
        ],
        "Moliyaviy savodxonlik": [
            {"q": "Inflyatsiya nima?", "o": ["Narx oshishi", "Narx tushishi", "Soliq", "Qarz"], "a": "Narx oshishi"},
            {"q": "Aktiv nima?", "o": ["Daromad keltiruvchi", "Xarajat keltiruvchi", "Qarz", "Soliq"],
             "a": "Daromad keltiruvchi"},
            {"q": "Passiv nima?", "o": ["Xarajat keltiruvchi", "Daromad keltiruvchi", "Mulk", "Sarmoya"],
             "a": "Xarajat keltiruvchi"},
            {"q": "Diversifikatsiya nima?", "o": ["Xavfni bo'lish", "Pul yig'ish", "Kredit olish", "Soliq to'lash"],
             "a": "Xavfni bo'lish"},
            {"q": "Murakkab foiz nima?", "o": ["Foizdan foiz", "Oddiy foiz", "Kredit foizi", "Soliq turi"],
             "a": "Foizdan foiz"},
            {"q": "Likvidlik nima?", "o": ["Tez pulga aylanish", "Qarz miqdori", "Soliq stavkasi", "Foyda foizi"],
             "a": "Tez pulga aylanish"},
            {"q": "Budjet nima?", "o": ["Kirim va chiqim rejasi", "Faqat daromad", "Soliq yig'indisi", "Bank hisobi"],
             "a": "Kirim va chiqim rejasi"},
            {"q": "Keshbek (Cashback) nima?",
             "o": ["Pulning bir qismini qaytishi", "Qarz olish", "Soliq to'lash", "Xizmat haqi"],
             "a": "Pulning bir qismini qaytishi"},
            {"q": "Depozit nima?", "o": ["Bankdagi omonat", "Kredit", "Soliq", "Sug'urta"], "a": "Bankdagi omonat"},
            {"q": "Aktsiya nima?", "o": ["Ulishli qimmatli qog'oz", "Qarz qog'ozi", "Soliq kvitansiyasi", "Shartnoma"],
             "a": "Ulishli qimmatli qog'oz"}
        ]
    }

# --- SESSION STATE INICIALIZATSIYA ---
if 'step' not in st.session_state:
    st.session_state.step = "main"
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_idx' not in st.session_state:
    st.session_state.current_idx = 0

# --- 1. ASOSIY SAHIFA ---
if st.session_state.step == "main":
    st.title("🎯 Testlar Markazi")
    subject = st.selectbox("Fanni tanlang:", list(st.session_state.quiz_data.keys()))

    if st.button("Testni boshlash", use_container_width=True):
        st.session_state.selected_subject = subject
        st.session_state.questions = list(st.session_state.quiz_data[subject])
        random.shuffle(st.session_state.questions)
        st.session_state.current_idx = 0
        st.session_state.score = 0
        st.session_state.step = "quiz"
        st.rerun()

# --- 2. TEST SAHIFASI ---
elif st.session_state.step == "quiz":
    q_num = st.session_state.current_idx
    questions = st.session_state.questions

    if q_num < len(questions):
        st.subheader(f"{q_num + 1}-savol")
        st.write(questions[q_num]['q'])

        # Variantlar
        options = list(questions[q_num]['o'])
        # Optionlarni faqat bir marta aralashtirish uchun keshlaymiz
        if f"opt_{q_num}" not in st.session_state:
            random.shuffle(options)
            st.session_state[f"opt_{q_num}"] = options

        selected_opt = st.radio("Javobni tanlang:", st.session_state[f"opt_{q_num}"], index=None)

        if st.button("Javobni tasdiqlash", use_container_width=True):
            if selected_opt == questions[q_num]['a']:
                st.success("To'g'ri!")
                st.session_state.score += 1
            else:
                st.error(f"Noto'g'ri! To'g'ri javob: {questions[q_num]['a']}")

            time.sleep(1)  # Natijani ko'rib olish uchun kichik tanaffus
            st.session_state.current_idx += 1
            st.rerun()

        if st.button("Testni yakunlash"):
            st.session_state.step = "result"
            st.rerun()
    else:
        st.session_state.step = "result"
        st.rerun()

# --- 3. NATIJA SAHIFASI ---
elif st.session_state.step == "result":
    st.title("📊 Natijangiz")
    st.balloons()  # Bayramona effekt
    st.header(f"Siz 10 tadan {st.session_state.score} ta to'g'ri topdingiz!")

    if st.button("Bosh menyuga qaytish", use_container_width=True):
        st.session_state.step = "main"
        st.rerun()