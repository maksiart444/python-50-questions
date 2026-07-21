import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from datetime import datetime
from PIL import Image, ImageTk

questions_list = [
    "1. Как тебя зовут?", "2. Сколько тебе лет?", "3. Где ты сейчас живешь?", "4. Кем ты работаешь?", "5. Чем занимаешься в свободное время?",
    "6. О чем ты мечтаешь прямо сейчас?", "7. Какой твой любимый цвет?", "8. Какая твоя любимая еда?", "9. Любишь ли ты путешествовать?", 
    "10. Какое твое самое большое достижение?", "11. Какой у тебя характер?", "12. Что тебя больше всего радует?", "13. Что тебя больше всего злит?", 
    "14. Какая у тебя главная привычка?", "15. Что бы ты изменил в своем характере?", "16. Как ты ведешь себя в стрессовой ситуации?", 
    "17. Есть ли у тебя главная цель на этот год?", "18. Какой навык ты хотел бы освоить?", "19. Что ты ценишь в людях?", 
    "20. Твой любимый музыкальный жанр?", "21. Любимый фильм?", "22. Как ты относишься к спорту?", "23. Твой идеальный выходной?", 
    "24. Что тебя вдохновляет?", "25. Твое отношение к деньгам?", "26. Что для тебя счастье?", "27. Твой самый смелый поступок?", 
    "28. Какую книгу ты бы посоветовал?", "29. Что ты думаешь о будущем?", "30. Что для тебя дружба?", "31. Твой любимый сезон года?", 
    "32. Что ты ешь на завтрак?", "33. Как ты справляешься с ленью?", "34. Твой самый необычный опыт?", "35. Что ты хотел бы изменить в мире?", 
    "36. Твой любимый способ отдыха?", "37. С кем бы ты хотел поужинать?", "38. Что для тебя любовь?", "39. Твой главный страх?", 
    "40. Что ты ценишь в жизни больше всего?", "41. Какое твое любимое время суток?", "42. Твой любимый вид спорта?", 
    "43. Что тебя может рассмешить?", "44. Твое отношение к соцсетям?", "45. Что ты считаешь своим успехом?", "46. Твоя мечта детства?", 
    "47. Твой любимый город?", "48. Что ты делаешь, когда тебе скучно?", "49. Твой девиз по жизни?", "50. Каким ты видишь себя через 5 лет?"
]

user_data = {}
question_index = 0

def get_comment(index, answer):
    comments = {
        0: f"✨ Приятно познакомиться, {answer}!", 1: "🌟 Замечательный возраст!", 2: f"📍 {answer}? Звучит как крутое место.", 
        3: f"💼 Профессия {answer} — это серьезно.", 4: "🎮 Отдых — это важно.", 5: f"🌈 Мечтать — это прекрасно.",
        6: f"🎨 Классный цвет — {answer}!", 7: f"🍕 Ням, {answer} — отличный аппетит.", 8: "✈️ Путешествия — это жизнь!",
        9: "🏆 Это впечатляет.", 10: "🦁 Хороший характер — залог успеха.", 11: "😊 Радость — это топливо для жизни.",
        12: "💭 Понимаю.", 13: f"📌 Привычка {answer} — интересно.", 14: "🚀 Самосовершенствование — путь сильных.",
        15: "🛡️ Стресс — это лишь испытание.", 16: "🎯 Отличная цель!", 17: f"🛠️ Навык {answer} — полезно.",
        18: "🤝 Честность — это база.", 19: f"🎵 Музыка {answer} — хороший вкус.", 20: f"🎬 Фильм {answer}? Интересно.",
        21: "⚽ Спорт — это круто!", 22: "🛋️ Идеальный выходной.", 23: f"💡 Вдохновение — это здорово.",
        24: "💰 Деньги — инструмент.", 25: "☀️ Счастье в мелочах.", 26: "🔥 Смелость города берет!", 27: f"📖 Книга {answer}.",
        28: "🔮 Будущее создаем мы сами.", 29: "👫 Друзья — это навсегда.", 30: f"🌸 {answer}? Красиво.", 31: f"🍳 Завтрак {answer}.",
        32: "⚡ Лень — двигатель прогресса.", 33: f"🌌 Опыт {answer} — бесценно.", 34: "🌍 Мир меняем мы.", 35: f"🏝️ Отдых {answer}.",
        36: f"🍷 Ужин — интересно.", 37: "❤️ Любовь — главное чувство.", 38: f"👻 Страх {answer} — это нормально.",
        39: "💎 Ценить жизнь — мудрость.", 40: f"🌙 Время {answer}? Романтично.", 41: f"🏃 Спорт {answer}?", 42: "😂 Смех — это жизнь!",
        43: "📱 Соцсети — окно в мир.", 44: f"🚀 Успех {answer}.", 45: f"👶 Мечта {answer}.", 46: f"🏙️ Город {answer} — супер.",
        47: f"🧩 Скука — время для творчества.", 48: f"📜 Девиз {answer}.", 49: "🚀 Амбициозно!"
    }
    return comments.get(index, "✅ Принято!")

