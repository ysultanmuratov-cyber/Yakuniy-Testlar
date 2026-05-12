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
    .stApp { margin-top: -100px !important; }
    header, [data-testid="stHeader"] { display: none !important; }
    
    /* Radio button matni uchun qo'shimcha havo */
    .stRadio label {
        padding: 20px 0px !important;
        line-height: 2.5 !important;
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
        },
        {
            "q": "Agar quyidagi $y' = f(x,y)$ differensial tenglamaning o‘ng tomonidagi $f(x,y)$ funksiya $\\forall \\lambda > 0$ uchun $f(\\lambda x, \\lambda y) = f(x,y)$ shartni bajarsa, u holda bu tenglamaga qanday differensial tenglama deyiladi?",
            "o": [
                "Koshi tenglamasi",
                "Bir jinsli differensial tenglama",
                "O‘zgaruvchilari ajraladigan differensial tenglama",
                "Bernulli differensial tenglamasi"
            ],
            "a": "Bir jinsli differensial tenglama"
        },
        {
            "q": "Ushbu $y' = a(x)y + b(x)$ ko‘rinishdagi tenglamaga qanday differensial tenglama deyiladi?",
            "o": [
                "Birinchi tartibli chiziqli differensial tenglamasi",
                "Bernulli differensial tenglamasi",
                "Rikkati differensial tenglamasi",
                "Eyler differensial tenglamasi"
            ],
            "a": "Birinchi tartibli chiziqli differensial tenglamasi"
        },
        {
            "q": "Bernulli differensial tenglamasining ko‘rinishini aniqlang?",
            "o": [
                "$y' = a(x)y' + b(x)y^3$",
                "$y' = a(x)y' + b(x)y$",
                "$y' = a(x)y' + b(x)y^n$",
                "$y' = a(x)y + b(x)y^n$"
            ],
            "a": "$y' = a(x)y + b(x)y^n$"
        },
        {
            "q": "Ushbu $y' = a(x)y + b(x)y^n$ Bernulli differensial tenglamasida $n=0$ bo‘lsa, qanday differensial tenglama hosil bo‘ladi?",
            "o": [
                "Chiziqli differensial tenglamasi",
                "Bir jinsli differensial tenglama",
                "Rikkati differensial tenglamasi",
                "Bernulli differensial tenglamasi"
            ],
            "a": "Chiziqli differensial tenglamasi"
        },
        {
            "q": "Rikkati differensial tenglamasining ko‘rinishini aniqlang?",
            "o": [
                "$y'' = a(x)y^2 + b(x)y + c(x)$",
                "$y' = a(x)y^2 + b(x)y'$",
                "$y' = a(x)y^2 + b(x)y + c(x)$",
                "$y' = a(x)y^4 + b(x)y' + c(x)$"
            ],
            "a": "$y' = a(x)y^2 + b(x)y + c(x)$"
        },
        {
            "q": "Umumiy holda Rikkati differensial tenglamasi kvadraturada integrallanadimi?",
            "o": [
                "integrallanadi",
                "integrallanmaydi",
                "(0,1) oraliqda integrallanadi",
                "(0,2) oraliqda integrallanadi"
            ],
            "a": "integrallanmaydi"
        },
        {
            "q": "Rikkati tenglamasining kamida nechta xususiy yechimi ma'lum bo'lsa, u holda uning umumiy yechimi bitta kvadratura yordamida topiladi?",
            "o": ["2 ta", "3 ta", "1 ta", "4 ta"],
            "a": "2 ta"
        },
        {
            "q": "Rikkati tenglamasining kamida nechta xususiy yechimi ma'lum bo'lsa, u holda uning umumiy yechimi kvadraturasiz topiladi?",
            "o": ["2 ta", "3 ta", "1 ta", "4 ta"],
            "a": "3 ta"
        },
        {
            "q": "Rikkati tenglamasining kamida nechta xususiy yechimi ma'lum bo'lsa, u holda uning umumiy yechimi ikkita kvadratura yordamida topiladi?",
            "o": ["2 ta", "3 ta", "1 ta", "4 ta"],
            "a": "1 ta"
        },
        {
            "q": "Ushbu $y' = a(x)y + b(x)y^n$ Bernulli differensial tenglamasining umumiy yechimini topishda quyidagi almashtirishlardan qaysi biri qo'llaniladi?",
            "o": [
                "$z = y^{1-n}$",
                "$z = y^{1+n}$",
                "$z = y^n$",
                "$z = y^{n-1}$"
            ],
            "a": "$z = y^{1-n}$"
        },
        {
            "q": "To‘liq differensialli tenglamaning ko‘rinishini aniqlang?",
            "o": [
                "$M(x,y)dx + N(x,y)dy = 0, \\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial y}$",
                "$M(x,y)dy + N(x,y)dx = 0, \\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial x}$",
                "$M(x,y)dx + N(x,y)dy = 0, \\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial x}$",
                "$M(x,y)dx + N(x,y)dy = 0, \\frac{\partial M}{\partial y} < \\frac{\partial N}{\partial x}$"
            ],
            "a": "$M(x,y)dx + N(x,y)dy = 0, \\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial x}$"
        },
        {
            "q": "Ushbu $M(x,y)dx + N(x,y)dy = 0$ differensial tenglama to‘liq differensial tenglama bo‘lishi uchun qanday shart bajarilishini ko‘rsating?",
            "o": [
                "$\\frac{\partial M}{\partial y} = -\\frac{\partial N}{\partial x}$",
                "$\\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial y}$",
                "$-\\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial x}$",
                "$\\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial x}$"
            ],
            "a": "$\\frac{\partial M}{\partial y} = \\frac{\partial N}{\partial x}$"
        },
        {
            "q": "$y' = f(x,y)$ tenglama uchun qo‘yilgan Koshi masalasi yechimi mavjud va yagona bo‘lishi uchun quyidagi shartlardan qaysi biri bajarilishi zarur?",
            "o": [
                "$f(x,y)$ funksiya yopiq sohada aniqlangan va uzluksiz bo‘lib, $y$ o‘zgaruvchi bo‘yicha Lipshits shartini qanoatlantirsa",
                "$f(x,y)$ funksiya yopiq sohada aniqlangan va uzluksiz bo‘lib, $x$ o‘zgaruvchi bo‘yicha o‘suvchi bo‘lsa",
                "$f(x,y)$ funksiya yopiq sohada aniqlangan va uzluksiz bo‘lib, $x$ o‘zgaruvchi bo‘yicha kamayuvchi bo‘lsa",
                "$f(x,y)$ funksiya yopiq sohada aniqlangan va uzluksiz bo‘lib, $x$ o‘zgaruvchi bo‘yicha davriy bo‘lsa"
            ],
            "a": "$f(x,y)$ funksiya yopiq sohada aniqlangan va uzluksiz bo‘lib, $y$ o‘zgaruvchi bo‘yicha Lipshits shartini qanoatlantirsa"
        },
        {
            "q": "Ushbu $y' = f(x,y)$ differensial tenglamada $f(x,y)$ funksiya $x, y$ o‘zgaruvchilar bo‘yicha $n \\geq 1$ marta uzluksiz differensiallanuvchi bo‘lsa, u holda qaralayotgan differensial tenglamaning ixtiyoriy yechimi:",
            "o": [
                "$(n+1)$ marta differensiallanuvchi bo‘ladi",
                "$(n+2)$ marta differensiallanuvchi bo‘ladi",
                "$(n+3)$ marta differensiallanuvchi bo‘ladi",
                "$(n+4)$ marta differensiallanuvchi bo‘ladi"
            ],
            "a": "$(n+1)$ marta differensiallanuvchi bo‘ladi"
        },
        {
            "q": "$P$ to‘g‘ri to‘rtburchakda aniqlangan $f(x,y)$ funksiya uchun $y$ o‘zgaruvchi bo‘yicha Lipshits shartini ko‘rsating?",
            "o": [
                "$|f(x,y_1) - f(x,y_2)| \\leq N |y_1 - y_2|, \\forall (x, y_j) \\in P, j=1,2, \\exists N > 0$",
                "$|f(x,y_1) - f(x,y_2)| = |f(x,y_1)|$",
                "$|f(x,y_1) - f(x,y_2)| > N |y_1 - y_2|, \\forall (x, y_j) \\in P, j=1,2, \\exists N > 0$",
                "$|f(x,y_1) - f(x,y_2)| \\geq |y_1 - y_2|, \\exists N > 0$"
            ],
            "a": "$|f(x,y_1) - f(x,y_2)| \\leq N |y_1 - y_2|, \\forall (x, y_j) \\in P, j=1,2, \\exists N > 0$"
        },
        {
            "q": "$y_1(x)$ va $y_2(x)$ funksiyalarning Vronskiy determinantini ko'rsating?",
            "o": [
                "$W(x) = \\begin{vmatrix} y_1(x) & y_2(x) \\\\ y_1'(x) & y_2'(x) \\end{vmatrix}$",
                "$W(x) = \\begin{vmatrix} -y_1(x) & y_2(x) \\\\ y_1'(x) & y_2'(x) \\end{vmatrix}$",
                "$W(x) = \\begin{vmatrix} y_1(x) & -y_2(x) \\\\ y_1'(x) & y_2'(x) \\end{vmatrix}$",
                "$W(x) = \\begin{vmatrix} y_1(x) & y_2(x) \\\\ y_1''(x) & y_2''(x) \\end{vmatrix}$"
            ],
            "a": "$W(x) = \\begin{vmatrix} y_1(x) & y_2(x) \\\\ y_1'(x) & y_2'(x) \\end{vmatrix}$"
        },
        {
            "q": "Ushbu $y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$ differensial tenglamaning ixtiyoriy $n$ ta $y_1(x), y_2(x), \\dots, y_n(x)$ chiziqli bog'lanmagan yechimlariga...",
            "o": [
                "normalangan yechimlar sistemasi deyiladi",
                "maxsus yechimlar sistemasi deyiladi",
                "fundamental yechimlar sistemasi deyiladi",
                "ortonormallangan yechimlar sistemasi deyiladi"
            ],
            "a": "fundamental yechimlar sistemasi deyiladi"
        },
        {
            "q": "Fundamental yechimlar sistemasi $\\cos x$ va $\\sin x$ bo'lgan differensial tenglamani toping?",
            "o": [
                "$y'' + y = 0$",
                "$y'' - y = 0$",
                "$y'' + y' = 0$",
                "$y'' = 0$"
            ],
            "a": "$y'' + y = 0$"
        },
        {
            "q": "Quyidagi shartlardan qaysi biri ushbu $y''' = f(x, y, y', y'')$ differensial tenglama uchun $x_0$ nuqtada qo'yilgan Koshi boshlang'ich sharti bo'ladi?",
            "o": [
                "$y(x_0) = y_0$",
                "$y(x_0) = y_0, y'(x_0) = y'_0, y''(x_0) = y''_0$",
                "$y(x_0) = y_0, y'(x_0) = y'_0$",
                "$y(x_0) = y_0, y'(x_0) = y'_0, y'''(x_0) = y'''_0$"
            ],
            "a": "$y(x_0) = y_0, y'(x_0) = y'_0, y''(x_0) = y''_0$"
        },
        {
            "q": "Eyler differensial tenglamasini ko'rsating?",
            "o": [
                "$y^{(n)} + y^{(n-1)} + \\dots + a_{n-1}y' = 0$",
                "$x^n y^{(n)} + a_1 x^{n-1} y^{(n-1)} + \\dots + a_{n-1} x y' + a_n y = 0$",
                "$x y^{(n)} + a_1 x y^{(n-1)} + \\dots + a_{n-1} x y' + a_n y = 0$",
                "$x y^{(n)} + a_1 x^{n-1} y^{(n-1)} + \\dots + a_{n-1} y' + y = 0$"
            ],
            "a": "$x^n y^{(n)} + a_1 x^{n-1} y^{(n-1)} + \\dots + a_{n-1} x y' + a_n y = 0$"
        },
        {
            "q": "Eyri differensial tenglamasini ko'rsating?",
            "o": [
                "$y'' - x^2 y = 0$",
                "$y'' - x y' = 0$",
                "$y'' + x y = 0$",
                "$y'' + y = 0$"
            ],
            "a": "$y'' + x y = 0$"
        },
        {
            "q": "Bessel differensial tenglamasini ko‘rsating?",
            "o": [
                "$x^2 y'' + xy' + (x^2 - \\nu^2)y = 0, \\nu \\text{-haqiqiy parametr}$",
                "$xy'' + xy' + (x^2 - \\nu^2)y = 0, \\nu \\text{-haqiqiy parametr}$",
                "$y'' + xy' + \\nu^2 y = 0, \\nu \\text{-haqiqiy parametr}$",
                "$y'' + y' + (x^2 - \\nu^2)y = 0, \\nu \\text{-haqiqiy parametr}$"
            ],
            "a": "$x^2 y'' + xy' + (x^2 - \\nu^2)y = 0, \\nu \\text{-haqiqiy parametr}$"
        },
        {
            "q": "Vandermond determinantini ko‘rsating?",
            "o": [
                "$V_n = \\begin{vmatrix} 2 & 2 & \\dots & 2 \\\\ 2 & 2 & \\dots & 2 \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\lambda_1^n & \\lambda_2^n & \\dots & \\lambda_n^n \\end{vmatrix}$",
                "$V_n = \\begin{vmatrix} 1 & 1 & \\dots & 1 \\\\ 1 & 1 & \\dots & 1 \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\lambda_1^n & \\lambda_2^n & \\dots & \\lambda_n^n \\end{vmatrix}$",
                "$V_n = \\begin{vmatrix} 1 & 1 & \\dots & 1 \\\\ \\lambda_1 & \\lambda_2 & \\dots & \\lambda_n \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\lambda_1^{n-1} & \\lambda_2^{n-1} & \\dots & \\lambda_n^{n-1} \\end{vmatrix}$",
                "$V_n = \\begin{vmatrix} 1 & 1 & \\dots & 1 \\\\ \\lambda_1 & \\lambda_2 & \\dots & \\lambda_n \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\lambda_1 & \\lambda_2 & \\dots & \\lambda_n \\end{vmatrix}$"
            ],
            "a": "$V_n = \\begin{vmatrix} 1 & 1 & \\dots & 1 \\\\ \\lambda_1 & \\lambda_2 & \\dots & \\lambda_n \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ \\lambda_1^{n-1} & \\lambda_2^{n-1} & \\dots & \\lambda_n^{n-1} \\end{vmatrix}$"
        },
        {
            "q": "Ushbu $x^n y^{(n)} + a_1 x^{n-1} y^{(n-1)} + \\dots + a_{n-1} xy' + a_n y = 0$ Eyler tenglamasini qanday almashtirish yordamida n-tartibli bir jinsli o‘zgarmas koeffitsiyentli differensial tenglamaga keltirish mumkin?",
            "o": [
                "$x = 2e^t$",
                "$y = 1 + e^{2x}$",
                "$y = 1 - e^x$",
                "$x = e^t$"
            ],
            "a": "$x = e^t$"
        },
        {
            "q": "Agar $f(x)$ funksiyani $x_0 \\in \\mathbb{R}$ nuqtaning biror atrofida darajali qatorga yoyish mumkin bo‘lsa, $f(x)$ ga ...",
            "o": [
                "davriy funksiya deyiladi",
                "golomorf funksiya deyiladi",
                "uzluksiz funksiya deyiladi",
                "meromorf funksiya deyiladi"
            ],
            "a": "golomorf funksiya deyiladi"
        },
        {
            "q": "Ushbu $y^{(n)} = f(x)$ tenglamaning umumiy yechimi qanday ko‘rinishda bo‘ladi?",
            "o": [
                "$y(x) = C_1 \\frac{x^{n-1}}{(n-1)!} + C_2 \\frac{x^{n-2}}{(n-2)!} + \\dots + C_{n-1}x + C_n$",
                "$y(x) = \\frac{1}{(n-1)!} \\int_{x_0}^x f(t)(x-t)^{n-1} dt + C_1 \\frac{x^{n-1}}{(n-1)!} + C_2 \\frac{x^{n-2}}{(n-2)!} + \\dots + C_{n-1}x + C_n$",
                "$y(x) = \\frac{1}{(n-1)!} \\int_{x_0}^x f(t)(x-t)^{n-1} dt$",
                "$y(x) = \\frac{1}{n!} \\int_{x_0}^x f(t)(x-t)^n dt$"
            ],
            "a": "$y(x) = \\frac{1}{(n-1)!} \\int_{x_0}^x f(t)(x-t)^{n-1} dt + C_1 \\frac{x^{n-1}}{(n-1)!} + C_2 \\frac{x^{n-2}}{(n-2)!} + \\dots + C_{n-1}x + C_n$"
        },
        {
            "q": "Bir jinsli o‘zgarmas koeffitsiyentli chiziqli differensial tenglamaning umumiy ko‘rinishini toping?",
            "o": [
                "$y^{(n)} + a_1(x)y^{(n-1)} + \\dots + a_{n-1}(x)y' = 0$",
                "$y^{(n)} + a_1(x)y^{(n-1)} + \\dots + a_{n-1}(x)y' + a_n(x)y = 0$",
                "$y^{(n)} + c_1 y^{(n-1)} + \\dots + c_{n-1}y' + c_n y = 0$",
                "$y^{(n)} + a_1 x y^{n-1} + \\dots + a_{n-1} x y' = 0$"
            ],
            "a": "$y^{(n)} + c_1 y^{(n-1)} + \\dots + c_{n-1}y' + c_n y = 0$"
        },
        {
            "q": "Bir jinsli bo‘lmagan o‘zgarmas koeffitsiyentli chiziqli differensial tenglamaning umumiy ko‘rinishini toping?",
            "o": [
                "$y^{(n)} + a_1(x)y^{(n-1)} + \\dots + a_{n-1}(x)y' = f(x)$",
                "$y^{(n)} + a_1(x)y^{(n-1)} + \\dots + a_{n-1}(x)y' + a_n(x)y = f(x)$",
                "$y^{(n)} + c_1 y^{(n-1)} + \\dots + c_{n-1}y' + c_n y = f(x)$",
                "$y^{(n)} + a_1 x y^{n-1} + \\dots + a_{n-1} x y' = f(x)$"
            ],
            "a": "$y^{(n)} + c_1 y^{(n-1)} + \\dots + c_{n-1}y' + c_n y = f(x)$"
        },
        {
            "q": "Hosilaga nisbatan yechilmagan birinchi tartibli differensial tenglamaning umumiy ko‘rinishini toping?",
            "o": [
                "$F(x, y, y') = 0$",
                "$F(x, y') = 0$",
                "$F(y, y') = f(x)$",
                "$F(y, y', y'') = f(x)$"
            ],
            "a": "$F(x, y, y') = 0$"
        },
        {
            "q": "Ushbu $y'' + f_1(x)y' + f_2(x)y = 0$ tenglama uchun Ostragradskiy-Liuvill formulasini toping?",
            "o": [
                "$W(x) = W(x_0) e^{- \\int_{x_0}^x f_1(t) dt}$",
                "$W(x) = -W(x_0) e^{\\int_{x_0}^x f_1(t) dt}$",
                "$W(x) = W(x_0) e^{1 - \\int_{x_0}^x f_1(t) dt}$",
                "$W(x) = -2W(x_0) e^{\\int_{x_0}^x f_1(t) dt}$"
            ],
            "a": "$W(x) = W(x_0) e^{- \\int_{x_0}^x f_1(t) dt}$"
        },
        {
            "q": "Ushbu $y'' + p_1(x)y' + p_2(x)y = 0$ tenglama uchun Ostragradskiy-Liuvill formulasini toping?",
            "o": [
                "$W(x) = W(x_0) e^{- \\int_{x_0}^x p_1(t) dt}$",
                "$W(x) = W(x_0) e^{\\int_{x_0}^x p_1(t) dt}$",
                "$W(x) = W(x_0) e^{1 - \\int_{x_0}^x p_1(t) dt}$",
                "$W(x) = -2W(x_0) e^{\\int_{x_0}^x p_1(t) dt}$"
            ],
            "a": "$W(x) = W(x_0) e^{- \\int_{x_0}^x p_1(t) dt}$"
        },
        {
            "q": "Lagranj differensial tenglamasini ko‘rsating?",
            "o": [
                "$y' = \\varphi(y')x + \\psi(y')$",
                "$y = \\varphi(y')x + \\psi(y)$",
                "$y = \\varphi(y')x + \\psi(y')$",
                "$y = \\varphi(y)x^2 + \\psi(y')$"
            ],
            "a": "$y = \\varphi(y')x + \\psi(y')$"
        },
        {
            "q": "Klero differensial tenglamasini ko‘rsating?",
            "o": [
                "$y' = \\varphi(y')x + \\psi(y')$",
                "$y' = yx + \\psi(y)$",
                "$y = y'x + \\psi(y')$",
                "$y = \\varphi(y)x^2 + \\psi(y')$"
            ],
            "a": "$y = y'x + \\psi(y')$"
        },
        {
            "q": "Agar $L: (y = \\varphi(x))$ chiziqning har bir nuqtasidagi urinma $\\Phi(x, y, C) = 0$ ga tegishli kamida bitta chiziqning urinmasi bilan bir xil bo‘lsa, unga $\\Phi(x, y, C) = 0$ chiziqlar oilasining ...",
            "o": [
                "o‘ramasi deyiladi",
                "umumiy yechimi deyiladi",
                "maxsus yechimi deyiladi",
                "regulyar yechimi deyiladi"
            ],
            "a": "o‘ramasi deyiladi"
        },
        {
            "q": "Ushbu $M(x,y)dx + N(x,y)dy = 0$ differensial tenglama uchun $\\mu(x,y)$ integrallovchi ko‘paytuvchi deyiladi, agarda:",
            "o": [
                "$\\mu(x,y)M(x,y)dx + \\mu(x,y)N(x,y)dy = 0$ o‘zgaruvchilarga ajraladigan tenglama bo‘lsa",
                "$\\mu(x,y)M(x,y)dx + \\mu(x,y)N(x,y)dy = 0$ bir jinsli tenglama bo‘lsa",
                "$\\mu(x,y)M(x,y)dx + \\mu(x,y)N(x,y)dy = 0$ Bernulli tenglamasi bo‘lsa",
                "$\\mu(x,y)M(x,y)dx + \\mu(x,y)N(x,y)dy = 0$ to‘la differensialli tenglama bo‘lsa"
            ],
            "a": "$\\mu(x,y)M(x,y)dx + \\mu(x,y)N(x,y)dy = 0$ to‘la differensialli tenglama bo‘lsa"
        },
        {
            "q": "Ushbu $y^{(n)} = f(x, y^{(k)}, \\dots, y^{(n-1)})$ differensial tenglamaning tartibi qanday almashtirish yordamida $k$ birlikka pasayadi?",
            "o": [
                "$y^{(k)} = z$",
                "$y^{(k+1)} = z$",
                "$y^{(k-1)} = z$",
                "$y^{(k+2)} = z$"
            ],
            "a": "$y^{(k)} = z$"
        },
        {
            "q": "Agar $y_1(x)$ va $y_2(x)$ lar $y'' + a(x)y' + b(x)y = 0$ differensial tenglamaning xususiy yechimlari bo‘lsa, u holda bu tenglamaning umumiy yechimi qanday ko‘rinishda bo‘ladi?",
            "o": [
                "$y = y_1 + y_2$",
                "$y = y_1 y_2$",
                "$y = C_1 y_1 + y_2$",
                "$y = C_1 y_1 + C_2 y_2$"
            ],
            "a": "$y = C_1 y_1 + C_2 y_2$"
        },
        {
            "q": "$L$ chiziqli operator bo‘lsa, u holda qaysi tenglik har doim o‘rinli bo‘ladi?",
            "o": [
                "$L[c_1 y_1 + c_2 y_2] = L[y_1] + L[y_2]$",
                "$L[y_1 + y_2] = L[y_1] L[y_2]$",
                "$L[y_1 + y_2] = L[y_1] + c L[y_2]$",
                "$L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$"
            ],
            "a": "$L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2]$"
        },
        {
            "q": "Quyidagi tenglamalarning qaysi biri n-tartibli chiziqli bir jinsli tenglama?",
            "o": [
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = f(x)$",
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$",
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y^2 = 0$",
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y^3 = 0$"
            ],
            "a": "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$"
        },
        {
            "q": "Quyidagi tenglamalarning qaysi biri n-tartibli chiziqli bir jinsli bo'lmas (bo'lmagan) tenglama?",
            "o": [
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = f(x)$",
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$",
                "$p_1(x)y^{(n-1)} + \\dots + p_n(x)y^2 = f(x)$",
                "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y^4 = f(x)$"
            ],
            "a": "$y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = f(x)$"
        },
        {
            "q": "Qaysi shart bajarilganda ushbu $y' = a(x)y^2 + b(x)y + c(x)$ Rikkati tenglamasi Bernulli tenglamasiga aylanadi?",
            "o": [
                "$c(x) = 0$",
                "$c(x) = 0, a(x) = 0$",
                "$c(x) = 0, b(x) = 0$",
                "$a(x) = 0, b(x) = 0$"
            ],
            "a": "$c(x) = 0$"
        },
        {
            "q": "Birinchi tartibli chiziqli differensial tenglamaning umumiy yechimi nechta ixtiyoriy o‘zgarmaslarga bog‘liq?",
            "o": ["ikkita", "bitta", "uchta", "to‘rtta"],
            "a": "bitta"
        },
        {
            "q": "Birinchi tartibli $y' = \varphi \\left( \\frac{y}{x} \\right)$ bir jinsli tenglama $y = xz$ almashtirish natijasida qanday turdagi tenglamaga keladi?",
            "o": [
                "To‘liq differensial tenglamaga",
                "Bernulli tenglamasiga",
                "Chiziqli tenglamaga",
                "O‘zgaruvchilari ajraladigan tenglamaga"
            ],
            "a": "O‘zgaruvchilari ajraladigan tenglamaga"
        },
        {
            "q": "$n$-tartibli differensial tenglamaning umumiy yechimi nechta ixtiyoriy o‘zgarmasga bog‘liq?",
            "o": ["$n$ ta", "$n+1$ ta", "$n+2$ ta", "4 ta"],
            "a": "$n$ ta"
        },
        {
            "q": "Ushbu $x^2 y'' + a_1 x y' + a_2 y = 0$ differensial tenglama turini toping?",
            "o": [
                "Rikkati tenglamasi",
                "O‘zgarmas koeffitsiyentli chiziqli tenglama",
                "Bernulli tenglamasi",
                "Eylerning ikkinchi tartibli bir jinsli tenglamasi"
            ],
            "a": "Eylerning ikkinchi tartibli bir jinsli tenglamasi"
        },
        {
            "q": "Ikkinchi tartibli chiziqli bir jinsli differensial tenglamaning chiziqli erkli yechimlarining maksimal sonini toping?",
            "o": ["uchta", "ikkita", "to‘rtta", "bitta"],
            "a": "ikkita"
        },
        {
            "q": "$x^k y'' + axy' + by = 0$ tenglama $k$ ning qanday qiymatida Eyler tenglamasi bo‘ladi?",
            "o": ["$k = 2$", "$k = 1$", "$k = 3$", "$k = 4$"],
            "a": "$k = 2$"
        },
        {
            "q": "Quyidagi tenglamalarning qaysi biri chiziqli bir jinsli tenglama?",
            "o": [
                "$y' + a(x)y^2 = b(x)$",
                "$y' + a(x)y^3 = b(x)$",
                "$y' + a(x)y = b(x)y^n, n \\neq 0, n \\neq 1$",
                "$y' + a(x)y = 0$"
            ],
            "a": "$y' + a(x)y = 0$"
        },
        {
            "q": "Hosilaga nisbatan yechilgan birinchi tartibli differensial tenglamaning umumiy ko‘rinishini toping?",
            "o": [
                "$y' = f(x)g(y)$",
                "$y' = f(x,y)$",
                "$y' = f(x, y, y')$",
                "$y = f(x, y')$"
            ],
            "a": "$y' = f(x,y)$"
        },
        {
            "q": "Ushbu $y^{(n)} = f(y^{(n-1)})$ tenglamaning tartibini qaysi almashtirish yordamida pasaytirish mumkin?",
            "o": ["$z = y^{(n-1)}$", "$z = y^{(n)}$", "$z = y'$", "$z = y^2$"],
            "a": "$z = y^{(n-1)}$"
        },
        {
            "q": "$y^{(V)}(x) = -4y''$ tenglama tartibini 3 birlikka pasaytiruvchi almashtirishni ko‘rsating?",
            "o": ["$z = y'$", "$z = y'''$", "$z = y''$", "$z = y^{(V)}$"],
            "a": "$z = y''$"
        },
        {
            "q": "Ushbu $y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$ bir jinsli differensial tenglamaning $y_1(x), y_2(x), \\dots, y_n(x)$ yechimlari chiziqli bog‘langan bo‘ladi, agarda ulardan tuzilgan Vronskiy determinanti uchun quyidagi shart bajarilsa:",
            "o": [
                "$W(y_1(x), y_2(x), \\dots, y_n(x)) = 0$",
                "$W(y_1(x), y_2(x), \\dots, y_n(x)) \\neq 0$",
                "$W(y_1(x), y_2(x), \\dots, y_n(x)) > 0$",
                "$W(y_1(x), y_2(x), \\dots, y_n(x)) < 0$"
            ],
            "a": "$W(y_1(x), y_2(x), \\dots, y_n(x)) = 0$"
        },
        {
            "q": "Ushbu $y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$ bir jinsli differensial tenglamaning $y_1(x), y_2(x), \\dots, y_n(x)$ yechimlari chiziqli bog‘lanmagan bo‘ladi, agarda ulardan tuzilgan Vronskiy determinanti uchun quyidagi shart bajarilsa:",
            "o": [
                "$W(y_1(x), y_2(x), \\dots, y_n(x)) = 0$",
                "$W(y_1(x), y_2(x), \\dots, y_n(x)) \\neq 0$",
                "$W(y_1(0), y_2(0), \\dots, y_n(0)) = 0$",
                "$W(y_1(x_0), y_2(x_0), \\dots, y_n(x_0)) = 0$"
            ],
            "a": "$W(y_1(x), y_2(x), \\dots, y_n(x)) \\neq 0$"
        },
        {
            "q": "Ushbu $y_1(x), y_2(x), \\dots, y_n(x)$ funksiyalar $y^{(n)} + p_1(x)y^{(n-1)} + \\dots + p_n(x)y = 0$ bir jinsli differensial tenglamaning fundamental yechimlar sistemasini tashkil qilsa, tenglamaning umumiy yechimi qaysi javobda to‘g‘ri ko‘rsatilgan?",
            "o": [
                "$y(x) = \\sum_{i=1}^n c_i y_i(x), c_i = const$",
                "$y(x) = \\sum_{i=1}^n y_i(x)$",
                "$y(x) = \\sum_{i=1}^n c_i y_i(x^2), c_i = const$",
                "$y(x) = \\sum_{i=1}^n (1 + y_i(x))$"
            ],
            "a": "$y(x) = \\sum_{i=1}^n c_i y_i(x), c_i = const$"
        },
        {
            "q": "$y_1, y_2$ va $y_3$ o‘zgarmas koeffitsiyentli 3-tartibli oddiy differensial tenglamaning chiziqli erkli xususiy yechimlari bo‘lsa, tenglamaning umumiy yechimini ko‘rsating?",
            "o": [
                "$y = c_1 y_1 + c_2 y_2 + c_3 y_3, c_1, c_2, c_3 \\text{- o‘zgarmas son}$",
                "$y = y_1 + c_1(y_2 + y_3), c_1 \\text{- o‘zgarmas son}$",
                "$y = c(y_1 + y_2), c_1 \\text{- o‘zgarmas son}$",
                "$y = e^{(y_1 + y_2)}$"
            ],
            "a": "$y = c_1 y_1 + c_2 y_2 + c_3 y_3, c_1, c_2, c_3 \\text{- o‘zgarmas son}$"
        },
        {
            "q": "Umumiy yechimdan olingan va undagi ixtiyoriy o‘zgarmas $c$ ga aniq $c = c_0$ qiymat berishdan hosil bo‘lgan $\\varphi(x, c_0)$ yechimga tenglamaning...",
            "o": [
                "Xususiy yechimi deyiladi",
                "Umumiy yechimi deyiladi",
                "Karrali yechimi deyiladi",
                "Umumiy integrali deyiladi"
            ],
            "a": "Xususiy yechimi deyiladi"
        },
        {
            "q": "Ushbu $\\begin{cases} \\frac{dx}{dt} = ax^k + by^l \\\\ \\frac{dy}{dt} = cx^m + dy^n \\end{cases}$ differensial tenglamalar sistemasining tartibini toping?",
            "o": ["1", "2", "$k$", "$n$"],
            "a": "1"
        },
        {
            "q": "Ushbu $\\begin{cases} \\frac{dx}{dt} = f(t,x,y) \\\\ \\frac{dy}{dt} = g(t,x,y) \\end{cases}$ normal sistemaning umumiy yechimi nechta ixtiyoriy o‘zgarmaslarga bog‘liq?",
            "o": ["2", "3", "4", "$n$"],
            "a": "2"
        },
        {
            "q": "$x' + g(t)x = f(t)x^k, k \\neq 0, k \\neq 1$ tenglamaning turini aniqlang?",
            "o": [
                "Bernulli tenglamasi",
                "Chiziqli tenglamasi",
                "O‘zgaruvchilari ajraladigan tenglama",
                "Klero tenglamasi"
            ],
            "a": "Bernulli tenglamasi"
        },
        {
            "q": "$x' + g(t)x = f(t)x^k$ tenglama qachon chiziqli tenglama bo‘ladi?",
            "o": ["$k = 0$", "$k = 1$", "$k = 2$", "$k = 3$"],
            "a": "$k = 0$"
        },
        {
            "q": "$n$-tartibli differensial tenglamaning oshkormas ko‘rinishdagi umumiy yechimi qaysi javobda berilgan?",
            "o": [
                "$\\Phi(x, y, C_1, \\dots, C_n) = 0$",
                "$y = \\varphi(x)$",
                "$\\Phi(x, y) = 0$",
                "$y = y(x)$"
            ],
            "a": "$\\Phi(x, y, C_1, \\dots, C_n) = 0$"
        },
        {
            "q": "Ikkinchi tartibli chiziqli o‘zgarmas koeffitsiyentli bir jinsli sistemaning xarakteristik sonlari haqiqiy va bir xil ishorali sonlar bo‘lsa, unda (0,0) maxsus nuqta turi qaysi javobda berilgan?",
            "o": ["Tugun tipidagi nuqta", "Egarsimon tipidagi nuqta", "Fokus", "Markaz"],
            "a": "Tugun tipidagi nuqta"
        },
        {
            "q": "Ikkinchi tartibli chiziqli o‘zgarmas koeffitsiyentli bir jinsli sistemaning xarakteristik sonlari haqiqiy har xil ishorali sonlar bo‘lsa, unda (0,0) maxsus nuqta turi qaysi javobda berilgan?",
            "o": ["Egarsimon tipidagi nuqta", "Tugun tipidagi nuqta", "Fokus", "Markaz"],
            "a": "Egarsimon tipidagi nuqta"
        },
        {
            "q": "Ikkinchi tartibli chiziqli o‘zgarmas koeffitsiyentli bir jinsli sistemaning xarakteristik sonlari kompleks son bo‘lib, uning haqiqiy qismi nolga teng bo‘lib ya’ni sof mavhum son bo‘lsa (0,0) maxsus nuqta turi qaysi javobda berilgan?",
            "o": ["Markaz tipidagi nuqta", "Tugun tipidagi nuqta", "Fokus", "Egarsimon tipidagi nuqta"],
            "a": "Markaz tipidagi nuqta"
        },
        {
            "q": "Quyidagi tenglamalarning qaysi biri ikkinchi tartibli differensial tenglama?",
            "o": [
                "$\\frac{d^2y}{dx^2} + \\sin(x+y) = 0$",
                "$\\frac{dy}{dx} + \\sin(x+y^2) = 0$",
                "$\\frac{d^2y}{dx^2} + \\cos(x+y'') = 0$",
                "$\\frac{d^3y}{dx^3} - \\sin x^2 = 0$"
            ],
            "a": "$\\frac{d^2y}{dx^2} + \\sin(x+y) = 0$"
        },
        {
            "q": "$y' = f(x+y-3)$ ko‘rinishdagi tenglamani yechish uchun qanday almashtirish bajarish kerak?",
            "o": [
                "$z = x + y - 3$",
                "$z = 2x + f(y) - 3$",
                "$z = xy - 3$",
                "$z = f(xy) - 3$"
            ],
            "a": "$z = x + y - 3$"
        }
    ]

