from tkinter import *

def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("错误")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = Tk()
root.geometry("400x600")
root.title("计算器")

screen = StringVar()

entry = Entry(root, textvar = screen, font="lucida 20 bold")
entry.pack(fill=X, ipadx=8, pady=10, padx=10)

button_frame = Frame(root)
button_frame.pack()

list_of_numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0", "."]
i = 0
for j in range(3, 6):
    for k in range(3):
        button = Button(button_frame, text=list_of_numbers[i], font='lucida 15 bold')
        button.grid(row=j, column=k, padx=3, pady=3)
        i += 1
        button.bind("<Button-1>", calculate)

button = Button(button_frame, text="C", font='lucida 15 bold')
button.grid(row=3, column=3, padx=3, pady=3)
button.bind("<Button-1>", calculate)

list_of_operators = ["+", "-", "*", "/"]
i = 0
for j in range(3, 7):
    button = Button(button_frame, text=list_of_operators[i], font='lucida 15 bold')
    button.grid(row=j, column=3, padx=3, pady=3)
    i += 1
    button.bind("<Button-1>", calculate)

button = Button(button_frame, text="=", font='lucida 15 bold')
button.grid(row=6, column=2, padx=3, pady=3)
button.bind("<Button-1>", calculate)

root.mainloop()