import calendar
import tkinter as tk
from tkinter import ttk, messagebox

# def show_calendar - функція для відображення місяця або року
def show_calendar():
    try:
        year = int(year_entry.get())
        month = month_combo.get()

        if month == "Повний рік":
            cal_text = calendar.TextCalendar().formatyear(year, 2, 1, 1, 3)
        else:
            month_num = month_list.index(month) + 1
            cal_text = calendar.month(year, month_num)

        calendar_output.delete("1.0", tk.END)
        calendar_output.insert(tk.END, cal_text)

    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректний рік.")

def clear_fields():
    year_entry.delete(0, tk.END)
    month_combo.set("Повний рік")
    calendar_output.delete("1.0", tk.END)

# Налаштовування графічного інтерфейсу
root = tk.Tk()
root.title("Календар")
root.geometry("400x400")

# Рік
tk.Label(root, text="Введіть рік:").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack()

# Місяць
tk.Label(root, text="Виберіть місяць:").pack(pady=5)
month_list = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
              "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень", "Повний рік"]
month_combo = ttk.Combobox(root, values=month_list, state="readonly")
month_combo.set("Повний рік")
month_combo.pack()

# Кнопки
tk.Button(root, text="Показати", command=show_calendar).pack(pady=10)
tk.Button(root, text="Очистити", command=clear_fields).pack(pady=5)

# Поле для виводу календаря
calendar_output = tk.Text(root, wrap=tk.WORD, width=50, height=15, bg="#f0f0f0", state="normal")
calendar_output.pack(pady=5)

# Основний цикл
root.mainloop()

# Інший варіант
#import calendar

#Y = int(input("Введіть рік: "))
#M = int(input("Введіть місяць: "))

# display the calendar
#print(calendar.month(Y, M))
#input()