if 'dt_71_140' not in st.session_state:
    st.session_state.dt_71_140 = [
        {
            "q": "Differensial tenglamaning integral chizig'i deb nimaga aytiladi?",
            "o": [
                "Differensial tenglama yechimining grafigiga",
                "Yechimdan olingan ikkinchi tartibli hosilaning grafigiga",
                "Yechimning hosilasining grafigiga",
                "Yechimdan olingan integralning grafigiga"
            ],
            "a": "Differensial tenglama yechimining grafigiga"
        },
        {
            "q": "Ushbu $y^{(n)} = f(x, y', \dots, y^{(n-1)})$ tenglama uchun qo'yilgan boshlang'ich shart qaysi javobda berilgan?",
            "o": [
                "$y(x_0) = y_0, y'(x_0) = y'_0, \dots, y^{(n-1)}(x_0) = y_0^{(n-1)}$",
                "$y(x_0) = y_0, y'(x_0) = y'_0, \dots, y^{(n-2)}(x_0) = y_0^{(n-2)}$",
                "$y(x_0) = y_0, y'(x_0) = y'_0, \dots, y^{(n-3)}(x_0) = y_0^{(n-3)}$",
                "$y(x_0) = y_0, y'(x_0) = y'_0, \dots, y^{(n-4)}(x_0) = y_0^{(n-4)}$"
            ],
            "a": "$y(x_0) = y_0, y'(x_0) = y'_0, \dots, y^{(n-1)}(x_0) = y_0^{(n-1)}$"
        },
        {
            "q": "Ushbu $y'' = xy'$ tenglamaning tartibini qaysi almashtirish yordamida pasaytirish mumkin?",
            "o": ["$z = y'$", "$z = y$", "$z = -y$", "$z = y^2$"],
            "a": "$z = y'$"
        },
        {
            "q": "Agar $f(x,y)$ funksiya $\\forall \\lambda > 0$ uchun $f(\\lambda x, \\lambda y) = \\lambda^k f(x,y)$ shartni qanoatlantirsa, $y' = f(x,y)$ tenglamaga...",
            "o": [
                "$k$-darajali bir jinsli differensial tenglama deyiladi",
                "$k$-darajali Bernulli tenglamasi deyiladi",
                "$k$-darajali bir jinslimas differensial tenglama deyiladi",
                "$k$-darajali Rikkati tenglamasi deyiladi"
            ],
            "a": "$k$-darajali bir jinsli differensial tenglama deyiladi"
        },
        {
            "q": "Rikkati tenglamasining bitta $y_1(x)$ yechimi ma'lum bo'lsa, uning umumiy yechimini topish uchun qanday almashtirish bajarish lozim?",
            "o": [
                "$y = y_1(x) + u(x)$",
                "$y = y_1(x)u(x)$",
                "$y = y_1^2(x) + u(x)$",
                "$y = y_1^2(x)u(x)$"
            ],
            "a": "$y = y_1(x) + u(x)$"
        },
        {
            "q": "Rikkati tenglamasi kvadraturada ... integrallanuvchi degan jumla qaysi javobda noto'g'ri berilgan?",
            "o": ["har doim", "bitta xususiy yechim berilganda", "ikkita xususiy yechim berilganda", "uchta xususiy yechim berilganda"],
            "a": "har doim"
        },
        {
            "q": "$D$ sohada o'zgarmasdan farqli garmonik bo'lgan $u(x)$ funksiya o'zining ekstremum qiymatiga ... erishadi.",
            "o": ["sohaning chegarasida", "sohaning ichida", "sohaning tashqarisida", "sohaning markazida"],
            "a": "sohaning chegarasida"
        },
        {
            "q": "Agar oddiy differensial tenglamalar sistemasiga erkli o'zgaruvchi oshkor ravishda kirmasa, bunday sistemaga...",
            "o": ["muxtor sistema deyiladi", "normal sistema deyiladi", "maxsus sistema deyiladi", "oddiy sistema deyiladi"],
            "a": "muxtor sistema deyiladi"
        },
        {
            "q": "Ushbu $L(p) = p^n + a_1 p^{n-1} + \\dots + a_{n-1}p + a_n$ ko'phad turg'un bo'ladi, agarda...",
            "o": [
                "$a_1, a_2, \\dots, a_n$ koeffitsiyentlari musbat bo'lsa",
                "$a_1, a_2, \\dots, a_n$ koeffitsiyentlari manfiy bo'lsa",
                "$a_1, a_2, \\dots, a_n$ koeffitsiyentlari teng bo'lsa",
                "$a_1, a_2, \\dots, a_n$ koeffitsiyentlari nol bo'lsa"
            ],
            "a": "$a_1, a_2, \\dots, a_n$ koeffitsiyentlari musbat bo'lsa"
        },
        {
            "q": "Agar tekislikda bir parametrli silliq $l$ chiziqlar oilasi $\\Phi(x, y, a) = 0$ ($a$ - parametr) berilgan bo'lsa, u holda bu oila chiziqlarini o'zgarmas $\\alpha$ burchak ostida kesib o'tuvchi $l_1$ chiziq berilgan oilaning...",
            "o": ["izogonal trayektoriyasi deyiladi", "oddiy trayektoriyasi deyiladi", "maxsus trayektoriyasi deyiladi", "umumiy trayektoriyasi deyiladi"],
            "a": "izogonal trayektoriyasi deyiladi"
        },
        {
            "q": "Agar bir vaqtda nolga teng bo‘lmagan shunday $\\alpha_1, \\alpha_2, \\dots, \\alpha_k$ o‘zgarmas sonlar mavjud bo‘lsaki, biror $I$ intervalda ushbu $\\alpha_1 \\varphi_1(x) + \\alpha_2 \\varphi_2(x) + \\dots + \\alpha_k \\varphi_k(x) = 0, \\forall x \\in I$ tenglik o‘rinli bo‘lsa, $\\varphi_1(x), \\varphi_2(x), \\dots, \\varphi_k(x)$ funksiyalar $I$ intervalda...",
            "o": ["chiziqli bog‘liq deyiladi", "chiziqli erkli deyiladi", "chiziqli bog‘lanmagan deyiladi", "uzluksiz deyiladi"],
            "a": "chiziqli bog‘liq deyiladi"
        },
        {
            "q": "Garmonik ossillyator tenglamasini ko‘rsating?",
            "o": [
                "$\\ddot{x} + \\omega^2 x = 0, x = x(t), \\omega \\text{-tebranish chastotasi}$",
                "$\\dot{x} + \\omega x = 0, x = x(t), \\omega \\text{-tebranish chastotasi}$",
                "$\\ddot{x} + \\omega y = 0, x = x(t), \\omega \\text{-tebranish chastotasi}$",
                "$\\ddot{x} - \\omega = 0, x = x(t), \\omega \\text{-tebranish chastotasi}$"
            ],
            "a": "$\\ddot{x} + \\omega^2 x = 0, x = x(t), \\omega \\text{-tebranish chastotasi}$"
        },
        {
            "q": "Ushbu $-y''(x) + q(x)y = \\lambda y(x), x \\in [0, \\pi], y(0) = 0, y(\\pi) = 0$ chegaraviy masalaning xos qiymati deb...",
            "o": [
                "noldan farqli yechimiga mos keluvchi $\\lambda$ parametrga aytiladi",
                "nol yechimiga mos keluvchi $\\lambda$ parametrga aytiladi",
                "ixtiyoriy yechimiga mos keluvchi $\\lambda$ parametrga aytiladi",
                "har qanday $\\lambda$ parametrga aytiladi"
            ],
            "a": "noldan farqli yechimiga mos keluvchi $\\lambda$ parametrga aytiladi"
        },
        {
            "q": "Ushbu $\\begin{cases} y_1' = f_1(x, y_1, y_2, \\dots, y_n) \\\\ y_2' = f_2(x, y_1, y_2, \\dots, y_n) \\\\ \\dots \\\\ y_n' = f_n(x, y_1, y_2, \\dots, y_n) \\end{cases}$ tenglamalar sistemasi...",
            "o": [
                "oddiy differensial tenglamalar sistemasining normal sistemasi deyiladi",
                "$n$-tartibli oddiy differensial tenglamalar sistemasi deyiladi",
                "1-tartibli chiziqli differensial tenglamalar sistemasi deyiladi",
                "1-tartibli o‘zgarmas koeffitsiyentli chiziqli differensial tenglamalar sistemasi deyiladi"
            ],
            "a": "oddiy differensial tenglamalar sistemasining normal sistemasi deyiladi"
        },
        {
            "q": "Ushbu $\\frac{dy_i}{dx} = \\sum_{j=1}^n a_{ij}y_j + b_i(x), i = 1, 2, \\dots, n$ tenglamalar sistemasi...",
            "o": [
                "chiziqli differensial tenglamalar sistemasining normal sistemasi deyiladi",
                "$n$-tartibli nochiziqli differensial tenglamalar sistemasi deyiladi",
                "1-tartibli nochiziqli differensial tenglamalar sistemasi deyiladi",
                "1-tartibli o‘zgarmas koeffitsiyentli nochiziqli differensial tenglamalar sistemasi deyiladi"
            ],
            "a": "chiziqli differensial tenglamalar sistemasining normal sistemasi deyiladi"
        },
        {
            "q": "Ushbu $M(x,y)dx + N(x,y)dy = 0$ differensial tenglama uchun integrallovchi ko‘paytuvchi $\\mu(x,y) = \\mu(x)$ bo‘lsa, u holda...",
            "o": [
                "$\\mu(x) = C e^{\\int \\frac{\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}}{N} dx}$",
                "$\\mu(x) = C e^{-\\int \\frac{\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}}{N} dx}$",
                "$\\mu(x) = C e^{\\int \\frac{\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}}{M} dx}$",
                "$\\mu(x) = C e^{\\int \\frac{\\frac{\\partial M}{\\partial x} + \\frac{\\partial N}{\\partial y}}{N} dx}$"
            ],
            "a": "$\\mu(x) = C e^{\\int \\frac{\\frac{\\partial M}{\\partial y} - \\frac{\\partial N}{\\partial x}}{N} dx}$"
        },
        {
            "q": "Ushbu $M(x,y)dx + N(x,y)dy = 0$ differensial tenglama uchun integrallovchi ko‘paytuvchi $\\mu(x,y) = \\mu(y)$ bo‘lsa, u holda...",
            "o": [
                "$\\mu(y) = C e^{\\int \\frac{\\frac{\\partial N}{\\partial x} - \\frac{\\partial M}{\\partial y}}{M} dy}$",
                "$\\mu(y) = C e^{-\\int \\frac{\\frac{\\partial N}{\\partial x} - \\frac{\\partial M}{\\partial y}}{M} dy}$",
                "$\\mu(y) = C e^{\\int \\frac{\\frac{\\partial N}{\\partial x} - \\frac{\\partial M}{\\partial y}}{N} dy}$",
                "$\\mu(y) = C e^{\\int \\frac{\\frac{\\partial N}{\\partial x} - \\frac{\\partial M}{\\partial y}}{M} dx}$"
            ],
            "a": "$\\mu(y) = C e^{\\int \\frac{\\frac{\\partial N}{\\partial x} - \\frac{\\partial M}{\\partial y}}{M} dy}$"
        },
        {
            "q": "Ushbu $y' = f(ax + by + c)$ differensial tenglamada $z = ax + by + c$ almashtirish bajarilsa, u qanday ko‘rinishga keladi?",
            "o": [
                "$z' = a + bf(z)$",
                "$yz' = a + bf(z)$",
                "$xz' = a + bf(z)$",
                "$yz' = ax + bf(z)$"
            ],
            "a": "$z' = a + bf(z)$"
        },
        {
            "q": "Agar $f(x,y)$ funksiya uchun $f(\\lambda^\\alpha x, \\lambda^\\beta y) = \\lambda^{\\beta - \\alpha} f(x,y), \\forall \\lambda > 0$ shart bajarilsa, $y' = f(x,y)$ tenglamaga...",
            "o": [
                "kvazi bir jinsli differensial tenglama deyiladi",
                "bir jinslimas differensial tenglama deyiladi",
                "Bernulli differensial tenglamasi deyiladi",
                "o‘zgaruvchilari ajraladigan differensial tenglama deyiladi"
            ],
            "a": "kvazi bir jinsli differensial tenglama deyiladi"
        },
        {
            "q": "Ushbu $y' = Ay^2 + Bx^{\\alpha}, A \\neq 0, B \\neq 0$ Rikkati tenglamasi kvadraturada integrallanuvchi bo'ladi, agarda...",
            "o": [
                "$\\frac{\\alpha}{2\\alpha + 4}$ soni butun bo'lsa",
                "$\\frac{1}{\\alpha + 4}$ soni butun bo'lsa",
                "$\\frac{1}{2\\alpha - 4}$ soni butun bo'lsa",
                "$\\frac{\\alpha}{2\\alpha + 4}$ soni musbat bo'lsa"
            ],
            "a": "$\\frac{\\alpha}{2\\alpha + 4}$ soni butun bo'lsa"
        },
        {
            "q": "Chiziqli bir jinsli $\\frac{dy}{dx} = p(x)y + q(x)$ differensial tenglamaning integrallovchi ko'paytuvchisini ko'rinishini aniqlang?",
            "o": [
                "$\\mu(x) = \\exp\\left\\{ - \\int p(x)dx \\right\\}$",
                "$\\mu(x) = \\exp\\left\\{ \\int p(x)dx \\right\\}$",
                "$\\mu(x) = \\exp\\left\\{ x + \\int p(x)dx \\right\\}$",
                "$\\mu(x) = \\exp\\left\\{ 2x + \\int p(x)dx \\right\\}$"
            ],
            "a": "$\\mu(x) = \\exp\\left\\{ - \\int p(x)dx \\right\\}$"
        },
        {
            "q": "Agar $f(x,y)$ funksiya $P$ sohaning har bir nuqtasida $f'_y(x,y)$ xususiy hosilaga ega bo'lib, $|f'_y(x,y)| \\leq C, C=const$ bo'lsa, u holda bu funksiya $P$ to'g'ri to'rtburchakda...",
            "o": [
                "$y$ - o'zgaruvchi bo'yicha Lipshits shartini qanoatlantiradi",
                "$y$ - o'zgaruvchi bo'yicha Lipshits shartini qanoatlantirmaydi",
                "$x$ - o'zgaruvchi bo'yicha Koshi shartini qanoatlantiradi",
                "$x$ - o'zgaruvchi bo'yicha uzilishga ega bo'ladi"
            ],
            "a": "$y$ - o'zgaruvchi bo'yicha Lipshits shartini qanoatlantiradi"
        },
        {
            "q": "$u(x), v(x)$ funksiyalar $[x_0, x]$ oraliqda uzluksiz va manfiymas va $u(x) \\leq A + \\int_{x_0}^x u(t)v(t) dt, A \\geq 0$ o‘rinli bo‘lsa, u holda $u(x)$ uchun qaysi tengsizlik bajariladi?",
            "o": [
                "$u(x) \\leq A \\exp \\left| \\int_{x_0}^x v(t) dt \\right|$",
                "$u(x) \\geq A \\exp \\left| \\int_{x_0}^x v(t) dt \\right|$",
                "$u(x) \\geq A \\left| \\int_{x_0}^x v(t) dt \\right|$",
                "$u(x) \\leq A - \\exp \\left| \\int_{x_0}^x v(t) dt \\right|$"
            ],
            "a": "$u(x) \\leq A \\exp \\left| \\int_{x_0}^x v(t) dt \\right|$"
        },
        {
            "q": "Ushbu $y' = f(x,y), y(x_0) = y_0$ Koshi masalasining yechimi mavjud, yagona va turg‘un bo‘lsa, Koshi masalasi...",
            "o": ["korrekt deyiladi", "nokorrekt deyiladi", "singulyar deyiladi", "bir jinsli deyiladi"],
            "a": "korrekt deyiladi"
        },
        {
            "q": "Quyidagi jumlalardan qaysi biri to‘g‘ri?",
            "o": [
                "Chiziqli bog‘liq funksiyalardan tuzilgan Vronskiy determinanti har doim nolga teng.",
                "Chiziqli erkli funksiyalardan tuzilgan Vronskiy determinanti har doim nolga teng.",
                "Chiziqli bog‘liq funksiyalardan tuzilgan Vronskiy determinanti har doim noldan farqli.",
                "Chiziqli differensial tenglamaning fundamental yechimlar sistemasidan tuzilgan Vronskiy determinanti har doim noldan katta."
            ],
            "a": "Chiziqli bog‘liq funksiyalardan tuzilgan Vronskiy determinanti har doim nolga teng."
        },
        {
            "q": "Quyidagi jumlalardan qaysi biri to‘g‘ri?",
            "o": [
                "Chiziqli differensial tenglamaning fundamental yechimlar sistemasidan tuzilgan Vronskiy determinanti har doim noldan farqli.",
                "Chiziqli differensial tenglamaning fundamental yechimlar sistemasidan tuzilgan Vronskiy determinanti har doim nolga teng.",
                "Chiziqli bog‘liq funksiyalardan tuzilgan Vronskiy determinanti har doim noldan farqli.",
                "Chiziqli differensial tenglamaning fundamental yechimlar sistemasidan tuzilgan Vronskiy determinanti har doim noldan katta."
            ],
            "a": "Chiziqli differensial tenglamaning fundamental yechimlar sistemasidan tuzilgan Vronskiy determinanti har doim noldan farqli."
        },
        {
            "q": "$y^{(V)} = f(x, y'', y''', y^{(IV)})$ tenglamaning tartibini qaysi almashtirish yordamida 2 birlikka pasaytirish mumkin?",
            "o": ["$y'' = z$", "$y' = z$", "$y''' = z$", "$y^{(IV)} = z$"],
            "a": "$y'' = z$"
        },
        {
            "q": "Ushbu $y' + p(x)y = q(x)$ tenglamaning umumiy yechimi qaysi ko‘rinishda bo‘ladi?",
            "o": [
                "$y = e^{- \\int p(x)dx} \\left( C + \\int q(x) e^{\\int p(x)dx} dx \\right)$",
                "$y = e^{\\int p(x)dx} \\left( C + \\int q(x) e^{\\int p(x)dx} dx \\right)$",
                "$y = e^{\\int p(x)dx} \\left( C + \\int p(x) e^{\\int q(x)dx} dx \\right)$",
                "$y = e^{- \\int q(x)dx} \\left( C + \\int p(x) e^{\\int q(x)dx} dx \\right)$"
            ],
            "a": "$y = e^{- \\int p(x)dx} \\left( C + \\int q(x) e^{\\int p(x)dx} dx \\right)$"
        },
        {
            "q": "O‘zgarmas koeffitsiyentli ikkinchi tartibli chiziqli bir jinsli differensial tenglamaning xususiy yechimi $e^{2x} \\cos 3x$ bo‘lsa, u holda bu tenglamaning xos sonlari qanday bo‘ladi?",
            "o": ["$2 \\pm 3i$", "2, 3", "$1 \\pm 2i$", "$3 \\pm 2i$"],
            "a": "$2 \\pm 3i$"
        },
        {
            "q": "Quyidagi $ay'' + 3xy' + 5y = 0$ tenglama Eyler tenglamasi bo‘lishi uchun $a$ nimaga teng bo‘lishi kerak?",
            "o": ["$x^2$", "$x$", "1", "0"],
            "a": "$x^2$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $(1+y^2)dx + (1+x^2)dy = 0$",
            "o": [
                "$\\text{arctg } x + \\text{arctg } y = C$",
                "$y = \\text{tg } \\ln Cx$",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$1 + e^y = C(1 + x^2)$"
            ],
            "a": "$\\text{arctg } x + \\text{arctg } y = C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $(1+y^2)dx + xydy = 0$",
            "o": [
                "$x^2(1+y^2) = C$",
                "$1 + e^y = C(1 + x^2)$",
                "$\\sqrt{1-x^2} + \\sqrt{1-y^2} = C$",
                "$y^2(1-y) = (x+C)^2, y=1$"
            ],
            "a": "$x^2(1+y^2) = C$"
        },
        {
            "q": "Differensial tenglamaning xususiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' \\sin x - y \\cos x = 0, y(\\pi/2) = 1$",
            "o": ["$y = \\sin x$", "$y = 1$", "$y = \\cos x$", "$y = \\text{tg } x$"],
            "a": "$y = \\sin x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(1+y^2)dx = x dy$",
            "o": [
                "$y = \\text{tg } \\ln Cx$",
                "$x^2 = (x^2 - y) \\ln Cx, y = x^2$",
                "$x = \\ln Cx$",
                "$1 + e^y = C(1 + x^2)$"
            ],
            "a": "$y = \\text{tg } \\ln Cx$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x \\sqrt{1+y^2} dx + y \\sqrt{1+x^2} dy = 0$",
            "o": [
                "$\\sqrt{1+x^2} + \\sqrt{1+y^2} = C$",
                "$\\sqrt{1-x^2} + \\sqrt{1-y^2} = C$",
                "$(x-y) \\ln Cx = x$",
                "$e^y = C(1 - e^{-x})$"
            ],
            "a": "$\\sqrt{1+x^2} + \\sqrt{1+y^2} = C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x \\sqrt{1-y^2} + y \\sqrt{1-x^2} \\frac{dy}{dx} = 0$",
            "o": [
                "$\\sqrt{1-x^2} + \\sqrt{1-y^2} = C$",
                "$y^2(1-y) = (x+C)^2, y=1$",
                "$(x-y) \\ln Cx = x$",
                "$1 + e^y = C(1 + x^2)$"
            ],
            "a": "$\\sqrt{1-x^2} + \\sqrt{1-y^2} = C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $e^{-y}(1+y') = 1$",
            "o": [
                "$e^y = C(1 - e^{-x})$",
                "$1 + e^y = C(1 + x^2)$",
                "$y^2(1-y) = (x+C)^2, y=1$",
                "$(x-y) \\ln Cx = x$"
            ],
            "a": "$e^y = C(1 - e^{-x})$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y \\ln y dx + x dy = 0, y(1) = 1$",
            "o": ["$y = 1$", "$y = x$", "$y = 2$", "$y = 3$"],
            "a": "$y = 1$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = a^{x+y} (a > 0, a \\neq 1)$ ",
            "o": [
                "$a^x + a^{-y} = C$",
                "$e^x + a^{-y} = C$",
                "$a^x + e^{-y} = C$",
                "$e^x + e^{-2y} = Ca$"
            ],
            "a": "$a^x + a^{-y} = C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $e^y(1+x^2)dy - 2x(1+e^y)dx = 0$",
            "o": [
                "$1 + e^y = C(1 + x^2)$",
                "$y^2(1-y) = (x+C)^2, y=1$",
                "$x^2 = (x^2 - y) \\ln Cx, y = x^2$",
                "$(x-y) \\ln Cx = x$"
            ],
            "a": "$1 + e^y = C(1 + x^2)$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x\\sqrt{1-y^2} = y'(1+x^2)$ ",
            "o": [
                "$y = \\sin \\left[ C + \\ln(1+x^2) \\right]$ ",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$y = \\text{tg } \\ln Cx$",
                "$(x-y) \\ln Cx = x$"
            ],
            "a": "$y = \\sin \\left[ C + \\ln(1+x^2) \\right]$ "
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $e^x \\sin^3 y + (1+e^x) \\cos y \\cdot y' = 0$",
            "o": [
                "$\\text{arctg } e^x = -\\frac{1}{2\\sin^2 y} + C$",
                "$(x-y) \\ln Cx = x$",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$y = \\text{tg } \\ln Cx$"
            ],
            "a": "$\\text{arctg } e^x = -\\frac{1}{2\\sin^2 y} + C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^2 \\sin x dx + \\cos^2 x \\ln y dy = 0$",
            "o": [
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$x + y = \\text{atg}(C + \\frac{y}{a})$",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$y = x(C - \\ln x)$"
            ],
            "a": "$y = (1 + Cy + \\ln y) \\cos x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = \\sin(x-y)$ ",
            "o": [
                "$x + C = \\text{ctg} \\left( \\frac{y-x}{2} + \\frac{\\pi}{4} \\right)$",
                "$\\text{tg } y/2 - e^x \\sin x$",
                "$1 + e^y = C(1 + x^2)$",
                "$y = \\text{tg } \\ln Cx$"
            ],
            "a": "$x + C = \\text{ctg} \\left( \\frac{y-x}{2} + \\frac{\\pi}{4} \\right)$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = ax + by + c$ ",
            "o": [
                "$b(ax + by + c) = C e^{bx}$",
                "$b(by + c) = C e^{2x}$",
                "$b(ax + c) = Cx$",
                "$by = C e^{-ax}$"
            ],
            "a": "$b(ax + by + c) = C e^{bx}$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $(x+y)^2 y' = a^2$",
            "o": [
                "$x + y = a \\text{ tg}(C + \\frac{y}{a})$",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$y^2(1-y) = (x+C)^2, y=1$",
                "$y = \\text{tg } \\ln Cx$"
            ],
            "a": "$x + y = a \\text{ tg}(C + \\frac{y}{a})$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y + xy' = a(1 + xy), y(1/a) = -a$",
            "o": ["$y = -1/x$", "$y = \\sin x$", "$y = \\cos x$", "$y = e^x$"],
            "a": "$y = -1/x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $(a^2 + y^2)dx + 2x\\sqrt{ax - x^2} dy = 0, y(a) = 0$",
            "o": [
                "$y = a \\text{ tg} \\sqrt{\\frac{a}{x} - 1}$",
                "$2y = a + \\text{ctg } x$",
                "$y = \\text{tg} \\sqrt{ax - 1}$",
                "$Cy = \\text{tg } ax$"
            ],
            "a": "$y = a \\text{ tg} \\sqrt{\\frac{a}{x} - 1}$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' + \\sin(x-y) = \\sin(x+y), y(\\pi) = \\pi/2$",
            "o": [
                "$\\text{tg } y/2 = e^2 \\sin x$",
                "$1 + e^y = C(1 + x^2)$",
                "$y = \\text{tg } \\ln Cx$",
                "$x^2 = (x^2 - y) \\ln Cx, y = x^2$"
            ],
            "a": "$\\text{tg } y/2 = e^2 \\sin x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $xy' = y + x \\cos^2(y/x)$ ",
            "o": [
                "$\\text{tg}(y/x) = \\ln Cx$",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$y = x e^{1+Cx}$",
                "$y + \\sqrt{y^2 - x^2} = Cx^2$"
            ],
            "a": "$\\text{tg}(y/x) = \\ln Cx$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x-y)dx + xdy = 0$",
            "o": [
                "$y = x(C - \\ln x)$",
                "$\\text{tg}(y/x) = \\ln Cx$",
                "$y = (1 + Cy + \\ln y) \\cos x$",
                "$y = x e^{1+Cx}$"
            ],
            "a": "$y = x(C - \\ln x)$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' = y(\\ln y - \\ln x)$",
            "o": [
                "$y = x e^{1+Cx}$",
                "$1 + e^y = C(1 + x^2)$",
                "$y + \\sqrt{y^2 - x^2} = Cx^2$",
                "$y^2 - 3xy + 2x^2 = C$"
            ],
            "a": "$y = x e^{1+Cx}$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x^2 dy = (y^2 - xy + x^2) dx$",
            "o": [
                "$(x - y) \\ln Cx = x$",
                "$y = (C + x^2) e^{x^2}$",
                "$(x - y) \\ln Cx = -x$",
                "$y + \\sqrt{y^2 - x^2} = Cx^2$"
            ],
            "a": "$(x - y) \\ln Cx = x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' = y + \\sqrt{y^2 - x^2}$",
            "o": [
                "$y + \\sqrt{y^2 - x^2} = Cx^2$",
                "$y^2(1 - y) = (x + C)^2; y = 1$",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$",
                "$y = C e^{-x} + e^{-x}$"
            ],
            "a": "$y + \\sqrt{y^2 - x^2} = Cx^2$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x^2 y' = x^2 + y^2$",
            "o": [
                "$2x = (x - y) \\ln Cx$",
                "$y^2 - 3xy + 2x^2 = C$",
                "$(x - y) \\ln Cx = -x$",
                "$x = C / y + y \\ln y$"
            ],
            "a": "$2x = (x - y) \\ln Cx$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(4x - 3y) dx + (2y - 3x) dy = 0$",
            "o": [
                "$y^2 - 3xy + 2x^2 = C$",
                "$(x - y) \\ln Cx = -x$",
                "$x = C / y + y \\ln y$",
                "$y = C e^{-x} + e^{-x}$"
            ],
            "a": "$y^2 - 3xy + 2x^2 = C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $(y-x)dx + (y+x)dy = 0$",
            "o": [
                "$y^2 + 2xy - x^2 = C$",
                "$1 + e^y = C(1 + x^2)$",
                "$y^2(1 - y) = (x + C)^2; y = 1$",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$"
            ],
            "a": "$y^2 + 2xy - x^2 = C$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' + 2y = e^x$",
            "o": [
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$",
                "$(x - y) \\ln Cx = x$",
                "$y = Cx - x^2$",
                "$y = (C + x^2) e^{x^2}$"
            ],
            "a": "$x^2 - (x^2 - y) \\ln Cx; y = x^2$"
        },
        {
            "q": "Differensial tenglamaning xususiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $x^2 + xy' = y, y(1) = 0$",
            "o": [
                "$y = x - x^2$",
                "$y = e^x x - 2$",
                "$y = x + \\ln x$",
                "$y = 1 - x^2$"
            ],
            "a": "$y = x - x^2$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' - 2xy = 2xe^{x^2}$ ",
            "o": [
                "$y = (C + x^2) e^{x^2}$",
                "$(x - y) \\ln Cx = x$",
                "$y = (C + x^2) \\ln x$",
                "$1 + e^y = C(1 + x^2)$"
            ],
            "a": "$y = (C + x^2) e^{x^2}$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' + 2xy = e^{-x^2}$ ",
            "o": [
                "$y = (C + x) e^{-x^2}$",
                "$y^2(1 - y) = (x + C)^2; y = 1$",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$",
                "$y = (C + x^2) \\ln x$"
            ],
            "a": "$y = (C + x) e^{-x^2}$"
        },
        {
            "q": "Differensial tenglamaning xususiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' \cos x - y \sin x = 2x, y(0) = 0$",
            "o": [
                "$y = x^2 / \cos x$",
                "$y = (1 + Cy + \ln y) \cos x$",
                "$1 + e^y = C(1 + x^2)$",
                "$(x - y) \ln Cx = x$"
            ],
            "a": "$y = x^2 / \cos x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $xy' - 2y = x^3 \cos x$",
            "o": [
                "$y = Cx^2 + x^2 \sin x$",
                "$y = x^2 / \cos x$",
                "$y = (1 + Cy + \ln y) \cos x$",
                "$y = \sin x / \cos^3 x$"
            ],
            "a": "$y = Cx^2 + x^2 \sin x$"
        },
        {
            "q": "Differensial tenglamaning xususiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y' - y \text{ tg} x = 1 / \cos^3 x, y(0) = 0$",
            "o": [
                "$y = \sin x / \cos^3 x$",
                "$y = (1 + Cy + \ln y) \cos x$",
                "$y = \text{tg } \ln Cx$",
                "$x^2 - (x^2 - y) \ln Cx; y = x^2$"
            ],
            "a": "$y = \sin x / \cos^3 x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $y'x \ln x - y = 3x^3 \ln^2 x$",
            "o": [
                "$y = (C + x^3) \ln x$",
                "$1 + e^y = C(1 + x^2)$",
                "$y = Cx^2 + x^2 \sin x$",
                "$y = x^2 / \cos x$"
            ],
            "a": "$y = (C + x^3) \ln x$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to‘g‘ri ko‘rsatilgan? $(2x - y^2) y' = 2y$",
            "o": [
                "$x = Cy - y^2 / 2$",
                "$y = (C + x^2) e^{x^2}$",
                "$x^2 - (x^2 - y) \ln Cx; y = x^2$",
                "$y' + 2xy = 2xy^2$"
            ],
            "a": "$x = Cy - y^2 / 2$"
        },
        {
            "q": "Differensial tenglamaning xususiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' + y \cos x = \cos x, y(0) = 1$",
            "o": ["$y = 1$", "$y = \sin x$", "$y = \cos x$", "$y = e^x$"],
            "a": "$y = 1$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = y / (2y \ln y + y - x)$ ",
            "o": [
                "$x = C/y + y \ln y$",
                "$y^2(1 - y) = (x + C)^2; y = 1$",
                "$(x - y) \ln Cx = x$",
                "$x = (C + y) e^{-y^2/2}$"
            ],
            "a": "$x = C/y + y \ln y$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(e^{-y^2/2} - xy)dy - dx = 0$",
            "o": [
                "$x = (C + y) e^{-y^2/2}$",
                "$y = (C + x) e^{(1-x)e^x}$",
                "$1 + e^y = C(1 + x^2)$",
                "$y' + 2xy = 2xy^2$"
            ],
            "a": "$x = (C + y) e^{-y^2/2}$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' - y e^x = 2x e^{e^x}$ ",
            "o": [
                "$y = (C + x^2) e^{e^x}$",
                "$x^2 - (x^2 - y) \ln Cx; y = x^2$",
                "$y^2 \ln x = C + \sin x$",
                "$y = (1 + Cy + \ln y) \cos x$"
            ],
            "a": "$y = (C + x^2) e^{e^x}$"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' + x e^x y = e^{(1-x)e^x}$ ",
            "o": [
                "$y = (C + x) e^{(1-x)e^x}$",
                "$1 + e^y = C(1 + x^2)$",
                "$(x - y) \ln Cx = -x$",
                "$y = (C + x^2) e^{e^x}$"
            ],
            "a": "$y = (C + x) e^{(1-x)e^x}$"
        }
    ]

