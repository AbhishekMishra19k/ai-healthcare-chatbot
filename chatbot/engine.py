symptom_db = {
    "flu": {
        "symptoms": ["fever", "cough", "fatigue", "headache", "body ache", "chills"],
        "remedies": [
            "Ginger tea piyo din mein 3 baar",
            "Tulsi + honey + ginger ka kadha piyo",
            "Steam lo — naak band ho toh relief milega",
            "Paracetamol 500mg lo fever ke liye",
        ],
        "medicines": ["Paracetamol", "Crocin", "Vicks"],
        "severity": "LOW",
        "advice": "Rest karo, pani zyada piyo. 3 din mein theek ho jaoge."
    },
    "covid-19": {
        "symptoms": ["fever", "cough", "loss of smell", "loss of taste", "breathlessness", "fatigue"],
        "remedies": [
            "Turant isolate ho jao",
            "Steam inhalation karo",
            "Kadha piyo — tulsi, ginger, black pepper",
            "Oxygen level check karte raho",
        ],
        "medicines": ["Paracetamol", "Vitamin C", "Zinc"],
        "severity": "HIGH",
        "advice": "SERIOUS: Turant doctor se milo! Test karwao!"
    },
    "malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache", "vomiting", "fatigue"],
        "remedies": [
            "Zyada se zyada pani piyo",
            "Neem ki patti ka juice piyo",
            "Complete bed rest karo",
        ],
        "medicines": ["Chloroquine", "Paracetamol"],
        "severity": "HIGH",
        "advice": "SERIOUS: Blood test karwao! Doctor ke paas jao!"
    },
    "dengue": {
        "symptoms": ["high fever", "rash", "joint pain", "eye pain", "nausea", "vomiting"],
        "remedies": [
            "Papaya leaf juice piyo — platelet badhata hai",
            "ORS solution piyo",
            "Complete rest karo",
            "Aspirin bilkul mat lo",
        ],
        "medicines": ["Paracetamol", "ORS"],
        "severity": "HIGH",
        "advice": "SERIOUS: Turant hospital jao! Platelet count check karwao!"
    },
    "common cold": {
        "symptoms": ["runny nose", "sneezing", "sore throat", "mild cough", "congestion"],
        "remedies": [
            "Garam pani se gargle karo",
            "Shahad + adrak + nimbu ka mixture lo",
            "Steam lo",
            "Warm soup piyo",
        ],
        "medicines": ["Cetrizine", "Sinarest", "Vicks VapoRub"],
        "severity": "LOW",
        "advice": "Ghabrao mat — 5-7 din mein theek ho jaoge."
    },
    "food poisoning": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "stomach pain", "cramps"],
        "remedies": [
            "ORS solution piyo — dehydration se bachao",
            "Solid khana mat khao 6 ghante tak",
            "Nimbu pani piyo",
            "Curd khao — good bacteria badhata hai",
        ],
        "medicines": ["ORS", "Pantoprazole", "Electral"],
        "severity": "MEDIUM",
        "advice": "Zyada pani piyo. 24 ghante mein theek na ho toh doctor ko dikhao."
    },
    "typhoid": {
        "symptoms": ["high fever", "weakness", "stomach pain", "headache", "loss of appetite"],
        "remedies": [
            "Sirf liquid diet lo — pani, juice, soup",
            "Complete bed rest karo",
            "Bananas khao",
        ],
        "medicines": ["Paracetamol", "Ciprofloxacin"],
        "severity": "HIGH",
        "advice": "SERIOUS: Doctor se milo — antibiotic course chahiye!"
    },
    "asthma": {
        "symptoms": ["breathlessness", "wheezing", "chest tightness", "cough"],
        "remedies": [
            "Inhaler turant use karo",
            "Seedha baitho — litao mat",
            "Triggers se door raho — dust, smoke",
            "Garam pani ki steam lo",
        ],
        "medicines": ["Salbutamol Inhaler", "Montelukast"],
        "severity": "HIGH",
        "advice": "SERIOUS: Inhaler kaam na kare toh turant hospital jao!"
    },
}

def extract_symptoms(user_input):
    user_input = user_input.lower()
    found = []
    all_symptoms = set()
    for data in symptom_db.values():
        all_symptoms.update(data["symptoms"])
    for symptom in all_symptoms:
        if symptom in user_input:
            found.append(symptom)
    return found

def match_disease(symptoms):
    if not symptoms:
        return None, 0
    scores = {}
    for disease, data in symptom_db.items():
        matches = len(set(symptoms) & set(data["symptoms"]))
        if matches > 0:
            score = round((matches / len(data["symptoms"])) * 100, 1)
            scores[disease] = score
    if not scores:
        return None, 0
    best = max(scores, key=scores.get)
    return best, scores[best]

def get_response(user_input):
    symptoms = extract_symptoms(user_input)
    if not symptoms:
        return {
            "status": "unknown",
            "message": "Mujhe symptoms samajh nahi aaye. Thoda detail mein batao jaise: 'mujhe bukhar hai aur khansi ho rahi hai'",
            "symptoms": [],
            "disease": None,
            "remedies": [],
            "medicines": [],
            "severity": "LOW",
            "advice": ""
        }
    disease, confidence = match_disease(symptoms)
    if not disease:
        return {
            "status": "unknown",
            "message": "Koi specific condition match nahi hui. Doctor se milo.",
            "symptoms": symptoms,
            "disease": None,
            "remedies": [],
            "medicines": [],
            "severity": "LOW",
            "advice": ""
        }
    data = symptom_db[disease]
    return {
        "status": "found",
        "message": f"Aapke symptoms se lagta hai yeh {disease.title()} ho sakta hai ({confidence}% match)",
        "symptoms": symptoms,
        "disease": disease.title(),
        "remedies": data["remedies"],
        "medicines": data["medicines"],
        "severity": data["severity"],
        "advice": data["advice"]
    }