# ─────────────────────────────────────────────────────────────────────────────
# AIHealthCare — Chatbot Engine
# Hindi + English + Hinglish full support
# Smart partial matching — sentences bhi samajhta hai
# ─────────────────────────────────────────────────────────────────────────────

# ── HINDI → ENGLISH keyword map ──────────────────────────────────────────────
HINDI_MAP = {
    # Fever
    "bukhar": "fever", "bukhaar": "fever", "tez bukhar": "fever",
    "body hot": "fever", "garmi": "fever", "temperature": "fever",
    # Cough
    "khansi": "cough", "khaansi": "cough", "khasi": "cough",
    "dry khansi": "dry cough", "balgam": "phlegm", "kaph": "phlegm",
    # Cold/Nose
    "sardi": "cold", "jukam": "cold", "nazla": "runny nose",
    "naak beh": "runny nose", "naak band": "congestion",
    "chheenk": "sneezing", "chheenkna": "sneezing",
    # Head
    "sir dard": "headache", "sar dard": "headache", "matha dard": "headache",
    "sir mein dard": "headache", "chakkar": "dizziness",
    "chakkar aa": "dizziness", "sir bhaari": "headache",
    # Throat
    "gala dard": "sore throat", "gale mein dard": "sore throat",
    "gala kharab": "sore throat", "nigalne mein": "sore throat",
    # Stomach
    "pet dard": "stomach pain", "pait dard": "stomach pain",
    "pet mein dard": "stomach pain", "pet mein jalan": "acidity",
    "ulti": "vomiting", "ultiyaan": "vomiting", "jee machlana": "nausea",
    "jee ghabrana": "nausea", "dast": "diarrhea", "loose motion": "diarrhea",
    "pechish": "diarrhea", "kabz": "constipation", "qabz": "constipation",
    "acidity": "acidity", "khatta dakar": "acidity",
    "seene mein jalan": "heartburn",
    # Body
    "thakan": "fatigue", "kamzori": "weakness", "kamzoori": "weakness",
    "badan dard": "body ache", "body ache": "body ache",
    "jodo mein dard": "joint pain", "jodo ka dard": "joint pain",
    "kamar dard": "back pain", "kamar mein dard": "back pain",
    "peeth dard": "back pain", "gardan dard": "neck pain",
    # Breathing
    "saans phoolna": "breathlessness", "saans lene mein": "breathlessness",
    "ghuttan": "breathlessness", "seene mein dard": "chest pain",
    "seena dard": "chest pain",
    # Skin
    "kharish": "itching", "khujli": "itching",
    "daane": "rash", "laal daane": "rash", "allergy": "allergy",
    # Mental
    "anxiety": "anxiety", "anxious": "anxiety",
    "stress": "stress", "tension": "stress", "ghabrahat": "anxiety",
    "depression": "depression", "udaas": "depression",
    "neend nahi": "insomnia", "neend nahi aati": "insomnia",
    "so nahi pa": "insomnia", "raat ko neend": "insomnia",
    "ghabrana": "anxiety", "darr": "anxiety", "panic": "anxiety",
    # Urinary
    "peshab mein jalan": "uti", "peshab jalan": "uti",
    "baar baar peshab": "frequent urination",
    # Eye
    "aankhein laal": "eye infection", "aankh laal": "eye infection",
    "aankhon mein jalan": "eye irritation",
    # Tooth
    "dant dard": "toothache", "daant dard": "toothache",
    # Period
    "periods mein dard": "period pain", "mc dard": "period pain",
    "mahine ka dard": "period pain",
    # General
    "sugar": "diabetes", "madhumeh": "diabetes",
    "bp high": "hypertension", "blood pressure": "hypertension",
    "upay batao": "advice", "kya karun": "advice",
    "kya khana chahiye": "diet", "diet": "diet",
}

