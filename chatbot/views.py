from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import urllib.request
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

        # Gemini API try karo
        api_key = getattr(settings, 'GEMINI_API_KEY', '').strip()
        if api_key:
            try:
                reply = _call_gemini(user_message, history, api_key)
                return JsonResponse({'status': 'success', 'message': reply, 'type': 'ai'})
            except Exception:
                pass

        # Fallback: local engine
        result = engine_response(user_message)
        reply = _format_engine_response(result)
        return JsonResponse({'status': 'success', 'message': reply, 'type': 'ai'})

    except Exception:
        return JsonResponse({'status': 'error', 'message': 'Kuch galat ho gaya.'}, status=500)


def _call_gemini(user_message, history, api_key):
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": "You are Dr. AI, a helpful healthcare assistant. Answer in Hindi/English/Hinglish."}]},
            {"role": "model", "parts": [{"text": "Namaste! Main Dr. AI hoon. Kuch bhi pucho!"}]}
        ] + [
            {"role": msg['role'] if msg['role'] == 'user' else 'model', "parts": [{"text": msg['content']}]}
            for msg in history[-8:]
        ] + [{"role": "user", "parts": [{"text": user_message}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1024}
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'),
                                  headers={'Content-Type': 'application/json'}, method='POST')
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode('utf-8'))
        return result['candidates'][0]['content']['parts'][0]['text']


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
    if result.get('advice'):
        sev = result.get('severity', 'LOW')
        icon = "🚨" if sev == "HIGH" else "⚠️" if sev == "MEDIUM" else "ℹ️"
        lines.append(f"{icon} **{result['advice']}**")