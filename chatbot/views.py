from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import urllib.request
import urllib.error
from datetime import datetime
from .engine import get_response as engine_response

HEALTH_SLOGANS = [
    {"text": "An apple a day keeps the doctor away!", "hindi": "Roz ek seb khao!", "icon": "🍎"},
    {"text": "Your health is your greatest wealth.", "hindi": "Swasthya hi sabse bada dhan hai.", "icon": "💪"},
    {"text": "Drink 8 glasses of water daily.", "hindi": "Roz 8 gilas pani piyo.", "icon": "💧"},
    {"text": "Exercise 30 minutes daily!", "hindi": "Roz 30 minute vyayam karo!", "icon": "🏃"},
    {"text": "Sleep 7-8 hours for a healthy life.", "hindi": "7-8 ghante ki neend lo.", "icon": "😴"},
    {"text": "Eat balanced meals.", "hindi": "Santulit bhojan khao.", "icon": "🥗"},
    {"text": "Wash hands regularly.", "hindi": "Haath dhote raho.", "icon": "🙌"},
    {"text": "Meditation keeps stress away.", "hindi": "Roz dhyan karo.", "icon": "🧘"},
    {"text": "Regular checkups detect diseases early.", "hindi": "Niyamit janch karo.", "icon": "🏥"},
    {"text": "Avoid junk food!", "hindi": "Junk food se bacho!", "icon": "❤️"},
    {"text": "Yoga strengthens body and mind.", "hindi": "Yoga karo.", "icon": "🧘‍♀️"},
    {"text": "Laughter is the best medicine!", "hindi": "Hansi sabse badi dawai hai!", "icon": "😄"},
    {"text": "Mental health matters too.", "hindi": "Mansik swasthya zaroori hai.", "icon": "🧠"},
]

SYSTEM_PROMPT = """You are Dr. AI — a 24/7 friendly healthcare assistant for AIHealthCare India.
Understand symptoms in Hindi, English, and Hinglish.
Give home remedies, medicine suggestions, and doctor referrals.
Respond in same language as user. Be warm and caring like a family doctor.
Always add: "⚕️ Serious symptoms mein real doctor se zaroor milo."
For emergencies always mention: 🚨 108 call karo!"""


def home(request):
    today = datetime.now()
    slogan_index = today.day % len(HEALTH_SLOGANS)
    return render(request, 'chatbot/home.html', {
        'slogan': HEALTH_SLOGANS[slogan_index],
        'today': today.strftime("%A, %d %B %Y"),
    })


def chat_page(request):
    return render(request, 'chatbot/index.html')


@csrf_exempt
def chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request'}, status=405)

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        history = data.get('history', [])

        if not user_message:
            return JsonResponse({'status': 'error', 'message': 'Message empty hai'}, status=400)

        # ── Try Gemini API ─────────────────────────────────────────────────
        api_key = getattr(settings, 'GEMINI_API_KEY', '').strip()
        if api_key:
            try:
                reply = _call_gemini(user_message, history, api_key)
                return JsonResponse({'status': 'success', 'message': reply, 'type': 'gemini'})
            except Exception as e:
                # Log silently, fallback to engine
                pass

        # ── Fallback: Local engine (works without API key) ─────────────────
        result = engine_response(user_message)
        reply = _format_engine_response(result)
        return JsonResponse({'status': 'success', 'message': reply, 'type': 'engine'})

    except Exception:
        return JsonResponse({'status': 'error', 'message': 'Kuch galat ho gaya. Dobara try karo.'}, status=500)


def _call_gemini(user_message, history, api_key):
    """Call Gemini API — supports both AIzaSy and AQ. key formats."""
    contents = [
        {"role": "user",  "parts": [{"text": SYSTEM_PROMPT}]},
        {"role": "model", "parts": [{"text": "Namaste! Main Dr. AI hoon 🙏 Kuch bhi poochho!"}]},
    ]

    for msg in history[-8:]:
        role = "user" if msg.get('role') == 'user' else "model"
        contents.append({"role": role, "parts": [{"text": msg.get('content', '')}]})

    contents.append({"role": "user", "parts": [{"text": user_message}]})

    payload = json.dumps({
        "contents": contents,
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 800,
        }
    }).encode('utf-8')

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    # Try with URL param first, then with header
    for headers in [
        {'Content-Type': 'application/json'},
        {'Content-Type': 'application/json', 'x-goog-api-key': api_key},
    ]:
        req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode('utf-8'))
                return result['candidates'][0]['content']['parts'][0]['text']
        except urllib.error.HTTPError as e:
            err_body = e.read().decode()
            if 'allowlist' in err_body.lower() or '403' in str(e.code):
                raise Exception(f"API key restricted: {err_body[:100]}")
            continue
        except Exception:
            continue

    raise Exception("Gemini API call failed")


def _format_engine_response(result):
    if result['status'] in ('greeting', 'general', 'unknown'):
        return result['message']

    lines = [result['message'], ""]

    if result.get('remedies'):
        lines.append("**🌿 Ghar ke Nuskhe:**")
        for r in result['remedies']:
            lines.append(f"  {r}")
        lines.append("")

    if result.get('medicines'):
        lines.append(f"**💊 Medicines:** {', '.join(result['medicines'])}")
        lines.append("")

    if result.get('doctor'):
        lines.append(f"**👨‍⚕️ Doctor:** {result['doctor']}")
        lines.append("")

    if result.get('advice'):
        sev = result.get('severity', 'LOW')
        icon = "🚨" if sev == "HIGH" else "⚠️" if sev == "MEDIUM" else "ℹ️"
        lines.append(f"{icon} **{result['advice']}**")
        lines.append("")

    lines.append("---")
    lines.append("_⚕️ Yeh general advice hai. Serious symptoms mein real doctor se zaroor milo._")
    return "\n".join(lines)