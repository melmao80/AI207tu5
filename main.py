import tkinter as tk
from tkinter import scrolledtext, font

# ==============================
# دیتابیس مشکلات موتور 207 تیپ 5 (TU5)
# ==============================
CAR_PROBLEMS = [
    {
        "symptom": "ماشین روشن نمی‌شود",
        "cause": "ضعف باتری یا خرابی استارت",
        "solution": "بررسی باتری، اتصالات و استارت",
        "severity": "زیاد"
    },
    {
        "symptom": "ریپ زدن موتور",
        "cause": "خرابی شمع، کوئل یا سنسور اکسیژن",
        "solution": "تعویض شمع و بررسی کوئل و سنسور اکسیژن",
        "severity": "متوسط"
    },
    {
        "symptom": "افزایش مصرف سوخت",
        "cause": "خرابی سنسور MAP یا اکسیژن",
        "solution": "دیاگ زدن و تعویض سنسور معیوب",
        "severity": "متوسط"
    },
    {
        "symptom": "داغ شدن موتور",
        "cause": "خرابی ترموستات یا فن رادیاتور",
        "solution": "بررسی فن، ترموستات و سطح آب رادیاتور",
        "severity": "خیلی زیاد"
    },
    {
        "symptom": "روشن شدن چراغ چک",
        "cause": "خطای سنسورها یا احتراق ناقص",
        "solution": "دیاگ زدن ECU و رفع خطا",
        "severity": "متوسط"
    },
    {
        "symptom": "لرزش در حالت درجا",
        "cause": "کثیفی دریچه گاز یا خرابی دسته موتور",
        "solution": "تمیز کردن دریچه گاز و بررسی دسته موتور",
        "severity": "کم"
    },
    {
        "symptom": "کاهش شتاب",
        "cause": "گرفتگی کاتالیزور یا فیلتر هوا",
        "solution": "بررسی کاتالیزور و تعویض فیلتر هوا",
        "severity": "متوسط"
    },
    {
        "symptom": "صدای غیرعادی موتور",
        "cause": "کمبود روغن یا خرابی یاتاقان",
        "solution": "بررسی سطح روغن و مراجعه فوری به مکانیک",
        "severity": "خیلی زیاد"
    },
]

# ==============================
# منطق تشخیص
# ==============================
def diagnose_car_problem(user_input):
    user_input = user_input.lower()
    for p in CAR_PROBLEMS:
        if p["symptom"] in user_input:
            return p
    return {
        "symptom": "نامشخص",
        "cause": "اطلاعات کافی موجود نیست",
        "solution": "علائم دقیق‌تر (صدا، چراغ چک، دما) را وارد کنید",
        "severity": "نامشخص"
    }

# ==============================
# ارسال پیام
# ==============================
def send_message():
    user_input = user_entry.get()
    if not user_input.strip():
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"👤 شما: {user_input}\n", "user")

    result = diagnose_car_problem(user_input)

    response = (
        "🤖 ربات تعمیرکار 207 TU5\n"
        f"🔧 مشکل: {result['symptom']}\n"
        f"⚠️ علت احتمالی: {result['cause']}\n"
        f"🛠 راه‌حل پیشنهادی: {result['solution']}\n"
        f"🔥 شدت مشکل: {result['severity']}\n\n"
    )

    chat_area.insert(tk.END, response, "bot")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)
    user_entry.delete(0, tk.END)

# ==============================
# رابط گرافیکی
# ==============================
root = tk.Tk()
root.title("🔧 چت‌بات تعمیر موتور 207 تیپ 5")
root.geometry("650x520")
root.resizable(False, False)
root.configure(bg="#eaeaea")

# فونت
chat_font = font.Font(family="Tahoma", size=10)
entry_font = font.Font(family="Tahoma", size=12)
title_font = font.Font(family="Tahoma", size=14, weight="bold")

# عنوان
title_label = tk.Label(
    root,
    text="🚗⚙️ چت‌بات تشخیص خرابی موتور پژو 207 تیپ 5 (TU5)",
    bg="#eaeaea",
    fg="#333333",
    font=title_font
)
title_label.pack(pady=10)

# باکس چت
chat_area = scrolledtext.ScrolledText(
    root,
    width=75,
    height=22,
    wrap=tk.WORD,
    state='disabled',
    font=chat_font,
    bg="#ffffff"
)
chat_area.pack(padx=10, pady=5)

chat_area.tag_config("user", foreground="#0d47a1")
chat_area.tag_config("bot", foreground="#1b5e20")

# فریم ورودی
input_frame = tk.Frame(root, bg="#eaeaea")
input_frame.pack(pady=10)

user_entry = tk.Entry(input_frame, width=45, font=entry_font)
user_entry.pack(side=tk.LEFT, padx=5)
user_entry.focus()

send_button = tk.Button(
    input_frame,
    text="ارسال 🔧",
    width=12,
    bg="#4caf50",
    fg="white",
    font=("Tahoma", 10, "bold"),
    command=send_message
)
send_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
