import tkinter as tk

root = tk.Tk()
root.resizable(width=False, height=False)

img = tk.PhotoImage(file="QR.png")
width, height = img.width(), img.height()
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_image((0, 0), image=img, anchor="nw")
entry = tk.Entry(master=canvas)

button = tk.Button(master=canvas, text="hello")

canvas.create_window((width / 2, 50), window=button, anchor="center")
canvas.create_window((width / 2, 100), window=entry, anchor="center")

root.mainloop()