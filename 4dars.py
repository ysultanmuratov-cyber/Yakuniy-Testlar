import streamlit as st
import random

# 1. Sahifa sozlamalari
st.set_page_config(page_title="Testlar Markazi", page_icon="🎯", layout="centered")

# 2. Yangilangan CSS (Tepadagi bo'shliqni yo'qotish va Card dizayni)
st.markdown("""
    <style>
    /* Sahifa tepasidagi bo'shliqni majburan yo'qotish */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        max-width: 600px !important;
    }
    header {visibility: hidden;} /* Streamlit yuqori chizig'ini yashirish */
    .stApp { background-color: #e6ebf0 !important; }
    
    /* Savol turadigan oq quti (Card) dizayni */
    .quiz-card {
        background-color: white !important;
        padding: 25px !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
        color: #333333 !important;
        margin-bottom: 20px !important;
    }
    
    /* Barcha matnlarni qora rangda qilish */
    h1, h2, h3, p, span, div, label { color: #333333 !important; }
    
    /* Tugmalar dizayni */
    .stButton button {
        width: 100%;
        background-color: #0088cc !important;
        color: white !important;
        border-radius: 10px !important;
        height: 48px;
        font-weight: bold;
        border: none;
        margin-top: 10px;
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
        {"q": "Shaxsiy byudjetni tuzishda qaysi xarajatlarni alohida belgilash tavsiya etiladi?", "o": ["Doimiy va o‘zgaruvchan xarajatlar", "Faoliyat xarajatlari", "Faqat o‘zgaruvchan xarajatlar", "Xarajatlarni hisoblamaslik"], "a": "Doimiy va o‘zgaruvchan xarajatlar"},
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
        {"q": "Qarz olish qaysi sharoitda arzon bo‘ladi?", "o": ["Foiz stavkasi past bo‘lsa", "Foiz stavkasi yuqori bo‘lsa", "Daromad oshsa", "Xarajat oshsa"], "a": "Foiz stavkasi past bo‘lsa"}
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
        {"q": "Shaxsiy moliyaviy reja qaysi elementlarni o‘z ichiga oladi?", "o": ["Daromadlar, xarajatlar, investitsiyalar, qarzlar", "Faoliyat xarajatlari", "Faqat xarajatlar", "Faqat qarzlar"], "a": "Daromadlar, xarajatlar, investitsiyalar, qarzlar"},
        {"q": "Nima uchun daromad va xarajatlarni muntazam kuzatib borish moliyaviy barqarorlikka erishishda muhim hisoblanadi?", "o": ["Bu sizga daromadni oshirish imkonini beradi", "Xarajatlarni nazorat qilish va moliyaviy maqsadlarga erishishga yordam beradi", "Bank kreditini olishni kafolatlaydi", "Faqat soliqlarni kamaytiradi"], "a": "Xarajatlarni nazorat qilish va moliyaviy maqsadlarga erishishga yordam beradi"},
        {"q": "Inflyatsiya yuqori bo‘lganda, uzoq muddatda bu qanday moliyaviy oqibatlarga olib kelishi mumkin?", "o": ["Pulning qiymati oshadi va xarid qobiliyati ko‘payadi", "Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati barqaror bo‘ladi", "Pul naqd holatda xavfsiz hisoblanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Qaysi sababga ko‘ra shaxsiy reja barcha ushbu elementlarni o‘z ichiga olishi muhim?", "o": ["Faqat bank qarzini olish uchun kerak", "Barcha moliyaviy resurslarni nazorat qilish va kelajakdagi moliyaviy qarorlarni ongli qabul qilish imkonini beradi", "Soliqlarni kamaytiradi", "Xarajatlarni oshirishni kafolatlaydi"], "a": "Barcha moliyaviy resurslarni nazorat qilish va kelajakdagi moliyaviy qarorlarni ongli qabul qilish imkonini beradi"},
        {"q": "Yuqori foiz stavkali kreditni uzoq muddatga olsangiz, bu qanday ta’sir qilishi mumkin?", "o": ["Xarajatlar kamayadi", "Foiz xarajatlari ko‘payadi va byudjet muvozanati buzilishi mumkin", "Daromadlar oshadi", "Xarajatlar o‘zgarmaydi"], "a": "Foiz xarajatlari ko‘payadi va byudjet muvozanati buzilishi mumkin"},
        {"q": "Konsolidatsiya qanday moliyaviy foyda keltirishi mumkin?", "o": ["Qarzlarni tezroq va osonroq boshqarish, foiz stavkasini kamaytirish imkoniyati", "Daromadni oshirish", "Soliqni kamaytirish", "Naqd pul miqdori oshirish"], "a": "Qarzlarni tezroq va osonroq boshqarish, foiz stavkasini kamaytirish imkoniyati"},
        {"q": "Nima uchun diversifikatsiya moliyaviy xavfni kamaytiradi?", "o": ["Barcha investitsiyalar bir xil daromad beradi", "Turli aktivlarga investitsiya qilish orqali bir aktivning yo‘qotishi boshqa aktivlarning daromadlari bilan qoplanadi", "Diversifikatsiya foiz stavkasini oshiradi", "Bu naqd pulni ko‘paytiradi"], "a": "Turli aktivlarga investitsiya qilish orqali bir aktivning yo‘qotishi boshqa aktivlarning daromadlari bilan qoplanadi"},
        {"q": "Byudjet “qizil rangda” bo‘lishi moliyaviy barqarorlik uchun qanday xavf tug‘diradi?", "o": ["Xarajatlarni nazorat qilish osonlashadi", "Qarzga bog‘lanish, jamg‘arma kamayishi va moliyaviy stress yuzaga keladi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Qarzga bog‘lanish, jamg‘arma kamayishi va moliyaviy stress yuzaga keladi"},
        {"q": "Portfelingizni turli moliyaviy aktivlar bilan diversifikatsiya qilish nima uchun tavsiya etiladi?", "o": ["Faqat aksiyalar daromad keltiradi", "Turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Bu naqd pulni oshiradi"], "a": "Turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi"},
        {"q": "Nima uchun SMART tamoyili moliyaviy rejani samarali qiladi?", "o": ["Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib, ularni amalga oshirish rejasi tuziladi", "Bank qarzini olish osonlashadi", "Xarajatlarni oshirish imkoniyati paydo bo‘ladi", "Foiz stavkasi oshadi"], "a": "Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib, ularni amalga oshirish rejasi tuziladi"},
        {"q": "Shaxsiy byudjetni nazorat qilishda moliyaviy ilovalar yoki jurnallardan foydalanish qanday foyda beradi?", "o": ["Daromad va xarajatlarni aniq kuzatish, moliyaviy maqsadlarga erishish va byudjetni muvozanatda saqlash imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Daromad va xarajatlarni aniq kuzatish, moliyaviy maqsadlarga erishish va byudjetni muvozanatda saqlash imkonini beradi"},
        {"q": "Nima uchun shaxsiy moliya uchun passiv daromad manbalarini yaratish tavsiya etiladi?", "o": ["Chunki passiv daromad qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Chunki bu bank kreditini olishni kafolatlaydi", "Chunki faqat xarajatlarni oshirish imkoniyatini beradi", "Chunki inflyatsiya kamayadi"], "a": "Chunki passiv daromad qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Agar siz yuqori foizli qarzga ega bo‘lsangiz, bu sizning moliyaviy qarorlaringizga qanday ta’sir qilishi mumkin?", "o": ["Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi", "Xarajatlar kamayadi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi"},
        {"q": "Oylik byudjetni tuzish va xarajatlarni yozib borish qanday asosiy foyda beradi?", "o": ["Xarajatlarni nazorat qilish va moliyaviy maqsadlarga erishish imkonini beradi", "Faqat daromad oshiradi", "Kredit olishni kafolatlaydi", "Soliqni kamaytiradi"], "a": "Xarajatlarni nazorat qilish va moliyaviy maqsadlarga erishish imkonini beradi"},
        {"q": "Nima uchun faqat bir turdagi aktivdan iborat portfel yuqori xavfga ega hisoblanadi?", "o": ["Chunki bitta aktivning qiymati tushsa, butun portfel qiymati sezilarli darajada pasayadi", "Chunki bitta aktiv barqaror daromad beradi", "Chunki diversifikatsiya ortadi", "Chunki bu naqd pul hsoblanadi"], "a": "Chunki bitta aktivning qiymati tushsa, butun portfel qiymati sezilarli darajada pasayadi"},
        {"q": "Nima uchun maqsadlarni aniq va o‘lchab bo‘ladigan qilib belgilash muhim?", "o": ["Chunki bu moliyaviy rejani amalga oshirish rejasi va monitoring qilish imkonini beradi", "Chunki bu faqat kredit olishni osonlashtiradi", "Chunki xarajatlarni oshiradi", "Chunki bank foizini oshiradi"], "a": "Chunki bu moliyaviy rejani amalga oshirish rejasi va monitoring qilish imkonini beradi"},
        {"q": "Xarajatlar daromaddan oshib ketgan bo‘lsa, qanday choralarni ko‘rish mumkin?", "o": ["Xarajatlarni qisqartirish, qo‘shimcha daromad manbalari yaratish, qarzlarni boshqarish", "Xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni qisqartirish, qo‘shimcha daromad manbalari yaratish, qarzlarni boshqarish"},
        {"q": "Qarzlarni konsolidatsiya qilish qanday moliyaviy foyda beradi?", "o": ["Qarzlarni boshqarish osonlashadi, foizni kamaytirish imkoniyati, stress kamayadi", "Daromad oshadi", "Xarajatlar oshadi", "Naqd pul kamayadi"], "a": "Qarzlarni boshqarish osonlashadi, foizni kamaytirish imkoniyati, stress kamayadi"},
        {"q": "Passiv daromad manbalarini yaratish nima uchun shaxsiy moliyaviy barqarorlik uchun foydali?", "o": ["Chunki passiv daromad qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Chunki bu faqat kredit olishni osonlashtiradi", "Chunki xarajatlarni oshirish imkonini beradi", "Chunki foiz stavkasi oshadi"], "a": "Chunki passiv daromad qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun turli aktivlarga sarmoya kiritish (investitsiya) tavsiya etiladi?", "o": ["Chunki turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi", "Chunki faqat qimmatbaho metallar xavfsiz", "Chunki faqat aksiyalar daromad beradi", "Chunki bu naqd pulni ko‘paytiradi"], "a": "Chunki turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi"},
        {"q": "Oylik byudjetni ilova yoki jurnal yordamida nazorat qilish qanday foyda beradi?", "o": ["Daromad va xarajatlarni aniq kuzatish, maqsadlarga erishish va byudjet muvozanati", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Daromad va xarajatlarni aniq kuzatish, maqsadlarga erishish va byudjet muvozanati"},
        {"q": "Xarajatlar daromaddan tez-tez oshib ketganda, moliya nazoratini kuchaytirish uchun nima qilish kerak?", "o": ["Xarajatlarni yozish, byudjet tuzish, maqsadlarni belgilash va passiv daromad yaratish", "Faqat xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni yozish, byudjet tuzish, maqsadlarni belgilash va passiv daromad yaratish"},
        {"q": "Nima uchun faqat bitta turdagi aktivga investitsiya qilish tavsiya etilmaydi?", "o": ["Chunki bitta aktiv qiymati tushsa, butun portfel sezilarli zarar ko‘radi", "Chunki bu naqd pulni oshiradi", "Chunki bu daromadni kafolatlaydi", "Chunki foiz stavkasi pasayadi"], "a": "Chunki bitta aktiv qiymati tushsa, butun portfel sezilarli zarar ko‘radi"},
        {"q": "SMART tamoyili moliyaviy maqsadlarni qanday samarali qiladi?", "o": ["Maqsadlar aniq, o‘lchab bo‘ladigan bo‘ladi va monitoring qilish imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Bank foizini oshiradi"], "a": "Maqsadlar aniq, o‘lchab bo‘ladigan bo‘ladi va monitoring qilish imkonini beradi"},
        {"q": "Qarzlarni birlashtirish (konsolidatsiya) moliyaviy jihatdan qanday foyda beradi?", "o": ["Qarzlarni boshqarish osonlashadi, foiz stavkasi va stress kamayadi", "Daromad oshadi", "Xarajat oshadi", "Naqd pul kamayadi"], "a": "Qarzlarni boshqarish osonlashadi, foiz stavkasi va stress kamayadi"},
        {"q": "Shaxsiy byudjetni tuzishda naqd pul, qarz, investitsiyalar va xarajatlarni birlashtirish nima uchun muhim?", "o": ["Barcha resurslarni nazorat qilish va ongli qaror qabul qilish uchun", "Faqat bank qarzini olish uchun", "Soliqlarni kamaytirish uchun", "Xarajatlarni oshirish uchun"], "a": "Barcha resurslarni nazorat qilish va ongli qaror qabul qilish uchun"},
        {"q": "Nima sababli faqat bir turdagi aktivdan (masalan, aksiyalar) iborat portfel yuqori xavfga ega?", "o": ["Bitta aktiv qiymati tushsa, portfelning umumiy qiymati pasayadi", "Diversifikatsiya ortadi", "Bu naqd pul hsoblanadi", "Bitta aktiv barqaror daromad beradi"], "a": "Bitta aktiv qiymati tushsa, portfelning umumiy qiymati pasayadi"},
        {"q": "Passiv daromad manbalari shaxsiy barqarorlik uchun nima uchun foydali?", "o": ["Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Foiz stavkasi oshadi"], "a": "Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun turli moliyaviy aktivlarga (aksiyalar, obligatsiyalar va h.k.) investitsiya qilish tavsiya etiladi?", "o": ["Xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Faqat aksiyalar daromad beradi", "Naqd pulni ko‘paytiradi"], "a": "Xavfni taqsimlaydi va portfel daromadini barqarorlashtiradi"},
        {"q": "Oylik byudjetni ilova yoki jurnalda nazorat qilish qanday foyda beradi?", "o": ["Aniqlik, maqsadlarga erishish va byudjet muvozanatini saqlash", "Faqat kredit olishni osonlashtirish", "Naqd pulni oshirish", "Soliqni kamaytirish"], "a": "Aniqlik, maqsadlarga erishish va byudjet muvozanatini saqlash"},
        {"q": "Inflyatsiya yuqori bo‘lganda, faqat naqd pul saqlash uzoq muddatda qanday oqibatlarga olib kelishi mumkin?", "o": ["Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati oshadi va xarid qobiliyati ko‘payadi", "Pul qiymati barqaror bo‘ladi", "Barqaror daromad ta’minlanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Shaxsiy moliyaviy barqarorlikni ta’minlash uchun qaysi choralar eng samarali?", "o": ["Xarajatlarni yozib borish, byudjet tuzish, maqsadlarni belgilash, passiv daromad yaratish", "Faqat xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni yozib borish, byudjet tuzish, maqsadlarni belgilash, passiv daromad yaratish"},
        {"q": "Yuqori foizli qarzga ega bo‘lish moliyaviy qarorlaringizga qanday ta’sir qilishi mumkin?", "o": ["Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi", "Xarajatlar kamayadi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi"},
        {"q": "Oylik byudjetni tuzish va xarajatlarni yozib borish moliyaviy savodxonlikka qanday yordam beradi?", "o": ["Xarajatlarni nazorat qilish va maqsadlarga erishish imkonini beradi", "Faqat daromad oshiradi", "Kredit olishni kafolatlaydi", "Soliqni kamaytiradi"], "a": "Xarajatlarni nazorat qilish va maqsadlarga erishish imkonini beradi"},
        {"q": "Investitsiya portfelingizda faqat bir turdagi aktiv (aksiyalar) bo‘lsa, bu qanday xavf tug‘diradi?", "o": ["Bitta aktiv qiymati tushsa, portfelning umumiy qiymati sezilarli pasayadi", "Diversifikatsiya ortadi", "Bu naqd pul hisoblanadi", "Bitta aktiv barqaror daromad beradi"], "a": "Bitta aktiv qiymati tushsa, portfelning umumiy qiymati sezilarli pasayadi"},
        {"q": "Shaxsiy moliyaviy maqsadlarni SMART tamoyili asosida belgilash qanday foyda beradi?", "o": ["Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib,monitoring qilish imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Bank foizini oshiradi"], "a": "Maqsadlar aniq va o‘lchab bo‘ladigan bo‘lib,monitoring qilish imkonini beradi"},
        {"q": "Qarzlarni konsolidatsiya qilish (birlashtirish) qanday foyda keltiradi?", "o": ["Qarzlarni boshqarish osonlashadi, foiz stavkasi va stress kamayadi", "Daromad oshadi", "Xarajatlar oshadi", "Naqd pul kamayadi"], "a": "Qarzlarni boshqarish osonlashadi, foiz stavkasi va stress kamayadi"},
        {"q": "Passiv daromad manbalarini yaratish shaxsiy moliyaviy barqarorlikni qanday oshiradi?", "o": ["Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi", "Faqat kredit olishni osonlashtiradi", "Xarajatlarni oshirish imkonini beradi", "Foiz stavkasi oshadi"], "a": "Qo‘shimcha mablag‘ keltiradi va daromadlarni diversifikatsiya qiladi"},
        {"q": "Nima uchun turli moliyaviy aktivlarga (aksiya, obligatsiya va h.k.) investitsiya qilish tavsiya etiladi?", "o": ["Turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi", "Faqat qimmatbaho metallar xavfsiz", "Faqat aksiyalar daromad beradi", "Bu naqd pulni ko‘paytiradi"], "a": "Turli aktivlar xavfni taqsimlaydi va umumiy portfel daromadini barqarorlashtiradi"},
        {"q": "Oylik byudjetni ilova yoki jurnal yordamida nazorat qilish qanday foyda beradi?", "o": ["Daromad va xarajatlarni aniq kuzatish, maqsadlarga erishish va byudjet muvozanati", "Faqat kredit olishni osonlashtiradi", "Naqd pulni oshiradi", "Soliq stavkasini kamaytiradi"], "a": "Daromad va xarajatlarni aniq kuzatish, maqsadlarga erishish va byudjet muvozanati"},
        {"q": "Nima uchun doimiy va o‘zgaruvchan xarajatlarni alohida hisoblash tavsiya etiladi?", "o": ["Chunki xarajatlarni nazorat qilish va moliyaviy reja tuzish osonlashadi", "Chunki foiz stavkasi oshadi", "Chunki naqd pul kamayadi", "Chunki bank qarzini olish osonlashadi"], "a": "Chunki xarajatlarni nazorat qilish va moliyaviy reja tuzish osonlashadi"},
        {"q": "Nima uchun investitsiya va jamg‘arma yaratish moliyaviy xavfni kamaytiradi?", "o": ["Chunki daromadlarni diversifikatsiya qilish orqali bir manba yo‘qotilganda boshqalar bilan qoplanadi", "Chunki foiz stavkasi oshadi", "Chunki xarajatlarni oshirish mumkin", "Chunki bu naqd pulni oshiradi"], "a": "Chunki daromadlarni diversifikatsiya qilish orqali bir manba yo‘qotilganda boshqalar bilan qoplanadi"},
        {"q": "Nima uchun moliyaviy qaror qabul qilishda daromad, xarajat, qarz va investitsiyalarni hisobga olish muhim?", "o": ["Chunki barcha resurslarni nazorat qilish va ongli qaror qabul qilish imkonini beradi", "Faqat kredit olishni osonlashtiradi", "Faqat xarajatlarni oshiradi", "Faqat soliqni kamaytiradi"], "a": "Chunki barcha resurslarni nazorat qilish va ongli qaror qabul qilish imkonini beradi"},
        {"q": "Oylik byudjetda xarajatlar daromaddan oshib ketgan bo‘lsa, bu qanday moliyaviy xavf tug‘diradi?", "o": ["Qarzga bog‘lanish, jamg‘arma kamayishi va moliyaviy stress yuzaga keladi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi", "Bank depoziti ko‘payadi"], "a": "Qarzga bog‘lanish, jamg‘arma kamayishi va moliyaviy stress yuzaga keladi"},
        {"q": "Shaxsiy investitsiya portfelingizda faqat bitta turdagi aktiv (masalan, obligatsiyalar) bo‘lsa, bu qanday xavf tug‘diradi?", "o": ["Bitta aktiv qiymati tushsa, umumiy portfel daromadi pasayadi", "Diversifikatsiya oshadi", "Naqd pul ko‘payadi", "Xarajatlar kamayadi"], "a": "Bitta aktiv qiymati tushsa, umumiy portfel daromadi pasayadi"},
        {"q": "Passiv daromad manbalarini yaratish qanday qilib shaxsiy moliyayiy erkinlikni oshiradi?", "o": ["Qo‘shimcha daromad ta’minlaydi va moliyaviy qarorlarni mustaqil qabul qilish imkonini beradi", "Faqat kredit olish imkonini beradi", "Xarajatlarni oshirish imkonini beradi", "Naqd pulni kamaytiradi"], "a": "Qo‘shimcha daromad ta’minlaydi va moliyaviy qarorlarni mustaqil qabul qilish imkonini beradi"},
        {"q": "Shaxsiy moliyaviy maqsadlarni belgilashda aniq muddat va o‘lchovlarni belgilash qanday foyda beradi?", "o": ["Maqsadga erishish jarayoni monitoring qilinadi va reja bo‘yicha harakat qilish osonlashadi", "Faqat kredit olish osonlashadi", "Xarajatlarni oshirish imkoniyati paydo bo‘ladi", "Inflyatsiyani kamaytiradi"], "a": "Maqsadga erishish jarayoni monitoring qilinadi va reja bo‘yicha harakat qilish osonlashadi"},
        {"q": "Qarzlarni boshqarishda foiz stavkasi va to‘lov muddatlarini hisobga olish nega muhim?", "o": ["Chunki foiz xarajatlari va byudjet muvozanati shu parametrlar bilan belgilanadi", "Faqat kredit olishni osonlashtiradi", "Daromad oshadi", "Naqd pul ko‘payadi"], "a": "Chunki foiz xarajatlari va byudjet muvozanati shu parametrlar bilan belgilanadi"},
        {"q": "Turli moliyaviy aktivlarga investitsiya qilish orqali siz portfelingizni diversifikatsiya qilasiz. Nima sababdan bu moliyaviy xavfni kamaytiradi?", "o": ["Chunki bitta aktivning yo‘qotilishi boshqa aktivlar bilan qoplanadi", "Chunki barcha aktivlar bir xil daromad beradi", "Chunki bu naqd pulni oshiradi", "Chunki xarajatlar kamayadi"], "a": "Chunki bitta aktivning yo‘qotilishi boshqa aktivlar bilan qoplanadi"}
    ]

# 141-210 bloki
if 'ms_141_210' not in st.session_state:
    st.session_state.ms_141_210 = [
        {"q": "Moliyaviy savodxonlikni oshirishda eng muhim qadamlar qaysilar?", "o": ["Byudjet tuzish, xarajat va daromadni nazorat qilish, qarzlarni boshqarish, investitsiya va passiv daromad yaratish", "Xarajatlarni oshirish va qarz olish", "Faqat bank depozitini oshirish", "Soliqdan qochish"], "a": "Byudjet tuzish, xarajat va daromadni nazorat qilish, qarzlarni boshqarish, investitsiya va passiv daromad yaratish"},
        {"q": "Sizning oylik daromadingiz barqaror, lekin xarajatlaringiz ko‘pincha oshib ketadi. Shaxsiy moliyaviy barqarorlikni ta’minlash uchun qanday choralar eng samarali hisoblanadi?", "o": ["Xarajatlarni yozib borish, byudjet tuzish, moliyaviy maqsadlarni belgilash, passiv daromad manbalarini yaratish", "Faqat xarajatlarni oshirish", "Bank depozitini kamaytirish", "Moliyaviy rejani bekor qilish"], "a": "Xarajatlarni yozib borish, byudjet tuzish, moliyaviy maqsadlarni belgilash, passiv daromad manbalarini yaratish"},
        {"q": "Inflyatsiya yuqori bo‘lganda, naqd pul saqlash uzoq muddatda qanday oqibatlarga olib kelishi mumkin?", "o": ["Pulning qiymati pasayadi va xarid qobiliyati kamayadi", "Pul qiymati oshadi va xarid qobiliyati ko‘payadi", "Pul qiymati barqaror bo‘ladi", "Barqaror daromad ta’minlanadi"], "a": "Pulning qiymati pasayadi va xarid qobiliyati kamayadi"},
        {"q": "Shaxsiy moliyaviy reja tuzishda qarz va foizlarni hisobga olish zarur. Agar siz yuqori foizli qarzga ega bo‘lsangiz, bu sizning byudjetingizga qanday ta’sir qilishi mumkin?", "o": ["Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi, byudjet qiyinlashadi", "Xarajatlar kamayadi", "Daromad oshadi", "Moliyaviy barqarorlik oshadi"], "a": "Foiz xarajatlari ko‘payadi va daromadning bir qismi qarz to‘lashga ketadi, byudjet qiyinlashadi"},
        {"q": "Shaxsiy investitsiya portfelingiz faqat bitta turdagi aktivdan iborat bo‘lsa, masalan, faqat aksiyalar, bu qanday xavf tug‘diradi?", "o": ["Bitta aktivning qiymati tushsa, portfelning umumiy qiymati sezilarli darajada pasayadi", "Diversifikatsiya ortadi", "Bu naqd pul hisoblanadi", "Bitta aktiv barqaror daromad beradi"], "a": "Bitta aktivning qiymati tushsa, portfelning umumiy qiymati sezilarli darajada pasayadi"}
    ]

# 4. Holatlarni boshqarish
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'test_started' not in st.session_state: st.session_state.test_started = False
if 'current_q_index' not in st.session_state: st.session_state.current_q_index = 0
if 'user_score' not in st.session_state: st.session_state.user_score = 0
if 'answered' not in st.session_state: st.session_state.answered = False
if 'selected_option' not in st.session_state: st.session_state.selected_option = None

# --- KIRISH ---
if not st.session_state.logged_in:
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.title("🎯 Kirish")
    
    # 1. Foydalanuvchilar bazasi (Xohlagancha qo'shishingiz mumkin)
    users = {
        "Murat": "12062006",
        "nilufar": "0455"
    }
    
    u_login = st.text_input("Foydalanuvchi nomi (Login):")
    u_pass = st.text_input("Parol:", type="password")
    
    if st.button("KIRISH"):
        # 2. Lug'atdan tekshirish
        if u_login in users and users[u_login] == u_pass:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Login yoki parol xato!")
            
    st.markdown('</div>', unsafe_allow_html=True)
# --- MENYU ---
else:
    if not st.session_state.test_started:
        st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
        st.title("🚀 Bo'limni tanlang")
        blok = st.radio("Blok:", ["1-70", "71-140", "141-210", "211-300"])
        
        if st.button("🚀 BOSHLA"):
            # Tanlangan blokni nusxalab olish (asli o'zgarmasligi uchun)
            if blok == "1-70":
                questions = list(st.session_state.ms_1_70)
            elif blok == "71-140":
                questions = list(st.session_state.ms_71_140)
            elif blok == "141-210":
                questions = list(st.session_state.ms_141_210)
            
            # 1. Savollar tartibini aralashtirish
            random.shuffle(questions)
            
            # 2. Har bir savol ichidagi variantlarni ham aralashtirish
            for q in questions:
                random.shuffle(q['o'])
                
            st.session_state.active_questions = questions
            st.session_state.test_started = True
            st.rerun()
   # --- TEST JARAYONI ---
    else:
        q_idx = st.session_state.current_q_index
        questions = st.session_state.active_questions
        
        # 1. Test davom etayotgan bo'lsa (Savollarni ko'rsatish)
        if q_idx < len(questions):
            curr = questions[q_idx]
            st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
            st.markdown(f"<h3>Savol {q_idx + 1}/{len(questions)}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 18px; font-weight: bold;'>{curr['q']}</p>", unsafe_allow_html=True)

            # Savolga hali javob berilmagan bo'lsa
            if not st.session_state.answered:
                ans = st.radio("Variantlar:", curr['o'], index=None, key=f"q_{q_idx}", label_visibility="collapsed")
                if st.button("TASDIQLASH"):
                    if ans:
                        st.session_state.answered = True
                        st.session_state.selected_option = ans
                        if ans == curr['a']: 
                            st.session_state.user_score += 1
                        st.rerun()
                    else:
                        st.warning("Iltimos, variantni tanlang!")
            
            # Savolga javob berilgan bo'lsa (Natijani ko'rsatish)
            else:
                for opt in curr['o']:
                    if opt == curr['a']:
                        st.success(f"To'g'ri javob: {opt} ✔️")
                    elif opt == st.session_state.selected_option:
                        st.error(f"Sizning javobingiz: {opt} ❌")
                    else:
                        st.write(opt)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Keyingi ➔"):
                        st.session_state.current_q_index += 1
                        st.session_state.answered = False
                        st.session_state.selected_option = None
                        st.rerun()
                with col2:
                    if st.button("🏠 MENU"):
                        st.session_state.test_started = False
                        st.session_state.current_q_index = 0
                        st.session_state.user_score = 0
                        st.session_state.answered = False
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # 2. Hamma savollar tugagan bo'lsa (Yakuniy natija)
        else:
            st.markdown('<div class="quiz-card" style="text-align: center;">', unsafe_allow_html=True)
            st.balloons()
            st.markdown("<h2>Test yakunlandi!</h2>", unsafe_allow_html=True)
            st.markdown(f"<h1>{st.session_state.user_score} / {len(questions)}</h1>", unsafe_allow_html=True)
            if st.button("🏠 ASOSIY MENYUGA QAYTISH"):
                st.session_state.test_started = False
                st.session_state.current_q_index = 0
                st.session_state.user_score = 0
                st.session_state.answered = False
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
