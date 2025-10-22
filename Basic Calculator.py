import tkinter as tk
import math

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            history_list.insert(tk.END, f"{expression} = {result}")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "CE":
        history_list.delete(0, tk.END)
    elif text == "√":
        try:
            value = float(entry.get())
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            history_list.insert(tk.END, f"√{value} = {result}")
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "π":
        entry.insert(tk.END, str(math.pi))
    elif text == "log":
        try:
            value = float(entry.get())
            result = math.log10(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            history_list.insert(tk.END, f"log({value}) = {result}")
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "x^y":
        entry.insert(tk.END, "**")
    elif text == "%":
        try:
            value = float(entry.get())
            result = value / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            history_list.insert(tk.END, f"{value}% = {result}")
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

# Main window setup
root = tk.Tk()
root.title("Scientific Calculator with History")
root.geometry("400x500")

# Entry field for input/output
entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=10)

# Button layout
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "π"],
    ["1", "2", "3", "-", "log"],
    ["0", ".", "=", "+", "x^y"],
    ["C", "%", "CE"]
]

# Create buttons dynamically
for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(expand=True, fill=tk.BOTH)
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 16", relief=tk.RAISED, bd=5)
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        btn.bind("<Button-1>", click)

# History label
history_label = tk.Label(root, text="History", font="Arial 14")
history_label.pack()

# History listbox with scrollbar
history_frame = tk.Frame(root)
history_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(history_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

history_list = tk.Listbox(history_frame, font="Arial 12", yscrollcommand=scrollbar.set)
history_list.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=history_list.yview)

# Run the application
root.mainloop()