import tkinter as tk
from tkinter import scrolledtext, font

# =====================================
# دیتابیس هوشمند مشکلات موتور TU5
# =====================================
CAR_PROBLEMS = [
    {
        "keywords": ["روشن", "استارت", "نمی‌شود", "خاموش"],
        "symptom": "ماشین روشن نمی‌شود",
        "cause": "ضعف باتری، خرابی استارت یا سوئیچ",
        "solution": "بررسی باتری، کابل‌ها و استارت",
        "severity": "زیاد"
    },
    {
        "keywords": ["ریپ", "لرزش", "تقه"],
        "symptom": "ریپ زدن موتور",
        "cause": "خرابی شمع، کوئل یا سنسور اکسیژن",
        "solution": "تعویض شمع و تست کوئل",
        "severity": "متوسط"
    },
    {
        "keywords": ["مصرف", "بنزین", "سوخت"],
        "symptom": "افزایش مصرف سوخت",
        "cause": "خرابی سنسور MAP یا اکسیژن",
        "solution": "دیاگ و تعویض سنسور معیوب",
        "severity": "متوسط"
    },
    {
        "keywords": ["داغ", "آب", "جوش"],
        "symptom": "داغ شدن موتور",
        "cause": "خرابی ترموستات یا فن",
        "solution": "بررسی فن، ترموستات و سطح آب",
        "severity": "خیلی زیاد"
    },
    {
        "keywords": ["چک", "خطا", "ecu"],
        "symptom": "روشن شدن چراغ چک",
        "cause": "خطای سنسورها یا احتراق ناقص",
        "solution": "دیاگ ECU",
        "severity": "متوسط"
    },
    {
        "keywords": ["صدا", "تق", "کوبش"],
        "symptom": "صدای غیرعادی موتور",
        "cause": "کمبود روغن یا خرابی یاتاقان",
        "solution": "خاموش کردن خودرو و مراجعه فوری",
        "severity": "خیلی زیاد"
    },
]

# =====================================
# موتور تشخیص هوشمند
# =====================================
def smart_diagnose(text):
    text = text.lower()
    best_match = None
    max_score = 0

    for problem in CAR_PROBLEMS:
        score = sum(1 for k in problem["keywords"] if k in text)
        if score > max_score:
            max_score = score
            best_match = problem

    if best_match and max_score > 0:
        return best_match

    return {
        "symptom": "نامشخص",
        "cause": "علائم کافی تشخیص داده نشد",
        "solution": "لطفاً توضیح دقیق‌تری وارد کنید",
        "severity": "نامشخص"
    }

# =====================================
# رابط کاربری
# =====================================
def send_message(event=None):
    user_text = entry.get()
    if not user_text.strip():
        return

    chat.config(state="normal")
    chat.insert(tk.END, f"شما: {user_text}\n", "user")

    result = smart_diagnose(user_text)

    response = (
        f"ربات تعمیرکار TU5:\n"
        f"مشکل: {result['symptom']}\n"
        f"علت: {result['cause']}\n"
        f"راه‌حل: {result['solution']}\n"
        f"شدت: {result['severity']}\n\n"
    )

    chat.insert(tk.END, response, "bot")
    chat.config(state="disabled")
    chat.yview(tk.END)
    entry.delete(0, tk.END)

# =====================================
# تنظیمات GUI
# =====================================
root = tk.Tk()
root.title("چت‌بات هوشمند تعمیر موتور 207 TU5")
root.geometry("720x560")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

title_font = font.Font(family="Tahoma", size=14, weight="bold")
chat_font = font.Font(family="Tahoma", size=10)
entry_font = font.Font(family="Tahoma", size=11)

tk.Label(
    root,
    text="سیستم هوشمند تشخیص خرابی موتور پژو 207 TU5",
    bg="#f4f6f8",
    fg="#263238",
    font=title_font
).pack(pady=10)

chat = scrolledtext.ScrolledText(
    root,
    width=80,
    height=24,
    wrap=tk.WORD,
    font=chat_font,
    state="disabled",
    bg="white"
)
chat.pack(padx=10)

chat.tag_config("user", foreground="#0d47a1")
chat.tag_config("bot", foreground="#1b5e20")

frame = tk.Frame(root, bg="#f4f6f8")
frame.pack(pady=10)

entry = tk.Entry(frame, width=50, font=entry_font)
entry.pack(side=tk.LEFT, padx=5)
entry.bind("<Return>", send_message)

btn = tk.Button(
    frame,
    text="ارسال",
    width=12,
    bg="#1976d2",
    fg="white",
    font=("Tahoma", 10, "bold"),
    command=send_message
)
btn.pack(side=tk.LEFT)

root.mainloop()