# ── DISEASE DATABASE ──────────────────────────────────────────────────────────
DISEASE_DB = {
    "flu": {
        "keywords": ["fever", "cough", "fatigue", "headache", "body ache", "chills",
                     "flu", "influenza", "bukhar", "khansi", "thakan", "badan"],
        "remedies": [
            "🫖 Adrak + tulsi + shahad ka kadha din mein 3 baar piyo",
            "💧 Garam pani zyada piyo — 8-10 glass daily",
            "🌬️ Steam lo — naak band ho toh relief milega",
            "😴 Complete bed rest karo",
            "🍲 Garam soup ya khichdi khao",
        ],
        "medicines": ["Paracetamol 500mg", "Crocin", "Vicks VapoRub"],
        "doctor": "General Physician",
        "severity": "LOW",
        "advice": "Ghabrao mat! 3-5 din mein theek ho jaoge. Bahar mat jao."
    },
    "common cold": {
        "keywords": ["runny nose", "sneezing", "sore throat", "congestion", "cold",
                     "sardi", "jukam", "nazla", "naak", "gala", "chheenk"],
        "remedies": [
            "🧂 Garam namak pani se din mein 4 baar gargle karo",
            "🍋 Shahad + adrak + nimbu garam pani mein piyo",
            "🌬️ Steam lo 10 minute — naak khul jayegi",
            "🍜 Garam soup piyo",
            "🧄 Kachcha lehsun khao — 2 kali",
        ],
        "medicines": ["Cetirizine", "Sinarest", "Vicks VapoRub"],
        "doctor": "General Physician",
        "severity": "LOW",
        "advice": "5-7 din mein theek ho jaoge. Thanda bilkul mat lo."
    },
    "headache": {
        "keywords": ["headache", "head pain", "migraine", "sir dard", "sar dard",
                     "matha", "head", "sir", "chakkar", "dizziness"],
        "remedies": [
            "💆 Nariyal tel ya sarso tel se sar ki maalish karo",
            "🧊 Mathe pe thanda kapda rakho",
            "🍵 Adrak wali chai piyo",
            "💧 Pani piyo — dehydration se sir dard hota hai",
            "😴 Andheri kamre mein lete jao — aankhen band karo",
        ],
        "medicines": ["Paracetamol 500mg", "Saridon", "Aspirin"],
        "doctor": "Neurologist (baar baar ho toh)",
        "severity": "LOW",
        "advice": "Screen time kam karo. Pani piyo. Neend puri lo."
    },
    "anxiety": {
        "keywords": ["anxiety", "stress", "tension", "ghabrahat", "panic", "darr",
                     "anxious", "worried", "ghabrana", "nervous", "depression",
                     "udaas", "anxiety", "mental", "upay", "kam karne"],
        "remedies": [
            "🧘 Roz 10 minute deep breathing karo — 4 secs in, 4 secs out",
            "📵 Sone se 1 ghante pehle phone band karo",
            "🏃 Rozana exercise karo — body ka natural stress reliever",
            "👥 Kisi dost ya family se baat karo",
            "📔 Apni feelings journal mein likho",
            "🎵 Soothing music suno",
        ],
        "medicines": ["Ashwagandha supplement", "Doctor se baat karo"],
        "doctor": "Psychiatrist / Psychologist",
        "severity": "MEDIUM",
        "advice": "Akele mat raho! Kisi se baat karo. Help maangna strength hai 💚"
    },
    "stress": {
        "keywords": ["stress", "tension", "pressure", "takleef", "pareshan",
                     "chinta", "worry", "anxious", "mental stress", "kam karne ke upay"],
        "remedies": [
            "🧘 Roz subah 10 minute meditation karo",
            "🏃 Walk pe jao — nature mein raho",
            "😴 7-8 ghante ki neend lo",
            "📵 Social media time limit karo",
            "🫂 Apne close friends se baat karo",
            "☕ Caffeine kam karo — chai/coffee",
        ],
        "medicines": ["Ashwagandha", "Doctor se guidance lo"],
        "doctor": "Psychiatrist / Counselor",
        "severity": "LOW",
        "advice": "Stress normal hai — but ignore mat karo. Roz thodi exercise zaroor karo."
    },
    "insomnia": {
        "keywords": ["insomnia", "sleeplessness", "neend nahi", "so nahi pa",
                     "raat ko neend", "neend nahi aati", "sleep problem"],
        "remedies": [
            "📵 Sone se 1 ghante pehle phone/TV band karo",
            "🥛 Garam doodh mein haldi mila ke piyo — raat ko",
            "🧘 Sone se pehle deep breathing karo",
            "⏰ Roz ek hi time par so — routine banao",
            "🌙 Kamra andhera aur thanda rakho",
        ],
        "medicines": ["Melatonin 3mg", "Ashwagandha — doctor se"],
        "doctor": "Psychiatrist / Sleep Specialist",
        "severity": "LOW",
        "advice": "Coffee/chai 3 baje ke baad mat lo. Exercise karo — raat ko neend aayegi."
    },
    "stomach pain": {
        "keywords": ["stomach pain", "stomach ache", "abdominal pain", "belly pain",
                     "pet dard", "pait dard", "pet mein dard", "stomach"],
        "remedies": [
            "🌿 Ajwain + namak garam pani ke saath lo",
            "🫚 Hing (asafoetida) garam pani mein piyo",
            "🍵 Saunf ki chai piyo",
            "💊 Digene ya Gelusil lo — acidity hai toh",
            "🛏️ Left side lete jao — gas relief hogi",
        ],
        "medicines": ["Pantoprazole", "Digene", "Gelusil", "Drotin"],
        "doctor": "Gastroenterologist",
        "severity": "MEDIUM",
        "advice": "Masaledar khana avoid karo. Zyada pani piyo. 2 din mein theek na ho toh doctor jao."
    },
    "acidity": {
        "keywords": ["acidity", "heartburn", "acid reflux", "khatta dakar",
                     "seene mein jalan", "pet mein jalan", "gas", "bloating"],
        "remedies": [
            "🥛 Thanda doodh piyo — turant relief milega",
            "🌿 Saunf khao khaane ke baad",
            "🍌 Kela khao — natural antacid hai",
            "🚫 Masaledar, fried khaana avoid karo",
            "⏰ Raat ko sone se 2 ghante pehle khana khao",
        ],
        "medicines": ["Pantoprazole", "Eno", "Gelusil", "Digene"],
        "doctor": "Gastroenterologist (baar baar ho toh)",
        "severity": "LOW",
        "advice": "Khana khaate waqt paani mat piyo. Chhote chhote meals lo."
    },
    "diarrhea": {
        "keywords": ["diarrhea", "loose motion", "loose stool", "watery stool",
                     "dast", "pechish", "bar bar bathroom", "loose"],
        "remedies": [
            "💧 ORS piyo har 15 minute baad — dehydration se bacho",
            "🍚 Chawal ka maad piyo",
            "🍌 Kela khao",
            "🥣 Khichdi aur dahi khao",
            "🚫 Doodh, fried, masaledar bilkul nahi",
        ],
        "medicines": ["ORS / Electral", "Loperamide", "Metronidazole — doctor se"],
        "doctor": "General Physician",
        "severity": "MEDIUM",
        "advice": "Blood aaye ya 24 ghante se zyada ho toh ZAROOR doctor jao!"
    },
    "vomiting": {
        "keywords": ["vomiting", "nausea", "ulti", "ubal aana", "jee machlana",
                     "throwing up", "vomit", "jee ghabrana"],
        "remedies": [
            "🌿 Adrak ka ras piyo — ulti rokta hai",
            "🍋 Nimbu + namak + pani piyo slowly",
            "💧 Chhote chhote ghoonth mein pani piyo",
            "🚫 6 ghante kuch solid mat khao",
            "🛏️ Seedhe lete raho — uthna mat turant",
        ],
        "medicines": ["Domperidone", "Ondansetron", "ORS"],
        "doctor": "General Physician",
        "severity": "MEDIUM",
        "advice": "Dehydration se bacho — ORS zaroor piyo."
    },
    "back pain": {
        "keywords": ["back pain", "lower back", "spine", "kamar dard", "kamar mein dard",
                     "peeth dard", "back ache", "kamar", "back"],
        "remedies": [
            "🌡️ Garam compress lagao — 15-20 minute",
            "🧘 Seedhe baitho — jhukke mat baitho",
            "💆 Sarso tel se garam maalish karo",
            "🚶 Halki walking karo — complete rest nahi",
            "🛏️ Sakht surface pe soo",
        ],
        "medicines": ["Ibuprofen", "Combiflam", "Volini gel"],
        "doctor": "Orthopedic / Spine Specialist",
        "severity": "MEDIUM",
        "advice": "1 hafte se zyada rahe ya pair mein jaaye toh doctor zaroor jao."
    },
    "joint pain": {
        "keywords": ["joint pain", "arthritis", "knee pain", "jodo mein dard",
                     "jodo ka dard", "ghutne", "joint", "gathiya"],
        "remedies": [
            "🌡️ Haldi wala doodh piyo — din mein 2 baar",
            "💆 Sarso tel se garam maalish karo",
            "🐟 Omega-3 wali cheezein khao — akhrot, fish",
            "⚖️ Vajan kam karo — joints pe load kam hoga",
        ],
        "medicines": ["Ibuprofen", "Diclofenac gel", "Calcium + Vitamin D"],
        "doctor": "Orthopedic / Rheumatologist",
        "severity": "MEDIUM",
        "advice": "Haldi + doodh roz piyo. Thanda paani aur AC se door raho."
    },
    "skin allergy": {
        "keywords": ["itching", "rash", "hives", "allergy", "kharish", "khujli",
                     "daane", "laal daane", "skin", "allergic"],
        "remedies": [
            "🧊 Ice pack lagao prabhavit jagah pe",
            "🌿 Neem ke patte ubaalke us pani se nahao",
            "🍯 Aloe vera gel lagao",
            "🧴 Calamine lotion lagao",
            "🚫 Triggering food/soap avoid karo",
        ],
        "medicines": ["Cetirizine", "Benadryl", "Hydrocortisone cream"],
        "doctor": "Dermatologist",
        "severity": "LOW",
        "advice": "Chehra/honth soojna ho ya saans mein takleef ho toh TURANT hospital!"
    },
    "dengue": {
        "keywords": ["dengue", "high fever", "rash", "joint pain", "platelet",
                     "mosquito", "eye pain"],
        "remedies": [
            "🍃 Papaya leaf juice piyo — platelet badhata hai",
            "💧 ORS aur coconut water piyo",
            "😴 Complete rest karo",
            "❌ Aspirin bilkul mat lo",
        ],
        "medicines": ["Paracetamol ONLY", "ORS", "Papaya leaf extract"],
        "doctor": "General Physician — Platelet Count ZAROOR",
        "severity": "HIGH",
        "advice": "🚨 SERIOUS! Turant hospital jao. Platelet count check karwao!"
    },
    "malaria": {
        "keywords": ["malaria", "chills", "sweating", "kaanpna", "pasina"],
        "remedies": [
            "💧 Bahut zyada pani aur ORS piyo",
            "🌿 Neem ki patti ka juice piyo",
            "😴 Complete bed rest",
        ],
        "medicines": ["Paracetamol", "ORS — doctor se malaria medicine"],
        "doctor": "General Physician — Blood Test ZAROOR",
        "severity": "HIGH",
        "advice": "🚨 SERIOUS! Blood test karwao aur doctor ke paas jao aaj hi!"
    },
    "covid": {
        "keywords": ["covid", "corona", "loss of smell", "loss of taste",
                     "smell nahi", "taste nahi", "breathlessness"],
        "remedies": [
            "🏠 Turant isolate ho jao",
            "🌬️ Steam inhalation karo din mein 3 baar",
            "🫖 Kadha piyo — tulsi, adrak, kali mirch",
            "📊 Oxygen level check karo",
        ],
        "medicines": ["Paracetamol", "Vitamin C 1000mg", "Zinc tablets"],
        "doctor": "General Physician / COVID Center",
        "severity": "HIGH",
        "advice": "🚨 Test karwao! Oxygen 94% se kam ho toh TURANT hospital!"
    },
    "diabetes": {
        "keywords": ["diabetes", "sugar", "blood sugar", "madhumeh",
                     "zyada pyaas", "baar baar peshab", "sugar ki bimari"],
        "remedies": [
            "🥗 Kam GI wala khaana — green sabzi, daal",
            "🚫 Meetha, maida, white rice band karo",
            "🏃 Rozana 30 minute walk ZAROOR karo",
            "🌿 Karele ka juice piyo — blood sugar kam karta hai",
        ],
        "medicines": ["Doctor ke bina mat lo — prescription chahiye"],
        "doctor": "Endocrinologist / Diabetologist",
        "severity": "HIGH",
        "advice": "🚨 Sugar monitor karo rozana. Doctor se regular checkup!"
    },
    "hypertension": {
        "keywords": ["hypertension", "blood pressure", "bp high", "bp", "high bp",
                     "uchha bp", "pressure"],
        "remedies": [
            "🧘 Rozana yoga aur deep breathing",
            "🚫 Namak bilkul kam karo",
            "🏃 Rozana 30 minute walk",
            "🍌 Kela khao — potassium BP kam karta hai",
        ],
        "medicines": ["Doctor ke bina mat lo — prescription chahiye"],
        "doctor": "Cardiologist / General Physician",
        "severity": "HIGH",
        "advice": "🚨 BP 140/90 se upar ho toh ZAROOR doctor jao!"
    },
    "uti": {
        "keywords": ["uti", "urine infection", "peshab mein jalan", "peshab jalan",
                     "burning urination", "frequent urination"],
        "remedies": [
            "💧 Bahut zyada pani piyo — 12-15 glass rozana",
            "🍹 Cranberry juice piyo",
            "🚫 Spicy khaana nahi",
            "🧼 Hygiene maintain karo",
        ],
        "medicines": ["Nitrofurantoin — DOCTOR SE", "Cranberry supplements"],
        "doctor": "General Physician / Urologist",
        "severity": "MEDIUM",
        "advice": "Antibiotic pura karo — adha chhodna nahi!"
    },
    "period pain": {
        "keywords": ["period pain", "periods mein dard", "mc dard", "menstrual",
                     "mahine ka dard", "periods", "period"],
        "remedies": [
            "🌡️ Pet pe garam compress lagao",
            "🫖 Adrak wali chai piyo — 2-3 baar",
            "🧘 Light stretching aur yoga karo",
            "🚫 Thanda pani bilkul nahi",
        ],
        "medicines": ["Meftal Spas", "Ibuprofen", "Buscopan"],
        "doctor": "Gynecologist (bahut zyada dard ho toh)",
        "severity": "LOW",
        "advice": "Warm water peena jari rakho. Rest karo."
    },
    "toothache": {
        "keywords": ["toothache", "tooth pain", "dant dard", "daant dard",
                     "tooth", "dant", "daant", "dental"],
        "remedies": [
            "🧂 Garam namak wale paani se kulle karo",
            "🌿 Laung (clove) daant pe rakho",
            "🧊 Bahar se ice pack lagao",
        ],
        "medicines": ["Ibuprofen 400mg", "Clove oil", "Sensodyne"],
        "doctor": "Dentist — jaldi jao!",
        "severity": "MEDIUM",
        "advice": "Pain killers sirf temporary hain — Dentist ke paas ZAROOR jao!"
    },
    "asthma": {
        "keywords": ["asthma", "breathlessness", "wheezing", "saans phoolna",
                     "ghuttan", "chest tightness", "inhaler"],
        "remedies": [
            "💨 Inhaler TURANT use karo",
            "🪑 Seedha baitho — kabhi lito mat attack mein",
            "🚭 Dhool, dhuaan se door raho",
        ],
        "medicines": ["Salbutamol Inhaler", "Montelukast — doctor se"],
        "doctor": "Pulmonologist / Chest Specialist",
        "severity": "HIGH",
        "advice": "🚨 Inhaler kaam na kare toh TURANT 108 call karo!"
    },
}

