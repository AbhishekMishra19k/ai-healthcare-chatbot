# 🏥 AIHealthCare — AI-Powered Healthcare Chatbot

A full-stack Django web application that provides AI-driven healthcare assistance, doctor appointment booking, and an online pharmacy — built for India with Hindi/English/Hinglish support.

---

## ✨ Features

- **AI Health Chatbot** — Powered by Google Gemini 2.0, supports Hindi, English & Hinglish
- **Symptom Checker** — Rule-based engine with home remedies and medicine suggestions
- **Doctor Appointments** — Browse specialists, book slots, get email confirmation
- **Online Pharmacy** — Browse and order medicines by category
- **User Accounts** — Register, login, edit profile with blood group & health details
- **Daily Health Slogans** — Rotating wellness tips on the homepage
- **Email Notifications** — Appointment confirmations sent to patient & admin

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.2, Python 3.13 |
| AI | Google Gemini 2.0 Flash API |
| Database | SQLite (local) / PostgreSQL / Neon (production) |
| Frontend | HTML5, Bootstrap, Vanilla JS |
| Deployment | Vercel + Neon DB |
| Email | Gmail SMTP |

---

## 🚀 Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/AbhishekMishra19k/ai-healthcare-chatbot.git
cd ai-healthcare-chatbot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
```
Then open `.env` and fill in:
- `SECRET_KEY` — any random string
- `GEMINI_API_KEY` — get from [Google AI Studio](https://aistudio.google.com)
- `EMAIL_HOST_USER` / `EMAIL_HOST_PASSWORD` — Gmail app password
- Leave `DATABASE_URL` empty to use SQLite locally

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Seed sample data (optional)
```bash
python add_doctors.py
python add_medicines.py
```

### 7. Create admin user
```bash
python manage.py createsuperuser
```

### 8. Start the development server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📁 Project Structure

```
ai-healthcare-chatbot/
├── chatbot/          # AI chat, symptom engine, home page
├── appointments/     # Doctor listing & appointment booking
├── medicines/        # Pharmacy / medicine ordering
├── accounts/         # User auth, profile management
├── healthcare/       # Django project settings & URLs
├── templates/        # Shared base template
├── add_doctors.py    # Script to seed doctor data
├── add_medicines.py  # Script to seed medicine data
├── .env.example      # Environment variable template
└── requirements.txt
```

---

## ⚙️ Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for development, `False` for production |
| `DATABASE_URL` | PostgreSQL URL (leave empty for SQLite) |
| `GEMINI_API_KEY` | Google Gemini API key |
| `EMAIL_HOST_USER` | Gmail address |
| `EMAIL_HOST_PASSWORD` | Gmail App Password |
| `ADMIN_EMAIL` | Email to receive appointment notifications |

---

## 🌐 Deployment (Vercel + Neon)

1. Push code to GitHub
2. Connect repo to [Vercel](https://vercel.com)
3. Add all environment variables in Vercel dashboard
4. Set `DATABASE_URL` to your [Neon](https://neon.tech) PostgreSQL URL
5. Deploy!

---

## 👨‍💻 Author

**Abhishek Mishra**  
GitHub: [@AbhishekMishra19k](https://github.com/AbhishekMishra19k)
