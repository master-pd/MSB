from telegram import Bot
import time
import random
import os

# ====== Banner ======
print("""
===================================
      Spam-Bot by master-pd
===================================
""")

# ====== Bot Token এবং Chat ID ======
bot_token = input("Bot Token লিখো: ").strip()
chat_id = input("Chat ID লিখো: ").strip()
bot = Bot(token=bot_token)

# ====== Predefined Messages ======
predefined_messages = [
    "হাই! কেমন আছো?",
    "আজকের দিনটা কেমন যাচ্ছে?",
    "মজা করছে তো?",
    "কোথায় আছো আজ?",
    "সব ঠিক আছে তো?",
    "যাই হোক মূল কথায় আসি।"
]

# ====== User Messages File(s) ======
files_input = input("মেসেজ ফাইলের নাম লিখো (কমা দিয়ে একাধিক হতে পারে, default: msg.txt): ").strip()
if files_input == "":
    files_input = "msg.txt"

# ফাইল লিস্ট থেকে মেসেজ লোড করা
user_messages = []
for f_name in files_input.split(","):
    f_name = f_name.strip()
    try:
        with open(f_name, "r", encoding="utf-8") as f:
            user_messages += [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"ফাইল {f_name} পাওয়া যায়নি, বাদ দেয়া হলো।")

# সব মেসেজ একত্র করা
all_messages = user_messages + predefined_messages

if not all_messages:
    print("কোনো মেসেজ পাওয়া যায়নি। msg.txt বা অন্য ফাইলে কিছু লিখে আবার চেষ্টা করো।")
    exit()

# ====== Number of Messages ======
try:
    count = int(input("কতগুলো মেসেজ পাঠাতে চাও: "))
except:
    print("ভুল ইনপুট! সংখ্যা দিতে হবে।")
    exit()

# ====== Log Files ======
success_log = "success_log.txt"
fail_log = "fail_log.txt"

# ====== Sending Messages ======
for i in range(count):
    msg = random.choice(all_messages)
    try:
        res = bot.send_message(chat_id=chat_id, text=msg)
        print(f"[{i+1}/{count}] পাঠানো হয়েছে: {msg}")
        with open(success_log, "a", encoding="utf-8") as log:
            log.write(f"{msg}\n")
        time.sleep(0.3)  # Sleep time 0.3 seconds
    except Exception as e:
        print(f"[{i+1}/{count}] সমস্যা হয়েছে: {e}")
        with open(fail_log, "a", encoding="utf-8") as log:
            log.write(f"{msg} | Error: {e}\n")
        time.sleep(0.3)  # Sleep time 0.3 seconds

print("সব মেসেজ পাঠানো শেষ।")