# ── GREETINGS ─────────────────────────────────────────────────────────────────
GREETINGS = ["namaste", "hello", "hi", "hey", "helo", "namaskar",
             "good morning", "good evening", "hii", "haai", "namasthe"]

GENERAL_RESPONSES = {
    "doctor": "👨‍⚕️ Doctor dhundhne ke liye /appointments pe jao!",
    "appointment": "📅 Appointment book karne ke liye /appointments pe jao!",
    "medicine": "💊 Medicines ke liye /medicines pe jao!",
    "help": "💡 Mujhe apne symptoms batao — 'mujhe bukhar hai aur khansi ho rahi hai'",
    "emergency": "🚨 Emergency hai? Turant 108 call karo!",
    "thanks": "🙏 Apna khayal rakho! Koi bhi sawaal ho toh poochho!",
    "shukriya": "🙏 Khyal rakhna! Sehat theek rakho!",
    "diet": "🥗 Healthy diet ke liye — subah khali pet paani piyo, fruits khao, junk food avoid karo!",
    "exercise": "🏃 Rozana 30 minute walk ya exercise karo — bahut fayda hoga!",
}


# ── MAIN FUNCTIONS ────────────────────────────────────────────────────────────

def normalize(text):
    """Convert Hindi/Hinglish words to English for matching."""
    text = text.lower().strip()
    for hindi_word, english_word in HINDI_MAP.items():
        text = text.replace(hindi_word, english_word)
    return text


