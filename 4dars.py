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
    
    # 1. Foydalanuvchilar bazasi (Siz ko'rsatgan variantda, o'zgarishsiz)
    users = {
        "Murat": "12062006",
        "Nilufar": "Nilufar0455",
        "Radjabboyeva_m": "12345678",
        "Minjiq_qiz": "Minjiq_qiz1234",
        "Lola": "Lola0504",
        "341241101229": "Oydin005",
        "Sultanovamarufa": "02112006Sm",
        "Shahriyor": "Poxxuy",
        "Ixtiyor": "200606",
        "Xudayberganovaf": "Farangiz0616",
        "Urunbayevasevinch": "Sevinch07042005",
        "Abdullayev": "Kamol05",
        "Ixlos": "Ixlos05",
        "Gulsanam": "2810xaydarova",
        "Samandarov": "Shoxrux06",
        "Xudayberganova": "Sevinch"
    }
    
    u_login = st.text_input("Foydalanuvchi nomi (Login):")
    u_pass = st.text_input("Parol:", type="password")
    
    if st.button("KIRISH"):
        # 2. To'g'ridan-to'g'ri lug'atdan tekshirish (Hech qanday o'zgartirishlarsiz)
        if u_login in users and users[u_login] == u_pass:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Login yoki parol xato!")

    # Muallif ma'lumotlari
    st.markdown("""
        <div style="text-align: center; margin-top: 20px; border-top: 1px solid #ddd; padding-top: 10px;">
            <p style="margin: 0; font-size: 14px; color: #666;">Yaratuvchi : <b>Murat Sultanov</b></p>
            <p style="margin: 0; font-size: 14px; color: #666;">Murojat uchun : <b>@murat_sultanov</b></p>
        </div>
    """, unsafe_allow_html=True)
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
