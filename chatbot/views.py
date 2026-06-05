from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json
import urllib.request
import urllib.error
from datetime import datetime

HEALTH_SLOGANS = [
    {"text": "An apple a day keeps the doctor away!", "hindi": "Roz ek seb khao, doctor se door raho!", "icon": "🍎"},
    {"text": "Your health is your greatest wealth.", "hindi": "Swasthya hi sabse bada dhan hai.", "icon": "💪"},
    {"text": "Drink 8 glasses of water daily for a healthy life.", "hindi": "Roz 8 gilas pani piyo, swasth raho.", "icon": "💧"},
    {"text": "Exercise 30 minutes daily — your body will thank you!", "hindi": "Roz 30 minute vyayam karo!", "icon": "🏃"},
    {"text": "Sleep 7-8 hours for a healthy mind and body.", "hindi": "7-8 ghante ki neend lo, tan-man swasth rakho.", "icon": "😴"},
    {"text": "Eat balanced meals — vitamins, proteins, and minerals.", "hindi": "Santulit bhojan khao.", "icon": "🥗"},
    {"text": "Wash hands regularly to prevent infections.", "hindi": "Haath dhote raho — infection se bacho.", "icon": "🙌"},
    {"text": "Meditation daily keeps stress away.", "hindi": "Roz dhyan karo, stress door bhagao.", "icon": "🧘"},
    {"text": "Regular checkups can detect diseases early.", "hindi": "Niyamit janch se bimari jaldi pakdi jati hai.", "icon": "🏥"},
    {"text": "Avoid junk food — your heart will thank you!", "hindi": "Junk food se bacho — dil khush rahega!", "icon": "❤️"},
    {"text": "Yoga strengthens both body and mind.", "hindi": "Yoga se tan aur man dono mazboot hote hain.", "icon": "🧘‍♀️"},
    {"text": "Laughter is the best medicine!", "hindi": "Hansi sabse badi dawai hai!", "icon": "😄"},
    {"text": "Mental health is as important as physical health.", "hindi": "Mansik swasthya utna hi zaroori hai jitna sharirik.", "icon": "🧠"},
]


def home(request):
    today = datetime.now()
    slogan_index = today.day % len(HEALTH_SLOGANS)
    daily_slogan = HEALTH_SLOGANS[slogan_index]
    return render(request, 'chatbot/home.html', {
        'slogan': daily_slogan,
        'today': today.strftime("%A, %d %B %Y")
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
            return JsonResponse({'status': 'error', 'message': 'Message cannot be empty.'}, status=400)

        api_key = settings.GEMINI_API_KEY
        if not api_key:
            return JsonResponse({
                'status': 'error',
                'message': 'AI service is not configured. Please contact the administrator.'
            }, status=503)

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": (
                        "You are Dr. AI, a 24/7 multilingual AI healthcare assistant for AIHealthCare India.\n"
                        "Your capabilities:\n"
                        "1. Understand symptoms in Hindi, English, and Hinglish\n"
                        "2. Provide home remedies (ghar ke nuskhe) for minor issues\n"
                        "3. Recommend medicines for common problems\n"
                        "4. Suggest which specialist doctor to see if condition is serious\n"
                        "5. Give diet and lifestyle advice\n"
                        "Respond in the same language as the user. Be warm, friendly, and helpful.\n"
                        "Always add a disclaimer for serious conditions to consult a real doctor."
                    )}]
                },
                {
                    "role": "model",
                    "parts": [{"text": "Namaste! Main Dr. AI hoon 🙏 Aapka 24/7 health assistant. Kuch bhi pucho!"}]
                }
            ] + [
                {
                    "role": msg['role'] if msg['role'] == 'user' else 'model',
                    "parts": [{"text": msg['content']}]
                }
                for msg in history[-8:]
            ] + [
                {"role": "user", "parts": [{"text": user_message}]}
            ],
            "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1024}
        }

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST'
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode('utf-8'))
            ai_reply = result['candidates'][0]['content']['parts'][0]['text']

        return JsonResponse({'status': 'success', 'message': ai_reply, 'type': 'ai'})

    except urllib.error.HTTPError as e:
        return JsonResponse({'status': 'error', 'message': 'AI service error. Please try again.'}, status=502)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': 'Something went wrong. Please try again.'}, status=500)
