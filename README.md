# 🚀 MSB-BOT 🚀

**Created by:** Md Rana  
**Address:** Dhaka, Bangladesh  
**Email:** mdranasheikhe2005@gmail.com  

---

## 🛠 Tool Name
**MSB-BOT** (Mass Telegram Messaging Bot)

---

## 🔹 Purpose / টুলের কাজ
MSB-BOT হলো **শুধু শিক্ষামূলক ও প্র্যাকটিসের জন্য তৈরি** একটি Telegram Bot।  
এটি ব্যবহার করে তুমি শিখতে পারবে:  

- Python দিয়ে Telegram Bot API ব্যবহার করা।  
- Predefined ও file-based messages পাঠানো।  
- Success / Fail log তৈরি ও দেখতে পারা।  

> ⚠️ **Important:**  
> কেবল নিজের Telegram চ্যাট বা টেস্ট গ্রুপে ব্যবহার করা উচিত।  
> অন্য কারো অনুমতি ছাড়া ব্যবহার করলে Telegram-এর নীতি লঙ্ঘন হবে এবং অ্যাকাউন্ট/বট ব্যান হতে পারে।  

---

## ⚡ Features / ফিচার
- ✅ Predefined messages পাঠানো।  
- ✅ Optional: File থেকে কাস্টম মেসেজ লোড।  
- ✅ প্রতি সেকেন্ডে 2টি মেসেজ পাঠানো।  
- ✅ Success / Fail log ফাইল তৈরি করে হিসাব রাখা।  

---

# 📦 INSTALLATION 🔰

## Termux Commands (Copy-Ready)
নিচের সব কমান্ড একসাথে কপি করে Termux-এ পেস্ট করতে পারবে:
### step 1
```
cd ~ rm -rf MSB
```
### step 2
```
rm -f success_log.txt fail_log.txt
```
### step 3
```
git clone https://github.com/master-pd/MSB.git
 cd MSB
```
### step 4
```
pkg update -y pkg upgrade -y
 pkg install python -y
pkg install git -y
pip install --upgrade
python-telegram-bot urllib3 requests
```
### step 5
```
chmod +x main.py
python main.py
```
