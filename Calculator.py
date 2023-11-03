import tkinter as tk


def on_click(event):
  text = event.widget.cget("text")

  if text == "=":
    try:
      result = str(eval(screen.get()))
      screen.set(result)
    except Exception:
      screen.set("Error")
  elif text == "C":
    screen.set("")
  else:
    screen.set(screen.get() + text)
root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
  "7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", "C", "=",
  "+"
]

i = 0
for btn in buttons:
  button = tk.Button(button_frame,
                     text=btn,
                     font="lucida 15 bold",
                     width=4,
                     height=2)
  button.grid(row=i // 4, column=i % 4)
  button.bind("<Button-1>", on_click)
  i += 1
  
root.mainloop()
