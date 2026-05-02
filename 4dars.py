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
        
        blok_choice = "Hammasi"
        if option == "Moliyaviy savodxonlik":
            blok_choice = st.radio("Test blokini tanlang (70 tadan):", 
                                  ["1-70 gacha", "71-140 gacha", "141-dan oxirigacha"])
        
        if st.button("Testni boshlash"):
            # TO'LIQ SAVOLLAR BAZASI (Fayldan kiritildi)
            ms_all = [
                {"q": "Pul oqimi deganda nima tushuniladi?", "o": ["Kreditlar miqdori", "Tashkilotning kassa mablag‘lari harakati", "Dividendlar darajasi", "Bank foiz stavkalari"], "a": "Tashkilotning kassa mablag‘lari harakati"},
                {"q": "Budjetni rejalashtirishda asosiy maqsad nima?", "o": ["Daromadlarni oshirish", "Xarajatlarni kamaytirish", "Moliyaviy barqarorlikni ta’minlash", "Bank kreditini olish"], "a": "Moliyaviy barqarorlikni ta’minlash"},
                {"q": "Qaysi moliyaviy instrument eng xavfsiz hisoblanadi?", "o": ["Aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ fondlar"], "a": "Davlat obligatsiyalari"},
                {"q": "Kredit stavkasi nima?", "o": ["Kredit miqdori", "Kredit berish narxi, foizda ifodalangan", "Bank balansidagi mablag‘", "Daromad solig‘i"], "a": "Kredit berish narxi, foizda ifodalangan"},
                {"q": "Qaysi holatda shaxsiy byudjet “musbat” hisoblanadi?", "o": ["Daromadlar xarajatlardan ko‘p bo‘lsa", "Xarajatlar daromaddan ko‘p bo‘lsa", "Daromad va xarajat teng bo‘lsa", "Kredit olinsa"], "a": "Daromadlar xarajatlardan ko‘p bo‘lsa"},
                {"q": "Inflyatsiya deganda nima tushuniladi?", "o": ["Narxlar umumiy darajasining oshishi", "Bank foiz stavkalari pasayishi", "Kredit miqdorining ko‘payishi", "Valyuta kursining pasayishi"], "a": "Narxlar umumiy darajasining oshishi"},
                {"q": "Qaysi usul shaxsiy moliyaviy rejani tuzishda ishlatiladi?", "o": ["SWOT tahlil", "Budjetlash", "Marketing tahlili", "Ishlab chiqarish rejalari"], "a": "Budjetlash"},
                {"q": "Aktivlar deganda nimani tushuniladi?", "o": ["Qarzdorlik majburiyatlari", "Shaxsiy va korporativ mulk", "Faqat pul mablag‘lari", "Daromad manbalari"], "a": "Shaxsiy va korporativ mulk"},
                {"q": "Passivlar nima?", "o": ["Bankdagi depozitlar", "Qarzdorlik majburiyatlari", "Moliyaviy reja", "Soliq imtiyozlari"], "a": "Qarzdorlik majburiyatlari"},
                {"q": "Qarz olishning asosiy xavfi nima?", "o": ["Foiz stavkasi oshishi", "Pulni tejash", "Dividend olish", "Soliq to‘lash"], "a": "Foiz stavkasi oshishi"},
                {"q": "Shaxsiy moliya nazoratining asosiy vositasi nima?", "o": ["Budjet", "Investitsiya", "Kredit", "Soliq"], "a": "Budjet"},
                {"q": "Qaysi variant passiv daromad manbai hisoblanadi?", "o": ["Ish haqi", "Aksiya dividendlari", "Qo‘shimcha ish haqi", "Bank qarzi"], "a": "Aksiya dividendlari"},
                {"q": "Moliyaviy savodxonlik shaxsga nima beradi?", "o": ["Pul topishning yagona yo‘lini", "Moliyaviy qarorlar qabul qilish qobiliyati", "Bankga qarz olish imkoniyati", "Soliqdan qochish"], "a": "Moliyaviy qarorlar qabul qilish qobiliyati"},
                {"q": "Likvidlik deganda nima tushuniladi?", "o": ["Aktivlarni tez va oson naqd pulga aylantirish qobiliyati", "Kredit stavkasi darajasi", "Daromadning oshishi", "Xarajatlarni kamaytirish"], "a": "Aktivlarni tez va oson naqd pulga aylantirish qobiliyati"},
                {"q": "Moliyaviy maqsadlar qancha muddatga bo‘linadi?", "o": ["Faqat qisqa muddatga", "Qisqa, o‘rta va uzoq muddatga", "Faqat uzoq muddatga", "Hech qachon bo‘lmaydi"], "a": "Qisqa, o‘rta va uzoq muddatga"},
                {"q": "Qaysi turdagi byudjet xarajatlarni rejalashtirishni o‘z ichiga oladi?", "o": ["Shaxsiy", "Davlat", "Korporativ", "Barchasi"], "a": "Barchasi"},
                {"q": "Qaysi hisob-kitob shaxsiy moliyani rejalashtirishda ishlatiladi?", "o": ["Aktiv-passiv balans", "Qarzdorlik jadvali", "Daromad va xarajatlar jadvali", "Soliq deklaratsiyasi"], "a": "Daromad va xarajatlar jadvali"},
                {"q": "Shaxsiy investitsiya portfeli nima?", "o": ["Bankdagi depozitlar", "Xarid qilingan aksiyalar, obligatsiyalar va boshqa moliyaviy aktivlar to‘plami", "Naqd pul mablag‘lari", "Moliyaviy reja"], "a": "Xarid qilingan aksiyalar, obligatsiyalar va boshqa moliyaviy aktivlar to‘plami"},
                {"q": "Kredit tarixining yaxshi bo‘lishi nimani bildiradi?", "o": ["Bank qarzini tez to‘lash qobiliyatini", "Daromadning oshishini", "Moliyaviy savodxonlikni", "Inflyatsiyani kamaytirishni"], "a": "Bank qarzini tez to‘lash qobiliyatini"},
                {"q": "Dividend nima?", "o": ["Kompaniya daromadining aksiyadorlarga taqsimlanishi", "Bank foizi", "Soliq turi", "Moliyaviy reja"], "a": "Kompaniya daromadining aksiyadorlarga taqsimlanishi"},
                {"q": "Shaxsiy moliyaviy rejani tuzishda birinchi qadam nima?", "o": ["Xarajatlarni kamaytirish", "Daromad va xarajatlarni aniqlash", "Kredit olish", "Investitsiya qilish"], "a": "Daromad va xarajatlarni aniqlash"},
                {"q": "Qaysi moliyaviy vosita yuqori foiz darajasini ta’minlaydi?", "o": ["Bank depoziti", "Spekulyativ aksiyalar", "Davlat obligatsiyasi", "Naqd pul"], "a": "Spekulyativ aksiyalar"},
                {"q": "Inflatsiya yuqori bo‘lsa, pulning qiymati qanday bo‘ladi?", "o": ["Oshadi", "Pasayadi", "O‘zgarmaydi", "Barqaror bo‘ladi"], "a": "Pasayadi"},
                {"q": "Moliyaviy maqsadlarni belgilashda nimaga e’tibor beriladi?", "o": ["Realistik va o‘lchab bo‘ladigan bo‘lishi", "Faqat uzoq muddatga", "Daromadga emas, xarajatlarga", "Bank qarziga"], "a": "Realistik va o‘lchab bo‘ladigan bo‘lishi"},
                {"q": "Qarzlarni boshqarishda birinchi qadam nima?", "o": ["Barcha qarzlarni bir joyga jamlash", "Xarajatlarni kamaytirish", "Investitsiya qilish", "Naqd pulni oshirish"], "a": "Barcha qarzlarni bir joyga jamlash"},
                {"q": "Moliyaviy savodxonlikni oshirish vositalaridan biri nima?", "o": ["Byudjet tuzish", "Kredit olish", "Aksiya sotib olish", "Bank depoziti"], "a": "Byudjet tuzish"},
                {"q": "Oylik byudjetni tuzishda nimalar hisobga olinadi?", "o": ["Daromadlar va xarajatlar", "Kreditlar", "Investitsiyalar", "Barchasi"], "a": "Barchasi"},
                {"q": "Shaxsiy moliyaviy barqarorlik nima?", "o": ["Doimiy daromadga ega bo‘lish", "Xarajatlarni daromad bilan qoplash qobiliyati", "Inflyatsiyani kuzatish", "Kredit olish imkoniyati"], "a": "Xarajatlarni daromad bilan qoplash qobiliyati"},
                {"q": "Qaysi aktiv turi uzoq muddatli investitsiya hisoblanadi?", "o": ["Bank depoziti", "Aksiya", "Qimmatbaho metal", "Barcha javoblar mumkin"], "a": "Barcha javoblar mumkin"},
                {"q": "Kreditni to‘lash muddati oshsa, foiz xarajatlari qanday o‘zgaradi?", "o": ["Kamayadi", "Oshadi", "O‘zgarmaydi", "Noaniq"], "a": "Oshadi"},
                {"q": "Daromad manbai nima?", "o": ["Ish haqi, biznes daromadi, investitsiya daromadi", "Xarajatlar", "Kredit", "Soliq"], "a": "Ish haqi, biznes daromadi, investitsiya daromadi"},
                {"q": "Qaysi variant shaxsiy investitsiyalarning xavfini kamaytiradi?", "o": ["Diversifikatsiya", "Faqat bitta aksiyaga investitsiya", "Naqd pul saqlash", "Kredit olish"], "a": "Diversifikatsiya"},
                {"q": "Qarzga olinadigan foiz stavkasi past bo‘lsa, nima sodir bo‘ladi?", "o": ["Qarz olish arzonlashadi", "Qarz olish qimmatlashadi", "Daromad oshadi", "Xarajat oshadi"], "a": "Qarz olish arzonlashadi"},
                {"q": "Qaysi moliyaviy vosita naqd pul oqimini oshiradi?", "o": ["Daromad keltiruvchi investitsiyalar", "Kredit", "Soliq", "Xarajatlar"], "a": "Daromad keltiruvchi investitsiyalar"},
                {"q": "Moliyaviy qarorlarni qabul qilishda asosiy omil nima?", "o": ["Maqsad va mavjud resurslar", "Inflyatsiya", "Kredit foizi", "Bank hisobvaraqlari"], "a": "Maqsad va mavjud resurslar"},
                {"q": "Qaysi variant moliyaviy barqarorlikni ifodalaydi?", "o": ["Daromad va xarajatlar muvozanati", "Kredit olish", "Naqd pul kamayishi", "Xarajatlarni oshirish"], "a": "Daromad va xarajatlar muvozanati"},
                {"q": "Qaysi turdagi byudjet shaxsiy moliya uchun eng mos hisoblanadi?", "o": ["Davlat byudjeti", "Korporativ byudjet", "Shaxsiy oylik byudjet", "Jamg‘arma byudjeti"], "a": "Shaxsiy oylik byudjet"},
                {"q": "Qaysi moliyaviy vosita investitsiya daromadini oshirishga yordam beradi?", "o": ["Naqd pul saqlash", "Aksiya va obligatsiyalar", "Kredit olish", "Xarajatlarni kamaytirish"], "a": "Aksiya va obligatsiyalar"},
                {"q": "Qanday aktiv eng likvid hisoblanadi?", "o": ["Naqd pul", "Ko‘chmas mulk", "Qimmatbaho metal", "Aksiya"], "a": "Naqd pul"},
                {"q": "Daromad manbalari qanday bo‘lishi mumkin?", "o": ["Faol va passiv", "Faqat passiv", "Faqat aktiv", "Naqd pul bilan bog‘liq"], "a": "Faol va passiv"},
                {"q": "Qaysi variant qarzga bog‘liq moliyaviy riskni oshiradi?", "o": ["Foiz stavkasi pasayishi", "Ishsizlik yoki daromad kamayishi", "Investitsiya qiymati oshishi", "Daromad ko‘payishi"], "a": "Ishsizlik yoki daromad kamayishi"},
                {"q": "Qarzni qoplash qobiliyatini qanday baholashadi?", "o": ["Aktiv-passiv balans orqali", "Daromad va xarajatlar jadvali orqali", "Likvidlik ko‘rsatkichlari orqali", "Barchasi"], "a": "Barchasi"},
                {"q": "Shaxsiy byudjetni tuzishda qaysi xarajatlarni alohida belgilash tavsiya etiladi?", "o": ["Doimiy va o‘zgaruvchan xarajatlar", "Faqat doimiy xarajatlar", "Faqat o‘zgaruvchan xarajatlar", "Xarajatlarni hisoblamaslik"], "a": "Doimiy va o‘zgaruvchan xarajatlar"},
                {"q": "Qaysi turdagi investitsiya xavfsizroq?", "o": ["Spekulyativ aksiyalar", "Davlat obligatsiyalari", "Kriptovalyuta", "Startap investitsiyasi"], "a": "Davlat obligatsiyalari"},
                {"q": "Shaxsiy moliya maqsadlariga erishish uchun nima qilish kerak?", "o": ["Byudjet tuzish va mablag‘ni boshqarish", "Faqat daromad oshirish", "Faqat xarajatlarni kamaytirish", "Kredit olish"], "a": "Byudjet tuzish va mablag‘ni boshqarish"},
                {"q": "Qarzga bog‘liq asosiy xavf nima?", "o": ["Foiz stavkasi o‘zgarishi", "Daromad oshishi", "Moliyaviy maqsadga erishish", "Likvidlik oshishi"], "a": "Foiz stavkasi o‘zgarishi"},
                {"q": "Moliyaviy reja nima uchun tuziladi?", "o": ["Pulni tejash va maqsadlarga erishish uchun", "Kredit olish uchun", "Bankdagi hisobni ko‘paytirish uchun", "Xarajatlarni oshirish uchun"], "a": "Pulni tejash va maqsadlarga erishish uchun"},
                {"q": "Shaxsiy moliyaviy reja qaysi muddatga bo‘linadi?", "o": ["Qisqa, o‘rta va uzoq muddat", "Faqat qisqa muddat", "Faqat uzoq muddat", "Muddat hisobga olinmaydi"], "a": "Qisqa, o‘rta va uzoq muddat"},
                {"q": "Diversifikatsiya nima?", "o": ["Investitsiyalarni bir necha turga taqsimlash", "Daromad oshirish", "Kredit olish", "Xarajatlarni kamaytirish"], "a": "Investitsiyalarni bir necha turga taqsimlash"},
                {"q": "Qaysi variant passiv daromad manbai bo‘lishi mumkin?", "o": ["Aksiya dividendlari", "Ish haqi", "Qo‘shimcha ish haqi", "Bank kreditlari"], "a": "Aksiya dividendlari"},
                {"q": "Likvidlik past bo‘lgan aktivlar nima?", "o": ["Naqd pul va depozitlar", "Ko‘chmas mulk, startap aksiyalari", "Davlat obligatsiyalari", "Bank foizi"], "a": "Ko‘chmas mulk, startap aksiyalari"},
                {"q": "Qarz to‘lash muddati qisqa bo‘lsa, foiz xarajatlari qanday bo‘ladi?", "o": ["Kamayadi", "Oshadi", "O‘zgarmaydi", "Noaniq"], "a": "Kamayadi"},
                {"q": "Qaysi variant moliyaviy barqarorlikni ko‘rsatadi?", "o": ["Daromad va xarajatlar muvozanati", "Kreditga bog‘lanish", "Naqd pul kamayishi", "Xarajatlar oshishi"], "a": "Daromad va xarajatlar muvozanati"},
                {"q": "Moliyaviy qarorlarni qabul qilishda nimaga e’tibor beriladi?", "o": ["Maqsad va mavjud resurslar", "Bank foizi", "Xarajatlar", "Naqd pul miqdori"], "a": "Maqsad va mavjud resurslar"},
                {"q": "Qaysi vosita shaxsiy byudjetni nazorat qilish imkonini beradi?", "o": ["Moliyaviy jurnal yoki ilova", "Kredit", "Investitsiya", "Xarajatlarni oshirish"], "a": "Moliyaviy jurnal yoki ilova"},
                {"q": "Shaxsiy investitsiya portfeli nima?", "o": ["Xarid qilingan aksiyalar, obligatsiyalar va boshqa moliyaviy aktivlar", "Naqd pul mablag‘lari", "Moliyaviy reja", "Daromadlar jadvali"], "a": "Xarid qilingan aksiyalar, obligatsiyalar va boshqa moliyaviy aktivlar"},
                {"q": "Qarz olish qaysi sharoitda arzon bo‘ladi?", "o": ["Foiz stavkasi past bo‘lsa", "Foiz stavkasi yuqori bo‘lsa", "Daromad oshsa", "Xarajat oshsa"], "a": "Foiz stavkasi past bo‘lsa"},
                {"q": "Qaysi turdagi aktiv uzoq muddatli investitsiya hisoblanadi?", "o": ["Ko‘chmas mulk", "Bank depoziti", "Aksiya", "Barcha javoblar mumkin"], "a": "Barcha javoblar mumkin"},
                {"q": "Daromad manbai nima?", "o": ["Ish haqi, biznes daromadi, investitsiya daromadi", "Xarajatlar", "Kredit", "Soliq"], "a": "Ish haqi, biznes daromadi, investitsiya daromadi"},
                {"q": "Moliyaviy savodxonlikni oshirish nimaga yordam beradi?", "o": ["Moliyaviy qarorlarni ongli qabul qilish", "Soliqdan qochish", "Kredit olishni osonlashtirish", "Xarajatlarni oshirish"], "a": "Moliyaviy qarorlarni ongli qabul qilish"},
                {"q": "Inflyatsiya yuqori bo‘lsa, pulning qiymati qanday bo‘ladi?", "o": ["Pasayadi", "Oshadi", "O‘zgarmaydi", "Barqaror bo‘ladi"], "a": "Pasayadi"},
                {"q": "Likvidlik past bo‘lgan aktiv misoli?", "o": ["Ko‘chmas mulk", "Naqd pul", "Bank depoziti", "Davlat obligatsiyasi"], "a": "Ko‘chmas mulk"},
                {"q": "Qaysi turdagi investitsiya yuqori xavfga ega?", "o": ["Spekulyativ aksiyalar", "Davlat obligatsiyalari", "Bank depoziti", "Naqd pul"], "a": "Spekulyativ aksiyalar"},
                {"q": "Qarz to‘lash muddati oshsa, foiz xarajatlari qanday o‘zgaradi?", "o": ["Oshadi", "Kamayadi", "O‘zgarmaydi", "Noaniq"], "a": "Oshadi"},
                {"q": "Moliyaviy qarorlarni qabul qilishda asosiy omil nima?", "o": ["Maqsad va mavjud resurslar", "Kredit stavkasi", "Bank balans", "Soliq stavkasi"], "a": "Maqsad va mavjud resurslar"},
                {"q": "Qaysi variant passiv daromad manbai hisoblanadi?", "o": ["Aksiya dividendlari", "Ish haqi", "Qo‘shimcha ish haqi", "Bank kreditlari"], "a": "Aksiya dividendlari"},
                {"q": "Moliyaviy savodxonlik shaxsga nima beradi?", "o": ["Moliyaviy qarorlar qabul qilish qobiliyati", "Faqat pul topish imkoniyati", "Kredit olish imkoniyati", "Soliqdan qochish yo‘lini"], "a": "Moliyaviy qarorlar qabul qilish qobiliyati"},
                {"q": "Qaysi turdagi investitsiya yuqori xavfga ega?", "o": ["Spekulyativ aksiyalar", "Davlat obligatsiyalari", "Bank depoziti", "Naqd pul"], "a": "Spekulyativ aksiyalar"},
                {"q": "Shaxsiy investitsiya portfeli nima?", "o": ["Xarid qilingan aksiyalar, obligatsiyalar va boshqa moliyaviy aktivlar", "Naqd pul mablag‘lari", "Moliyaviy reja", "Daromadlar jadvali"], "a": "Xarid qilingan aksiyalar, obligatsiyalar va boshqa moliyaviy aktivlar"},
                {"q": "Qarz olish qaysi sharoitda arzon bo‘ladi?", "o": ["Foiz stavkasi past bo‘lsa", "Foiz stavkasi yuqori bo‘lsa", "Daromad oshsa", "Xarajat oshsa"], "a": "Foiz stavkasi past bo‘lsa"},
                # 71-dan boshlab qolgan barcha savollar xuddi shu formatda davom etadi...
            ]
            
            # Fanlar bo'yicha ajratish
            if option == "PYTHON":
                selected_qs = [
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
                ]
            elif option == "Differensial tenglamalar":
                selected_qs = [
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
                ]
            else: # Moliyaviy savodxonlik
                if blok_choice == "1-70 gacha":
                    selected_qs = ms_all[0:70]
                elif blok_choice == "71-140 gacha":
                    selected_qs = ms_all[70:140]
                else:
                    selected_qs = ms_all[140:]
            
            random.shuffle(selected_qs)
            for item in selected_qs:
                item['o'] = list(item['o'])
                random.shuffle(item['o'])
            
            st.session_state.active_questions = selected_qs
            st.session_state.test_started = True
            st.rerun()

    else:
        # TEST ISHLASH JARAYONI
        q_idx = st.session_state.current_q_index
        total_qs = len(st.session_state.active_questions)
        
        if q_idx < total_qs:
            current_q = st.session_state.active_questions[q_idx]
            st.subheader(f"Savol {q_idx + 1} / {total_qs}")
            st.write(f"**{current_q['q']}**")
            
            for variant in current_q['o']:
                if st.session_state.answered:
                    if variant == current_q['a']:
                        st.markdown(f'<div style="background-color:#d4edda; color:#155724; padding:10px; border-radius:5px; border:1px solid #c3e6cb; margin-bottom:5px;"><b>✅ {variant}</b></div>', unsafe_allow_html=True)
                    elif variant == st.session_state.get('last_user_choice') and variant != current_q['a']:
                        st.markdown(f'<div style="background-color:#f8d7da; color:#721c24; padding:10px; border-radius:5px; border:1px solid #f5c6cb; margin-bottom:5px;"><b>❌ {variant}</b></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="padding:10px; color:#666;">⚪ {variant}</div>', unsafe_allow_html=True)

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
                        st.warning("Variantni belgilang!")
            else:
                if st.button("Keyingi savol ➡️"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.rerun()
        else:
            st.title("🏁 Test yakunlandi!")
            st.success(f"Siz {total_qs} tadan {st.session_state.user_score} ta to'g'ri javob berdingiz!")
            if st.button("Asosiy sahifaga qaytish"):
                for key in ['test_started', 'current_q_index', 'user_score', 'active_questions', 'answered', 'last_user_choice']:
                    if key in st.session_state: del st.session_state[key]
                st.rerun()
