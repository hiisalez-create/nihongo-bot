import os
import requests
import datetime

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DAILY_LESSONS = [
    {
        "level": "N5",
        "topic": "දෛනික ආචාර (Daily Greeting)",
        "jp": "お疲れ様でした。",
        "romaji": "Otsukaresama deshita.",
        "en": "Thank you for your hard work.",
        "si": "හොඳින් වැඩ කළා / වෙහෙස මහන්සි වුණා."
    },
    {
        "level": "N4",
        "topic": "උදව් ඉල්ලා සිටීම",
        "jp": "ちょっと手伝ってくれない？",
        "romaji": "Chotto tetsudatte kurenai?",
        "en": "Could you help me for a bit?",
        "si": "පොඩි උදව්වක් කරන්න පුළුවන්ද?"
    },
    {
        "level": "N3",
        "topic": "අදහස් දැක්වීම",
        "jp": "明日は雨が降るらしいよ。",
        "romaji": "Ashita wa ame ga furu rashii yo.",
        "en": "I heard it's going to rain tomorrow.",
        "si": "හෙට වැසි වසිනු ඇතිලු."
    },
    {
        "level": "N2",
        "topic": "සූක්ෂම ව්‍යාකරණ",
        "jp": "彼は知っていながら、私に教えなかった。",
        "romaji": "Kare wa shitte inagara, watashi ni oshienakatta.",
        "en": "Even though he knew, he didn't tell me.",
        "si": "ඔහු දැනගෙන සිටියත්, මට කීවේ නැත."
    }
]

def send_lesson():
    day_index = datetime.datetime.now().day % len(DAILY_LESSONS)
    lesson = DAILY_LESSONS[day_index]
    
    message = (
        f"🇯🇵 *JLPT {lesson['level']} Daily Nihongo* 🇯🇵\n\n"
        f"📌 *මාතෘකාව:* {lesson['topic']}\n\n"
        f"✍️ *Japanese:* {lesson['jp']}\n"
        f"🔤 *Romaji:* {lesson['romaji']}\n"
        f"🌐 *English:* {lesson['en']}\n"
        f"🇱🇰 *සිංහල:* {lesson['si']}\n\n"
        f"💡 *දවසට එක වචනයක් හෝ වාක්‍යයක් පුහුණු වන්න!* 💪"
    )
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    response = requests.post(url, json=payload)
    print(response.json())

if __name__ == "__main__":
    send_lesson()
