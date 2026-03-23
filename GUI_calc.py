import tkinter as tk

def click(btn):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(btn))

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
window = tk.Tk()
window.title("Calculator")

# Entry box
entry = tk.Entry(window, width=25, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

# Create buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, width=5, height=2, command=equal).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width=5, height=2, command=lambda t=text: click(t)).grid(row=row, column=col)

# Clear button
tk.Button(window, text='C', width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4)

window.mainloop()