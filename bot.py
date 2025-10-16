import os 
import datetime 
import jdatetime 
from hijri_converter import Hijri, Gregorian 
import telegram 
 
def get_dates(): 
    today_gregorian = datetime.datetime.now() 
    today_jalali = jdatetime.datetime.now() 
 
    hijri = Hijri.fromgregorian( 
        today_gregorian.year,  
        today_gregorian.month,  
        today_gregorian.day 
    ) 
 
    return { 
        'gregorian': today_gregorian.strftime("%Y/%%m/%%d"), 
        'jalali': today_jalali.strftime("%Y/%%m/%%d"), 
        'hijri': f"{hijri.year}/{hijri.month:02d}/{hijri.day:02d}" 
    } 
 
def get_day_message(day_number): 
    messages = { 
        0: "خدایا، این هفته را با برکت و رحمتت آغاز کن.", 
        1: "خدایا، در تمام کارهایم مددکارم باش.", 
        2: "خدایا، بر دانایی و خردم بیفزا.", 
        3: "خدایا، قلبم را از محبت لبریز کن.", 
        4: "خدایا، روزیم را گسترده و کاریم را آسان کن.", 
        5: "خدایا، این روز را برایم مبارک گردان.", 
        6: "خدایا، جمعهات را بر ما مبارک کن." 
    } 
    return messages.get(day_number, "خدایا، شکرت برای این روز زیبا.") 
 
def get_daily_reminder(day_number): 
    reminders = { 
        0: "سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", 
        1: "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللَّهِ", 
        2: "أَسْتَغْفِرُ اللَّهَ وَأَتُوبُ إِلَيْهِ", 
        3: "حَسْبِيَ اللَّهُ وَنِعْمَ الْوَكِيلُ", 
        4: "اللَّهُمَّ صَلِّ عَلَى مُحَمَّدٍ وَآلِ مُحَمَّدٍ", 
        5: "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ", 
        6: "لَا إِلَهَ إِلَّا اللَّهُ وَحْدَهُ لَا شَرِيكَ لَهُ" 
    } 
    return reminders.get(day_number, "اللَّهُ أَكْبَرُ") 
 
def create_message(): 
    dates = get_dates() 
    day_of_week = datetime.datetime.now().weekday() 
    day_message = get_day_message(day_of_week) 
    daily_reminder = get_daily_reminder(day_of_week) 
 
بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ  
صبح همگی بخیر، فرشته‌های مهربون! 🌅 
 
امروز:  
📅 **{dates['jalali']}** (هجری شمسی)  
📅 **{dates['gregorian']}** (میلادی)  
📅 **{dates['hijri']}** (هجری قمری) 
 
✨ **ذکر امروز:**  
{daily_reminder} 
 
🕊️ **پیام امروز:** "{day_message}" 
 
#ذکر_روز #صبح_بخیر 
    return message 
 
def send_to_telegram(): 
    # گرفتن توکن از Environment Variables 
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN') 
    chat_id = os.environ.get('TELEGRAM_CHAT_ID') 
 
    if not bot_token or not chat_id: 
        print("Error: Token or Chat ID not set!") 
        return False 
 
    try: 
        bot = telegram.Bot(token=bot_token) 
        message = create_message() 
        bot.send_message(chat_id=chat_id, text=message) 
        print("پیام با موفقیت ارسال شد!") 
        return True 
    except Exception as e: 
        print(f"Error: {e}") 
        return False 
 
if __name__ == "__main__": 
    send_to_telegram() 
