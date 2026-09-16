from tkinter import *
from tkinter import ttk

BASES = {
    "Decimal(10)": 10,
    "Binary(2)": 2,
    "Octal(8)": 8,
    "Hexadecimal(16)": 16,
}

BG = "#f4f6f8"
ACCENT = "#2f6fed"

window = Tk()
window.title("Ajinkya's Base Convertor")
window.geometry("480x420")
window.config(background=BG)

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", font=("Arial", 13), padding=6)
style.configure(
    "Accent.TButton",
    font=("Arial", 14, "bold"),
    padding=10,
    background=ACCENT,
    foreground="white",
)
style.map("Accent.TButton", background=[("active", "#1f57c9")])

container = Frame(window, bg=BG, padx=30, pady=30)
container.pack(expand=True)

result_label = None  # keeps track of the current result/error label so old ones don't stack up


def to_base(value, base):
    """Convert a non-negative integer to its string representation in the given base."""
    if value == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while value > 0:
        result = digits[value % base] + result
        value //= base
    return result


def temp_text(event):
    if input_box.get() == "Enter Number...":
        input_box.delete(0, "end")


def show_result(text, is_error=False):
    global result_label
    if result_label is not None:
        result_label.destroy()
    result_label = Label(
        container,
        text=text,
        font=("Arial", 20, "bold"),
        bg=BG,
        fg="#d32f2f" if is_error else "#1b1b1b",
        wraplength=380,
    )
    result_label.pack(pady=(15, 0))


def click():
    n = input_box.get().strip()
    a = menu.get()
    b = menu2.get()

    if a not in BASES or b not in BASES:
        show_result("Please select both bases!", is_error=True)
        return
    if not n or n == "Enter Number...":
        show_result("Please enter a number!", is_error=True)
        return

    try:
        value = int(n, BASES[a])
    except ValueError:
        show_result(f"'{n}' is not a valid {a} number!", is_error=True)
        return

    show_result(to_base(value, BASES[b]))


title = Label(
    container,
    text="DATA BASE CONVERTER",
    font=("Arial", 22, "bold"),
    bg=BG,
    fg="#1b1b1b",
)
title.pack(pady=(0, 20))

input_box = Entry(container, font=("Arial", 16), width=28, relief="solid", bd=1)
input_box.insert(0, "Enter Number...")
input_box.bind("<FocusIn>", temp_text)
input_box.pack(ipady=6, pady=(0, 15))

menu = StringVar()
menu.set("Select Initial Base")
drop = ttk.Combobox(container, textvariable=menu, values=list(BASES.keys()), state="readonly", width=26)
drop.pack(pady=(0, 10))

menu2 = StringVar()
menu2.set("Select Final Base")
drop2 = ttk.Combobox(container, textvariable=menu2, values=list(BASES.keys()), state="readonly", width=26)
drop2.pack(pady=(0, 20))

button = ttk.Button(container, text="Convert!", command=click, style="Accent.TButton")
button.pack(fill="x")

window.mainloop()