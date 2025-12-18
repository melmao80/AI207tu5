import tkinter as tk
from tkinter import scrolledtext, font

# =====================================
# دیتابیس مشکلات موتور TU5
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
# منطق تشخیص
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
# ارسال پیام
# =====================================
def send_message(event=None):
    text = entry.get()
    if not text.strip():
        return

    chat.config(state="normal")
    chat.insert(tk.END, f"YOU ▶ {text}\n\n", "user")

    result = smart_diagnose(text)

    response = (
        "AI MECHANIC ▶\n"
        f"Problem: {result['symptom']}\n"
        f"Cause: {result['cause']}\n"
        f"Solution: {result['solution']}\n"
        f"Severity: {result['severity']}\n\n"
    )

    chat.insert(tk.END, response, "bot")
    chat.config(state="disabled")
    chat.yview(tk.END)
    entry.delete(0, tk.END)

# =====================================
# UI - Dark Professional
# =====================================
root = tk.Tk()
root.title("AI Engine Diagnostic System - TU5")
root.geometry("760x600")
root.configure(bg="#0f1115")
root.resizable(False, False)

title_font = font.Font(family="Segoe UI", size=15, weight="bold")
chat_font = font.Font(family="Consolas", size=10)
entry_font = font.Font(family="Segoe UI", size=11)

# Title
tk.Label(
    root,
    text="AI-Based Engine Diagnostic System (Peugeot 207 TU5)",
    bg="#0f1115",
    fg="#00e5ff",
    font=title_font
).pack(pady=15)

# Chat box
chat = scrolledtext.ScrolledText(
    root,
    width=88,
    height=24,
    wrap=tk.WORD,
    font=chat_font,
    bg="#161a20",
    fg="#e0e0e0",
    insertbackground="white",
    state="disabled",
    borderwidth=0
)
chat.pack(padx=15)

chat.tag_config("user", foreground="#42a5f5")
chat.tag_config("bot", foreground="#00e676")

# Input frame
frame = tk.Frame(root, bg="#0f1115")
frame.pack(pady=15)

entry = tk.Entry(
    frame,
    width=55,
    font=entry_font,
    bg="#1e2228",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry.pack(side=tk.LEFT, ipady=6, padx=8)
entry.bind("<Return>", send_message)
entry.focus()

send_btn = tk.Button(
    frame,
    text="SEND",
    width=12,
    bg="#00e5ff",
    fg="#0f1115",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    command=send_message
)
send_btn.pack(side=tk.LEFT)

root.mainloop()
