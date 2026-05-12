import streamlit as st
import random
import pandas as pd
from datetime import datetime
import os

def save_log(user, subject, score, total):
    log_file = "user_logs.csv"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = pd.DataFrame([[now, user, subject, score, total]], 
                            columns=['Vaqt', 'Foydalanuvchi', 'Fan', 'Ball', 'Jami'])
    
    if not os.path.isfile(log_file):
        new_data.to_csv(log_file, index=False)
    else:
        new_data.to_csv(log_file, mode='a', header=False, index=False)

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# To'liq Premium CSS (Yuqoriga surilgan varianti)
st.markdown("""
    <style>
    /* Sahifani eng yuqoriga majburan ko'tarish */
    .stApp {
        margin-top: -100px !important; /* Bu qiymatni oshirsangiz yanada tepaga chiqadi */
    }
    
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }

    /* Tepadagi ortiqcha bo'sh joylarni (header) butunlay yo'q qilish */
    header, [data-testid="stHeader"] {
        display: none !important;
    }

    /* Elementlar orasini yanada zich qilish */
    [data-testid="stVerticalBlock"] {
        gap: 0.2rem !important;
    }
    
    /* Logotipni tepaga taqash */
    .logo-container {
        margin-top: 0px !important;
        padding-top: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)
# 3. Savollar Bazasi
# 1-70 bloki
if 'ms_1_70' not in st.session_state:
    st.session_state.ms_1_70 = [
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
]

# 71-140 bloki
if 'ms_71_140' not in st.session_state:
    st.session_state.ms_71_140 = [
        {"q": "Qaysi vosita shaxsiy byudjetni nazorat qilish imkonini beradi?", "o": ["Moliyaviy jurnal yoki ilova", "Kredit", "Investitsiya", "Naqd pul"], "a": "Moliyaviy jurnal yoki ilova"},
        {"q": "Shaxsiy moliyaviy reja qaysi muddatga bo‘linadi?", "o": ["Qisqa, o‘rta va uzoq muddat", "Faqat qisqa muddat", "Faqat uzoq muddat", "Muddat hisobga olinmaydi"], "a": "Qisqa, o‘rta va uzoq muddat"},
        {"q": "Qaysi turdagi aktiv yuqori likvidlikka ega?", "o": ["Naqd pul", "Ko‘chmas mulk", "Startap aksiyalari", "Qimmatbaho metal"], "a": "Naqd pul"},
        {"q": "Diversifikatsiya nima?", "o": ["Investitsiyalarni bir necha turga taqsimlash", "Daromad oshirish", "Kredit olish", "Xarajatlarni kamaytirish"], "a": "Investitsiyalarni bir necha turga taqsimlash"},
        {"q": "Qaysi turdagi daromad faol hisoblanadi?", "o": ["Ish haqi", "Aksiya dividendlari", "Passiv investitsiyalar", "Bank foizi"], "a": "Ish haqi"},
        {"q": "Qarzga bog‘liq asosiy xavf nima?", "o": ["Foiz stavkasi o‘zgarishi", "Daromad oshishi", "Moliyaviy maqsadga erishish", "Likvidlik oshishi"], "a": "Foiz stavkasi o‘zgarishi"},
        {"q": "Shaxsiy moliyaviy barqarorlik nima?", "o": ["Daromad va xarajatlar muvozanati", "Kredit olish imkoniyati", "Bank depozitlari mavjudligi", "Xarajatlarni oshirish"], "a": "Daromad va xarajatlar muvozanati"},
        {"q": "Moliyaviy reja tuzishdan maqsad nima?", "o": ["Maqsadlarga erishish va mablag‘ni boshqarish", "Kredit olish", "Xarajatlarni oshirish", "Bank depozitini oshirish"], "a": "Maqsadlarga erishish va mablag‘ni boshqarish"},
        {"q": "Qaysi aktiv uzoq muddatli investitsiya hisoblanadi?", "o": ["Ko‘chmas mulk", "Bank depoziti", "Aksiya", "Barcha javoblar mumkin"], "a": "Barcha javoblar mumkin"},
        {"q": "Daromad manbai nima?", "o": ["Ish haqi, biznes daromadi, investitsiya daromadi", "Xarajatlar", "Kredit", "Soliq"], "a": "Ish haqi, biznes daromadi, investitsiya daromadi"},
        {"q": "Moliyaviy qarorlarni qabul qilishda nimaga e’tibor beriladi?", "o": ["Maqsad va resurslar", "Bank foizlari", "Kredit stavkasi", "Soliq stavkasi"], "a": "Maqsad va resurslar"},
        {"q": "Shaxsiy moliyaviy maqsadlarni belgilashda eng muhim omil nima?", "o": ["Realistik bo‘lishi", "Bank qarzi", "Inflyatsiya", "Xarajatlarni oshirish"], "a": "Realistik bo‘lishi"},
        {"q": "Likvidlik past bo‘lgan aktivlar misoli?", "o": ["Ko‘chmas mulk", "Naqd pul", "Bank depoziti", "Davlat obligatsiyasi"], "a": "Ko‘chmas mulk"},
        {"q": "Shaxsiy byudjetni nazorat qilish vositasi nima?", "o": ["Moliyaviy jurnal yoki ilova", "Kredit", "Investitsiya", "Naqd pul"], "a": "Moliyaviy jurnal yoki ilova"},
        {"q": "Qaysi turdagi investitsiya xavfsizroq hisoblanadi?", "o": ["Davlat obligatsiyalari", "Kriptovalyuta", "Spekulyativ aksiyalar", "Startap investitsiyasi"], "a": "Davlat obligatsiyalari"},
        {"q": "Qaysi variant shaxsiy byudjetni “qizil rangda” ko‘rsatadi?", "o": ["Xarajatlar daromaddan ko‘p bo‘lsa", "Daromadlar xarajatdan ko‘p bo‘lsa", "Daromad va xarajat teng bo‘lsa", "Kredit olingan bo‘lsa"], "a": "Xarajatlar daromaddan ko‘p bo‘lsa"},
        {"q": "Qarz to‘lash muddati qisqa bo‘lsa, foiz xarajatlari qanday bo‘ladi?", "o": ["Kamayadi", "Oshadi", "O‘zgarmaydi", "Noaniq"], "a": "Kamayadi"},
        {"q": "Shaxsiy moliyaviy barqarorlikni qanday aniqlash mumkin?", "o": ["Daromad va xarajatlar muvozanati orqali", "Naqd pul mavjudligi orqali", "Bank depozitlari orqali", "Kredit olish orqali"], "a": "Daromad va xarajatlar muvozanati orqali"},
        {"q": "Moliyaviy riskni kamaytirishning eng samarali yo‘li nima?", "o": ["Diversifikatsiya", "Kredit olish", "Xarajatlarni oshirish", "Naqd pul saqlash"], "a": "Diversifikatsiya"},
        {"q": "Qaysi turdagi daromad passiv hisoblanadi?", "o": ["Aksiya dividendlari", "Ish haqi", "Qo‘shimcha ish haqi", "Faqat bank foizi"], "a": "Aksiya dividendlari"},
        {"q": "Shaxsiy moliyaviy reja qaysi elementlarni o‘z ichiga oladi?", "o": ["Daromadlar, xarajatlar, investitsiyalar, qarzlar", "Faqat daromadlar", "Faqat xarajatlar", "Faqat qarzlar"], "a": "Daromadlar, xarajatlar, investitsiyalar, qarzlar"},
        {"q": "Nima uchun daromad va xarajatlarni muntazam kuzatib borish moliyaviy barqarorlikka erishishda muhim hisoblanadi?", "o": ["Bu sizga daromadni oshirish imkonini beradi", "Xarajatlarni nazorat qilish va moliyaviy maqsadlarga erishishga yordam beradi", "Bank kreditini olishni kafolatlaydi", "Faqat soliqlarni kamaytiradi"], "a": "Xarajatlarni nazorat qilish va moliyaviy maqsadlarga erishishga yordam beradi"},
        {"q": "Inflyatsiya yuqori bo‘lganda, jamg‘armangiz faqat naqd puldan iborat bo‘lsa, uzoq muddatda bu qanday oqibatlarga olib kelishi mumkin?", "o": ["Pulning qiymati oshadi va xarid qobiliyati ko‘payadi", "Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati barqaror bo‘ladi, hech qanday o‘zgarish bo‘lmaydi", "Pul naqd holatda xavfsiz hisoblanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Qaysi sababga ko‘ra shaxsiy reja barcha moliyaviy elementlarni o‘z ichiga olishi muhim?", "o": ["Chunki bu faqat bank qarzini olish uchun kerak", "Chunki barcha moliyaviy resurslarni nazorat qilish va ongli qaror qabul qilish imkonini beradi", "Chunki bu soliqlarni kamaytiradi", "Chunki bu xarajatlarni oshirishni kafolatlaydi"], "a": "Chunki barcha moliyaviy resurslarni nazorat qilish va ongli qaror qabul qilish imkonini beradi"},
        {"q": "Yuqori foiz stavkali kreditni uzoq muddatga olish byudjetga qanday ta’sir qilishi mumkin?", "o": ["Xarajatlar kamayadi va moliyaviy barqarorlik oshadi", "Foiz xarajatlari ko‘payadi va byudjet muvozanati buzilishi mumkin", "Daromadlar oshadi", "Xarajatlar o‘zgarmaydi"], "a": "Foiz xarajatlari ko‘payadi va byudjet muvozanati buzilishi mumkin"},
        {"q": "Qarzlarni konsolidatsiya qilish qanday moliyaviy foyda keltirishi mumkin?", "o": ["Qarzlarni oson boshqarish va foiz stavkasini kamaytirish imkoniyati", "Daromadni oshirish", "Soliqni kamaytirish", "Naqd pul miqdorini oshirish"], "a": "Qarzlarni oson boshqarish va foiz stavkasini kamaytirish imkoniyati"},
        {"q": "Nima uchun diversifikatsiya moliyaviy xavfni kamaytiradi?", "o": ["Chunki barcha investitsiyalar bir xil daromad beradi", "Chunki turli aktivlar orqali birining yo‘qotishi boshqasining daromadi bilan qoplanadi", "Chunki diversifikatsiya foiz stavkasini oshiradi", "Chunki bu naqd pulni ko‘paytiradi"], "a": "Chunki turli aktivlar orqali birining yo‘qotishi boshqasining daromadi bilan qoplanadi"},
        {"q": "Byudjet “qizil rangda” bo‘lishi moliyaviy barqarorlik uchun qanday xavf tug‘diradi?", "o": ["Xarajatlarni nazorat qilish osonlashadi", "Qarzga bog‘lanish, jamg‘arma kamayishi va moliyaviy stress", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Qarzga bog‘lanish, jamg‘arma kamayishi va moliyaviy stress"},
        {"q": "Qaysi sababga ko‘ra portfelni turli moliyaviy aktivlar bilan diversifikatsiya qilish tavsiya etiladi?", "o": ["Faqat aksiyalar daromad keltiradi", "Turli aktivlar xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Bu naqd pulni oshiradi"], "a": "Turli aktivlar xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi"},
        {"q": "Nima uchun SMART tamoyili moliyaviy rejani samarali qiladi?", "o": ["Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib, monitoring qilish mumkin bo‘ladi", "Chunki bank qarzini olish osonlashadi", "Chunki xarajatlarni oshirish imkoniyati paydo bo‘ladi", "Chunki foiz stavkasi oshadi"], "a": "Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib, monitoring qilish mumkin bo‘ladi"},
        {"q": "Shaxsiy byudjetni nazorat qilishda moliyaviy ilovalardan foydalanish qanday foyda beradi?", "o": ["Daromad va xarajatlarni aniq kuzatish va byudjetni muvozanatda saqlash", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Daromad va xarajatlarni aniq kuzatish va byudjetni muvozanatda saqlash"},
        {"q": "Nima uchun shaxsiy moliya uchun passiv daromad manbalarini yaratish tavsiya etiladi?", "o": ["Chunki passiv daromad qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Chunki bu bank kreditini olishni kafolatlaydi", "Chunki xarajatlarni oshirish imkoniyatini beradi", "Chunki inflyatsiya kamayadi"], "a": "Chunki passiv daromad qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Yuqori foizli qarzga ega bo‘lish moliyaviy qarorlaringizga qanday ta’sir qilishi mumkin?", "o": ["Foiz xarajatlari ko‘payib, shaxsiy byudjet qiyinlashadi", "Xarajatlar kamayadi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Foiz xarajatlari ko‘payib, shaxsiy byudjet qiyinlashadi"},
        {"q": "Daromad va xarajatlarni yozib borish moliyaviy savodxonlik uchun qanday foyda beradi?", "o": ["Xarajatlarni nazorat qilish va maqsadlarga erishish imkonini beradi", "Faqat daromad oshiradi", "Kredit olishni kafolatlaydi", "Soliqni kamaytiradi"], "a": "Xarajatlarni nazorat qilish va maqsadlarga erishish imkonini beradi"},
        {"q": "Nima uchun faqat bir turdagi aktivdan iborat portfel yuqori xavfga ega?", "o": ["Chunki bitta aktiv qiymati tushsa, butun portfel qiymati sezilarli pasayadi", "Chunki bitta aktiv barqaror daromad beradi", "Chunki diversifikatsiya ortadi", "Chunki bu naqd pul hisoblanadi"], "a": "Chunki bitta aktiv qiymati tushsa, butun portfel qiymati sezilarli pasayadi"},
        {"q": "Nima uchun moliyaviy maqsadlarni SMART tamoyili bo‘yicha aniq va o‘lchab bo‘ladigan qilib belgilash muhim?", "o": ["Chunki bu rejani amalga oshirish va monitoring qilish imkonini beradi", "Chunki bu faqat kredit olishni osonlashtiradi", "Chunki xarajatlarni oshiradi", "Chunki bank foizini oshiradi"], "a": "Chunki bu rejani amalga oshirish va monitoring qilish imkonini beradi"},
        {"q": "Xarajatlar daromaddan oshib ketganda qanday choralarni ko‘rish maqsadga muvofiq?", "o": ["Xarajatlarni qisqartirish, qo‘shimcha daromad manbalarini yaratish", "Xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni qisqartirish, qo‘shimcha daromad manbalarini yaratish"},
        {"q": "Qarzlarni konsolidatsiya qilish (birlashtirish) qanday foyda beradi?", "o": ["Qarzlarni boshqarish osonlashadi va foiz stavkasi kamayishi mumkin", "Daromad oshadi", "Xarajatlar oshadi", "Naqd pul kamayadi"], "a": "Qarzlarni boshqarish osonlashadi va foiz stavkasi kamayishi mumkin"},
        {"q": "Passiv daromad manbalarini yaratishning asosiy afzalligi nimada?", "o": ["Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Foiz stavkasi oshadi"], "a": "Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun investitsiya portfelida turli aktivlar (aksiya, obligatsiya, metall) bo‘lishi tavsiya etiladi?", "o": ["Xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Faqat aksiyalar daromad beradi", "Bu naqd pulni ko‘paytiradi"], "a": "Xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi"},
        {"q": "Byudjetni ilova yoki jurnal yordamida nazorat qilish qanday natija beradi?", "o": ["Daromad va xarajatlarni aniq kuzatish va byudjetni muvozanatda saqlash", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Daromad va xarajatlarni aniq kuzatish va byudjetni muvozanatda saqlash"},
        {"q": "Muntazam ravishda xarajatlar oshib ketganda qanday nazorat choralari ko‘riladi?", "o": ["Xarajatlarni yozib borish, byudjet tuzish va passiv daromad yaratish", "Faqat xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni yozib borish, byudjet tuzish va passiv daromad yaratish"},
        {"q": "Nima uchun faqat bitta turdagi aktivga (masalan, faqat yuqori xavfli) investitsiya qilish tavsiya etilmaydi?", "o": ["Bitta aktiv qiymati tushsa, butun portfel sezilarli zarar ko‘radi", "Bu naqd pulni oshiradi", "Bu daromadni kafolatlaydi", "Foiz stavkasi pasayadi"], "a": "Bitta aktiv qiymati tushsa, butun portfel sezilarli zarar ko‘radi"},
        {"q": "SMART tamoyili moliyaviy maqsadlarni qanday samarali qiladi?", "o": ["Maqsadlar aniq bo‘lib, ularni amalga oshirish rejasi va monitoringi shakllanadi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkoniyatini beradi", "Bank foizini oshiradi"], "a": "Maqsadlar aniq bo‘lib, ularni amalga oshirish rejasi va monitoringi shakllanadi"},
        {"q": "Qarzlarni birlashtirish moliyaviy jihatdan qanday yengillik yaratadi?", "o": ["Boshqarish osonlashadi, foiz kamayadi va moliyaviy stress pasayadi", "Daromad oshadi", "Xarajatlar oshadi", "Naqd pul kamayadi"], "a": "Boshqarish osonlashadi, foiz kamayadi va moliyaviy stress pasayadi"},
        {"q": "Nima uchun shaxsiy byudjetda naqd pul, qarz, investitsiya va xarajatlarni birlashtirish muhim?", "o": ["Barcha resurslarni nazorat qilish va ongli qarorlar qabul qilish uchun", "Faqat bank qarzini olish uchun", "Soliqlarni kamaytirish uchun", "Xarajatlarni oshirish uchun"], "a": "Barcha resurslarni nazorat qilish va ongli qarorlar qabul qilish uchun"},
        {"q": "Nima sababli faqat bir turdagi aktivdan (masalan, aksiya) iborat portfel yuqori xavfga ega?", "o": ["Bitta aktiv qiymati tushsa, portfel qiymati sezilarli pasayadi", "Diversifikatsiya ortadi", "Bu naqd pul hisoblanadi", "Bitta aktiv barqaror daromad beradi"], "a": "Bitta aktiv qiymati tushsa, portfel qiymati sezilarli pasayadi"},
        {"q": "Passiv daromad manbalarini yaratish shaxsiy moliya uchun nima beradi?", "o": ["Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Foiz stavkasi oshadi"], "a": "Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun turli moliyaviy aktivlarga (aksiya, obligatsiya, metall) investitsiya qilish tavsiya etiladi?", "o": ["Xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi", "Faqat metallar xavfsiz", "Faqat aksiyalar daromad beradi", "Bu naqd pulni ko‘paytiradi"], "a": "Xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi"},
        {"q": "Oylik byudjetni ilova yoki jurnalda nazorat qilish qanday foyda beradi?", "o": ["Maqsadlarga erishish va byudjetni muvozanatda saqlash imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Maqsadlarga erishish va byudjetni muvozanatda saqlash imkonini beradi"},
        {"q": "Inflyatsiya yuqori bo‘lganda, faqat naqd pul saqlash qanday oqibatga olib keladi?", "o": ["Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati oshadi va xarid qobiliyati ko‘payadi", "Pul qiymati barqaror bo‘ladi", "Barqaror daromad ta’minlanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Doimiy daromad bo'la turib xarajatlar oshib ketsa, qaysi choralar samarali?", "o": ["Xarajatlarni yozish, byudjet tuzish va passiv daromad yaratish", "Faqat xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni yozish, byudjet tuzish va passiv daromad yaratish"},
        {"q": "Yuqori foizli qarzga ega bo‘lish moliyaviy qarorlarga qanday ta’sir qiladi?", "o": ["Foiz xarajatlari ko‘payib, byudjet qiyinlashadi", "Xarajatlar kamayadi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Foiz xarajatlari ko‘payib, byudjet qiyinlashadi"},
        {"q": "Byudjet tuzish va xarajatlarni yozib borish savodxonlikni qanday oshiradi?", "o": ["Xarajatlarni nazorat qilish va maqsadlarga erishish imkonini beradi", "Faqat daromad oshiradi", "Kredit olishni kafolatlaydi", "Soliqni kamaytiradi"], "a": "Xarajatlarni nazorat qilish va maqsadlarga erishish imkonini beradi"},
        {"q": "Investitsiya portfelida faqat aksiyalar bo'lishi qanday xavf tug‘diradi?", "o": ["Bitta aktiv qiymati tushsa, umumiy qiymat sezilarli pasayadi", "Diversifikatsiya ortadi", "Bu naqd pul hisoblanadi", "Bitta aktiv barqaror daromad beradi"], "a": "Bitta aktiv qiymati tushsa, umumiy qiymat sezilarli pasayadi"},
        {"q": "Shaxsiy moliyaviy maqsadlarni SMART tamoyili asosida belgilash qanday foyda beradi?", "o": ["Maqsadlar aniq bo‘lib, monitoring qilish imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Bank foizini oshiradi"], "a": "Maqsadlar aniq bo‘lib, monitoring qilish imkonini beradi"},
        {"q": "Qarzlarni konsolidatsiya qilish (birlashtirish) qanday foyda keltiradi?", "o": ["Qarzlarni boshqarish osonlashadi va moliyaviy stress kamayadi", "Daromad oshadi", "Xarajatlar oshadi", "Naqd pul kamayadi"], "a": "Qarzlarni boshqarish osonlashadi va moliyaviy stress kamayadi"},
        {"q": "Passiv daromad manbalarini yaratish moliyaviy barqarorlikni qanday oshiradi?", "o": ["Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Foiz stavkasi oshadi"], "a": "Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun turli moliyaviy aktivlarga (aksiya, obligatsiya, metall) investitsiya qilish tavsiya etiladi?", "o": ["Xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Faqat aksiyalar daromad beradi", "Bu naqd pulni ko‘paytiradi"], "a": "Xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi"},
        {"q": "Oylik byudjetni ilova yordamida nazorat qilish qanday foyda beradi?", "o": ["Xarajatlarni aniq kuzatish va byudjetni muvozanatda saqlash", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Xarajatlarni aniq kuzatish va byudjetni muvozanatda saqlash"},
        {"q": "Inflyatsiya yuqori bo‘lganda, faqat naqd pul saqlash qanday oqibatga olib keladi?", "o": ["Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati oshadi va xarid qobiliyati ko‘payadi", "Pul qiymati barqaror bo‘ladi", "Barqaror daromad ta’minlanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Nima uchun doimiy va o‘zgaruvchan xarajatlarni alohida hisoblash tavsiya etiladi?", "o": ["Xarajatlarni nazorat qilish va reja tuzish osonlashadi", "Chunki foiz stavkasi oshadi", "Chunki naqd pul kamayadi", "Chunki bank qarzini olish osonlashadi"], "a": "Xarajatlarni nazorat qilish va reja tuzish osonlashadi"},
        {"q": "Nima uchun investitsiya va jamg‘arma yaratish moliyaviy xavfni kamaytiradi?", "o": ["Daromadlarni diversifikatsiya qilish orqali xavfni qoplaydi", "Chunki foiz stavkasi oshadi", "Chunki xarajatlarni oshirish mumkin", "Chunki bu naqd pulni oshiradi"], "a": "Daromadlarni diversifikatsiya qilish orqali xavfni qoplaydi"},
        {"q": "Shaxsiy moliyaviy qaror qabul qilishda barcha resurslarni hisobga olish nima uchun muhim?", "o": ["Barcha resurslarni nazorat qilish va ongli qaror qabul qilish uchun", "Faqat kredit olishni osonlashtiradi", "Faqat xarajatlarni oshiradi", "Faqat soliqni kamaytiradi"], "a": "Barcha resurslarni nazorat qilish va ongli qaror qabul qilish uchun"},
        {"q": "Oylik xarajatlar daromaddan oshib ketishi qanday xavf tug‘diradi?", "o": ["Qarzga bog‘lanish va moliyaviy stress yuzaga keladi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi", "Bank depoziti ko‘payadi"], "a": "Qarzga bog‘lanish va moliyaviy stress yuzaga keladi"},
        {"q": "Shaxsiy investitsiya portfelingizda faqat obligatsiyalar bo‘lishi qanday xavf tug‘diradi?", "o": ["Bitta aktiv qiymati tushsa, umumiy portfel daromadi pasayadi", "Diversifikatsiya oshadi", "Naqd pul ko‘payadi", "Xarajatlar kamayadi"], "a": "Bitta aktiv qiymati tushsa, umumiy portfel daromadi pasayadi"},
        {"q": "Passiv daromad manbalarini yaratish qanday qilib shaxsiy moliyaviy erkinlikni oshiradi?", "o": ["Qo‘shimcha daromad va mustaqil qaror qabul qilish imkonini beradi", "Faqat kredit olish imkonini beradi", "Xarajatlarni oshirish imkonini beradi", "Naqd pulni kamaytiradi"], "a": "Qo‘shimcha daromad va mustaqil qaror qabul qilish imkonini beradi"},
        {"q": "Shaxsiy moliyaviy maqsadlarda aniq muddat va o‘lchovlarni belgilash qanday foyda beradi?", "o": ["Maqsadga erishishni monitoring qilish va reja bo‘yicha harakat qilish osonlashadi", "Faqat kredit olish osonlashadi", "Xarajatlarni oshirish imkoniyati paydo bo‘ladi", "Inflyatsiyani kamaytiradi"], "a": "Maqsadga erishishni monitoring qilish va reja bo‘yicha harakat qilish osonlashadi"},
        {"q": "Qarzlarni boshqarishda foiz stavkasi va to‘lov muddatlarini hisobga olish nega muhim?", "o": ["Foiz xarajatlari va byudjet muvozanati shu parametrlar bilan belgilanadi", "Faqat kredit olishni osonlashtiradi", "Daromad oshadi", "Naqd pul ko‘payadi"], "a": "Foiz xarajatlari va byudjet muvozanati shu parametrlar bilan belgilanadi"},
        {"q": "Nima sababdan diversifikatsiya moliyaviy xavfni kamaytiradi?", "o": ["Bitta aktivning yo‘qotilishi boshqa aktivlar bilan qoplanadi", "Barcha aktivlar bir xil daromad beradi", "Bu naqd pulni oshiradi", "Xarajatlar kamayadi"], "a": "Bitta aktivning yo‘qotilishi boshqa aktivlar bilan qoplanadi"},
]

# 141-210 bloki
if 'ms_141_210' not in st.session_state:
    st.session_state.ms_141_210 = [
        {"q": "Moliyaviy savodxonlikni oshirishda eng muhim qadamlar qaysilar?", "o": ["Byudjet tuzish, xarajat nazorati va investitsiya yaratish", "Xarajatlarni oshirish va qarz olish", "Faqat bank depozitini oshirish", "Soliqdan qochish"], "a": "Byudjet tuzish, xarajat nazorati va investitsiya yaratish"},
        {"q": "Oylik daromad barqaror bo‘lib, xarajatlar oshib ketsa, qanday choralar samarali?", "o": ["Byudjet tuzish, maqsadlarni belgilash va passiv daromad yaratish", "Faqat xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Byudjet tuzish, maqsadlarni belgilash va passiv daromad yaratish"},
        {"q": "Inflyatsiya yuqori bo‘lganda, naqd pul saqlash qanday oqibatlarga olib keladi?", "o": ["Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati oshadi va xarid qobiliyati ko‘payadi", "Pul qiymati barqaror bo‘ladi", "Barqaror daromad ta’minlanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Yuqori foizli qarzga ega bo‘lish byudjetga qanday ta’sir qilishi mumkin?", "o": ["Foiz xarajatlari ko‘payib, byudjet qiyinlashadi", "Xarajatlar kamayadi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Foiz xarajatlari ko‘payib, byudjet qiyinlashadi"},
        {"q": "Investitsiya portfeli faqat bir turdagi aktivdan (masalan, aksiya) iborat bo‘lishi qanday xavf tug‘diradi?", "o": ["Bitta aktiv qiymati tushsa, portfelning umumiy qiymati sezilarli pasayadi", "Diversifikatsiya ortadi", "Bu naqd pul hisoblanadi", "Bitta aktiv barqaror daromad beradi"], "a": "Bitta aktiv qiymati tushsa, portfelning umumiy qiymati sezilarli pasayadi"},
        {"q": "Moliyaviy maqsadlarni SMART tamoyiliga muvofiq belgilash qanday foyda beradi?", "o": ["Amalga oshirish rejasi va monitoring qilish imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkoniyatini beradi", "Bank foizini oshiradi"], "a": "Amalga oshirish rejasi va monitoring qilish imkonini beradi"},
        {"q": "Qarzlarni konsolidatsiya qilish qanday foyda keltiradi?", "o": ["Boshqarish osonlashadi, foiz kamayadi va stress kamayadi", "Daromad oshadi", "Xarajatlar oshadi", "Naqd pul kamayadi"], "a": "Boshqarish osonlashadi, foiz kamayadi va stress kamayadi"},
        {"q": "Passiv daromad manbalarini yaratish barqarorlikni qanday oshiradi?", "o": ["Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Foiz stavkasi oshadi"], "a": "Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun turli moliyaviy aktivlarga (aksiya, obligatsiya, metall) investitsiya qilish tavsiya etiladi?", "o": ["Xavfni taqsimlaydi va umumiy daromadni barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Faqat aksiyalar daromad beradi", "Bu naqd pulni ko‘paytiradi"], "a": "Xavfni taqsimlaydi va umumiy daromadni barqarorlashtiradi"},
        {"q": "Oylik byudjetni nazorat qilish jarayoni qanday foyda beradi?", "o": ["Daromad va xarajatni kuzatish hamda maqsadlarga erishish imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Daromad va xarajatni kuzatish hamda maqsadlarga erishish imkonini beradi"},
        {"q": "Shaxsiy byudjetni tuzishda daromad va xarajatlarni ajratish zarur. Nima uchun doimiy va o‘zgaruvchan xarajatlarni alohida hisoblash tavsiya etiladi?", "o": ["A) Chunki xarajatlarni nazorat qilish va moliyaviy reja tuzish osonlashadi", "B) Chunki foiz stavkasi oshadi", "C) Chunki naqd pul kamayadi", "D) Chunki bank qarzini olish osonlashadi"], "a": "A) Chunki xarajatlarni nazorat qilish va moliyaviy reja tuzish osonlashadi"},
        {"q": "Sizning oylik daromadingiz barqaror, lekin xarajatlaringiz tez-tez oshib ketadi. Xarajatlarni nazorat qilish va moliyaviy barqarorlikni ta’minlash uchun qanday choralar eng samarali hisoblanadi?", "o": ["A) Xarajatlarni yozib borish, byudjet tuzish, moliyaviy maqsadlarni belgilash va passiv daromad manbalarini yaratish", "B) Faqat xarajatlarni oshirish", "C) Bank depozitini kamaytirish", "D) Moliyaviy rejani bekor qilish"], "a": "A) Xarajatlarni yozib borish, byudjet tuzish, moliyaviy maqsadlarni belgilash va passiv daromad manbalarini yaratish"},
        {"q": "Moliyaviy reja tuzishda qarz va foizlarni hisobga olish zarur. Agar siz yuqori foizli qarzga ega bo‘lsangiz, bu sizning byudjetingizga qanday ta’sir qiladi?", "o": ["A) Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi, byudjet qiyinlashadi", "B) Xarajatlar kamayadi", "C) Daromad oshadi", "D) Moliyaviy barqarorlik oshadi"], "a": "A) Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi, byudjet qiyinlashadi"},
        {"q": "Shaxsiy investitsiya portfelingizda faqat bir turdagi aktiv mavjud bo‘lsa, masalan, faqat aksiyalar. Nima sababli bu portfel yuqori xavfga ega hisoblanadi?", "o": ["A) Chunki bitta aktivning qiymati tushsa, portfelning umumiy qiymati sezilarli darajada pasayadi", "B) Chunki diversifikatsiya ortadi", "C) Chunki bu naqd pul hisoblanadi", "D) Chunki bitta aktiv barqaror daromad beradi"], "a": "A) Chunki bitta aktivning qiymati tushsa, portfelning umumiy qiymati sezilarli darajada pasayadi"},
        {"q": "Passiv daromad manbalarini yaratish shaxsiy moliyaviy barqarorlikni qanday oshiradi?", "o": ["A) Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "B) Faqat kredit olishni osonlashtiradi", "C) Xarajatlarni oshirish imkonini beradi", "D) Foiz stavkasi oshadi"], "a": "A) Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "SMART tamoyiliga muvofiq moliyaviy maqsadlarni belgilash qanday foyda beradi?", "o": ["A) Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib, ularni amalga oshirish rejasi va monitoring qilish imkonini beradi", "B) Faqat kredit olishni osonlashtiradi", "C) Xarajatlarni oshirish imkoniyatini beradi", "D) Bank foizini oshiradi"], "a": "A) Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib, ularni amalga oshirish rejasi va monitoring qilish imkonini beradi"},
        {"q": "Qarzlarni konsolidatsiya qilish qanday moliyaviy foyda keltiradi?", "o": ["A) Qarzlarni boshqarish osonlashadi, foiz stavkasi kamayadi va moliyaviy stress kamayadi", "B) Daromad oshadi", "C) Xarajatlar oshadi", "D) Naqd pul kamayadi"], "a": "A) Qarzlarni boshqarish osonlashadi, foiz stavkasi kamayadi va moliyaviy stress kamayadi"},
        {"q": "Investitsiya portfelingizda aksiyalar, obligatsiyalar va qimmatbaho metallar mavjud. Nima sababdan turli moliyaviy aktivlarga sarmoya kiritish tavsiya etiladi?", "o": ["A) Chunki turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi", "B) Faqat qimmatbaho metallar xavfsiz", "C) Faqat aksiyalar daromad beradi", "D) Bu naqd pulni ko‘paytiradi"], "a": "A) Chunki turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi"},
        {"q": "Oylik byudjetni ilova yoki jurnal yordamida nazorat qilish qanday foyda beradi?", "o": ["A) Daromad va xarajatlarni aniq kuzatish, moliyaviy maqsadlarga erishish va byudjetni muvozanatda saqlash imkonini beradi", "B) Faqat kredit olishni osonlashtiradi", "C) Naqd pulni oshiradi", "D) Soliq stavkasini kamaytiradi"], "a": "A) Daromad va xarajatlarni aniq kuzatish, moliyaviy maqsadlarga erishish va byudjetni muvozanatda saqlash imkonini beradi"},
        {"q": "Inflyatsiya yuqori bo‘lganda, faqat naqd pul saqlash uzoq muddatda qanday oqibatlarga olib keladi?", "o": ["A) Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "B) Pul qiymati oshadi va xarid qobiliyati ko‘payadi", "C) Pul qiymati barqaror bo‘ladi", "D) Barqaror daromad ta’minlanadi"], "a": "A) Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Shaxsiy byudjetni tuzishda doimiy va o‘zgaruvchan xarajatlarni alohida hisoblash nima uchun muhim?", "o": ["A) Chunki xarajatlarni nazorat qilish va moliyaviy reja tuzish osonlashadi", "B) Chunki foiz stavkasi oshadi", "C) Chunki naqd pul kamayadi", "D) Chunki bank qarzini olish osonlashadi"], "a": "A) Chunki xarajatlarni nazorat qilish va moliyaviy reja tuzish osonlashadi"},
        {"q": "Siz o‘zingizning shaxsiy investitsiya portfelingizni yaratmoqchisiz. Nima uchun daromad va xavfni balanslash muhim?", "o": ["A) Chunki balansi to‘g‘ri bo‘lsa, yuqori xavfli investitsiya daromadni oshiradi va xavfni kamaytiradi", "B) Chunki bu faqat bank kreditini olish imkonini beradi", "C) Chunki xarajatlarni oshirishni kafolatlaydi", "D) Chunki inflyatsiyani kamaytiradi"], "a": "A) Chunki balansi to‘g‘ri bo‘lsa, yuqori xavfli investitsiya daromadni oshiradi va xavfni kamaytiradi"},
        {"q": "Aksiyalar, obligatsiyalar va qimmatbaho metallar portfelingizda mavjud. Nima sababdan turli aktivlar orqali diversifikatsiya qilish tavsiya etiladi?", "o": ["A) Chunki bitta aktivning yo‘qotilishi boshqa aktivlarning daromadi bilan qoplanadi va umumiy xavf kamayadi", "B) Chunki barcha aktivlar bir xil daromad beradi", "C) Chunki bu naqd pulni oshiradi", "D) Chunki xarajatlar kamayadi"], "a": "A) Chunki bitta aktivning yo‘qotilishi boshqa aktivlarning daromadi bilan qoplanadi va umumiy xavf kamayadi"},
        {"q": "Dividend to‘lovlari bo‘yicha aksiyalarga sarmoya kiritish qanday moliyaviy foyda keltiradi?", "o": ["A) Qo‘shimcha passiv daromad keltiradi va portfel daromadini barqarorlashtiradi", "B) Faqat foiz stavkasini oshiradi", "C) Xarajatlarni oshiradi", "D) Pul qiymatini pasaytiradi"], "a": "A) Qo‘shimcha passiv daromad keltiradi va portfel daromadini barqarorlashtiradi"},
        {"q": "Obligatsiyalarga investitsiya qilish odatda xavf darajasi pastroq hisoblanadi. Nima uchun bu uzoq muddatli moliyaviy reja uchun foydali hisoblanadi?", "o": ["A) Chunki barqaror foiz daromadi beradi va portfel xavfini kamaytiradi", "B) Chunki daromad yuqori bo‘ladi va xavf oshadi", "C) Chunki naqd pulni oshiradi", "D) Chunki xarajatlarni kamaytiradi"], "a": "A) Chunki barqaror foiz daromadi beradi va portfel xavfini kamaytiradi"},
        {"q": "Siz yangi boshlovchi investor sifatida faqat yuqori daromadli aksiyalarga sarmoya kiritishni rejalashtiryapsiz. Nima uchun bu xavfli bo‘lishi mumkin?", "o": ["A) Chunki yuqori daromad odatda yuqori xavf bilan birga keladi, yo‘qotish ehtimoli oshadi", "B) Chunki barcha daromad barqaror bo‘ladi", "C) Chunki foiz stavkasi oshadi", "D) Chunki xarajatlar kamayadi"], "a": "A) Chunki yuqori daromad odatda yuqori xavf bilan birga keladi, yo‘qotish ehtimoli oshadi"},
        {"q": "Sarmoya portfelini diversifikatsiya qilishning boshqa sababi nima?", "o": ["A) Bir aktivning yo‘qotishini boshqa aktivlar bilan qoplash imkonini beradi va barqaror daromad yaratadi", "B) Faqat aksiyalar daromad keltiradi", "C) Faqat qimmatbaho metallar xavfsiz", "D) Bu naqd pulni oshiradi"], "a": "A) Bir aktivning yo‘qotishini boshqa aktivlar bilan qoplash imkonini beradi va barqaror daromad yaratadi"},
        {"q": "Investor sifatida siz obligatsiyalarni va aksiyalarni aralashtirgan portfelga ega bo‘lishni rejalashtiryapsiz. Nima sababdan bu uzoq muddatli barqaror daromadni ta’minlaydi?", "o": ["A) Chunki obligatsiyalar barqaror foiz daromadi beradi, aksiyalar esa o‘sish imkonini beradi va xavfni kamaytiradi", "B) Chunki bitta aktiv yuqori daromad beradi", "C) Chunki naqd pul oshadi", "D) Chunki xarajatlar kamayadi"], "a": "A) Chunki obligatsiyalar barqaror foiz daromadi beradi, aksiyalar esa o‘sish imkonini beradi va xavfni kamaytiradi"},
        {"q": "Qimmatbaho metallar (oltin, kumush) portfelingizda mavjud. Nima sababdan ular moliyaviy xavfni kamaytirishga yordam beradi?", "o": ["A) Chunki inflyatsiya va bozordagi beqarorlik vaqtida qimmatbaho metallar qiymati barqaror qoladi", "B) Chunki ular yuqori daromad beradi", "C) Chunki ular xarajatlarni kamaytiradi", "D) Chunki foiz stavkasi oshadi"], "a": "A) Chunki inflyatsiya va bozordagi beqarorlik vaqtida qimmatbaho metallar qiymati barqaror qoladi"},
        {"q": "Passiv investitsiya fondlariga (ETF, indeks fondlari) sarmoya kiritish qanday afzallik beradi?", "o": ["A) Xavfni taqsimlash, portfelni diversifikatsiya qilish va xarajatlarni kamaytirish imkonini beradi", "B) Faqat foiz stavkasini oshiradi", "C) Xarajatlarni oshiradi", "D) Naqd pulni oshiradi"], "a": "A) Xavfni taqsimlash, portfelni diversifikatsiya qilish va xarajatlarni kamaytirish imkonini beradi"},
        {"q": "Investitsiyaga kirishdan oldin sarmoyaning likvidligi va muddatini hisobga olish nega muhim?", "o": ["A) Chunki pulni istalgan vaqtda chiqarish va moliyaviy ehtiyojlarni qoplash imkoniyati moliyaviy barqarorlikni ta’minlaydi", "B) Chunki faqat foiz oshadi", "C) Chunki xarajatlar kamayadi", "D) Chunki inflyatsiya pasayadi"], "a": "A) Chunki pulni istalgan vaqtda chiqarish va moliyaviy ehtiyojlarni qoplash imkoniyati moliyaviy barqarorlikni ta’minlaydi"},
        {"q": "Inflyatsiya yuqori bo‘lsa, narxlar doimiy oshadi va pulning xarid qobiliyati pasayadi. Nima uchun shaxsiy jamg‘armalarni faqat naqd pul shaklida saqlash xavfli hisoblanadi?", "o": ["A) Chunki pul qiymati pasayadi va xarid qobiliyati kamayadi", "B) Chunki daromad oshadi", "C) Chunki foiz stavkasi barqaror bo‘ladi", "D) Chunki bank depozitlari avtomatik ravishda daromad beradi"], "a": "A) Chunki pul qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Inflyatsiyaga qarshi himoya sifatida qaysi investitsiya vositalari tavsiya etiladi?", "o": ["A) Qimmatbaho metallar, aksiyalar va ko‘chmas mulk", "B) Faqat naqd pul", "C) Faqat qisqa muddatli depozitlar", "D) Faqat yuqori foizli qarzlar"], "a": "A) Qimmatbaho metallar, aksiyalar va ko‘chmas mulk"},
        {"q": "Inflyatsiya yuqori bo‘lgan davrda bankdagi naqd pul depozitlari nima sababdan daromadni kamaytiradi?", "o": ["A) Chunki foiz daromadi inflyatsiya darajasidan past bo‘lsa, real daromad kamayadi", "B) Chunki pul qiymati oshadi", "C) Chunki depozit barqaror daromad beradi", "D) Chunki xarajatlar kamayadi"], "a": "A) Chunki foiz daromadi inflyatsiya darajasidan past bo‘lsa, real daromad kamayadi"},
        {"q": "Sizning oylik xarajatlaringiz inflyatsiyadan oshib ketayotgan bo‘lsa, qanday moliyaviy strategiya tavsiya etiladi?", "o": ["A) Passiv daromad manbalarini yaratish, investitsiya portfelini diversifikatsiya qilish va real qiymati yuqori aktivlarga sarmoya kiritish", "B) Faqat naqd pul yig‘ish", "C) Faqat qarz olish", "D) Xarajatlarni oshirish"], "a": "A) Passiv daromad manbalarini yaratish, investitsiya portfelini diversifikatsiya qilish va real qiymati yuqori aktivlarga sarmoya kiritish"},
        {"q": "Inflyatsiya va real daromad o‘rtasidagi bog‘liqlik nima?", "o": ["A) Inflyatsiya oshsa, real daromad kamayadi, chunki pulning xarid qobiliyati pasayadi", "B) Inflyatsiya oshsa, real daromad oshadi", "C) Inflyatsiya real daromadga ta’sir qilmaydi", "D) Inflyatsiya faqat qarzlarni kamaytiradi"], "a": "A) Inflyatsiya oshsa, real daromad kamayadi, chunki pulning xarid qobiliyati pasayadi"},
        {"q": "Inflyatsiya yuqori bo‘lgan sharoitda aksiyalarga investitsiya qilish qanday foyda beradi?", "o": ["A) Aksiyalar qiymati oshishi mumkin, bu inflyatsiyadan himoya beradi va portfel daromadini barqarorlashtiradi", "B) Aksiyalar hech qanday foyda bermaydi", "C) Faqat qarz olish foydali bo‘ladi", "D) Naqd pul daromad keltiradi"], "a": "A) Aksiyalar qiymati oshishi mumkin, bu inflyatsiyadan himoya beradi va portfel daromadini barqarorlashtiradi"},
        {"q": "Real daromad va nominal daromad farqi nima?", "o": ["A) Nominal daromad inflyatsiyani hisobga olmaydi, real daromad esa inflyatsiya inobatga olingan daromaddir", "B) Nominal daromad past, real daromad yuqori bo‘ladi", "C) Nominal daromad inflyatsiyadan oshib ketadi", "D) Real daromad inflyatsiya bilan kamaymaydi"], "a": "A) Nominal daromad inflyatsiyani hisobga olmaydi, real daromad esa inflyatsiya inobatga olingan daromaddir"},
        {"q": "Sizning investitsiya portfelingizda inflyatsiyaga qarshi himoya yo‘q. Bu qanday xavf tug‘diradi?", "o": ["A) Real daromad kamayadi va moliyaviy barqarorlik zaiflashadi", "B) Foiz daromadi oshadi", "C) Xarajatlar kamayadi", "D) Moliyaviy barqarorlik oshadi"], "a": "A) Real daromad kamayadi va moliyaviy barqarorlik zaiflashadi"},
        {"q": "Inflyatsiya yuqori bo‘lgan davrda qimmatbaho metallarga investitsiya qilish tavsiya etiladi. Nima sababdan?", "o": ["A) Chunki ular inflyatsiya sharoitida o‘z qiymatini saqlab qoladi va real daromadni himoya qiladi", "B) Chunki ular yuqori daromad beradi", "C) Chunki xarajatlar kamayadi", "D) Chunki naqd pul oshadi"], "a": "A) Chunki ular inflyatsiya sharoitida o‘z qiymatini saqlab qoladi va real daromadni himoya qiladi"},
        {"q": "Inflyatsiya bo‘lganda shaxsiy byudjetni qanday boshqarish tavsiya etiladi?", "o": ["A) Xarajatlarni nazorat qilish, real qiymati yuqori aktivlarga sarmoya kiritish va jamg‘armalarni diversifikatsiya qilish", "B) Faqat naqd pul yig‘ish", "C) Faqat qarz olish", "D) Xarajatlarni oshirish"], "a": "A) Xarajatlarni nazorat qilish, real qiymati yuqori aktivlarga sarmoya kiritish va jamg‘armalarni diversifikatsiya qilish"},
        {"q": "Inflyatsiya yuqori bo‘lganda, odamlar ko‘pincha xarajatlarni oldindan oshirishga harakat qilishadi. Bu qanday moliyaviy oqibatlarga olib keladi?", "o": ["A) Xarajatlar oshadi, pulning xarid qobiliyati pasayadi va bozor narxlari yanada ko‘tariladi", "B) Pul qiymati barqaror qoladi", "C) Daromad oshadi", "D) Soliq kamayadi"], "a": "A) Xarajatlar oshadi, pulning xarid qobiliyati pasayadi va bozor narxlari yanada ko‘tariladi"},
        {"q": "Shaxsiy jamg‘armalarni inflyatsiyaga qarshi himoya qilish uchun qaysi vositalar samarali?", "o": ["A) Qimmatbaho metallar, aksiyalar va ko‘chmas mulk investitsiyalari", "B) Faqat naqd pul", "C) Faqat qisqa muddatli depozitlar", "D) Faqat kreditlar"], "a": "A) Qimmatbaho metallar, aksiyalar va ko‘chmas mulk investitsiyalari"},
        {"q": "Inflyatsiya darajasi daromaddan yuqori bo‘lsa, bu sizning real daromadingizga qanday ta’sir qiladi?", "o": ["A) Real daromad kamayadi, chunki xarid qobiliyati pasayadi", "B) Real daromad oshadi", "C) Real daromad barqaror bo‘ladi", "D) Faqat qarz oshadi"], "a": "A) Real daromad kamayadi, chunki xarid qobiliyati pasayadi"},
        {"q": "Inflyatsiya yuqori bo‘lgan sharoitda obligatsiyalarga sarmoya kiritish qanday xavf tug‘diradi?", "o": ["A) Foiz daromadining qiymati inflyatsiya tufayli kamayadi, real daromad pasayadi", "B) Foiz daromadi oshadi", "C) Xarajatlar kamayadi", "D) Moliyaviy barqarorlik oshadi"], "a": "A) Foiz daromadining qiymati inflyatsiya tufayli kamayadi, real daromad pasayadi"},
        {"q": "Aksiyalarga investitsiya qilish inflyatsiyaga qarshi himoya bo‘lishi mumkin. Nima sababdan?", "o": ["A) Chunki kompaniyalar mahsulot va xizmatlar narxini oshirishi mumkin, bu esa aksiyalar qiymatini oshiradi", "B) Chunki foiz stavkasi oshadi", "C) Chunki xarajatlarni kamayadi", "D) Chunki pul qiymati pasayadi"], "a": "A) Chunki kompaniyalar mahsulot va xizmatlar narxini oshirishi mumkin, bu esa aksiyalar qiymatini oshiradi"},
        {"q": "Inflyatsiya davrida real aktivlarga, masalan, ko‘chmas mulkga sarmoya kiritish qanday foyda beradi?", "o": ["A) Chunki ko‘chmas mulk qiymati inflyatsiyadan kamroq ta’sirlanadi va pulning xarid qobiliyatini saqlaydi", "B) Chunki u daromad bermaydi", "C) Chunki xarajatlarni oshiradi", "D) Chunki bank foizi oshadi"], "a": "A) Chunki ko‘chmas mulk qiymati inflyatsiyadan kamroq ta’sirlanadi va pulning xarid qobiliyatini saqlaydi"},
        {"q": "Nominal daromad va real daromad farqi inflyatsiya bilan bog‘liq bo‘lsa, nima yuz beradi?", "o": ["A) Nominal daromad inflyatsiyani hisobga olmaydi, real daromad esa inflyatsiyani chiqarib hisoblanadi, shuning uchun real daromad kamayishi mumkin", "B) Nominal va real daromad bir xil bo‘ladi", "C) Nominal daromad kamayadi, real daromad oshadi", "D) Inflyatsiya daromadga ta’sir qilmaydi"], "a": "A) Nominal daromad inflyatsiyani hisobga olmaydi, real daromad esa inflyatsiyani chiqarib hisoblanadi, shuning uchun real daromad kamayishi mumkin"},
        {"q": "Sizning portfelingizda inflyatsiyaga qarshi hech qanday himoya yo‘q. Bu qanday moliyaviy xavf tug‘diradi?", "o": ["A) Real daromad kamayadi va moliyaviy barqarorlik zaiflashadi", "B) Foiz daromadi oshadi", "C) Xarajatlar kamayadi", "D) Moliyaviy barqarorlik oshadi"], "a": "A) Real daromad kamayadi va moliyaviy barqarorlik zaiflashadi"},
        {"q": "Inflyatsiyaga qarshi himoya sifatida qimmatbaho metallarga (oltin, kumush) sarmoya kiritishning sababi nima?", "o": ["A) Chunki ular inflyatsiya sharoitida o‘z qiymatini saqlab qoladi va real daromadni himoya qiladi", "B) Chunki ular yuqori daromad beradi", "C) Chunki xarajatlarni kamaytiradi", "D) Chunki naqd pulni oshiradi"], "a": "A) Chunki ular inflyatsiya sharoitida o‘z qiymatini saqlab qoladi va real daromadni himoya qiladi"},
        {"q": "Inflyatsiya yuqori bo‘lganda shaxsiy byudjetni boshqarish bo‘yicha eng muhim strategiyalar qaysilar?", "o": ["A) Xarajatlarni nazorat qilish, real qiymati yuqori aktivlarga sarmoya kiritish va jamg‘armalarni diversifikatsiya qilish", "B) Faqat naqd pul yig‘ish", "C) Faqat qarz olish", "D) Xarajatlarni oshirish"], "a": "A) Xarajatlarni nazorat qilish, real qiymati yuqori aktivlarga sarmoya kiritish va jamg‘armalarni diversifikatsiya qilish"},
        {"q": "Mo‘tadil inflyatsiya darajasida (yiliga 2–5%) shaxsiy jamg‘armalarni naqd pulda saqlash xavfli emasmi?", "o": ["A) Qisman xavf mavjud, chunki pulning xarid qobiliyati asta-sekin kamayadi; investitsiya orqali bu xavfni kamaytirish mumkin", "B) Hech qanday xavf yo‘q, naqd pul qiymatini saqlaydi", "C) Pulning qiymati oshadi", "D) Faqat qarz olish tavsiya etiladi"], "a": "A) Qisman xavf mavjud, chunki pulning xarid qobiliyati asta-sekin kamayadi; investitsiya orqali bu xavfni kamaytirish mumkin"},
        {"q": "Shiddatli inflyatsiya (yiliga 10–50%) davrida jamg‘armalarni naqd pulda saqlash nima oqibatga olib keladi?", "o": ["A) Pul tez qadrsizlanadi, xarid qobiliyati keskin kamayadi va real daromad yo‘qoladi", "B) Pul qiymati barqaror qoladi", "C) Foiz daromadi oshadi", "D) Bank depozitlari xavfsiz bo‘ladi"], "a": "A) Pul tez qadrsizlanadi, xarid qobiliyati keskin kamayadi va real daromad yo‘qoladi"},
        {"q": "Giperinflyatsiya (yiliga 100% va undan yuqori) sharoitida odamlar odatda nima qiladi?", "o": ["A) Pulni tezda real aktivlarga (ko‘chmas mulk, qimmatbaho metallar, xorijiy valyuta) aylantiradi", "B) Naqd pul yig‘ishni davom ettiradi", "C) Bank depozitlarini oshiradi", "D) Xarajatlarni kamaytiradi"], "a": "A) Pulni tezda real aktivlarga (ko‘chmas mulk, qimmatbaho metallar, xorijiy valyuta) aylantiradi"},
        {"q": "Mo‘tadil inflyatsiya davrida sarmoya portfelingizni qanday boshqarish tavsiya etiladi?", "o": ["A) Balansli portfel, bir qismi aksiyalar va obligatsiyalarga, bir qismi qimmatbaho metallar va ko‘chmas mulkka sarmoya kiritish", "B) Faqat naqd pul", "C) Faqat yuqori xavfli aktivlar", "D) Xarajatlarni oshirish"], "a": "A) Balansli portfel, bir qismi aksiyalar va obligatsiyalarga, bir qismi qimmatbaho metallar va ko‘chmas mulkka sarmoya kiritish"},
        {"q": "Shiddatli inflyatsiya davrida kreditlar va qarzlar qanday foyda yoki xavf tug‘dirishi mumkin?", "o": ["A) Agar foizlar past bo‘lsa, qarz real qiymatda qadrsizlanadi, lekin foizlar yuqori bo‘lsa, qarz xavf tug‘diradi", "B) Har qanday qarz foydali bo‘ladi", "C) Qarzni olish zarar keltirmaydi", "D) Naqd pul xavfsizroq"], "a": "A) Agar foizlar past bo‘lsa, qarz real qiymatda qadrsizlanadi, lekin foizlar yuqori bo‘lsa, qarz xavf tug‘diradi"},
        {"q": "Giperinflyatsiya sharoitida shaxsiy byudjetni boshqarishning eng samarali strategiyasi nima?", "o": ["A) Pulni tezda real aktivlarga aylantirish, xarajatlarni nazorat qilish va investitsiya portfelini diversifikatsiya qilish", "B) Faqat naqd pul yig‘ish", "C) Faqat qarz olish", "D) Xarajatlarni oshirish"], "a": "A) Pulni tezda real aktivlarga aylantirish, xarajatlarni nazorat qilish va investitsiya portfelini diversifikatsiya qilish"},
        {"q": "Inflyatsiyaning turli darajalari real daromadga qanday ta’sir qiladi?", "o": ["A) Mo‘tadil inflyatsiya asta-sekin kamaytiradi, shiddatli inflyatsiya sezilarli darajada kamaytiradi, giperinflyatsiya esa deyarli yo‘q qiladi", "B) Har qanday inflyatsiya real daromadni oshiradi", "C) Inflyatsiya real daromadga ta’sir qilmaydi", "D) Faqat nominal daromad kamayadi"], "a": "A) Mo‘tadil inflyatsiya asta-sekin kamaytiradi, shiddatli inflyatsiya sezilarli darajada kamaytiradi, giperinflyatsiya esa deyarli yo‘q qiladi"},
        {"q": "Shiddatli va giperinflyatsiya davrida qimmatbaho metallar va xorijiy valyutaga sarmoya kiritish tavsiya etiladi. Nima sababdan?", "o": ["A) Chunki ular pul qadrsizlanishidan himoya qiladi va real daromadni saqlaydi", "B) Chunki ular har doim yuqori daromad beradi", "C) Chunki xarajatlar kamayadi", "D) Chunki bank depozitlari xavfsizroq bo‘ladi"], "a": "A) Chunki ular pul qadrsizlanishidan himoya qiladi va real daromadni saqlaydi"},
        {"q": "Mo‘tadil inflyatsiya davrida investitsiyaga sarmoya kiritishning afzalligi nima?", "o": ["A) Pul qadrsizlanishini kamaytiradi, real daromadni saqlashga yordam beradi va portfel xavfini boshqaradi", "B) Har qanday investitsiya zarar keltiradi", "C) Faqat naqd pul xavfsizroq", "D) Xarajatlarni oshiradi"], "a": "A) Pul qadrsizlanishini kamaytiradi, real daromadni saqlashga yordam beradi va portfel xavfini boshqaradi"},
        {"q": "Giperinflyatsiya sharoitida shaxsiy moliyaviy barqarorlikni saqlash uchun qaysi choralar eng muhim?", "o": ["A) Pulni real aktivlarga tezkor aylantirish, xarajatlarni kamaytirish va qarzlarni minimallashtirish", "B) Faqat bank depozitlariga ishonish", "C) Xarajatlarni oshirish", "D) Naqd pul yig‘ish"], "a": "A) Pulni real aktivlarga tezkor aylantirish, xarajatlarni kamaytirish va qarzlarni minimallashtirish"},
        {"q": "Sizga telefon orqali noma’lum shaxs “tezkor investitsiya orqali katta daromad keltiradi” deb aytmoqda va mablag‘ingizni so‘ramoqda. Nima qilishingiz kerak?", "o": ["A) Mablag‘ni bermasdan, taklifni tekshirish va shubhali holatlarda rad etish", "B) Darhol mablag‘ni yuborish", "C) Faqat qarz olib yuborish", "D) Inflyatsiya tufayli o‘ylash shart emas"], "a": "A) Mablag‘ni bermasdan, taklifni tekshirish va shubhali holatlarda rad etish"},
        {"q": "Moliyaviy firibgarlik qanday ko‘rinishlarda uchrashi mumkin?", "o": ["A) Pyramida sxemalari, phishing, soxta investitsiya loyihalari, kredit kartasi firibgarligi", "B) Faqat bank depozitlari xavfsiz", "C) Faqat inflyatsiya bilan bog‘liq", "D) Faqat naqd pulni oshirish"], "a": "A) Pyramida sxemalari, phishing, soxta investitsiya loyihalari, kredit kartasi firibgarligi"},
        {"q": "Onlayn bank hisobingizdan noma’lum tranzaksiya amalga oshirilsa, qanday choralarni ko‘rish kerak?", "o": ["A) Bankga darhol xabar berish, hisobni bloklash va tranzaksiyani tekshirish", "B) Faqat tranzaksiyani e’tiborsiz qoldirish", "C) Mablag‘ni oshirish", "D) Inflyatsiyani kutish"], "a": "A) Bankga darhol xabar berish, hisobni bloklash va tranzaksiyani tekshirish"},
        {"q": "Phishing xabarlari odatda qanday maqsad bilan yuboriladi?", "o": ["A) Foydalanuvchining shaxsiy ma’lumotlarini, parollarini yoki karta ma’lumotlarini o‘g‘irlash", "B) Mablag‘ni oshirish", "C) Inflyatsiyani nazorat qilish", "D) Xarajatlarni kamaytirish"], "a": "A) Foydalanuvchining shaxsiy ma’lumotlarini, parollarini yoki karta ma’lumotlarini o‘g‘irlash"},
        {"q": "Moliyaviy firibgarlikni oldini olish uchun shaxsiy moliyaviy xavfsizlikda nimalarga e’tibor berish kerak?", "o": ["A) Kuchli parollar ishlatish, shubhali havolalardan foydalanmaslik, mablag‘larni tekshirilgan manbalarda saqlash", "B) Har qanday investitsiyaga mablag‘ yuborish", "C) Xarajatlarni oshirish", "D) Inflyatsiya tufayli moliyaviy xavfsizlikni e’tiborsiz qoldirish"], "a": "A) Kuchli parollar ishlatish, shubhali havolalardan foydalanmaslik, mablag‘larni tekshirilgan manbalarda saqlash"},
        {"q": "Sizga noma’lum shaxs “faqat bugun, katta foiz bilan qarz beraman” deb aytmoqda. Nima sababdan bu firibgarlik bo‘lishi mumkin?", "o": ["A) Chunki yuqori foiz va shoshilinch talab odatda firibgarlik belgisi hisoblanadi", "B) Chunki qarz olish har doim xavfsiz", "C) Chunki bank foizini oshiradi", "D) Chunki xarajatlarni kamaytiradi"], "a": "A) Chunki yuqori foiz va shoshilinch talab odatda firibgarlik belgisi hisoblanadi"},
        {"q": "Pyramid (piramida) sxemalari qanday ishlaydi va ular nima sababdan xavflidir?", "o": ["A) Yangi ishtirokchilar mablag‘ini eski ishtirokchilarga tarqatish orqali daromad keltiradi; oxir-oqibat ko‘pchilik mablag‘ini yo‘qotadi", "B) Ballar ishtirokchilar daromad oladi", "C) Faqat banklar foyda ko‘radi", "D) Inflyatsiya bilan bog‘liq"], "a": "A) Yangi ishtirokchilar mablag‘ini eski ishtirokchilarga tarqatish orqali daromad keltiradi; oxir-oqibat ko‘pchilik mablag‘ini yo‘qotadi"},
        {"q": "Onlayn xarid paytida shaxsiy karta ma’lumotlarini so‘rayotgan shubhali saytga nimalar qilish kerak?", "o": ["A) Hech qanday ma’lumot bermaslik, saytni tekshirish va xavfsiz manbadan foydalanish", "B) Darhol karta ma’lumotini kiritish", "C) Xarajatlarni oshirish", "D) Pulni inflyatsiyaga bog‘lash"], "a": "A) Hech qanday ma’lumot bermaslik, saytni tekshirish va xavfsiz manbadan foydalanish"},
        {"q": "Moliyaviy firibgarlikni oldini olish uchun shaxsiy byudjetni qanday boshqarish tavsiya etiladi?", "o": ["A) Mablag‘ni faqat tekshirilgan manbalarda saqlash va shubhali investitsiyalardan saqlanish", "B) Har qanday investitsiyaga mablag‘ yuborish", "C) Naqd pulni oshirish", "D) Inflyatsiya tufayli qarz olish"], "a": "A) Mablag‘ni faqat tekshirilgan manbalarda saqlash va shubhali investitsiyalardan saqlanish"},
    ]
    
    # 211-300 bloki
if 'ms_211_300' not in st.session_state:
    st.session_state.ms_211_300 = [
        {"q": "Sizning do‘stingiz “tezkor boyib ketish” imkoniyati bilan sizni firibgarlik sxemasiga jalb qilmoqchi. Siz nima qilasiz?", "o": ["A) Mablag‘ni bermasdan rad etish, do‘stni ogohlantirish va moliyaviy xavfsizlikni saqlash", "B) Darhol mablag‘ni yuborish", "C) Faqat qarz olish", "D) Inflyatsiya tufayli kutish"], "a": "A) Mablag‘ni bermasdan rad etish, do‘stni ogohlantirish va moliyaviy xavfsizlikni saqlash"},
        {"q": "Siz bankdan shaxsiy kredit olmoqchisiz. Nima sababdan kreditning yillik foiz stavkasini va umumiy qaytariladigan summani oldindan hisoblash muhim?", "o": ["A) Chunki bu sizning moliyaviy imkoniyatingizni aniqlash va qarz yukini boshqarish imkonini beradi", "B) Chunki faqat bank foyda oladi", "C) Chunki qarz avtomatik daromad keltiradi", "D) Chunki inflyatsiya foizga ta’sir qilmaydi"], "a": "A) Chunki bu sizning moliyaviy imkoniyatingizni aniqlash va qarz yukini boshqarish imkonini beradi"},
        {"q": "Kredit olishda “amortizatsiya jadvali” nima uchun muhim?", "o": ["A) Chunki u har oy to‘lanadigan asosiy qarz va foiz summasini ko‘rsatadi, shaxsiy byudjetni boshqarishni osonlashtiradi", "B) Chunki foiz stavkasi oshadi", "C) Chunki qarz avtomatik kamayadi", "D) Chunki inflyatsiya barqaror bo‘ladi"], "a": "A) Chunki u har oy to‘lanadigan asosiy qarz va foiz summasini ko‘rsatadi, shaxsiy byudjetni boshqarishni osonlashtiradi"},
        {"q": "Sizga yuqori foizli tezkor kredit taklif qilinmoqda. Nima sababdan bu moliyaviy xavf tug‘diradi?", "o": ["A) Chunki foizlar tez oshadi va qarz tezda oshib ketadi, byudjetni qiyinlashtiradi", "B) Chunki daromad oshadi", "C) Chunki inflyatsiya kamayadi", "D) Chunki qarz xavfsiz hisoblanadi"], "a": "A) Chunki foizlar tez oshadi va qarz tezda oshib ketadi, byudjetni qiyinlashtiradi"},
        {"q": "Bank qarzini olishdan oldin shaxsiy moliyaviy holatni tahlil qilish nega muhim?", "o": ["A) Chunki daromad va xarajatlar qarzni qaytarish qobiliyatini aniqlaydi va moliyaviy barqarorlikni saqlashga yordam beradi", "B) Chunki har qanday qarz xavfsiz bo‘ladi", "C) Chunki xarajatlarni oshirish tavsiya etiladi", "D) Chunki inflyatsiya bilan bog‘liq emas"], "a": "A) Chunki daromad va xarajatlar qarzni qaytarish qobiliyatini aniqlaydi va moliyaviy barqarorlikni saqlashga yordam beradi"},
        {"q": "Kreditning muddatini uzaytirish foiz xarajatlariga qanday ta’sir qiladi?", "o": ["A) Umumiy foiz xarajatlari ko‘payadi, lekin oyma-oy to‘lovlar kamayadi", "B) Foiz xarajatlari kamayadi", "C) Foizlar barqaror qoladi", "D) Moliyaviy barqarorlik oshadi"], "a": "A) Umumiy foiz xarajatlari ko‘payadi, lekin oyma-oy to‘lovlar kamayadi"},
        {"q": "Siz konsalidasiyalashgan kreditni olishni rejalashtiryapsiz. Bu nima maqsadda amalga oshiriladi?", "o": ["A) Bir nechta qarzlarni birlashtirib, foiz stavkasini kamaytirish va to‘lovlarni boshqarishni osonlashtirish", "B) Qarzlarni oshirish", "C) Naqd pulni kamaytirish", "D) Xarajatlarni oshirish"], "a": "A) Bir nechta qarzlarni birlashtirib, foiz stavkasini kamaytirish va to‘lovlarni boshqarishni osonlashtirish"},
        {"q": "O‘z-o‘zidan qarzni tez to‘lash (early repayment) qaysi holatda foydali bo‘ladi?", "o": ["A) Agar foiz stavkalari yuqori bo‘lsa va qo‘shimcha to‘lov bilan foiz xarajatini kamaytirish mumkin bo‘lsa", "B) Faqat nominal daromad oshadi", "C) Inflyatsiya tufayli zarar keltiradi", "D) Naqd pul kamayadi"], "a": "A) Agar foiz stavkalari yuqori bo‘lsa va qo‘shimcha to‘lov bilan foiz xarajatini kamaytirish mumkin bo‘lsa"},
        {"q": "Bank qarzini olishda kafillik (garantiya) nima uchun muhim hisoblanadi?", "o": ["A) Chunki u kredit xavfini kamaytiradi va bank tomonidan qarz berishni osonlashtiradi", "B) Chunki qarz avtomatik to‘lanadi", "C) Chunki foiz stavkasi oshadi", "D) Chunki inflyatsiya kamayadi"], "a": "A) Chunki u kredit xavfini kamaytiradi va bank tomonidan qarz berishni osonlashtiradi"},
        {"q": "Kreditni qaytarishda kechikish qanday moliyaviy oqibatlarga olib keladi?", "o": ["A) Kechikish uchun jarima foizi qo‘llanadi, kredit reytingi pasayadi va moliyaviy barqarorlik zaiflashadi", "B) Foizlar kamayadi", "C) Xarajatlar kamayadi", "D) Naqd pul oshadi"], "a": "A) Kechikish uchun jarima foizi qo‘llanadi, kredit reytingi pasayadi va moliyaviy barqarorlik zaiflashadi"},
        {"q": "Shaxsiy byudjetni kredit to‘lovlariga moslashtirish nima uchun muhim?", "o": ["A) Chunki har oy qarz to‘lovlari va foizlar hisobga olinmasa, byudjet muvozanati buziladi va moliyaviy stress oshadi", "B) Chunki foizlar avtomatik kamayadi", "C) Chunki xarajatlarni oshirish foydali", "D) Chunki inflyatsiya barqaror bo‘ladi"], "a": "A) Chunki har oy qarz to‘lovlari va foizlar hisobga olinmasa, byudjet muvozanati buziladi va moliyaviy stress oshadi"},
        {"q": "Siz oylik daromadingizning katta qismini kredit to‘lovlariga sarflashni rejalashtiryapsiz. Nima sababdan bu tavsiya etilmaydi?", "o": ["A) Chunki byudjetning asosiy qismini qarzga sarflash moliyaviy barqarorlikni zaiflashtiradi va boshqa xarajatlarni qiyinlashtiradi", "B) Chunki foiz stavkasi avtomatik oshadi", "C) Chunki qarz daromad keltiradi", "D) Chunki inflyatsiya pasayadi"], "a": "A) Chunki byudjetning asosiy qismini qarzga sarflash moliyaviy barqarorlikni zaiflashtiradi va boshqa xarajatlarni qiyinlashtiradi"},
        {"q": "Kredit olishda APR (Annual Percentage Rate) nima uchun muhim?", "o": ["A) Chunki u barcha xarajatlarni, shu jumladan foiz va boshqa to‘lovlarni yillik foizda ko‘rsatadi, qarzni solishtirishni osonlashtiradi", "B) Chunki foiz stavkasi faqat bank foydasini bildiradi", "C) Chunki xarajatlarni oshirishni tavsiya qiladi", "D) Chunki inflyatsiya bilan bog‘liq emas"], "a": "A) Chunki u barcha xarajatlarni, shu jumladan foiz va boshqa to‘lovlarni yillik foizda ko‘rsatadi, qarzni solishtirishni osonlashtiradi"},
        {"q": "Kredit olishdan oldin shaxsiy qarz-to‘lov qobiliyatini baholash nega zarur?", "o": ["A) Chunki daromad va xarajatlarni hisobga olmasdan qarz olish, moliyaviy stress va kechikish xavfini oshiradi", "B) Chunki qarz har doim xavfsiz", "C) Chunki foiz stavkasi oshadi", "D) Chunki xarajatlar kamayadi"], "a": "A) Chunki daromad va xarajatlarni hisobga olmasdan qarz olish, moliyaviy stress va kechikish xavfini oshiradi"},
        {"q": "Kredit to‘lovlarini kechiktirish bank reytingiga qanday ta’sir qiladi?", "o": ["A) Reyting pasayadi, kelajakda kredit olish qiyinlashadi va foiz stavkasi oshadi", "B) Reyting oshadi", "C) Xarajatlar kamayadi", "D) Naqd pul oshadi"], "a": "A) Reyting pasayadi, kelajakda kredit olish qiyinlashadi va foiz stavkasi oshadi"},
        {"q": "Konsolidatsiya qilingan kredit bilan bir nechta qarzlarni birlashtirish qanday foyda beradi?", "o": ["A) Foiz xarajatlarini kamaytiradi, to‘lovlarni boshqarishni osonlashtiradi va moliyaviy stressni kamaytiradi", "B) Qarz oshadi", "C) Xarajatlarni oshiradi", "D) Naqd pul kamayadi"], "a": "A) Foiz xarajatlarini kamaytiradi, to‘lovlarni boshqarishni osonlashtiradi va moliyaviy stressni kamaytiradi"},
        {"q": "Kredit olishda garov (collateral) nima uchun muhim?", "o": ["A) Chunki u qarz oluvchi va bank o‘rtasidagi xavfni kamaytiradi va qarz olish imkoniyatini oshiradi", "B) Chunki qarz avtomatik to‘lanadi", "C) Chunki foiz stavkasi oshadi", "D) Chunki inflyatsiya kamayadi"], "a": "A) Chunki u qarz oluvchi va bank o‘rtasidagi xavfni kamaytiradi va qarz olish imkoniyatini oshiradi"},
        {"q": "Kredit foizlari va muddatini tushunmasdan qarz olishning qanday xavfi mavjud?", "o": ["A) Foizlar va to‘lov muddati noto‘g‘ri tushunilgan bo‘lsa, qarz tez oshadi va byudjet muvozanati buziladi", "B) Foizlar kamayadi", "C) Xarajatlar kamayadi", "D) Naqd pul oshadi"], "a": "A) Foizlar va to‘lov muddati noto‘g‘ri tushunilgan bo‘lsa, qarz tez oshadi va byudjet muvozanati buziladi"},
        {"q": "Shaxsiy kredit olishdan oldin taqqoslash va banklarning shartlarini tekshirish nima uchun muhim?", "o": ["A) Chunki bu eng qulay foiz, muddat va to‘lov shartlarini tanlashga yordam beradi", "B) Chunki har qanday bank xavfsiz", "C) Xarajatlarni oshirishni tavsiya qiladi", "D) Inflyatsiya tufayli qarz xavfsiz bo‘ladi"], "a": "A) Chunki bu eng qulay foiz, muddat va to‘lov shartlarini tanlashga yordam beradi"},
        {"q": "Siz bankga 1 yil muddatga depozit qo‘yishni rejalashtiryapsiz. Nima sababdan yillik foiz stavkasini oldindan bilish muhim?", "o": ["A) Chunki bu sizning daromadingizni oldindan rejalashtirish va shaxsiy byudjetni boshqarish imkonini beradi", "B) Chunki depozit avtomatik daromad keltiradi", "C) Chunki inflyatsiya hisobga olinmaydi", "D) Chunki xarajatlar oshadi"], "a": "A) Chunki bu sizning daromadingizni oldindan rejalashtirish va shaxsiy byudjetni boshqarish imkonini beradi"},
        {"q": "Omonat turlaridan qaysi biri inflyatsiyaga qarshi ko‘proq himoya beradi?", "o": ["A) O‘sish stavkali depozitlar yoki indekslangan depozitlar", "B) Faqat naqd pul saqlash", "C) Qisqa muddatli depozitlar", "D) Kreditlar"], "a": "A) O‘sish stavkali depozitlar yoki indekslangan depozitlar"},
        {"q": "Bank depozitini muddatidan oldin yechish (early withdrawal) qaysi xavfni tug‘diradi?", "o": ["A) Foiz daromadi kamayadi yoki jarima olinadi, real daromad pasayadi", "B) Foiz daromadi oshadi", "C) Xarajatlar kamayadi", "D) Naqd pul oshadi"], "a": "A) Foiz daromadi kamayadi yoki jarima olinadi, real daromad pasayadi"},
        {"q": "Omonatning kapitalizatsiyasi (foizlarni qo‘shib hisoblash) nima foyda beradi?", "o": ["A) Foizlar asosiy summaga qo‘shiladi va keyingi davrda foizlar ustiga foiz hisoblanadi, daromad oshadi", "B) Foizlar kamayadi", "C) Xarajatlarni oshiradi", "D) Inflyatsiya pasayadi"], "a": "A) Foizlar asosiy summaga qo‘shiladi va keyingi davrda foizlar ustiga foiz hisoblanadi, daromad oshadi"},
        {"q": "Depozit tanlashda bankning moliyaviy barqarorligini tekshirish nega muhim?", "o": ["A) Chunki bankning ishonchliligi daromadingiz va kapitalingiz xavfsizligini ta’minlaydi", "B) Chunki har qanday bank xavfsiz", "C) Chunki foiz stavkasi oshadi", "D) Chunki xarajatlar kamayadi"], "a": "A) Chunki bankning ishonchliligi daromadingiz va kapitalingiz xavfsizligini ta’minlaydi"},
        {"q": "Foyda olish uchun qaysi depozit muddatini tanlash tavsiya etiladi?", "o": ["A) Moliyaviy maqsadlar va likvidlik ehtiyojlarini hisobga olgan holda optimal muddat", "B) Har qanday uzun muddat foydali bo‘ladi", "C) Faqat qisqa muddatli depozit", "D) Muddat muhim emas"], "a": "A) Moliyaviy maqsadlar va likvidlik ehtiyojlarini hisobga olgan holda optimal muddat"},
        {"q": "Omonatga mablag‘ qo‘yishda inflyatsiya darajasi nima uchun muhim?", "o": ["A) Chunki real daromadni hisoblash va pul qadrsizlanishini oldini olish zarur", "B) Chunki foiz har doim oshadi", "C) Xarajatlar kamayadi", "D) Naqd pul oshadi"], "a": "A) Chunki real daromadni hisoblash va pul qadrsizlanishini oldini olish zarur"},
        {"q": "Bank omonati va jamg‘arma hisobining farqi nima?", "o": ["A) Omonat – belgilangan muddatga qo‘yiladi, jamg‘arma hisob – istalgan vaqtda yechish va qo‘shish mumkin", "B) Ikkisi ham bir xil", "C) Faqat jamg‘arma xavfsiz", "D) Omonat foiz bermaydi"], "a": "A) Omonat – belgilangan muddatga qo‘yiladi, jamg‘arma hisob – istalgan vaqtda yechish va qo‘shish mumkin"},
        {"q": "Siz bir necha depozit variantlarini solishtiryapsiz. Nima asosida tanlov qilish tavsiya etiladi?", "o": ["A) Foiz stavkasi, muddat, kapitalizatsiya turi va bank ishonchliligi asosida", "B) Faqat foiz stavkasi bo‘yicha", "C) Faqat muddat bo‘yicha", "D) Inflyatsiyaga qarab emas"], "a": "A) Foiz stavkasi, muddat, kapitalizatsiya turi va bank ishonchliligi asosida"},
        {"q": "Omonatga mablag‘ qo‘yishda diversifikatsiya nima foyda beradi?", "o": ["A) Mablag‘ni bir nechta depozit va banklarda taqsimlash, xavfni kamaytiradi va barqaror daromadni ta’minlaydi", "B) Faqat bitta depozit foydali", "C) Xarajatlarni oshiradi", "D) Foiz stavkasi avtomatik oshadi"], "a": "A) Mablag‘ni bir nechta depozit va banklarda taqsimlash, xavfni kamaytiradi va barqaror daromadni ta’minlaydi"},
        {"q": "Kapitalizatsiya davri (har oy, har chorak, yil oxiri) foiz daromadiga qanday ta’sir qiladi?", "o": ["A) Foizlar tezroq asosiy summaga qo‘shiladi va daromad oshadi", "B) Foizlar kamayadi", "C) Xarajatlarni oshiradi", "D) Inflyatsiya pasayadi"], "a": "A) Foizlar tezroq asosiy summaga qo‘shiladi va daromad oshadi"},
        {"q": "Omonat turlaridan qaysi biri shaxsiy byudjet uchun eng likvid hisoblanadi?", "o": ["A) Jamg‘arma hisoblar, chunki istalgan vaqtda mablag‘ yechish mumkin", "B) Uzun muddatli depozitlar", "C) Muddatli depozitlar", "D) Kreditlar"], "a": "A) Jamg‘arma hisoblar, chunki istalgan vaqtda mablag‘ yechish mumkin"},
        {"q": "Inflyatsiya yuqori bo‘lgan davrda depozitning real daromadi qanday ta’sir qiladi?", "o": ["A) Nominal foiz daromadi oshsa ham, real daromad pasayishi mumkin", "B) Har doim oshadi", "C) Foizlar barqaror bo‘ladi", "D) Xarajatlar kamayadi"], "a": "A) Nominal foiz daromadi oshsa ham, real daromad pasayishi mumkin"},
        {"q": "Omonatga mablag‘ qo‘yishda yillik foiz stavkasi va muddatni hisobga olgan holda qanday hisoblash tavsiya etiladi?", "o": ["A) Foiz daromadini oldindan hisoblash va byudjetga qo‘shish", "B) Faqat foiz stavkasini bilish kifoya", "C) Muddatni hisoblash shart emas", "D) Inflyatsiya tufayli hisoblash kerak emas"], "a": "A) Foiz daromadini oldindan hisoblash va byudjetga qo‘shish"},
        {"q": "Depozit va jamg‘arma hisobi o‘rtasidagi asosiy farq nima?", "o": ["A) Depozit – belgilangan muddatga va foiz bilan, jamg‘arma esa istalgan vaqtda mablag‘ qo‘yish va yechish mumkin", "B) Ikkisi ham bir xil", "C) Jamg‘arma daromad bermaydi", "D) Depozit foiz bermaydi"], "a": "A) Depozit – belgilangan muddatga va foiz bilan, jamg‘arma esa istalgan vaqtda mablag‘ qo‘yish va yechish mumkin"},
        {"q": "Bank omonatini diversifikatsiya qilish nima foyda beradi?", "o": ["A) Mablag‘ni bir nechta bank va depozit turlarida saqlash, xavfni kamaytiradi va daromadni barqaror qiladi", "B) Faqat bitta depozit xavfsiz", "C) Xarajatlarni oshiradi", "D) Foiz stavkasi oshadi"], "a": "A) Mablag‘ni bir nechta bank va depozit turlarida saqlash, xavfni kamaytiradi va daromadni barqaror qiladi"},
        {"q": "Siz depozit mablag‘ingizni qo‘shimcha daromad olish uchun qaysi strategiya bilan boshqarasiz?", "o": ["A) Optimal muddatli depozit tanlash, kapitalizatsiyadan foydalanish va byudjetni rejalashtirish", "B) Faqat foiz stavkasini hisoblash", "C) Muddatni hisoblash shart emas", "D) Naqd pulni oshirish"], "a": "A) Optimal muddatli depozit tanlash, kapitalizatsiyadan foydalanish va byudjetni rejalashtirish"},
        {"q": "Uy buxgalteriyasi nima uchun muhim?", "o": ["A) Chunki shaxsiy daromad va xarajatlarni nazorat qilish, byudjetni rejalashtirish va moliyaviy barqarorlikni ta’minlashga yordam beradi", "B) Chunki faqat bank depozitlari xavfsiz bo‘ladi", "C) Chunki har oy qarz olish zarur bo‘ladi", "D) Chunki inflyatsiya avtomatik hisoblanadi"], "a": "A) Chunki shaxsiy daromad va xarajatlarni nazorat qilish, byudjetni rejalashtirish va moliyaviy barqarorlikni ta’minlashga yordam beradi"},
        {"q": "Uy byudjetini tuzishda birinchi qadam nima?", "o": ["A) Daromad va xarajatlarni aniqlash va yozib olish", "B) Kredit olish", "C) Naqd pul yig‘ish", "D) Foiz stavkasini oshirish"], "a": "A) Daromad va xarajatlarni aniqlash va yozib olish"},
        {"q": "Xarajatlarni kategoriyalarga ajratish (masalan, oziq-ovqat, transport, uy-joy) nima foyda beradi?", "o": ["A) Pul oqimini kuzatish va keraksiz xarajatlarni aniqlash osonlashadi", "B) Xarajatlarni oshiradi", "C) Foiz daromadi oshadi", "D) Inflyatsiya kamayadi"], "a": "A) Pul oqimini kuzatish va keraksiz xarajatlarni aniqlash osonlashadi"},
        {"q": "Shaxsiy moliyaviy jurnalni yuritish qanday foyda beradi?", "o": ["A) Daromad va xarajatlarni yozib borish, byudjetni tahlil qilish va moliyaviy reja tuzishga yordam beradi", "B) Faqat qarz olishga yordam beradi", "C) Xarajatlarni oshiradi", "D) Naqd pul avtomatik ko‘payadi"], "a": "A) Daromad va xarajatlarni yozib borish, byudjetni tahlil qilish va moliyaviy reja tuzishga yordam beradi"},
        {"q": "Shaxsiy byudjetni rejalashtirishda zaxira jamg‘armasi nima uchun muhim?", "o": ["A) Favqulodda vaziyatlarda moliyaviy barqarorlikni saqlashga yordam beradi", "B) Xarajatlarni oshirish uchun", "C) Foiz stavkasini oshirish uchun", "D) Inflyatsiyani kamaytirish uchun"], "a": "A) Favqulodda vaziyatlarda moliyaviy barqarorlikni saqlashga yordam beradi"},
        {"q": "Uy buxgalteriyasida balans nima maqsadda ishlatiladi?", "o": ["A) Daromad va xarajatlarni solishtirish va byudjetning muvozanatini aniqlash", "B) Faqat qarz olishni ko‘rsatadi", "C) Xarajatlarni oshiradi", "D) Naqd pulni oshiradi"], "a": "A) Daromad va xarajatlarni solishtirish va byudjetning muvozanatini aniqlash"},
        {"q": "Moliyaviy maqsadlarni belgilash nima foyda beradi?", "o": ["A) Byudjetni rejalashtirish va mablag‘ni samarali taqsimlash imkonini beradi", "B) Faqat qarz olish uchun", "C) Xarajatlarni oshiradi", "D) Foiz daromadi oshadi"], "a": "A) Byudjetni rejalashtirish va mablag‘ni samarali taqsimlash imkonini beradi"},
        {"q": "Xarajatlarni kuzatmasdan yashash qanday xavf tug‘diradi?", "o": ["A) Mablag‘ noto‘g‘ri sarflanadi, qarz ortadi va moliyaviy barqarorlik zaiflashadi", "B) Foizlar oshadi", "C) Inflyatsiya kamayadi", "D) Daromad avtomatik oshadi"], "a": "A) Mablag‘ noto‘g‘ri sarflanadi, qarz ortadi va moliyaviy barqarorlik zaiflashadi"},
        {"q": "Shaxsiy byudjetda “majburiy” va “ixtiyoriy” xarajatlarni ajratish nima foyda beradi?", "o": ["A) Keraksiz xarajatlarni qisqartirish va moliyaviy reja tuzish osonlashadi", "B) Xarajatlarni oshiradi", "C) Foiz daromadi oshadi", "D) Inflyatsiya kamayadi"], "a": "A) Keraksiz xarajatlarni qisqartirish va moliyaviy reja tuzish osonlashadi"},
        {"q": "Uy buxgalteriyasini muntazam yuritishning asosiy foydasi nima?", "o": ["A) Moliyaviy qarorlarni ongli qabul qilish, byudjetni boshqarish va moliyaviy barqarorlikni ta’minlash", "B) Faqat qarz olishni osonlashtiradi", "C) Xarajatlarni oshiradi", "D) Naqd pulni oshiradi"], "a": "A) Moliyaviy qarorlarni ongli qabul qilish, byudjetni boshqarish va moliyaviy barqarorlikni ta’minlash"},
        {"q": "Dunyo bo‘ylab ilk banklar qachon va qayerda paydo bo‘lgan?", "o": ["A) XIV-XV asrlarda Italiyada, asosan Florensiya va Venetsiyada", "B) XVIII asrda Angliyada", "C) XX asrda AQShda", "D) XVI asrda Germaniyada"], "a": "A) XIV-XV asrlarda Italiyada, asosan Florensiya va Venetsiyada"},
        {"q": "Bankning asosiy vazifasi nima?", "o": ["A) Pulni jamg‘arish, qarz berish, moliyaviy vositalarni ta’minlash va iqtisodiy faoliyatni qo‘llab-quvvatlash", "B) Faqat kredit berish", "C) Faqat inflyatsiya nazorat qilish", "D) Faqat savdo bilan shug‘ullanish"], "a": "A) Pulni jamg‘arish, qarz berish, moliyaviy vositalarni ta’minlash va iqtisodiy faoliyatni qo‘llab-quvvatlash"},
        {"q": "Markaziy bankning asosiy vazifasi nima?", "o": ["A) Milliy valyutani nazorat qilish, inflyatsiyani boshqarish, bank tizimini barqarorlashtirish", "B) Faqat depozitlar bilan shug‘ullanish", "C) Faqat kredit berish", "D) Faqat shaxsiy byudjetni nazorat qilish"], "a": "A) Milliy valyutani nazorat qilish, inflyatsiyani boshqarish, bank tizimini barqarorlashtirish"},
        {"q": "Banklar nimaga qarz beradi va foiz oladi?", "o": ["A) Chunki qarz mablag‘larini iqtisodiy faoliyatga yo‘naltirish va daromad olish imkonini beradi", "B) Faqat xarajatlarni oshirish uchun", "C) Naqd pulni kamaytirish uchun", "D) Inflyatsiyani kamaytirish uchun"], "a": "A) Chunki qarz mablag‘larini iqtisodiy faoliyatga yo‘naltirish va daromad olish imkonini beradi"},
        {"q": "Bank tizimining asosiy elementlari qaysilar?", "o": ["A) Markaziy bank, tijorat banklari, kredit ittifoqlari va boshqa moliyaviy institutlar", "B) Faqat tijorat banklari", "C) Faqat depozitlar", "D) Faqat qimmatbaho metallar"], "a": "A) Markaziy bank, tijorat banklari, kredit ittifoqlari va boshqa moliyaviy institutlar"},
        {"q": "Birinchi zamonaviy tijorat banklari qayerda paydo bo‘lgan?", "o": ["A) XVI–XVII asrlarda Italiyada va Gollandiyada", "B) XVIII asrda Angliyada", "C) XIX asrda AQShda", "D) XX asrda Germaniyada"], "a": "A) XVI–XVII asrlarda Italiyada va Gollandiyada"},
        {"q": "Bank kartalari va elektron to‘lov tizimlari nima uchun muhim?", "o": ["A) Chunki ular naqd pulni kamaytiradi, tezkor va xavfsiz to‘lov imkonini beradi", "B) Faqat xarajatlarni oshiradi", "C) Naqd pulni oshiradi", "D) Inflyatsiyani kamaytiradi"], "a": "A) Chunki ular naqd pulni kamaytiradi, tezkor va xavfsiz to‘lov imkonini beradi"},
        {"q": "Banklar qanday moliyaviy xizmatlarni ko‘rsatadi?", "o": ["A) Depozitlar qabul qilish, kredit berish, investitsiya xizmatlari, valyuta operatsiyalari", "B) Faqat depozitlar", "C) Faqat kredit berish", "D) Faqat inflyatsiya nazorat qilish"], "a": "A) Depozitlar qabul qilish, kredit berish, investitsiya xizmatlari, valyuta operatsiyalari"},
        {"q": "Bank tizimi rivojlanishi iqtisodiyotga qanday ta’sir qiladi?", "o": ["A) Mablag‘ oqimini samarali taqsimlaydi, investitsiya va ish o‘rinlarini yaratadi", "B) Xarajatlarni oshiradi", "C) Faqat foizlarni oshiradi", "D) Naqd pulni kamaytiradi"], "a": "A) Mablag‘ oqimini samarali taqsimlaydi, investitsiya va ish o‘rinlarini yaratadi"},
        {"q": "Zamonaviy bank tizimining asosiy tamoyillari qaysilar?", "o": ["A) Shaffoflik, ishonchlilik, moliyaviy xavfsizlik, mijozlarni himoya qilish", "B) Faqat foiz olish", "C) Faqat depozitlar", "D) Faqat qarz berish"], "a": "A) Shaffoflik, ishonchlilik, moliyaviy xavfsizlik, mijozlarni himoya qilish"},
        {"q": "Bank orqali amalga oshiriladigan asosiy operatsiyalar qaysilar?", "o": ["A) Depozit qabul qilish, kredit berish, valyuta ayirboshlash, to‘lovlarni amalga oshirish", "B) Faqat depozit qabul qilish", "C) Faqat kredit berish", "D) Faqat inflyatsiya nazorat qilish"], "a": "A) Depozit qabul qilish, kredit berish, valyuta ayirboshlash, to‘lovlarni amalga oshirish"},
        {"q": "Onlayn bank xizmatlarining asosiy foydasi nima?", "o": ["A) Tezkor, qulay va xavfsiz to‘lovlar, hisobni nazorat qilish imkoniyati", "B) Xarajatlarni oshiradi", "C) Naqd pulni kamaytiradi", "D) Foiz stavkasini oshiradi"], "a": "A) Tezkor, qulay va xavfsiz to‘lovlar, hisobni nazorat qilish imkoniyati"},
        {"q": "Plastik kartalar orqali amalga oshiriladigan operatsiyalar qaysilar?", "o": ["A) Naqd pul yechish, to‘lovlarni amalga oshirish, hisobni nazorat qilish", "B) Faqat depozit qo‘yish", "C) Faqat kredit berish", "D) Inflyatsiyani kamaytirish"], "a": "A) Naqd pul yechish, to‘lovlarni amalga oshirish, hisobni nazorat qilish"},
        {"q": "Bank hisobvarag‘iga mablag‘ kiritishning asosiy usullari qaysilar?", "o": ["A) Naqd pul, elektron pul, boshqa banklar orqali o‘tkazmalar", "B) Faqat naqd pul", "C) Faqat boshqa bank orqali", "D) Faqat valyuta ayirboshlash"], "a": "A) Naqd pul, elektron pul, boshqa banklar orqali o‘tkazmalar"},
        {"q": "Kredit operatsiyalarida foiz stavkasini tanlash nima muhim?", "o": ["A) Chunki foiz stavkasi qarzning umumiy qiymatini belgilaydi va byudjetga ta’sir qiladi", "B) Foizlar avtomatik hisoblanadi", "C) Xarajatlar oshadi", "D) Naqd pul kamayadi"], "a": "A) Chunki foiz stavkasi qarzning umumiy qiymatini belgilaydi va byudjetga ta’sir qiladi"}
    ]
    # Differensial tenglamalar bloklari
if 'dt_1_70' not in st.session_state:
    st.session_state.dt_1_70 = [
        {
            "q": "Erkli o‘zgaruvchi $x \in (a,b)$, noma’lum funksiyasi $y(x)$ va uning $y'(x), y''(x), \dots, y^{(n)}(x)$ hosilalari orasidagi ushbu $F(x,y(x),y'(x),\dots,y^{(n)}(x))=0$ funksional bog‘lanishga...",
            "o": [
                "1-tartibli oddiy differensial tenglama deyiladi",
                "3-tartibli oddiy differensial tenglama deyiladi",
                "2-tartibli oddiy differensial tenglama deyiladi",
                "n-tartibli oddiy differensial tenglama deyiladi"
            ],
            "a": "n-tartibli oddiy differensial tenglama deyiladi"
        },
        {
            "q": "Quyidagi masalalardan qaysi biriga birinchi tartibli hosilaga nisbatan yechilgan differensial tenglama uchun Koshi masalasi deyiladi?",
            "o": [
                "$y' = f(x,y), y(x_0) = y_0$",
                "$y'' = f(x,y), y(x_0) = y_0$",
                "$y' = f(x,y), y'(x_0) = y_0$",
                "$y'' = f(x,y), y'(x_0) = y_0$"
            ],
            "a": "$y' = f(x,y), y(x_0) = y_0$"
        },
        {
            "q": "Quyidagi masalalardan qaysi biriga ikkinchi tartibli hosilaga nisbatan yechilgan differensial tenglama uchun Koshi masalasi deyiladi?",
            "o": [
                "$y'' = f(x,y,y'), y(x_0) = y_0, y'(x_0) = y_0$",
                "$y' = f(x,y,y'), y(x_0) = y_0, y'(x_0) = y_0$",
                "$y' = f(x,y), y'(x_0) = y_0$",
                "$y'' = f(x,y), y'(x_0) = y_0$"
            ],
            "a": "$y'' = f(x,y,y'), y(x_0) = y_0, y'(x_0) = y_0$"
        },
        {
            "q": "Izoklina deb nimaga aytiladi?",
            "o": [
                "Tekislikdagi shunday nuqtalarning geometrik o‘rniga aytiladiki, u nuqtalarda berilgan differensial tenglama integral chiziqlariga o‘tkazilgan urinmalar Ox o‘qining musbat yo‘nalishi bilan bir xil burchak tashkil etadi.",
                "Tekislikdagi shunday nuqtalarga aytiladiki, u nuqtalarda berilgan differensial tenglama yagona yechimga ega bo‘ladi.",
                "Tekislikdagi shunday nuqtalarning geometrik o‘rniga aytiladiki, u nuqtalarda berilgan differensial tenglama integral chiziqlariga o‘tkazilgan urinmalar Oy o‘qi bilan bir xil burchak tashkil etadi.",
                "Tekislikdagi shunday nuqtalarning geometrik o‘rniga aytiladiki, u nuqtalar faqat ellipsdan iborat bo‘ladi."
            ],
            "a": "Tekislikdagi shunday nuqtalarning geometrik o‘rniga aytiladiki, u nuqtalarda berilgan differensial tenglama integral chiziqlariga o‘tkazilgan urinmalar Ox o‘qining musbat yo‘nalishi bilan bir xil burchak tashkil etadi."
        },
        {
            "q": "Ushbu $y' = f(x) \cdot g(y)$ ko‘rinishdagi differensial tenglama qanday differensial tenglama deyiladi?",
            "o": [
                "Koshi tenglamasi",
                "O‘zgaruvchilari ajraladigan differensial tenglama",
                "Rikkati differensial tenglamasi",
                "Bernulli differensial tenglamasi"
            ],
            "a": "O‘zgaruvchilari ajraladigan differensial tenglama"
        }
    ]

if 'dt_71_140' not in st.session_state:
    st.session_state.dt_71_140 = [] # 71-140 savollar

if 'dt_141_210' not in st.session_state:
    st.session_state.dt_141_210 = [] # 141-210 savollar

if 'dt_211_300' not in st.session_state:
    st.session_state.dt_211_300 = [] # 211-300 savollar

# 4. Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'current_q_index' not in st.session_state: st.session_state.current_q_index = 0
if 'user_score' not in st.session_state: st.session_state.user_score = 0
if 'answered' not in st.session_state: st.session_state.answered = False
if 'selected_option' not in st.session_state: st.session_state.selected_option = None

# --- ASOSIY MANTIQIY ZANJIR ---

# 1. Foydalanuvchi tizimga kirmagan bo'lsa
if not st.session_state.get('logged_in', False):
    # Kirish oynasidagi logotip
    st.image("sayt.jpg", width=260)
    
    users = {
        "Murat": "12062006", "Nilufar": "Nilufar0455", "Radjabboyeva_m": "12345678",
        "Minjiq_qiz": "Minjiq_qiz1234", "Lola": "Lola0504", "341241101229": "Oydin005",
        "Sultanovamarufa": "02112006Sm", "Shahriyor": "Poxxuy", "Ixtiyor": "200606",
        "Xudayberganovaf": "Farangiz0616", "Urunbayevasevinch": "Sevinch07042005",
        "Abdullayev": "Kamol05", "Ixlos": "Ixlos05", "Gulsanam": "2810xaydarova",
        "Samandarov": "Shoxrux06", "Xudayberganova": "Sevinch06", "Erkayev": "Akmal06", 
        "CharosD": "DCh07172005", "Rozimova": "Sevinch2", "MadrimovaG": "Gulshoda006", 
        "Rozmetov": "Bekchon05", "admin": "murat_admin", "Yuldashova":"Zuxra05", "otaboyeva": "sevinch01",
        "iskandarova": "maftuna12", "qadamova": "aziza23"
    }
    
    u_login = st.text_input("Foydalanuvchi nomi (Login):")
    u_pass = st.text_input("Parol:", type="password")

    if st.button("KIRISH"):
        if u_login in users and users[u_login] == u_pass:
            st.session_state.logged_in = True
            st.session_state.u_login = u_login
            st.rerun()
        else:
            st.error("Login yoki parol xato!")

# 2. Foydalanuvchi tizimga kirgan bo'lsa
else:
    # --- ADMIN PANEL BOSHLANISHI ---
    # Bu yerda o'zingizni loginngizni yozing (masalan, "Murat")
    if st.session_state.get('u_login') == "admin":
        with st.expander("🛡️ ADMIN PANEL (Foydalanuvchilar harakati)"):
            if os.path.exists("user_logs.csv"):
                df = pd.read_csv("user_logs.csv")
                st.dataframe(df, use_container_width=True)
                
                if st.button("🗑️ Loglarni tozalash"):
                    os.remove("user_logs.csv")
                    st.rerun()
            else:
                st.info("Hozircha hech qanday harakat qayd etilmadi.")
            
            if st.button("⬅️ Tizimdan chiqish"):
                st.session_state.logged_in = False
                st.rerun()
        st.divider() # Panel va test orasini ajratish
    # --- ADMIN PANEL TUGASHI ---

    # Test jarayoni boshlanadi
    if not st.session_state.get('test_started', False):
        # ... (bu yerda eski menyu kodingiz davom etadi)
        # --- MENYU QISMI ---
        st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

        # Elementlarni o'rtaga surish uchun ustunlar
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            # Logotipni markazga olish
            st.image("sayt.jpg", use_container_width=True)
            
            # Sarlavhani markazlashtirish
            st.markdown("<h2 style='text-align: center; margin-top: 0;'>🚀 Fan va Bo'limni tanlang</h2>", unsafe_allow_html=True)
            
            # 1. Fan tanlash menyusi
            fan = st.selectbox("Fanni tanlang:", 
                               ["Moliyaviy savodxonlik", "Differensial tenglamalar", "Python Dasturlash"])
            
            # 2. Bo'lim tanlash (Fan turiga qarab o'zgaradi)
            if fan == "Moliyaviy savodxonlik":
                st.markdown("<p style='text-align: center; color: #475569;'>📚 Bo'limni tanlang:</p>", unsafe_allow_html=True)
                blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-300"], label_visibility="collapsed")
            elif fan == "Differensial tenglamalar":
                st.markdown("<p style='text-align: center; color: #475569;'>📐 Differensial tenglamalar testi</p>", unsafe_allow_html=True)
                blok = "Diff_Tenglamalar"
            else:
                st.markdown("<p style='text-align: center; color: #475569;'>🐍 Python dasturlash testi</p>", unsafe_allow_html=True)
                blok = "Python_Test"

            # 3. BOSHLA tugmasi va mantiqi
            if st.button("🚀 BOSHLA"):
                st.session_state.current_fan = fan
                # Tanlangan fanga qarab savollarni yuklash
                if fan == "Moliyaviy savodxonlik":
                    if blok == "1-70": st.session_state.active_questions = list(st.session_state.ms_1_70)
                    elif blok == "71-140": st.session_state.active_questions = list(st.session_state.ms_71_140)
                    elif blok == "141-210": st.session_state.active_questions = list(st.session_state.ms_141_210)
                    elif blok == "211-300": st.session_state.active_questions = list(st.session_state.ms_211_300)
                elif fan == "Differensial tenglamalar":
                    st.session_state.active_questions = list(st.session_state.dt_1_70)
                elif fan == "Python Dasturlash":
                    st.session_state.active_questions = list(st.session_state.python_testlar)
                
                # Savollarni aralashtirish
                random.shuffle(st.session_state.active_questions)
                for q in st.session_state.active_questions:
                    random.shuffle(q['o'])
                    
                st.session_state.test_started = True
                st.session_state.current_q_index = 0
                st.session_state.user_score = 0
                st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        # --- TEST JARAYONI ---
        q_idx = st.session_state.get('current_q_index', 0)
        questions = st.session_state.get('active_questions', [])
        
        if q_idx < len(questions):
            curr = questions[q_idx]
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>Savol {q_idx + 1}/{len(questions)}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 18px; font-weight: bold; text-align: center;'>{curr['q']}</p>", unsafe_allow_html=True)

            if not st.session_state.get('answered', False):
                ans = st.radio("Variantlar:", curr['o'], index=None, key=f"q_{q_idx}", label_visibility="collapsed")
                
                col_a, col_b = st.columns([1, 1])
                with col_a:
                    if st.button("✅ TASDIQLASH"):
                        if ans:
                            st.session_state.answered = True
                            st.session_state.selected_option = ans
                            if ans == curr['a']: 
                                st.session_state.user_score += 1
                            st.rerun()
                        else:
                            st.warning("Iltimos, variantni tanlang!")
                
                with col_b:
                    if st.button("🛑 TO'XTATISH"):
                        # To'xtatganda sessiyadan savollar uzunligini olib, oxirgi sahifaga o'tamiz
                        questions_len = len(st.session_state.get('active_questions', []))
                        st.session_state.current_q_index = questions_len
                        st.rerun()
            
            else:  
                # Javob berilgandan keyin natijani ko'rsatish
                for opt in curr['o']:
                    if opt == curr['a']:
                        st.success(f"To'g'ri javob: {opt} ✔️")
                    elif opt == st.session_state.get('selected_option'):
                        st.error(f"Sizning javobingiz: {opt} ❌")
                    else:
                        st.write(opt)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    if st.button("Keyingi ➔"):
                        st.session_state.current_q_index += 1
                        st.session_state.answered = False
                        st.session_state.selected_option = None
                        st.rerun()
                with col2:
                    if st.button("📊 NATIJA"):
                        st.session_state.current_q_index = len(questions)
                        st.rerun()
                with col3:
                    if st.button("🏠 MENU"):
                        st.session_state.test_started = False
                        st.session_state.current_q_index = 0
                        st.session_state.user_score = 0
                        st.session_state.answered = False
                        st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)

        else:
           
            # --- NATIJALAR SAHIFASI ---
            st.markdown('<div class="quiz-card" style="text-align: center;">', unsafe_allow_html=True)
            st.balloons()
            
            # Xatolikni oldini olish uchun sessiyadan ma'lumotlarni xavfsiz olamiz
            # Agar 'fan' topilmasa, 'Noma'lum fan' deb yozadi
            current_user = st.session_state.get('u_login', 'Mehmon')
            current_subject = fan if 'fan' in locals() else "Aniqlanmagan fan"
            current_score = st.session_state.get('user_score', 0)
            total_questions = len(questions) if 'questions' in locals() else 0
            
            # Ma'lumotlarni yozish (faqat bir marta)
            if 'log_saved' not in st.session_state:
                save_log(current_user, current_subject, current_score, total_questions)
                st.session_state.log_saved = True # Qayta-qayta yozmaslik uchun
            
            st.markdown("<h2>Test yakunlandi!</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1>Natija: {current_score} / {total_questions}</h1>", unsafe_allow_html=True)
            
            if st.button("🏠 ASOSIY MENUGA QAYTISH"):
                st.session_state.test_started = False
                st.session_state.current_q_index = 0
                st.session_state.user_score = 0
                st.session_state.answered = False
                if 'log_saved' in st.session_state: del st.session_state.log_saved
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
# 3. Footer (Har doim ko'rinadi)
st.markdown(f"""
    <div class="footer" style="text-align: center; padding-top: 20px; padding-bottom: 20px;">
        <p style="margin: 0; font-size: 13px; color: #64748B; font-family: sans-serif;">Yaratuvchi: <b>Murat Sultanov</b></p>
        <div style="margin-top: 8px; display: flex; justify-content: center; align-items: center; gap: 20px;">
            <a href="https://t.me/murat_sultanov" target="_blank" style="display: flex; align-items: center; gap: 5px; color: #0088cc; text-decoration: none; font-size: 14px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="18" height="18">
                <span>@murat_sultanov</span>
            </a>
            <a href="https://instagram.com/muratsultanov__" target="_blank" style="display: flex; align-items: center; gap: 5px; color: #E1306C; text-decoration: none; font-size: 14px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="18" height="18">
                <span>@muratsultanov__</span>
            </a>
        </div>
    </div>
""", unsafe_allow_html=True)