def is_greeting(text):
    t = text.lower().strip()
    words = t.split()
    # Word boundary check - hi should not match nahi
    return any(g in words or t == g for g in GREETINGS) and len(words) <= 4


def get_general_response(text):
    t = text.lower()
    for key, response in GENERAL_RESPONSES.items():
        if key in t:
            return response
    return None


def match_disease(user_input):
    """Smart matching — works with sentences, Hindi, and partial words."""
    normalized = normalize(user_input)
    original = user_input.lower()
    combined = normalized + " " + original

    scores = {}
    for disease, data in DISEASE_DB.items():
        matches = 0
        for kw in data["keywords"]:
            # Check both normalized and original
            if kw in combined:
                matches += 1
            # Partial word match — "sir" matches "sir dard"
            elif any(kw in word or word in kw for word in combined.split()):
                matches += 0.5

        if matches > 0:
            score = round((matches / len(data["keywords"])) * 100, 1)
            scores[disease] = score

    if not scores:
        return None, 0

    best = max(scores, key=scores.get)
    return best, scores[best]


def get_response(user_input):
    """Main function — returns structured response dict."""
    user_input = user_input.strip()

    # ── Greeting ──────────────────────────────────────────────────────────────
    if is_greeting(user_input):
        return {
            "status": "greeting",
            "message": (
                "Namaste! 🙏 Main **Dr. AI** hoon — aapka 24/7 health assistant!\n\n"
                "Mujhe apne **symptoms** batao — main diagnosis karunga.\n\n"
                "Jaise:\n"
                "• _'Mujhe 2 din se bukhar hai aur khansi ho rahi hai'_\n"
                "• _'Pet mein dard aur ulti aa rahi hai'_\n"
                "• _'Sir dard ho raha hai'_\n"
                "• _'Anxiety aur stress bahut ho raha hai'_\n\n"
                "Hindi, English ya Hinglish — koi bhi bolsakte ho! 💚"
            ),
            "symptoms": [], "disease": None, "remedies": [],
            "medicines": [], "severity": "LOW", "advice": "", "doctor": "",
        }

    # ── Disease matching FIRST ───────────────────────────────────────────────
    disease, confidence = match_disease(user_input)

    # ── General question — only if no disease matched ────────────────────────
    if not disease or confidence < 5:
        gen = get_general_response(user_input)
        if gen:
            return {
                "status": "general",
                "message": gen,
                "symptoms": [], "disease": None, "remedies": [],
                "medicines": [], "severity": "LOW", "advice": "", "doctor": "",
            }

    if not disease or confidence < 5:
        return {
            "status": "unknown",
            "message": (
                "Mujhe aapki problem samajh aane mein thodi mushkil aayi 🤔\n\n"
                "Thoda aur detail mein batao:\n"
                "• **'Mujhe 2 din se bukhar hai aur khansi ho rahi hai'**\n"
                "• **'Pet mein dard aur ulti aa rahi hai'**\n"
                "• **'Anxiety aur stress bahut ho raha hai'**\n\n"
                "Ya neeche quick buttons use karo! 👇"
            ),
            "symptoms": [], "disease": None, "remedies": [],
            "medicines": [], "severity": "LOW", "advice": "", "doctor": "",
        }

    data = DISEASE_DB[disease]
    return {
        "status": "found",
        "message": (
            f"Aapke symptoms sun ke lagta hai yeh **{disease.title()}** ho sakta hai 🩺\n"
            f"(Confidence: {confidence:.0f}%)"
        ),
        "symptoms": [],
        "disease": disease.title(),
        "remedies": data["remedies"],
        "medicines": data["medicines"],
        "severity": data["severity"],
        "advice": data["advice"],
        "doctor": data.get("doctor", "General Physician"),
    }