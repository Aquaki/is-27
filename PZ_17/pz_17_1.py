import tkinter as tk
from tkinter import ttk
from datetime import datetime

def calculate_age(event=None):
    try:
        birth_date = datetime.strptime(birth_entry.get(), "%m/%d/%Y")
        today = datetime.now()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_entry.delete(0, tk.END)
        age_entry.insert(0, str(age))
    except ValueError:
        pass

def submit_form():
    print("Форма отправлена!")
    print(f"Username: {username_entry.get()}")
    print(f"Email: {email_entry.get()}")
    print(f"Password: {'*' * len(password_entry.get())}")
    print(f"Address: {address_entry.get()}")
    print(f"Birth Date: {birth_entry.get()}")
    print(f"Age: {age_entry.get()}")
    print(f"Gender: {gender.get()}")
    print(f"Agreed to rules: {agree_var.get() == 1}")

def reset_form():
    for entry in [username_entry, email_entry, password_entry, address_entry, birth_entry, age_entry]:
        entry.delete(0, tk.END)
    gender.set("Pria")
    agree_var.set(0)

# Создание основного окна
root = tk.Tk()
root.title("Форма регистрации")
root.geometry("400x500")

# Настройка стилей
style = ttk.Style()
style.configure("Dark.TLabelframe",
               background=root.cget('bg'),
               bordercolor="#333333",
               relief="solid",
               borderwidth=1)
style.configure("Dark.TLabelframe.Label",
               background=root.cget('bg'),
               foreground="black")

# Раздел информации о пользователе
user_info_frame = ttk.LabelFrame(root, text="User login info",
                               style="Dark.TLabelframe", padding=10)
user_info_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(user_info_frame, text="Username:").grid(row=0, column=0, sticky="w")
username_entry = ttk.Entry(user_info_frame)
username_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(user_info_frame, text="Email:").grid(row=1, column=0, sticky="w")
email_entry = ttk.Entry(user_info_frame)
email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(user_info_frame, text="Password:").grid(row=2, column=0, sticky="w")
password_entry = ttk.Entry(user_info_frame, show="*")
password_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

# Раздел личных данных
personal_data_frame = ttk.LabelFrame(root, text="Data diri",
                                  style="Dark.TLabelframe", padding=10)
personal_data_frame.pack(fill="x", padx=10, pady=5)

ttk.Label(personal_data_frame, text="Alamat:").grid(row=0, column=0, sticky="w")
address_entry = ttk.Entry(personal_data_frame)
address_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(personal_data_frame, text="Tanggal lahir:").grid(row=1, column=0, sticky="w")
birth_entry = ttk.Entry(personal_data_frame)
birth_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
birth_entry.bind("<FocusOut>", calculate_age)

ttk.Label(personal_data_frame, text="Usia:").grid(row=2, column=0, sticky="w")
age_entry = ttk.Entry(personal_data_frame, state="readonly")
age_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(personal_data_frame, text="Jenis kelamin:").grid(row=3, column=0, sticky="w")
gender_frame = ttk.Frame(personal_data_frame)
gender_frame.grid(row=3, column=1, sticky="w", padx=5, pady=2)

gender = tk.StringVar(value="Pria")
ttk.Radiobutton(gender_frame, text="Pria", variable=gender, value="Pria").pack(side="left")
ttk.Radiobutton(gender_frame, text="Wanita", variable=gender, value="Wanita").pack(side="left", padx=10)

# Раздел согласия
action_frame = ttk.LabelFrame(root, style="Dark.TLabelframe", padding=10)
action_frame.pack(fill="x", padx=10, pady=5)

# Чекбокс согласия
agree_var = tk.IntVar()
agree_frame = ttk.Frame(action_frame)
agree_frame.pack(fill="x", pady=(0, 10))

ttk.Label(agree_frame, text="Saya bersedia mengikuti aturan forum").pack(side="left")
ttk.Checkbutton(agree_frame, variable=agree_var).pack(side="left", padx=5)

# Кнопки
button_frame = ttk.Frame(action_frame)
button_frame.pack(fill="x")

submit_button = ttk.Button(button_frame, text="Submit", command=submit_form)
submit_button.pack(side="left", padx=(0, 5))

reset_button = ttk.Button(button_frame, text="Reset", command=reset_form)
reset_button.pack(side="left")

# Настройка растягивания колонок
user_info_frame.columnconfigure(1, weight=1)
personal_data_frame.columnconfigure(1, weight=1)

root.mainloop()