if 'dt_141_210' not in st.session_state:
    st.session_state.dt_141_210 = [
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' + 2xy = 2xy^2$",
            "o": [
                "$y = 1 / (1 + C e^{x^2})$ \n\n",
                "$y = (C + x) e^{(1-x)e^x}$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$y = 1 / (1 + C e^{x^2})$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2y' - y = y / e^x$",
            "o": [
                "$y^2 = (x + C) e^x$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$y^4 + 2x^2 y^2 + 2y^2 = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = -1$ \n\n"
            ],
            "a": "$y^2 = (x + C) e^x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^3 + e^y) y' = 3x^2$",
            "o": [
                "$x^3 e^{-y} = C + y$ \n\n",
                "$1 + e^y = C(1 + x^3)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y = e^{-x^2} / (C - x)$ \n\n"
            ],
            "a": "$x^3 e^{-y} = C + y$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' + 2xy = y^2 e^{x^2}$ ",
            "o": [
                "$y = e^{x^2} / (C - x)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y^4 + 2x^2 y^2 + 2y^2 = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
            ],
            "a": "$y = e^{x^2} / (C - x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' - 2y e^x = 2\\sqrt{y} e^x$",
            "o": [
                "$\\sqrt{y} + 1 = C e^{e^x}$ \n\n",
                "$y = (x - 2) e^x + x + 2$ \n\n",
                "$y = e^{-x^2} / (C - x)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$\\sqrt{y} + 1 = C e^{e^x}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2y' \\ln x + y/x = \\cos x / y$",
            "o": [
                "$y^2 \\ln x = C + \\sin x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n",
                "$y^2(C - x) \\sin x = 1$ \n\n"
            ],
            "a": "$y^2 \\ln x = C + \\sin x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' - y \\cos x = y^3 \\cos x$",
            "o": [
                "$y^2(C - x) \\sin x = 1$ \n\n",
                "$x - y^2 \\cos^2 x = C$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n",
                "$y^4 + 2x^2 y^2 + 2y^2 = C$ \n\n"
            ],
            "a": "$y^2(C - x) \\sin x = 1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + y^2 + 1)dy + xydx = 0$",
            "o": [
                "$y^4 + 2x^2 y^2 + 2y^2 = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$y^4 + 2x^2 y^2 + 2y^2 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^{(IV)} = x$",
            "o": [
                "$y = x^5 / 120 + c_1 x^3 + c_2 x^2 + c_3 x + c_4$ \n\n",
                "$y = x^5 / 60 + c_1 x^3 + 2c_2 x^2 + c_3 x + 3c_4$ \n\n",
                "$y = x^5 / 40 + 3c_1 x^3 + c_2 x^2 + 2c_3 x + c_4$ \n\n",
                "$y = x^5 / 30 + c_1 x^3 + 2c_2 x^2 + 3c_3 x + c_4$ \n\n"
            ],
            "a": "$y = x^5 / 120 + c_1 x^3 + c_2 x^2 + c_3 x + c_4$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y''' = -x + \\cos x$",
            "o": [
                "$y = -x^4 / 24 - \\sin x + c_1 x^2 + c_2 x + c_3$ \n\n",
                "$y = -x^4 / 12 - \\cos x + c_1 x^2 + c_2 x + c_3$ \n\n",
                "$y = -x^4 / 24 - \\text{tg } x + c_1 x^2 + c_2 x + c_3$ \n\n",
                "$y = -x^4 / 6 - \\text{ctg } x + c_1 x^2 + c_2 x + c_3$ \n\n"
            ],
            "a": "$y = -x^4 / 24 - \\sin x + c_1 x^2 + c_2 x + c_3$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = xe^x$",
            "o": [
                "$y = (x - 2) e^x + c_1 x + c_2$ \n\n",
                "$y^4 + 2x^2 y^2 + 2y^2 = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$y = (x - 2) e^x + c_1 x + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = 2x \\ln x$",
            "o": [
                "$y = (x^3 / 3) \\ln x - (5x^3 / 18) + c_1 x + c_2$ \n\n",
                "$y = (x^4 / 4) \\ln x + c_1 x + c_2$ \n\n",
                "$y = (x^3 / 3) \\sin x - (x^3 / 9) + c_1 x + c_2$ \n\n",
                "$y = (x^2 / 2) \\ln 2x - (x^2 / 12) + c_1 x + c_2$ \n\n"
            ],
            "a": "$y = (x^3 / 3) \\ln x - (5x^3 / 18) + c_1 x + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'' = y'$ ",
            "o": [
                "$y = c_1 x^2 + c_2$ \n\n",
                "$y = c_1 x^2 + e^x c_2$ \n\n",
                "$y = c_1 \\sin x + c_2$ \n\n",
                "$y = c_1 x + c_2 \\sin x$ \n\n"
            ],
            "a": "$y = c_1 x^2 + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'' + y' = 0$",
            "o": [
                "$y = c_1 \\ln x + c_2$ \n\n",
                "$y = c_1 x^2 + c_2$ \n\n",
                "$y = c_1 x^2 + e^x c_2$ \n\n",
                "$y = c_1 e^{x^2} + c_2$ \n\n"
            ],
            "a": "$y = c_1 \\ln x + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'' = (1 + 2x^2) y'$ ",
            "o": [
                "$y = c_1 e^{x^2} + c_2$ \n\n",
                "$y = c_1 \\ln x + c_2$ \n\n",
                "$y = c_1 x^2 + c_2$ \n\n",
                "$y = c_1 x^2 + e^x c_2$ \n\n"
            ],
            "a": "$y = c_1 e^{x^2} + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'' = y' + x^3$",
            "o": [
                "$y = (x^3 / 3) + c_1 x^2 + c_2$ \n\n",
                "$y = c_1 e^{x^2} + c_2$ \n\n",
                "$y = c_1 \\ln x + c_2$ \n\n",
                "$y = c_1 x^2 + c_2$ \n\n"
            ],
            "a": "$y = (x^3 / 3) + c_1 x^2 + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x \\ln x y'' = y'$ ",
            "o": [
                "$y = c_1 x(\\ln x - 1) + c_2$ \n\n",
                "$y = (x^3 / 3) + c_1 x^2 + c_2$ \n\n",
                "$y = c_1 e^{x^2} + c_2$ \n\n",
                "$y = c_1 \\ln x + c_2$ \n\n"
            ],
            "a": "$y = c_1 x(\\ln x - 1) + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'' = y' \\ln(y'/x)$ ",
            "o": [
                "$y = (c_1 x - c_1^2) e^{(x/c_1) + 1} + c_2$ \n\n",
                "$y = c_1 x(\\ln x - 1) + c_2$ \n\n",
                "$y = (x^3 / 3) + c_1 x^2 + c_2$ \n\n",
                "$y = c_1 e^{x^2} + c_2$ \n\n"
            ],
            "a": "$y = (c_1 x - c_1^2) e^{(x/c_1) + 1} + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = -\\sqrt{1-(y')^2}$ ",
            "o": [
                "$y = c_2 + c_1 x - \\sin(x + c_1)$ \n\n",
                "$y = (c_1 x - c_1^2) e^{(x/c_1) + 1} + c_2$ \n\n",
                "$y = c_1 x(\\ln x - 1) + c_2$ \n\n",
                "$y = (x^3 / 3) + c_1 x^2 + c_2$ \n\n"
            ],
            "a": "$y = c_2 + c_1 x - \\sin(x + c_1)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy''' - y'' = 0$",
            "o": [
                "$y = c_1 x^3 + c_2 x + c_3$ \n\n",
                "$y = c_2 + c_1 x - \\sin(x + c_1)$ \n\n",
                "$y = (c_1 x - c_1^2) e^{(x/c_1) + 1} + c_2$ \n\n",
                "$y = c_1 x(\\ln x - 1) + c_2$ \n\n"
            ],
            "a": "$y = c_1 x^3 + c_2 x + c_3$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = \\sqrt{1+(y')^2}$",
            "o": [
                "$y = \\text{ch}(x + c_1) + c_2$ \n\n",
                "$y = c_1 x^3 + c_2 x + c_3$ \n\n",
                "$y = c_2 + c_1 x - \\sin(x + c_1)$ \n\n",
                "$y = (c_1 x - c_1^2) e^{(x/c_1) + 1} + c_2$ \n\n"
            ],
            "a": "$y = \\text{ch}(x + c_1) + c_2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = (y')^2$",
            "o": [
                "$y = c_2 - \\ln(c_1 - x)$ \n\n",
                "$y = \\text{ch}(x + c_1) + c_2$ \n\n",
                "$y = c_1 x^3 + c_2 x + c_3$ \n\n",
                "$y = c_2 + c_1 x - \\sin(x + c_1)$ \n\n"
            ],
            "a": "$y = c_2 - \\ln(c_1 - x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = -\\sqrt{1-(y')^2}$ ",
            "o": [
                "$y = c_2 - \\cos(c_1 + x)$ \n\n",
                "$y = c_2 - \\ln(c_1 - x)$ \n\n",
                "$y = \\text{ch}(x + c_1) + c_2$ \n\n",
                "$y = c_1 x^3 + c_2 x + c_3$ \n\n"
            ],
            "a": "$y = c_2 - \\cos(c_1 + x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'' = 1+(y')^2$",
            "o": [
                "$y = c_2 - \\ln \\cos(c_1 + x)$ \n\n",
                "$y = c_2 - \\cos(c_1 + x)$ \n\n",
                "$y = c_2 - \\ln(c_1 - x)$ \n\n",
                "$y = \\text{ch}(x + c_1) + c_2$ \n\n"
            ],
            "a": "$y = c_2 - \\ln \\cos(c_1 + x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(2 - 9xy^2)x dx + (4y^2 - 6x^2 y)y dy = 0$",
            "o": [
                "$x^2 - 3x^2 y^2 + y^4 = C$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$x e^{-y} - y^3 = C$ \n\n"
            ],
            "a": "$x^2 - 3x^2 y^2 + y^4 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $e^{-y} dx - (2y + x e^{-y}) dy = 0$",
            "o": [
                "$x e^{-y} - y^2 = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$x^2 - x^2 y^2 + y^4 = C$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$x e^{-y} - y^2 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $\\frac{y}{x} dx + (y^3 + \\ln x) dy = 0$",
            "o": [
                "$4y \\ln x + y^4 = C$ \n\n",
                "$x e^{-y} - y^2 = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$x^2 - x^2 y^2 + y^4 = C$ \n\n"
            ],
            "a": "$4y \\ln x + y^4 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $\\frac{3x^2 + y^2}{y^2} dx - \\frac{2x^3 + 5y}{y^3} dy = 0$",
            "o": [
                "$x + \\frac{x^3}{y^2} + \\frac{5}{y} = C$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
            ],
            "a": "$x + \\frac{x^3}{y^2} + \\frac{5}{y} = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x(1 + \\sqrt{x^2 - y}) dx - \\sqrt{x^2 - y} dy = 0$",
            "o": [
                "$x^2 + \\frac{2}{3}(x^2 - y)^{3/2} = C$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$x^2 + \\frac{2}{3}(x^2 - y)^{3/2} = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(1 + y^2 \\sin 2x) dx - 2y \\cos^2 x dy = 0$",
            "o": [
                "$x - y^2 \\cos^2 x = C$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$x - y^2 \\cos^2 x = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $3x^2(1 + \\ln y) dx - (2y - x^3/y) dy = 0$",
            "o": [
                "$x^3 + x^3 \\ln y - y^2 = C$ \n\n",
                "$y^2 - x^2(C - 2y); x = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$x^3 + x^3 \\ln y - y^2 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(\\frac{x}{\\sin y} + 2) dx + \\frac{(x^2+1)\\cos y}{\\cos 2y - 1} dy = 0$",
            "o": [
                "$x^2 + 1 = 2(C - 2x) \\sin y$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n",
                "$y \\sin xy = C$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n"
            ],
            "a": "$x^2 + 1 = 2(C - 2x) \\sin y$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + y^2 + x) dx + y dy = 0$",
            "o": [
                "$2x + \\ln(x^2 + y^2) = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$2x + \\ln(x^2 + y^2) = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + y^2 + y) dx - x dy = 0$",
            "o": [
                "$x + \\text{arctg } \\frac{x}{y} = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$x + \\text{arctg } \\frac{x}{y} = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y dy = (x dy + y dx)\\sqrt{1 + y^2}$",
            "o": [
                "$xy + C = \\sqrt{1 + y^2}$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$x + \\text{arctg } \\frac{x}{y} = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
            ],
            "a": "$xy + C = \\sqrt{1 + y^2}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy^2(xy' + y) = 1$",
            "o": [
                "$2x^3 y^3 - 3x^2 = C$ \n\n",
                "$x^2 + \\ln y = Cx^3; x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$2x^3 y^3 - 3x^2 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^2 dx - (xy + x^3) dy = 0$",
            "o": [
                "$y^2 - x^2(C - 2y); x = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$\\sin \\frac{x}{y} = C e^{-y^2}$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$y^2 - x^2(C - 2y); x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(y - 1/x) dx + dy/x = 0$",
            "o": [
                "$(x^2 - C)y = 2x$ \n\n",
                "$x^2 + \\ln y = Cx^3; x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$-x + 1 = xy(\\text{arctg } y + C); x=0, y=0$ \n\n"
            ],
            "a": "$(x^2 - C)y = 2x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + 3 \\ln y) y dx = x dy$",
            "o": [
                "$x^2 + \\ln y = Cx^3; x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y \\sin xy = C$ \n\n"
            ],
            "a": "$x^2 + \\ln y = Cx^3; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^2 dx + (xy + \\text{tg } xy) dy = 0$",
            "o": [
                "$y \\sin xy = C$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n",
                "$y^2 = C x^2 e^{2y^2}$ \n\n",
                "$x^2 + \\ln y = Cx^3; x = 0$ \n\n"
            ],
            "a": "$y \\sin xy = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y(x + y) dx + (xy + 1) dy = 0$",
            "o": [
                "$x^2/2 + xy + \\ln |y| = C; y = 0$ \n\n",
                "$y^2 = C x^2 e^{2y^2}$ \n\n",
                "$\\sin \\frac{x}{y} = C e^{-x^2}$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$x^2/2 + xy + \\ln |y| = C; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y(y^2 + 1) dx + x(y^2 - x + 1) dy = 0$",
            "o": [
                "$-x + 1 = xy(\\text{arctg } y + C); x = 0, y = 0$ \n\n",
                "$2xy^2 + (\\frac{1}{xy}) = C; x = 0, y = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$x + 2 \\ln |x| + \\frac{3}{2} y^2 - \\frac{y}{x} = C; x = 0$ \n\n"
            ],
            "a": "$-x + 1 = xy(\\text{arctg } y + C); x = 0, y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + 2x + y) dx - (x - 3y^2 y) dy = 0$",
            "o": [
                "$x + 2 \\ln |x| + \\frac{3}{2} y^2 - \\frac{y}{x} = C; x = 0$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$\\ln \\frac{x^2}{y^2} + 1 = 2y + C; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$x + 2 \\ln |x| + \\frac{3}{2} y^2 - \\frac{y}{x} = C; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y dx - x dy = 2x^3 \\text{tg } \\frac{y}{x} dx$",
            "o": [
                "$\\sin \\frac{y}{x} = C e^{-x^2}$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$2xy^2 + (\\frac{1}{xy}) = C; x = 0, y = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
            ],
            "a": "$\\sin \\frac{y}{x} = C e^{-x^2}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^2 dx + (e^x - y) dy = 0$",
            "o": [
                "$\\ln |y| - y e^{-x} = C; y = 0$ \n\n",
                "$x \\sqrt{1 + (y^2/x^2)} + \\ln |\\frac{y}{x} + \\sqrt{1 + \\frac{y^2}{x^2}}| = C; x = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = -1$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$\\ln |y| - y e^{-x} = C; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy dx - (y^2 + x^2 y + x^2) dy = 0$",
            "o": [
                "$\\ln \\frac{x^2}{y^2} + 1 = 2y + C; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$x^2 y \\ln Cxy = -1; x = 0, y = 0$ \n\n"
            ],
            "a": "$\\ln \\frac{x^2}{y^2} + 1 = 2y + C; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x^2 y (y dx + x dy) = 2y dx + x dy$",
            "o": [
                "$x^2 y \\ln Cxy = -1; x = 0, y = 0$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$(y - x)^2 - 2C(x + y) - C^2; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$x^2 y \\ln Cxy = -1; x = 0, y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 - y^2 + y) dx + x(2y - 1) dy = 0$",
            "o": [
                "$x^2 + y^2 - y + Cx; x = 0$ \n\n",
                "$y(x + C)^2 = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$2xy^2 + (\\frac{1}{xy}) = C; x = 0, y = 0$ \n\n"
            ],
            "a": "$x^2 + y^2 - y + Cx; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(2x^2 y^2 + y) dx + (x^3 y - x) dy = 0$",
            "o": [
                "$x^2 y + \\ln |\\frac{x}{y}| = C; x = 0, y = 0$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n"
            ],
            "a": "$x^2 y + \\ln |\\frac{x}{y}| = C; x = 0, y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(2x^2 y^3 - 1) y dx + (4x^3 y^2 - 1) x dy = 0$",
            "o": [
                "$2xy^2 + (\\frac{1}{xy}) = C; x = 0, y = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$\\sin y = -(x^2 + 1) \\ln C(x^2 + 1)$ \n\n",
                "$\\sin^2 y = Cx - x^2; x = 0$ \n\n"
            ],
            "a": "$2xy^2 + (\\frac{1}{xy}) = C; x = 0, y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y(x + y^2) dx + x^2(y - 1) dy = 0$",
            "o": [
                "$\\ln |\\frac{x+y}{y}| + \\frac{y(1+y)}{x+y} = C; y = 0, y = -x$ \n\n",
                "$(Cx + 1)^2 = 1 - y^2$ \n\n",
                "$1 + e^y = C(1 + x^3)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$\\ln |\\frac{x+y}{y}| + \\frac{y(1+y)}{x+y} = C; y = 0, y = -x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 - \\sin^2 y) dx + x \\sin 2y dy = 0$",
            "o": [
                "$\\sin^2 y = Cx - x^2; x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y = \\text{tg } \\ln Cx$ \n\n",
                "$y = C \\ln x^2 y$ \n\n"
            ],
            "a": "$\\sin^2 y = Cx - x^2; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x(\\ln y + 2 \\ln x - 1) dy = 2y dx$",
            "o": [
                "$y = C \\ln x^2 y$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$4y = (x + C)^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$y = C \\ln x^2 y$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + 1)(2x dx + \\cos y dy) = 2x \\sin y dx$",
            "o": [
                "$\\sin y = -(x^2 + 1) \\ln C(x^2 + 1)$ \n\n",
                "$\\ln Cy = x \\pm 2 e^{x/2}$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y^2 = C x^2 e^{2y^2}$ \n\n"
            ],
            "a": "$\\sin y = -(x^2 + 1) \\ln C(x^2 + 1)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(2x^2 y^2 - y) dx + (2x^3 y - x) dy = 0$",
            "o": [
                "$xy(C - x^2 - y^2) = -1; x = 0, y = 0$ \n\n",
                "$(Cx + 1)^2 = 1 - y^2$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$xy(C - x^2 - y^2) = -1; x = 0, y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x^3 y' + y + (x^3 y^2 - x) y' = 0$",
            "o": [
                "$y^2 = C x^2 e^{x^2 y^2}$ \n\n",
                "$x^2 y = C; y = Cx$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
            ],
            "a": "$y^2 = C x^2 e^{x^2 y^2}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 - y) dx + x(y + 1) dy = 0$",
            "o": [
                "$x \\sqrt{1 + (y^2/x^2)} + \\ln |\\frac{y}{x} + \\sqrt{1 + \\frac{y^2}{x^2}}| = C; x = 0$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$xy(C - x^2 - y^2) = -1; x = 0, y = 0$ \n\n"
            ],
            "a": "$x \\sqrt{1 + (y^2/x^2)} + \\ln |\\frac{y}{x} + \\sqrt{1 + \\frac{y^2}{x^2}}| = C; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^2(y dx - 2x dy) = x^3 (x dy - 2y dx)$ ",
            "o": [
                "$x^2 - 4y^2 = C y^3 \\sqrt{xy}; x = 0, y = 0$ \n\n",
                "$y = C \\ln x^2 y$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$4y = (x + C)^2$ \n\n"
            ],
            "a": "$x^2 - 4y^2 = C y^3 \\sqrt{xy}; x = 0, y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2xy dx + (x^2 - y^2) dy = 0$",
            "o": [
                "$3x^2 y - y^3 = C$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y(x + C)^2 = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$3x^2 y - y^3 = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(y' + 1)^3 = 27(x + y)^2$",
            "o": [
                "$y + x = (x + C)^3$ \n\n",
                "$x^2 + C^2 = 2Cy$ \n\n",
                "$y(x + C)^2 = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$y + x = (x + C)^3$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 - 4y = 0$",
            "o": [
                "$y(x + C)^2 = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y + x = (x + C)^3$ \n\n",
                "$x^2 + C^2 = 2Cy$ \n\n"
            ],
            "a": "$y = (x + C)^2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'^2 = y$",
            "o": [
                "$(y - x)^2 - 2C(x + y) - C^2; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$\\text{arcsin } \\frac{y}{x^2} = \\ln Cx^2; |x| = y^2$ \n\n",
                "$1 + e^y = C(1 + x^3)$ \n\n"
            ],
            "a": "$(y - x)^2 - 2C(x + y) - C^2; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 + y^2 = yy'(y' + 1)$ ",
            "o": [
                "$4y = (x + C)^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y = C e^x$ \n\n",
                "$x^2 + C^2 = 2Cy$ \n\n"
            ],
            "a": "$4y = (x + C)^2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 + xy' = y^2 + xy$",
            "o": [
                "$y = C e^x$ \n\n",
                "$x^2 + C^2 = 2Cy$ \n\n",
                "$\\text{arcsin } \\frac{y}{x^2} = \\ln Cx^2; |x| = y^2$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$y = C e^x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'^2 - 2yy' + x = 0$",
            "o": [
                "$x^2 + C^2 = 2Cy$ \n\n",
                "$\\text{arcsin } \\frac{y}{x^2} = \\ln Cx^2; |x| = y^2$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y = 2x^2 + C$ \n\n"
            ],
            "a": "$x^2 + C^2 = 2Cy$ \n\n"
        },
        {
            "q": "Quyidagi tenglamalarning qaysi biri $n$-tartibli o'zgarmas koeffitsiyentli chiziqli bir jinsli bo'lmagan tenglama?",
            "o": [
                "$y^{(n)} + a_1 y^{(n-1)} + \\dots + a_n y = 0$ \n\n",
                "$y^{(n)} + a_1 y^{(n-1)} + \\dots + a_n y = f(x)$ \n\n",
                "$y^{(n)} + p_1(x) y^{(n-1)} + \\dots + p_n(x) y = f(x)$ \n\n",
                "$y^{(n)} + p_1(x) y^{(n-1)} + \\dots + p_n(x) y = 0$ \n\n"
            ],
            "a": "$y^{(n)} + a_1 y^{(n-1)} + \\dots + a_n y = f(x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 - 2xy' = 8x^2$",
            "o": [
                "$y = 2x^2 + C$ \n\n",
                "$\\ln Cy = x \\pm 2 e^{x/2}$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$y = 2x^2 + C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 - 2yy' = y^2(e^x - 1)$ ",
            "o": [
                "$\\ln Cy = x \\pm 2 e^{x/2}; y = 0$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$\\text{arctg } u + \\frac{1}{2} \\ln |(u-1)/(u+1)| = \\pm x + C$ \n\n"
            ],
            "a": "$\\ln Cy = x \\pm 2 e^{x/2}; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^4 + y'^2 = y^2$",
            "o": [
                "$\\text{arctg } u + \\frac{1}{2} \\ln |(u-1)/(u+1)| = \\pm x + C, u = \\sqrt{\\sqrt{1 + 4y^2}-1}$ \n\n",
                "$(Cx + 3)^2 = 1 - y^2$ \n\n",
                "$1 + e^{y+1} = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$\\text{arctg } u + \\frac{1}{2} \\ln |(u-1)/(u+1)| = \\pm x + C, u = \\sqrt{\\sqrt{1 + 4y^2}-1}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y(xy' - y)^2 = y - 2xy'$ ",
            "o": [
                "$(Cx + 1)^2 = 1 - y^2$ \n\n",
                "$1 + e^y = C(1 + x^3)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y^2 = (x + C)^3$ \n\n"
            ],
            "a": "$(Cx + 1)^2 = 1 - y^2$ \n\n"
        }
    ]

if 'dt_211_280' not in st.session_state:
    st.session_state.dt_211_280 = [
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $8y'^3 = 27y$",
            "o": [
                "$y^2 = (x + C)^3$ \n\n",
                "$(x + C)^2 + y^2 = 1$ \n\n",
                "$x^2 y \\ln Cy - 1y = 0$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$y^2 = (x + C)^3$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 (y'^2 + 1) = 1$",
            "o": [
                "$(x + C)^2 y = 1$ \n\n",
                "$x^2 y \\ln Cy = 1$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$(x - 1)^{4/3} + y^{4/3} = C$ \n\n"
            ],
            "a": "$(x + C)^2 y = 1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2y + (x^2 y + 1) xy' = 0$",
            "o": [
                "$x^2 y \\ln Cy - 1y = 0$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$(x - 1)^{4/3} + y^{4/3} = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
            ],
            "a": "$x^2 y \\ln Cy - 1y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $yy'^3 + x = 1$",
            "o": [
                "$(x - 1)^{4/3} + y^{4/3} = C$ \n\n",
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$x^2 y = C; y = Cx$ \n\n"
            ],
            "a": "$(x - 1)^{4/3} + y^{4/3} = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $4(1 - y) = (3y - 2)^2 y'^2$",
            "o": [
                "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$x^2 y = C; y = Cx$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$y^2(1 - y) = (x + C)^2; y = 1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'(xy' + y) = 2y^2$",
            "o": [
                "$x^2 y = C; y = Cx^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$(x + C)^2 = 4Cy; y = 0, y = -x$ \n\n",
                "$(x + 2)^{4/3} + C = 4e^{-y/3}$ \n\n"
            ],
            "a": "$x^2 y = C; y = Cx^2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy'^2 = y(2y' - 1)$ ",
            "o": [
                "$(x + C)^2 = 4Cy; y = 0, y = x$ \n\n",
                "$(x + 2)^{4/3} + C = 4e^{-y/3}$ \n\n",
                "$y = Cx^2 \\pm 2\\sqrt{x/7}$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$(x + C)^2 = 4Cy; y = 0, y = x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^3 + (x + 2) e^y = 0$",
            "o": [
                "$3(x + 2)^{4/3} + C = 4e^{-y/3}$ \n\n",
                "$y = Cx^{-3} \\pm 2\\sqrt{x/7}$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$3(x + 2)^{4/3} + C = 4e^{-y/3}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(xy' + 3y)^2 = 7x$",
            "o": [
                "$y = Cx^{-3} \\pm 2\\sqrt{x/7}$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$\\ln Cy = x \\pm \\sin x; y = 0$ \n\n"
            ],
            "a": "$y = Cx^{-3} \\pm 2\\sqrt{x/7}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'(2y - y') = y^2 \\sin^2 x$",
            "o": [
                "$\\ln Cy = x \\pm \\sin x; y = 0$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$x^2 + (Cy + 1)^2 = 1; y = 0$ \n\n",
                "$2(x - C)^2 + 2y^2 = C^2; y = \\pm x$ \n\n"
            ],
            "a": "$\\ln Cy = x \\pm \\sin x; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x(y - xy')^2 = xy'^2 - 2yy'$ ",
            "o": [
                "$x^2 + (Cy + 1)^2 = 1; y = 0$ \n\n",
                "$2(x - C)^2 + 2y^2 = C^2; y = \\pm x$ \n\n",
                "$y = C e^{x^2} - x^2$ \n\n",
                "$y = C(x + 1) e^{-x}; x = -1$ \n\n"
            ],
            "a": "$x^2 + (Cy + 1)^2 = 1; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $yy'(yy' - 2x) = x^2 - 2y^2$",
            "o": [
                "$2(x - C)^2 + 2y^2 = C^2; y = \\pm x$ \n\n",
                "$y = C e^{x^2} - x^2$ \n\n",
                "$y = C(x + 1) e^{-x}; x = -1$ \n\n",
                "$\\ln |x| = C + \\ln(y^2 + 1); x = 0$ \n\n"
            ],
            "a": "$2(x - C)^2 + 2y^2 = C^2; y = \\pm x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y'^2 + 4xy' - y^2 - 2x^2 y - x^4 - 4x^2 = 0$",
            "o": [
                "$y = C e^x - x^2$ \n\n",
                "$y = C(x + 1) e^{-x}; x = -1$ \n\n",
                "$\\ln |x| = C + \\ln(y^2 + 1); x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$y = C e^x - x^2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy dx + (x + 1) dy = 0$",
            "o": [
                "$y = C(x + 1) e^{-x}; x = -1$ \n\n",
                "$\\ln |x| = C + \\ln(y^2 + 1); x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y = C e^{x^2} - x^2$ \n\n"
            ],
            "a": "$y = C(x + 1) e^{-x}; x = -1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $\\sqrt{y^2 + 1} dx = xy dy$",
            "o": [
                "$\\ln |x| = C + \\ln(y + \\sqrt{y^2 + 1}); x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$y = C(x + 1) e^{-x}; x = -1$ \n\n",
                "$y = C e^{x^2} - x^2$ \n\n"
            ],
            "a": "$\\ln |x| = C + \\ln(y + \\sqrt{y^2 + 1}); x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 - 1)y' + 2xy^2 = 0; y(0) = 1$",
            "o": [
                "$y(\\ln |x^2 - 1| + C) = 1; y = 0; y[\\ln(1 - x^2) + 1] = 1$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$y = 2 + C \\cos x; y = 2 - 3 \\cos x$ \n\n"
            ],
            "a": "$y(\\ln |x^2 - 1| + C) = 1; y = 0; y[\\ln(1 - x^2) + 1] = 1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' \\text{ctg } x + y = 2; y(x) \\to -1$",
            "o": [
                "$y = 2 + C \\cos x; y = 2 - 3 \\cos x$ \n\n",
                "$y^2 - 2 = C e^{1/x}$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$y = 2 + C \\cos x; y = 2 - 3 \\cos x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = 3 \\sqrt[3]{y^2}; y(2) = 0$",
            "o": [
                "$y = (x - C)^3; y = 0; y = (x - 2)^3; y = 0$ \n\n",
                "$y(1 - Cx) = 1; y = 0; y(1 + x) = 1$ \n\n",
                "$y^2 - 2 = C e^{1/x}$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$y = (x - C)^3; y = 0; y = (x - 2)^3; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' + y = y^2; y(1) = 0.5$",
            "o": [
                "$y(1 - Cx) = 1; y = 0; y(1 + x) = 1$ \n\n",
                "$y^2 - 2 = C e^{1/x}$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$y(1 - Cx) = 1; y = 0; y(1 + x) = 1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x^2 yy' + y^2 = 2$",
            "o": [
                "$y^2 - 2 = C e^{1/x}$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(C e^{-x^2} - 1)y - 2y = 0$ \n\n"
            ],
            "a": "$y^2 - 2 = C e^{1/x}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y - xy' = 2xy$",
            "o": [
                "$(C e^{-2x} - 1)y - 2y = 0$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y^2 - 2 = C e^{1/x}$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$(C e^{-2x} - 1)y - 2y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $e^{-s}(1 + \\frac{ds}{dt}) = 1$",
            "o": [
                "$e^{-s} = 1 + C e^t$ \n\n",
                "$e^s = x + C e^t$ \n\n",
                "$e^{-s} + C = 1$ \n\n",
                "$s + e^s = C + e^t$ \n\n"
            ],
            "a": "$e^{-s} = 1 + C e^t$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $z' = 10^{x+z}$ ",
            "o": [
                "$z = -\\lg(C - 10^x)$ \n\n",
                "$z = \\sin(C - 10^x)$ \n\n",
                "$z = \\text{tg }(C - 10^x)$ \n\n",
                "$z = \\cos(C - 10^x)$ \n\n"
            ],
            "a": "$z = -\\lg(C - 10^x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x \\frac{dy}{dx} + t = 1$",
            "o": [
                "$x^2 + t^2 - 2t + C = 0$ \n\n",
                "$x + t - 2t^2 + C = 0$ \n\n",
                "$2x^2 + t + C = 0$ \n\n",
                "$x + 2t^2 - t = C$ \n\n"
            ],
            "a": "$x^2 + t^2 - 2t + C = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = \\cos(y - x)$ ",
            "o": [
                "$\\text{ctg } \\frac{y-x}{2} = x + C; y - x = 2\\pi k, k = 0, \\pm 1, \\dots$ \n\n",
                "$2x + y - 1 = C e^x$ \n\n",
                "$y' - x^2 = Cy; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$\\text{ctg } \\frac{y-x}{2} = x + C; y - x = 2\\pi k, k = 0, \\pm 1, \\dots$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' - y = 2x - 3$",
            "o": [
                "$2x + y - 1 = C e^x$ \n\n",
                "$y' - x^2 = Cy; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n"
            ],
            "a": "$2x + y - 1 = C e^x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x + 2y)y' = 1; y(0) = -1$",
            "o": [
                "$x + 2y + 2 = C e^y; x + 2y + 2 = 0$ \n\n",
                "$(x - y) \\ln Cx = -x$ \n\n",
                "$\\sqrt{4x + 2y - 1} - 2 \\ln(\\sqrt{4x + 2y - 1} + 2) = x + C$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$x + 2y + 2 = C e^y; x + 2y + 2 = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = \\sqrt{4x + 2y - 1}$ ",
            "o": [
                "$\\sqrt{4x + 2y - 1} - 2 \\ln(\\sqrt{4x + 2y - 1} + 2) = x + C$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$x + y = Cx^2; x = 0$ \n\n",
                "$\\ln(x^2 + y^2) = C - 2 \\text{arctg }(y/x)$ \n\n"
            ],
            "a": "$\\sqrt{4x + 2y - 1} - 2 \\ln(\\sqrt{4x + 2y - 1} + 2) = x + C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x + 2y)dx - xdy = 0$",
            "o": [
                "$x + y = Cx^2; x = 0$ \n\n",
                "$\\ln(x^2 + y^2) = C - 2 \\text{arctg }(y/x)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$x + y = Cx^2; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x - y)dx + (x + y)dy = 0$",
            "o": [
                "$\\ln(x^2 + y^2) = C - 2 \\text{arctg }(y/x)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$x + y = Cx^2; x = 0$ \n\n"
            ],
            "a": "$\\ln(x^2 + y^2) = C - 2 \\text{arctg }(y/x)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(y^2 - 2xy)dx + 2x^2 dy = 0$",
            "o": [
                "$x(y - x) = Cy; y = 0$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$\\ln(x^2 + y^2) = C - 2 \\text{arctg }(y/x)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
            ],
            "a": "$x(y - x) = Cy; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x^3 y = xyy'$ ",
            "o": [
                "$x = \\pm y \\sqrt{\\ln Cx}; y = 0$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$y = C e^{x^2}$ \n\n",
                "$y^2 - x^2 = Cy; y = 0$ \n\n"
            ],
            "a": "$x = \\pm y \\sqrt{\\ln Cx}; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y^2 + x^2 y' = xyy'$ ",
            "o": [
                "$y = C e^{y/x}$ \n\n",
                "$y^2 - x^2 = Cy; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n"
            ],
            "a": "$y = C e^{y/x}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x^2 + y^2)y' = 2xy$",
            "o": [
                "$y^2 - x^2 = Cy; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = -x \\ln \\ln Cx$ \n\n"
            ],
            "a": "$y^2 - x^2 = Cy; y = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' - y = x \\text{tg } \\frac{y}{x}$ ",
            "o": [
                "$\\sin \\frac{y}{x} = Cx$ \n\n",
                "$y^2 - x^2 = Cy; y = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n"
            ],
            "a": "$\\sin \\frac{y}{x} = Cx$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' = y \\ln e^{y/x}$ ",
            "o": [
                "$y = -x \\ln \\ln Cx$ \n\n",
                "$x^2 = (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$y = -x \\ln \\ln Cx$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' - y = (x + y) \\ln \\frac{x+y}{x}$ ",
            "o": [
                "$\\ln \\frac{x+y}{x} = Cx$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$x^2 = (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n"
            ],
            "a": "$\\ln \\frac{x+y}{x} = Cx$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $xy' = y \\cos \\ln \\frac{y}{x}$ ",
            "o": [
                "$\\ln Cx = \\text{ctg } (\\frac{1}{2} \\ln \\frac{y}{x}); y = x e^{2\\pi k}$ \n\n",
                "$2x + y - 1 = C e^{e^x}$ \n\n",
                "$(y - x + 2)^2 + 2x = C$ \n\n",
                "$\\ln \\frac{x+y}{x} = Cx$ \n\n"
            ],
            "a": "$\\ln Cx = \\text{ctg } (\\frac{1}{2} \\ln \\frac{y}{x}); y = x e^{2\\pi k}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(y + \\sqrt{xy}) dx = x dy$",
            "o": [
                "$2 \\sqrt{y/x} = \\ln Cx; y = 0; x = 0$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$2 \\sqrt{y/x} = \\ln Cx; y = 0; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(2x - 4y + 6) dx + (x + y - 3) dy = 0$",
            "o": [
                "$(y - 2x)^3 = C(y - x - 1)^2; y = x + 1$ \n\n",
                "$x^2 = (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$2x + y - 1 = C e^{e^x}$ \n\n",
                "$(y - x + 2)^2 + 2x = C$ \n\n"
            ],
            "a": "$(y - 2x)^3 = C(y - x - 1)^2; y = x + 1$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(2x + y + 1)dx - (4x + 2y - 3)dy = 0$",
            "o": [
                "$2x + y - 1 = C e^{2y-x}$ \n\n",
                "$(y - x + 2)^2 + 2x = C$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$(y - x + 5)^5 (x + 2y - 2) = C$ \n\n"
            ],
            "a": "$2x + y - 1 = C e^{2y-x}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x - y - 1 + (y - x + 2) y' = 0$",
            "o": [
                "$(y - x + 2)^2 + 2x = C$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$(y - x + 5)^5 (x + 2y - 2) = C$ \n\n",
                "$(y + 2)^2 = C(x + y - 1); y = 1 - x$ \n\n"
            ],
            "a": "$(y - x + 2)^2 + 2x = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(x + 4y)y' = 2x + 3y - 5$",
            "o": [
                "$(y - x + 5)^5 (x + 2y - 2) = C$ \n\n",
                "$(y + 2)^2 = C(x + y - 1); y = 1 - x$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$(y - x + 2)^2 + 2x = C$ \n\n"
            ],
            "a": "$(y - x + 5)^5 (x + 2y - 2) = C$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(y + 2)dx - (2x + y - 4)dy = 0$",
            "o": [
                "$(y + 2)^2 = C(x + y - 1); y = 1 - x$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$(y - x + 2)^2 + 2x = C$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$(y + 2)^2 = C(x + y - 1); y = 1 - x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = 2 (\\frac{y+2}{x+y-1})^2$ ",
            "o": [
                "$y + 2 = C e^{-2 \\text{arctg } \\frac{y+2}{x-3}}$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$y + 2 = C e^{-2 \\text{arctg } \\frac{y+2}{x-3}}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $(y' + 1) \\ln \\frac{y+x}{x+3} = \\frac{y+x}{x+3}$",
            "o": [
                "$\\ln \\frac{y+x}{x+3} = 1 + \\frac{C}{x+y}$ \n\n",
                "$\\sin \\frac{y-2x}{x+1} = C(x + 1)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n"
            ],
            "a": "$\\ln \\frac{y+x}{x+3} = 1 + \\frac{C}{x+y}$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = \\frac{y+2}{x+1} + \\text{tg } \\frac{y-2x}{x+1}$ ",
            "o": [
                "$\\sin \\frac{y-2x}{x+1} = C(x + 1)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$\\sin \\frac{y-2x}{x+1} = C(x + 1)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $x^2(y' - x) = y^2$",
            "o": [
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$2x + y - 1 = C e^{e^x}$ \n\n"
            ],
            "a": "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x^2 y' = y^3 + xy$",
            "o": [
                "$x = -y^2 \\ln Cx$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$x^2 y \\ln Cx^2 - 1y = 0; x = 0$ \n\n"
            ],
            "a": "$x = -y^2 \\ln Cx$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2x dy + (x^2 y^2 + 1) y dx = 0$",
            "o": [
                "$x^2 y \\ln Cx^2 - 1y = 0; x = 0$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$x^2 y \\ln Cx^2 - 1y = 0; x = 0$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y dx + x(2xy + 1) dy = 0$",
            "o": [
                "$1 + e^y = C(1 + x^2)$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$(2\\sqrt{y} - x) \\ln C(2\\sqrt{y} - x) = x; 2\\sqrt{y} = x$ \n\n"
            ],
            "a": "$1 + e^y = C(1 + x^2)$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2y' + x = 4\\sqrt{y}$ ",
            "o": [
                "$(2\\sqrt{y} - x) \\ln C(2\\sqrt{y} - x) = x; 2\\sqrt{y} = x$ \n\n",
                "$x^2 y \\ln Cx^2 - 1y = 0; x = 0$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$x = -y^2 \\ln Cx$ \n\n"
            ],
            "a": "$(2\\sqrt{y} - x) \\ln C(2\\sqrt{y} - x) = x; 2\\sqrt{y} = x$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $y' = y^2 - \\frac{2}{x^2}$ ",
            "o": [
                "$1 - xy = Cx^3(2 + xy); xy = -2$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n",
                "$1 + e^y = C(1 + x^2)$ \n\n"
            ],
            "a": "$1 - xy = Cx^3(2 + xy); xy = -2$ \n\n"
        },
        {
            "q": "Differensial tenglamaning umumiy yechimi qaysi qatorda to'g'ri ko'rsatilgan? $2xy' + y = y^2 \\sqrt{x - x^2 y^2}$ ",
            "o": [
                "$2 \\sqrt{1/(xy^2 - 1)} = -\\ln Cx; y = 0; xy^2 = 0$ \n\n",
                "$(x - y) \\ln Cx = x$ \n\n",
                "$x^2 - (x^2 - y) \\ln Cx; y = x^2$ \n\n",
                "$y = (1 + Cy + \\ln y) \\cos x$ \n\n"
            ],
            "a": "$2 \\sqrt{1/(xy^2 - 1)} = -\\ln Cx; y = 0; xy^2 = 0$ \n\n"
        },
        {
            "q": "$y = x^3 + C_1 x + C_2$ parabolalar oilasining differensial tenglamasini toping:",
            "o": [
                "$y'' = 6x$ \n\n",
                "$y' = 6x + 2$ \n\n",
                "$y' = 6x^2 + 2$ \n\n",
                "$y = xy - e^{y'}$ \n\n"
            ],
            "a": "$y'' = 6x$ \n\n"
        },
        {
            "q": "$y = e^{y'}$ chiziqlar oilasining differensial tenglamasini toping:",
            "o": [
                "$y = e^{xy'/y}$ \n\n",
                "$y = e^{y'}$ \n\n",
                "$y = 1 + e^{y'}$ \n\n",
                "$y = xy' - e^{y'}$ \n\n"
            ],
            "a": "$y = xy' - e^{y'}$ \n\n"
        },
        {
            "q": "$b$ sonining qanday qiymatlarida $y'' + by = 0$ tenglamaning barcha yechimlari butun sonlar o'qi $(-\\infty, +\\infty)$ da chegaralangan?",
            "o": [
                "$b > 0$ \n\n",
                "$b < 0$ \n\n",
                "$b = 0$ \n\n",
                "$b = -1$ \n\n"
            ],
            "a": "$b > 0$ \n\n"
        },
        {
            "q": "$y' e^{x^2} = x \\cdot e^{x^2} - y$ differensial tenglamaning turini aniqlang:",
            "o": [
                "Bir jinsli bo'lmagan chiziqli differensial tenglama \n\n",
                "Bernulli tenglamasi \n\n",
                "Rikatti tenglamasi \n\n",
                "Eyler tenglamasi \n\n"
            ],
            "a": "Bir jinsli bo'lmagan chiziqli differensial tenglama \n\n"
        },
        {
            "q": "Quyidagilarning qaysi biri $y' + p(x)y = 0$ tenglamaning umumiy yechimi bo'ladi?",
            "o": [
                "$y = p(x)$ \n\n",
                "$y = C e^{p(x)}$ \n\n",
                "$y = p'(x)$ \n\n",
                "$y = C e^{-\\int p(x) dx}$ \n\n"
            ],
            "a": "$y = C e^{-\\int p(x) dx}$ \n\n"
        },
        {
            "q": "$y' + x \\cdot y = y^3$ tenglamani qaysi almashtirish yordamida chiziqli tenglamaga keltirish mumkin?",
            "o": [
                "$z = y^{-2}$ \n\n",
                "$z = y^{-3}$ \n\n",
                "$z = y^2$ \n\n",
                "$z = y^3$ \n\n"
            ],
            "a": "$z = y^{-2}$ \n\n"
        },
        {
            "q": "$y^{IV} + 8y'' + 16 = 0$ tenglamaning umumiy yechimini toping.",
            "o": [
                "$y = [C_1 \\cos 2x + C_2 \\sin 2x] e^{3x}$ \n\n",
                "$y = [(C_1 + C_2 x) \\cos 5x + (C_3 + C_4 x) \\sin 5x] e^{3x}$ \n\n",
                "$y = [(C_1 + C_2 x) \\cos 2x + (C_3 + C_4 x) \\sin 2x] e^{0x}$ \n\n",
                "$y = [(C_1 + C_2 x) \\cos 2x + (C_3 + C_4 x) \\sin 2x] e^{3x}$ \n\n"
            ],
            "a": "$y = [(C_1 + C_2 x) \\cos 2x + (C_3 + C_4 x) \\sin 2x] e^{0x}$ \n\n"
        },
        {
            "q": "$y''' - 8y = 0$ tenglamani yeching.",
            "o": [
                "$y = C_1 e^{2x} + e^{-x}(C_2 \\cos \\sqrt{3}x + C_3 \\sin \\sqrt{3}x)$ \n\n",
                "$y = C_1 e^{-x} + e^x(C_2 \\cos \\sqrt{3}x + C_3 \\sin \\sqrt{3}x)$ \n\n",
                "$y = C_1 e^{-x} + e^{2x}(C_2 \\cos \\sqrt{3}x + C_3 \\sin \\sqrt{3}x)$ \n\n",
                "$y = C_1 e^{-x} + e^{3x}(C_2 \\cos 4x + C_3 \\sin 4x)$ \n\n"
            ],
            "a": "$y = C_1 e^{2x} + e^{-x}(C_2 \\cos \\sqrt{3}x + C_3 \\sin \\sqrt{3}x)$ \n\n"
        },
        {
            "q": "$y'' + y' - 2y = 3x e^x$ tenglamaning bir jinsli bo'lmagan qismining yechimi qanday ko'rinishda izlanadi?",
            "o": [
                "$y_1 = x e^x (ax + b)$ \n\n",
                "$y_1 = e^x (ax + b)$ \n\n",
                "$y_1 = e^{-x} (ax + b)$ \n\n",
                "$y_1 = ax e^x$ \n\n"
            ],
            "a": "$y_1 = x e^x (ax + b)$ \n\n"
        },
        {
            "q": "$x^2 y'' - 4xy' + 6y = 0$ tenglamani yeching.",
            "o": [
                "$y(x) = C_1 x^{-2} + C_2 x^{-3}$ \n\n",
                "$y(x) = C_1 x^2 + C_2 x^{-3}$ \n\n",
                "$y(x) = C_1 x^{-2} + C_2 x^3$ \n\n",
                "$y(x) = C_1 x^2 + C_2 x^3$ \n\n"
            ],
            "a": "$y(x) = C_1 x^2 + C_2 x^3$ \n\n"
        },
        {
            "q": "$(x-2)^2 y'' - 3(x-2)y' + 4y = x$ Eyler tenglamasini yechish uchun qanday almashtirish bajarish kerak?",
            "o": [
                "$x - 2 = e^t$ \n\n",
                "$x + 2 = e^t$ \n\n",
                "$x = e^t$ \n\n",
                "$x = e^{-t}$ \n\n"
            ],
            "a": "$x - 2 = e^t$ \n\n"
        },
        {
            "q": "Differensial tenglamada: $y' = f(\\frac{a_1 x + b_1 y + c_1}{k(a_1 x + b_1 y) + c_2})$ qanday shakl almashtirish bajarib o'zgaruvchilari ajraladigan differensial tenglamaga olib kelinadi?",
            "o": [
                "$z^{-2} = a_1 x + b_1 y$ \n\n",
                "$z = a_1 x - b_1 y$ \n\n",
                "$z = a_1 x + b_1 y$ \n\n",
                "$z^{-1} = a_1 x + b_1 y$ \n\n"
            ],
            "a": "$z = a_1 x + b_1 y$ \n\n"
        },
        {
            "q": "Ushbu $y' = f(\\frac{2x + 3y + 6}{4x + 6y - 8})$ differensial tenglamada qanday shakl almashtirish bajarib o'zgaruvchilari ajraladigan differensial tenglamaga olib kelinadi?",
            "o": [
                "$z = 2x + 3y$ \n\n",
                "$z = 2x - 3y$ \n\n",
                "$z^{-1} = 2x - 3y$ \n\n",
                "$z^{-2} = 2x + 3y$ \n\n"
            ],
            "a": "$z = 2x + 3y$ \n\n"
        },
        {
            "q": "$y' = a(x)y^2 + b(x)y + c(x)$ Rikkati tenglamasini bitta xususiy yechimi berilgan bo'lsa, uni qanday turdagi tenglamaga keltirish mumkin?",
            "o": [
                "Lagranj tenglamasiga \n\n",
                "Bernulli tenglamasiga \n\n",
                "Eyler tenglamasiga \n\n",
                "Eyri tenglamasiga \n\n"
            ],
            "a": "Bernulli tenglamasiga \n\n"
        },
        {
            "q": "Ushbu $x' + p(t)x = f(t)x^m$ Bernulli tenglamasi $m$ ning qanday qiymatida chiziqli differensial tenglama bo'ladi?",
            "o": [
                "$0$ \n\n",
                "$-2$ \n\n",
                "$2$ \n\n",
                "$-1$ \n\n"
            ],
            "a": "$0$ \n\n"
        },
        {
            "q": "Ushbu $\\frac{dx}{dt} + p(t)x = f(t)x^m$ Bernulli tenglamasi $m$ ning qaysi qiymatida chiziqli bir jinsli differensial tenglamaga aylanadi?",
            "o": [
                "$1$ \n\n",
                "$3$ \n\n",
                "$4$ \n\n",
                "$0$ \n\n"
            ],
            "a": "$1$ \n\n"
        }
    ]

if 'dt_281_350' not in st.session_state:
    st.session_state.dt_281_350 = []
    
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
                st.markdown("<p style='text-align: center; color: #475569;'>📐 Blokni tanlang:</p>", unsafe_allow_html=True)
                blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-280", "281-350", "351-395"], key="diff_blok", label_visibility="collapsed")
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
                
                    if blok == "1-70":
                        st.session_state.active_questions = list(st.session_state.dt_1_70)
                    elif blok == "71-140":
                        st.session_state.active_questions = list(st.session_state.dt_71_140)
                    elif blok == "141-210":
                        st.session_state.active_questions = list(st.session_state.dt_141_210)
                    elif blok == "211-280":
                        st.session_state.active_questions = list(st.session_state.dt_211_280)
                    elif blok == "281-350":
                        st.session_state.active_questions = list(st.session_state.dt_281_350)
                    elif blok == "351-395":
                        st.session_state.active_questions = list(st.session_state.dt_351_395)
                     
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
            
            # Savol raqami
            st.markdown(f"<h3 style='text-align: center;'>Savol {q_idx + 1}/{len(questions)}</h3>", unsafe_allow_html=True)
            
            # Savol matnini LaTeX bilan chiqarish (Kitobdagidek chiroyli chiqadi)
            st.write("---")
            st.markdown(f"#### {curr['q']}") 
            st.write("---")

            if not st.session_state.get('answered', False):
                # Variantlarni chiqarish
                ans = st.radio("Javobingizni tanlang:", curr['o'], index=None, key=f"q_{q_idx}")
                
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
                        st.session_state.current_q_index = len(questions)
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
            
            current_user = st.session_state.get('u_login', 'Mehmon')
            current_subject = st.session_state.get('current_fan', 'Aniqlanmagan fan')
            current_score = st.session_state.get('user_score', 0)
            total_questions = len(questions)
            
            if 'log_saved' not in st.session_state:
                save_log(current_user, current_subject, current_score, total_questions)
                st.session_state.log_saved = True
            
            st.markdown("<h2>Test yakunlandi!</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1 style='color: #2563eb;'>Natija: {current_score} / {total_questions}</h1>", unsafe_allow_html=True)
            
            if st.button("🏠 ASOSIY MENUGA QAYTISH"):
                st.session_state.test_started = False
                st.session_state.current_q_index = 0
                st.session_state.user_score = 0
                st.session_state.answered = False
                if 'log_saved' in st.session_state: 
                    del st.session_state.log_saved
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

# 3. Footer (Har doim ko'rinadi)
st.markdown(f"""
    <div class="footer" style="text-align: center; padding-top: 40px; padding-bottom: 20px;">
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
