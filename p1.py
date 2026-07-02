import tkinter as tk

# -----------------
# ตั้งค่าหน้าต่าง
# -----------------
root = tk.Tk()
root.title("iPhone Calculator")
root.configure(bg="black")
root.resizable(False, False)

expression = ""

display = tk.Entry(
    root,
    font=("Helvetica", 30),
    bg="black",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# -----------------
# ฟังก์ชัน
# -----------------
def press(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)

def equal():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""

# -----------------
# ปุ่ม
# -----------------
buttons = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

color_number = "#505050"
color_operator = "#FF9500"
color_top = "#A5A5A5"

for r, row in enumerate(buttons):
    c = 0
    for text in row:

        if text in ["AC", "+/-", "%"]:
            bg = color_top
            fg = "black"
        elif text in ["/", "*", "-", "+", "="]:
            bg = color_operator
            fg = "white"
        else:
            bg = color_number
            fg = "white"

        if text == "AC":
            cmd = clear
        elif text == "=":
            cmd = equal
        elif text == "+/-":
            cmd = lambda: None
        elif text == "%":
            cmd = lambda: press("/100")
        else:
            cmd = lambda x=text: press(x)

        if text == "0":
            btn = tk.Button(
                root,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                font=("Helvetica", 20),
                bd=0,
                width=10,
                height=2
            )
            btn.grid(row=r+1, column=c, columnspan=2,
                     padx=4, pady=4, sticky="nsew")
            c += 2
        else:
            btn = tk.Button(
                root,
                text=text,
                command=cmd,
                bg=bg,
                fg=fg,
                font=("Helvetica", 20),
                bd=0,
                width=5,
                height=2
            )
            btn.grid(row=r+1, column=c, padx=4,
                     pady=4, sticky="nsew")
            c += 1

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()