root = tk.Tk()
root.title("Анкета Pro")
root.geometry("800x600")
canvas = tk.Canvas(root, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def draw_ui(event=None):
    canvas.delete("all")
    w, h = root.winfo_width(), root.winfo_height()
    # Загружаем фон и сохраняем его в переменную canvas, чтобы он не удалялся
    if os.path.exists("bg.png"):
        img = Image.open("bg.png").resize((w, h), Image.Resampling.LANCZOS)
        bg = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg
    # Рисуем текст поверх фона
    canvas.create_text(w/2, 40, text="Анкета: 50 вопросов", font=("Segoe UI", 28, "bold"), fill="white")
    canvas.create_text(w/2, 80, text="Автор: Артём Максименко", font=("Segoe UI", 12), fill="#bdc3c7")
canvas.bind('<Configure>', draw_ui)

label = tk.Label(root, text=questions_list[0], font=("Segoe UI", 20), fg="white", bg="#1a1a2e")
label.place(relx=0.5, rely=0.4, anchor="center")

entry = tk.Entry(root, font=("Segoe UI", 18))
entry.place(relx=0.5, rely=0.5, anchor="center", width=400, height=40)
entry.focus_set()

def save_data():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    df = pd.DataFrame(list(user_data.items()), columns=['Вопрос', 'Ответ'])
    
    excel_path = os.path.join(os.getcwd(), f"anketa_{ts}.xlsx")
    txt_path = os.path.join(os.getcwd(), f"anketa_{ts}.txt")
    
    writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Анкета')
    
    worksheet = writer.sheets['Анкета']
    for i, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(i, i, max_len)
    
    writer.close()
    
    with open(txt_path, "w", encoding="utf-8") as f:
        for q, a in user_data.items():
            f.write(f"{q}: {a}\n")
            
    messagebox.showinfo("Готово", "Все сохранено!")
    root.destroy()

def on_click(event=None):
    global question_index
    answer = entry.get().strip()
    if not answer: return
    
    # ВОЗВРАЩЕННАЯ ВАЛИДАЦИЯ
    if question_index == 0:
        if any(char.isdigit() for char in answer):
            messagebox.showerror("Ошибка", "Имя не должно содержать цифры!")
            return
    elif question_index == 1:
        if not answer.isdigit() or not (0 < int(answer) < 120):
            messagebox.showerror("Ошибка", "Возраст — только цифры (1-119)!")
            return
    
    user_data[questions_list[question_index]] = answer
    entry.delete(0, tk.END)
    
    if question_index == 49:
        save_data()
    else:
        label.config(text=get_comment(question_index, answer))
        question_index += 1
        root.after(1000, lambda: label.config(text=questions_list[question_index]))

btn = tk.Button(root, text="Ответить", command=on_click, font=("Segoe UI", 16), bg="#2ecc71")
btn.place(relx=0.5, rely=0.6, anchor="center")
entry.bind('<Return>', on_click)
root.mainloop()